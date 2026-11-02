# cofactor_0132

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **C** — pantetheine 4&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTLQETSVLEPTLQGTTTLPGLLAQRVAEHPEAIAVAYRDDKLTFRELASRSAALADYLEHLGVSADDCVGLFVEPSIDLMVGAWGILNAGAAYLPLSPEYPEDRLRYMIENSETKIILAQQRLVSRLRELAPKDVTIVTLRESEAFVRPEGTEAPAARSARPDTLAYVIYTSGSTGKPKGVMIEHRSIVNQLGWLRETYAIDRSKVILQKTPMSFDAAQWEILSPANGATVVMGAPGVYADPEGLIETIVKHNVTTLQCVPTLLQGLIDTEKFPECVSLQQIFSGGEALSRLLAIQTTQEMPGRALINVYGPTETTINSSSFPVDPADLDEGPQSISIGSPVHGTTYHILDKETLKPVGVGEIGELYIGGIQLARGYLHRDDLTAERFLEIELEEGAEPVRLYKTGDLGQWNNDGTVQFAGRADNQVKLRGYRVELDEISLAIENHDWVRNAAVIVKNDGRTGFQNLIACIELSEKEAALMDQGNHGSHHASKKSKLQVKAQLSNPGLRDDAELAARPAFDLEGAEPTPEQRARVFARKTYRFYEGGAVTQADLLGLLGATVTAGYSRKAADLAPAELGQILRWFGQYISEERLLPKYGYASPGALYATQMYFELEGVGGLKPGYYYYQPVRHQLVLISEREATGKATAQIHFIGKKSGIEPVYKNNILEVLEIETGHMVGLFEQILPAYGLDIHDRAYEPAVKDLLDVADEDYYLGTFELVPHAGARDDQAEVYVQTHGGKVAGLPEGQYRYENGELTRFSDDIVLKKHVIAINQSVYQAASFGISVYSRAEEEWLKYITLGKKLQHLMMNGLNLGFMSSGYSSKTGNPLPASRRMDAVLGANGVDSAPMYFFVGGRISDEQIGHEGMREDSVHMRGPAELIRDDLVSFLPDYMIPNRVVVFDRLPLSANGKIDVKALAASDQVNAELVERPFVAPRTETEKEIAAVWEKALRRENASVQDDFFESGGNSLIAVGLVRELNARLGVSLPLQSVLESPTIEKLARRLEREVAQESSRFVRLHAETGKARPVICWPGLGGYPMNLRSLAGEIGLGRSFYGVQSYGINEGETPYETITEMAKKDIEALKEIQPAGPYTLWGYSFGARVAFETAYQLEQAGEKVDNLFLIAPGSPKVRAENGKVWGREASFANRGYTTILFSVFTGTISGPDLDRCLETVTDEASFAEFISELKGIDVDLARRIISVVGQTYEFEYSFHELAERTLQAPISIFKAVGDDYSFLENSSGYSAEPPTVIDLDADHYSLLREDIGELVKHIRYLLGE

[Multiple Choices]
A. FAD
B. Mg(2+)
C. pantetheine 4'-phosphate
D. FMN
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

> The exact supplied sequence matches the UniProt entry for indigoidine synthase, which annotates pantetheine 4'-phosphate as its cofactor and links that annotation to experimental evidence from the cited 2007 paper. The paper’s cited scope includes cofactor and phosphopantetheinylation, though it was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence is consistent with a nonribosomal peptide synthetase containing a carrier-protein domain. Such domains require a covalently attached phosphopantetheine arm for substrate handling, making the pantetheine-phosphate choice biologically fitting and distinguishing it from FAD, FMN, or Mg2+.


**Missing item-specific fact**

> The exact protein-specific cofactor annotation and experimental confirmation are not supplied, but they are not necessary for the broad distinction among these choices if the NRPS/carrier-domain interpretation is made.


**Reason**

> The sequence and general biology of NRPS carrier domains provide a meaningful basis for selecting the pantetheine-phosphate option; this is more than recognizing a database entry or relying on an unspecified predictor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, pantetheine 4'-phosphate is the one consistent with the phosphopantetheine-dependent carrier-domain chemistry of an NRPS.


### Important caveats

- The reviewer-only UniProt record is sequence-matched, but it was not available to the evaluated model.
- The evidence links the cofactor annotation to a publication with experimental evidence codes; the primary study was not independently assessed here.
- The biologically familiar carrier-domain modification is often described as phosphopantetheine, while the annotated and offered choice is pantetheine 4'-phosphate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is consistent with a nonribosomal peptide synthetase containing a carrier-protein domain. Such domains require a covalently attached phosphopantetheine arm for substrate handling, making the pantetheine-phosphate choice biologically fitting and distinguishing it from FAD, FMN, or Mg2+.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact protein-specific cofactor annotation and experimental confirmation are not supplied, but they are not necessary for the broad distinction among these choices if the NRPS/carrier-domain interpretation is made.",
    "reason": "The sequence and general biology of NRPS carrier domains provide a meaningful basis for selecting the pantetheine-phosphate option; this is more than recognizing a database entry or relying on an unspecified predictor."
  },
  "case_id": "cofactor_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry for indigoidine synthase, which annotates pantetheine 4'-phosphate as its cofactor and links that annotation to experimental evidence from the cited 2007 paper. The paper’s cited scope includes cofactor and phosphopantetheinylation, though it was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only UniProt record is sequence-matched, but it was not available to the evaluated model.",
    "The evidence links the cofactor annotation to a publication with experimental evidence codes; the primary study was not independently assessed here.",
    "The biologically familiar carrier-domain modification is often described as phosphopantetheine, while the annotated and offered choice is pantetheine 4'-phosphate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, pantetheine 4'-phosphate is the one consistent with the phosphopantetheine-dependent carrier-domain chemistry of an NRPS."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry for indigoidine synthase, which annotates pantetheine 4'-phosphate as its cofactor and links that annotation to experimental evidence from the cited 2007 paper. The paper’s cited scope includes cofactor and phosphopantetheinylation, though it was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence is consistent with a nonribosomal peptide synthetase containing a carrier-protein domain. Such domains require a covalently attached phosphopantetheine arm for substrate handling, making the pantetheine-phosphate choice biologically fitting and distinguishing it from FAD, FMN, or Mg2+.",
    "missing_item_specific_fact": "The exact protein-specific cofactor annotation and experimental confirmation are not supplied, but they are not necessary for the broad distinction among these choices if the NRPS/carrier-domain interpretation is made.",
    "reason": "The sequence and general biology of NRPS carrier domains provide a meaningful basis for selecting the pantetheine-phosphate option; this is more than recognizing a database entry or relying on an unspecified predictor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, pantetheine 4'-phosphate is the one consistent with the phosphopantetheine-dependent carrier-domain chemistry of an NRPS."
  },
  "important_caveats": [
    "The reviewer-only UniProt record is sequence-matched, but it was not available to the evaluated model.",
    "The evidence links the cofactor annotation to a publication with experimental evidence codes; the primary study was not independently assessed here.",
    "The biologically familiar carrier-domain modification is often described as phosphopantetheine, while the annotated and offered choice is pantetheine 4'-phosphate."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q1MWN4 (Indigoidine synthase, EC 4.3.3.9, a single-module NRPS from Streptomyces lavendulae) explicitly annotates pantetheine 4'-phosphate as the cofactor with experimental evidence (ECO:0000269, PubMed:17237222). The primary paper reports phosphopantetheinylation at Ser-972 and confirms the cofactor experimentally. This is consistent with the well-established biochemistry of NRPS enzymes, which use 4'-phosphopantetheine as a covalently attached prosthetic group on the PCP (peptidyl carrier protein) domain.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark NRPS domain signatures: the adenylation (A) domain A3 motif 'TSGSTGKPKG' (a highly conserved NRPS-specific motif), the 'HH' motif (HxHHxH) characteristic of the A domain, and a condensation (C) domain region. The overall C-A-PCP architecture of a ~1282-residue protein is diagnostic of a single-module non-ribosomal peptide synthetase. NRPS enzymes universally require 4'-phosphopantetheine as their prosthetic group, covalently tethered to a conserved serine in the PCP domain. The distractors (FAD, FMN for flavoproteins; Mg²⁺ for kinases/nucleases) are cofactors of entirely different enzyme classes and are inconsistent with NRPS domain architecture.


**Missing item-specific fact**

> None critical. Recognizing NRPS domain motifs (TSGSTGKPKG, HH motif) and knowing that NRPS enzymes require phosphopantetheine are general biochemistry/molecular biology knowledge, not a protein-specific database lookup.


**Reason**

> A model with knowledge of NRPS domain signatures can identify the enzyme class from the sequence and then apply the general rule that NRPS uses 4'-phosphopantetheine. The distractors are cofactors for unrelated enzyme classes (oxidoreductases, metalloenzymes), making them eliminable by the same domain-recognition reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Pantetheine 4'-phosphate is the sole cofactor/prosthetic group of NRPS enzymes. FAD, FMN, and Mg²⁺ are not associated with NRPS catalytic mechanism. The wording 'cofactor' is slightly imprecise (it is technically a prosthetic group), but UniProt and the literature classify it under COFACTOR, and no other option is defensible.


### Important caveats

- The sequence does not include the full PCP domain serine context in an easily visible form, so identification relies on recognizing A-domain and C-domain motifs rather than the phosphopantetheinylation site itself.
- The term 'cofactor' is used loosely; 4'-phosphopantetheine is a prosthetic group (covalently attached), but this is standard usage in UniProt annotations and the literature.
- The protein is a single-module NRPS (indigoidine synthase), which is a relatively rare and specialized class; however, the domain signatures are well-conserved across all NRPS enzymes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark NRPS domain signatures: the adenylation (A) domain A3 motif 'TSGSTGKPKG' (a highly conserved NRPS-specific motif), the 'HH' motif (HxHHxH) characteristic of the A domain, and a condensation (C) domain region. The overall C-A-PCP architecture of a ~1282-residue protein is diagnostic of a single-module non-ribosomal peptide synthetase. NRPS enzymes universally require 4'-phosphopantetheine as their prosthetic group, covalently tethered to a conserved serine in the PCP domain. The distractors (FAD, FMN for flavoproteins; Mg²⁺ for kinases/nucleases) are cofactors of entirely different enzyme classes and are inconsistent with NRPS domain architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognizing NRPS domain motifs (TSGSTGKPKG, HH motif) and knowing that NRPS enzymes require phosphopantetheine are general biochemistry/molecular biology knowledge, not a protein-specific database lookup.",
    "reason": "A model with knowledge of NRPS domain signatures can identify the enzyme class from the sequence and then apply the general rule that NRPS uses 4'-phosphopantetheine. The distractors are cofactors for unrelated enzyme classes (oxidoreductases, metalloenzymes), making them eliminable by the same domain-recognition reasoning."
  },
  "case_id": "cofactor_0132",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q1MWN4 (Indigoidine synthase, EC 4.3.3.9, a single-module NRPS from Streptomyces lavendulae) explicitly annotates pantetheine 4'-phosphate as the cofactor with experimental evidence (ECO:0000269, PubMed:17237222). The primary paper reports phosphopantetheinylation at Ser-972 and confirms the cofactor experimentally. This is consistent with the well-established biochemistry of NRPS enzymes, which use 4'-phosphopantetheine as a covalently attached prosthetic group on the PCP (peptidyl carrier protein) domain."
  },
  "important_caveats": [
    "The sequence does not include the full PCP domain serine context in an easily visible form, so identification relies on recognizing A-domain and C-domain motifs rather than the phosphopantetheinylation site itself.",
    "The term 'cofactor' is used loosely; 4'-phosphopantetheine is a prosthetic group (covalently attached), but this is standard usage in UniProt annotations and the literature.",
    "The protein is a single-module NRPS (indigoidine synthase), which is a relatively rare and specialized class; however, the domain signatures are well-conserved across all NRPS enzymes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Pantetheine 4'-phosphate is the sole cofactor/prosthetic group of NRPS enzymes. FAD, FMN, and Mg²⁺ are not associated with NRPS catalytic mechanism. The wording 'cofactor' is slightly imprecise (it is technically a prosthetic group), but UniProt and the literature classify it under COFACTOR, and no other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0132",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q1MWN4 (Indigoidine synthase, EC 4.3.3.9, a single-module NRPS from Streptomyces lavendulae) explicitly annotates pantetheine 4'-phosphate as the cofactor with experimental evidence (ECO:0000269, PubMed:17237222). The primary paper reports phosphopantetheinylation at Ser-972 and confirms the cofactor experimentally. This is consistent with the well-established biochemistry of NRPS enzymes, which use 4'-phosphopantetheine as a covalently attached prosthetic group on the PCP (peptidyl carrier protein) domain.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark NRPS domain signatures: the adenylation (A) domain A3 motif 'TSGSTGKPKG' (a highly conserved NRPS-specific motif), the 'HH' motif (HxHHxH) characteristic of the A domain, and a condensation (C) domain region. The overall C-A-PCP architecture of a ~1282-residue protein is diagnostic of a single-module non-ribosomal peptide synthetase. NRPS enzymes universally require 4'-phosphopantetheine as their prosthetic group, covalently tethered to a conserved serine in the PCP domain. The distractors (FAD, FMN for flavoproteins; Mg²⁺ for kinases/nucleases) are cofactors of entirely different enzyme classes and are inconsistent with NRPS domain architecture.",
    "missing_item_specific_fact": "None critical. Recognizing NRPS domain motifs (TSGSTGKPKG, HH motif) and knowing that NRPS enzymes require phosphopantetheine are general biochemistry/molecular biology knowledge, not a protein-specific database lookup.",
    "reason": "A model with knowledge of NRPS domain signatures can identify the enzyme class from the sequence and then apply the general rule that NRPS uses 4'-phosphopantetheine. The distractors are cofactors for unrelated enzyme classes (oxidoreductases, metalloenzymes), making them eliminable by the same domain-recognition reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Pantetheine 4'-phosphate is the sole cofactor/prosthetic group of NRPS enzymes. FAD, FMN, and Mg²⁺ are not associated with NRPS catalytic mechanism. The wording 'cofactor' is slightly imprecise (it is technically a prosthetic group), but UniProt and the literature classify it under COFACTOR, and no other option is defensible."
  },
  "important_caveats": [
    "The sequence does not include the full PCP domain serine context in an easily visible form, so identification relies on recognizing A-domain and C-domain motifs rather than the phosphopantetheinylation site itself.",
    "The term 'cofactor' is used loosely; 4'-phosphopantetheine is a prosthetic group (covalently attached), but this is standard usage in UniProt annotations and the literature.",
    "The protein is a single-module NRPS (indigoidine synthase), which is a relatively rare and specialized class; however, the domain signatures are well-conserved across all NRPS enzymes."
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

**Accession:** `Q1MWN4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 86. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
"Q1MWN4"
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17237222","source":"PubMed"}],"value":"Blue pigment synthetase-encoding gene A"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17237222","source":"PubMed"}],"value":"Blue-pigment synthetase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"17237222","source":"PubMed"}],"value":"4.3.3.9"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Indigoidine synthase"}}}
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:47942"},"evidences":[{"evidenceCode":"ECO:0000269","id":"17237222","source":"PubMed"}],"name":"pantetheine 4'-phosphate"}],"commentType":"COFACTOR"}
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q1MWN4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:19.982445+00:00.  

```json
{"citation":{"authors":["Takahashi H.","Kumagai T.","Kitani K.","Mori M.","Matoba Y.","Sugiyama M."],"citationCrossReferences":[{"database":"PubMed","id":"17237222"},{"database":"DOI","id":"10.1074/jbc.m611319200"}],"citationType":"journal article","firstPage":"9073","id":"17237222","journal":"J. Biol. Chem.","lastPage":"9081","publicationDate":"2007","title":"Cloning and characterization of a Streptomyces single module type non-ribosomal peptide synthetase catalyzing a blue pigment synthesis.","volume":"282"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAE93896.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 11924 / 8197-20"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","DOMAIN","PHOSPHOPANTETHEINYLATION AT SER-972","MUTAGENESIS OF LYS-598; TYR-601; SER-603 AND TYR-608"]}
```

Source SHA-256: `c906708546c246df109b67b213b4f68804827919bfda2c2ba8983251d4e84193`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)  
**Locator:** `lines 15-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-01T06:28:29.129628+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:BAE93896.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, COFACTOR,
RP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, DOMAIN, PHOSPHOPANTETHEINYLATION AT
RP   SER-972, AND MUTAGENESIS OF LYS-598; TYR-601; SER-603 AND TYR-608.
RC   STRAIN=ATCC 11924 / 8197-20;
RX   PubMed=17237222; DOI=10.1074/jbc.m611319200;
RA   Takahashi H., Kumagai T., Kitani K., Mori M., Matoba Y., Sugiyama M.;
RT   "Cloning and characterization of a Streptomyces single module type non-
RT   ribosomal peptide synthetase catalyzing a blue pigment synthesis.";
RL   J. Biol. Chem. 282:9073-9081(2007).
```

Source SHA-256: `8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q1MWN4?format=txt&versions=86)  
**Locator:** `lines 54-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 86 / 1.  
**Retrieved:** 2026-11-01T06:28:29.129628+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=pantetheine 4'-phosphate; Xref=ChEBI:CHEBI:47942;
CC         Evidence={ECO:0000269|PubMed:17237222};
```

Source SHA-256: `8bc7849e41bbdb1a1fb6219925e8964b5a472463d6a363ad036ff4c8e31af55f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 132. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
