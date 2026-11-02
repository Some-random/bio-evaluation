# cofactor_0134

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
MVNIYIFGDQTVRVDDAVHKLLHVKNNPILKSFLDGSFAAIRKQIFLLPANERTSLPDAHTLPLLLEAVRRGRRHVALESALVCLCEIGQYIALLQTTDLCHPPTGSILVGFCTGSLAAAAVSCVRTSIDLLTLGIEAVVVAFRVGMHVARRANALGGDGGSQWKPWSLAVTDGSESETEKILEEFTRDEVSGVHVANRHDAYILAKGLPAIMKPYVSAAGSNTLTISGTPRVLEALKASPHLRGTKSLPVSIYAPYHAAHLYNEADVESIFACKPVESALFHRELRTPLISCATGTVLKEKTFGDLLRALVMEILTCQIRFDKVEESIVQHTPGATAQLIPIHTNIAPRMKTSLTQVGLQVECFKAIANQEPAAEALSESPSNDSSKIAIIGFSGRFPEADGLNEFWELLQQGLDVHKPIPADRFDLEAHYDATLREKNTSRIKHGCWIRSPGSFDARFFQMSPREACQTDPAQRLALLTAYEAMEMAGFVPDRTPSSQRDRVGVYYGMTSDDWREVNSSQDIDTYFIPGGIRAFVPGRINYFFKFSGPSITVDTACSSSLAAIHTACNALLNSDCDTALAGGTNILTNPDNFAGLDRGHFLSSTGNCKTFDDDADGYCRADGVGTVILKRLQDAIADNDPIFGVIVGARTSHSAEAVSITRPLADAQAHLFRKLLAESGIHPHEISYIEMHGTGTQAGDAVEMKSVLDSFARDDSRAPDRPLHLGSVKANVGHGESASGVTALIKVLLMMQKNRIPPHCGIKGRINRHFPTDMEYRNVHIPFMETDWTRPQEGKRRSFINNFSAAGGNTAVLVEDAPLLEQSRAISSPDPQRYHVITLSARSVRSLSKNMRALGEFIGSETSPGLLARIAYTTTARRMHHSYRVAFVGNDLQEVKRRFLDTDVTEAIKPCPTKSPGVGFLFTGQGAQQTAMARELYDRFTSFRADILEFEAVGRGHGFPSILPLITGAVDVEELSPMIVQLGTVVIQIAMARLWQTWGLTPEYALGHSLGEYAALQIAGVLSISDTIYLAGSRAALLEKRCTAGSHGMLAVKASVAHLEEALKGMQVEVSCINGFDDTVLSGTNDEIDRASKELSELKVTFKRLILPFAFHSSQVDPILEELEHIASQLSFQPPRIPIVSPTVGHIITDEGTIGAQYIRRHCREPVNFLGAIQAAQGSGICNSGALAVEIGAHPILTRMMKAAVGSSVTVCSTLSHREDMFKTLTESLSVLHLAGVRLNWDEYHRDFNNQVVMLPAYSWDYQDYWIQYQNNFCLTKGSPERSESVDAIQPMSTRLSPSVQKILEEEMTAAQASIIIESDITDPELLPVALDHKVNGVTLCPSSLYADIGHTLGTYLLGKKEDVTDYKIDVSNMAVEKALVVKGTGPQLFRASLDMDWNMLRGMMKVYSVNNMGTLTTHHAQCTIELQRPHQWQEGWNRQLYLIQRSIEQLKKGVEEGWTHKMRRGVAYRLFSSMMQYGPSYQAMEEVIFDSSGLEATAQVRLQSTTGRYSFNPVWSDSLGHITGFVTNCNDSIDLTENLFVNHGWGFMRCVEPFSPDTVYQTHVKMQPVDGNNGFYVGDVYVLNDHRIIAQYGAVTFQKVARRVLEMLLPATTSKGRSSNIRPRNVGTAQSAKIVQSKRRTQTPHVEDAWQQVLEMIARELGVDPGQLTEDVNFTDMGVDSLMSLTIIGNFREFLSLDVPWSLFEDCPSVQSLRIYLNMSSLSESDSIETSSYPTPDESTTTTITSPSGSDRNVGRNSGIDGVGTTVGLVLSILAEEIGVNVRDLSNADGLSELGLDSLLSITALGRVRDETDLDLPSDFFLEHSSVAAITAALHAIFGSTEQGPEQSLITSHPPAMSINLQGDEGCPQTLFLFPDGSGSSTSYSALPTISKDVRVYAMDCPYLKRPNELAKCQLQDLTPVYVAEIRRRQLRGPYSLGGWSAGGIAAYEAAQYLVDQGERVERLILIDSPNPMGLGKCPPHFYRFLEEAGVFGVHGGRKPPAWLLQHFQAFNDVLSQYTLEPFRPADATPNTTLIYAQDGVCKSPRDPRPERHPGDPEVFSWLLENRVDMSCNGWDQLLGEDNIHLGTVFDANHFTIVRTPAVVRLSEIVRMAMSRKFQ

[Multiple Choices]
A. FMN
B. Mg(2+)
C. pantetheine 4'-phosphate
D. heme b
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

> The exact sequence matches the UniProt entry for a non-reducing polyketide synthase, whose cofactor annotation is pantetheine 4'-phosphate. The annotation is based on a PROSITE rule, so it supports the key as a computational annotation, not as a directly demonstrated experimental requirement.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a large multidomain fungal polyketide synthase containing an acyl-carrier-protein domain. Such domains use a conserved serine site modified with phosphopantetheine to carry intermediates, making pantetheine 4'-phosphate the biologically relevant choice over FMN, Mg(2+), or heme b.


**Missing item-specific fact**

> No direct cofactor measurement is supplied; the inference relies on identifying the PKS/ACP architecture and its established phosphopantetheinylation requirement.


**Reason**

> The sequence and choices provide a meaningful domain-function argument for the answer, rather than requiring only recall of this protein's database entry. The protein-specific annotation strengthens the key but is reviewer-only evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, pantetheine 4'-phosphate is the fitting cofactor for the ACP component of a polyketide synthase.


### Important caveats

- The cited UniProt cofactor annotation is computationally assigned by a PROSITE rule; it is not direct experimental evidence.
- The sequence match establishes source identity for the reviewer, but that accession and annotation were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a large multidomain fungal polyketide synthase containing an acyl-carrier-protein domain. Such domains use a conserved serine site modified with phosphopantetheine to carry intermediates, making pantetheine 4'-phosphate the biologically relevant choice over FMN, Mg(2+), or heme b.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No direct cofactor measurement is supplied; the inference relies on identifying the PKS/ACP architecture and its established phosphopantetheinylation requirement.",
    "reason": "The sequence and choices provide a meaningful domain-function argument for the answer, rather than requiring only recall of this protein's database entry. The protein-specific annotation strengthens the key but is reviewer-only evidence."
  },
  "case_id": "cofactor_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for a non-reducing polyketide synthase, whose cofactor annotation is pantetheine 4'-phosphate. The annotation is based on a PROSITE rule, so it supports the key as a computational annotation, not as a directly demonstrated experimental requirement."
  },
  "important_caveats": [
    "The cited UniProt cofactor annotation is computationally assigned by a PROSITE rule; it is not direct experimental evidence.",
    "The sequence match establishes source identity for the reviewer, but that accession and annotation were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, pantetheine 4'-phosphate is the fitting cofactor for the ACP component of a polyketide synthase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry for a non-reducing polyketide synthase, whose cofactor annotation is pantetheine 4'-phosphate. The annotation is based on a PROSITE rule, so it supports the key as a computational annotation, not as a directly demonstrated experimental requirement.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a large multidomain fungal polyketide synthase containing an acyl-carrier-protein domain. Such domains use a conserved serine site modified with phosphopantetheine to carry intermediates, making pantetheine 4'-phosphate the biologically relevant choice over FMN, Mg(2+), or heme b.",
    "missing_item_specific_fact": "No direct cofactor measurement is supplied; the inference relies on identifying the PKS/ACP architecture and its established phosphopantetheinylation requirement.",
    "reason": "The sequence and choices provide a meaningful domain-function argument for the answer, rather than requiring only recall of this protein's database entry. The protein-specific annotation strengthens the key but is reviewer-only evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, pantetheine 4'-phosphate is the fitting cofactor for the ACP component of a polyketide synthase."
  },
  "important_caveats": [
    "The cited UniProt cofactor annotation is computationally assigned by a PROSITE rule; it is not direct experimental evidence.",
    "The sequence match establishes source identity for the reviewer, but that accession and annotation were not provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q2TXQ8 (Non-reducing polyketide synthase aoiG, Aspergillus oryzae) explicitly annotates pantetheine 4'-phosphate (CHEBI:47942) as the cofactor (evidence ECO:0000255|PROSITE-ProRule:PRU00258). This is a computational annotation based on the ACP (acyl carrier protein) domain signature, but it is strongly grounded in established PKS biochemistry: the ACP domain of all polyketide synthases is post-translationally phosphopantetheinylated, and pantetheine 4'-phosphate serves as the swinging-arm prosthetic group that carries acyl intermediates. The EC assignment (2.3.1.-) and the 2121-aa multi-domain architecture are consistent with a fungal NR-PKS.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 2121-aa length indicates a multi-domain megasynthase. The sequence contains the well-known KS-domain motif 'GHSAG' (visible as 'GHSAGDAVEMK' in the C-terminal region), which is a hallmark of ketosynthase domains in polyketide synthases. Recognizing this as a fungal NR-PKS leads to the well-established biological fact that PKS enzymes carry an ACP domain whose essential prosthetic group is pantetheine 4'-phosphate (the phosphopantetheinyl arm derived from CoA). None of the distractors (FMN for flavoproteins, Mg²⁺ for nucleotidyl/kinase-type reactions, heme b for cytochromes/peroxidases) correspond to any domain found in PKS architecture.


**Missing item-specific fact**

> Precise identification of the ACP-domain 'GGDSL/GADLS' serine-acceptor motif within the 2121-aa sequence is non-trivial from raw sequence alone; however, the KS-domain 'GHSAG' signature and the overall multi-domain size are sufficient to classify the enzyme as a PKS, from which the pantetheine 4'-phosphate requirement follows by general enzymology.


**Reason**

> A knowledgeable reader can identify the KS signature, infer PKS membership, and deduce the ACP/pantetheine 4'-phosphate requirement through domain-to-cofactor biological reasoning. The distractors are all cofactors of unrelated enzyme classes, making them eliminable by general knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> FMN, Mg²⁺, and heme b are cofactors of oxidoreductases, nucleotidyl-transferases, and hemoproteins respectively—none of which match PKS domain architecture. Pantetheine 4'-phosphate is the unique and defining prosthetic group of the ACP domain in PKS enzymes. No other option is defensible for a polyketide synthase.


### Important caveats

- The UniProt cofactor annotation is computational (PROSITE-ProRule PRU00258), not direct experimental measurement, though the underlying biology (ACP phosphopantetheinylation) is extensively validated across PKS enzymes.
- The protein was integrated into Swiss-Prot in April 2025; the author's source snapshot is unknown but the sequence matches exactly.
- Identifying the KS 'GHSAG' motif and ACP signature from a 2121-aa raw sequence requires domain-level pattern recognition that is feasible but not trivial for all readers.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 2121-aa length indicates a multi-domain megasynthase. The sequence contains the well-known KS-domain motif 'GHSAG' (visible as 'GHSAGDAVEMK' in the C-terminal region), which is a hallmark of ketosynthase domains in polyketide synthases. Recognizing this as a fungal NR-PKS leads to the well-established biological fact that PKS enzymes carry an ACP domain whose essential prosthetic group is pantetheine 4'-phosphate (the phosphopantetheinyl arm derived from CoA). None of the distractors (FMN for flavoproteins, Mg²⁺ for nucleotidyl/kinase-type reactions, heme b for cytochromes/peroxidases) correspond to any domain found in PKS architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of the ACP-domain 'GGDSL/GADLS' serine-acceptor motif within the 2121-aa sequence is non-trivial from raw sequence alone; however, the KS-domain 'GHSAG' signature and the overall multi-domain size are sufficient to classify the enzyme as a PKS, from which the pantetheine 4'-phosphate requirement follows by general enzymology.",
    "reason": "A knowledgeable reader can identify the KS signature, infer PKS membership, and deduce the ACP/pantetheine 4'-phosphate requirement through domain-to-cofactor biological reasoning. The distractors are all cofactors of unrelated enzyme classes, making them eliminable by general knowledge."
  },
  "case_id": "cofactor_0134",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q2TXQ8 (Non-reducing polyketide synthase aoiG, Aspergillus oryzae) explicitly annotates pantetheine 4'-phosphate (CHEBI:47942) as the cofactor (evidence ECO:0000255|PROSITE-ProRule:PRU00258). This is a computational annotation based on the ACP (acyl carrier protein) domain signature, but it is strongly grounded in established PKS biochemistry: the ACP domain of all polyketide synthases is post-translationally phosphopantetheinylated, and pantetheine 4'-phosphate serves as the swinging-arm prosthetic group that carries acyl intermediates. The EC assignment (2.3.1.-) and the 2121-aa multi-domain architecture are consistent with a fungal NR-PKS."
  },
  "important_caveats": [
    "The UniProt cofactor annotation is computational (PROSITE-ProRule PRU00258), not direct experimental measurement, though the underlying biology (ACP phosphopantetheinylation) is extensively validated across PKS enzymes.",
    "The protein was integrated into Swiss-Prot in April 2025; the author's source snapshot is unknown but the sequence matches exactly.",
    "Identifying the KS 'GHSAG' motif and ACP signature from a 2121-aa raw sequence requires domain-level pattern recognition that is feasible but not trivial for all readers."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "FMN, Mg²⁺, and heme b are cofactors of oxidoreductases, nucleotidyl-transferases, and hemoproteins respectively—none of which match PKS domain architecture. Pantetheine 4'-phosphate is the unique and defining prosthetic group of the ACP domain in PKS enzymes. No other option is defensible for a polyketide synthase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0134",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q2TXQ8 (Non-reducing polyketide synthase aoiG, Aspergillus oryzae) explicitly annotates pantetheine 4'-phosphate (CHEBI:47942) as the cofactor (evidence ECO:0000255|PROSITE-ProRule:PRU00258). This is a computational annotation based on the ACP (acyl carrier protein) domain signature, but it is strongly grounded in established PKS biochemistry: the ACP domain of all polyketide synthases is post-translationally phosphopantetheinylated, and pantetheine 4'-phosphate serves as the swinging-arm prosthetic group that carries acyl intermediates. The EC assignment (2.3.1.-) and the 2121-aa multi-domain architecture are consistent with a fungal NR-PKS.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 2121-aa length indicates a multi-domain megasynthase. The sequence contains the well-known KS-domain motif 'GHSAG' (visible as 'GHSAGDAVEMK' in the C-terminal region), which is a hallmark of ketosynthase domains in polyketide synthases. Recognizing this as a fungal NR-PKS leads to the well-established biological fact that PKS enzymes carry an ACP domain whose essential prosthetic group is pantetheine 4'-phosphate (the phosphopantetheinyl arm derived from CoA). None of the distractors (FMN for flavoproteins, Mg²⁺ for nucleotidyl/kinase-type reactions, heme b for cytochromes/peroxidases) correspond to any domain found in PKS architecture.",
    "missing_item_specific_fact": "Precise identification of the ACP-domain 'GGDSL/GADLS' serine-acceptor motif within the 2121-aa sequence is non-trivial from raw sequence alone; however, the KS-domain 'GHSAG' signature and the overall multi-domain size are sufficient to classify the enzyme as a PKS, from which the pantetheine 4'-phosphate requirement follows by general enzymology.",
    "reason": "A knowledgeable reader can identify the KS signature, infer PKS membership, and deduce the ACP/pantetheine 4'-phosphate requirement through domain-to-cofactor biological reasoning. The distractors are all cofactors of unrelated enzyme classes, making them eliminable by general knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "FMN, Mg²⁺, and heme b are cofactors of oxidoreductases, nucleotidyl-transferases, and hemoproteins respectively—none of which match PKS domain architecture. Pantetheine 4'-phosphate is the unique and defining prosthetic group of the ACP domain in PKS enzymes. No other option is defensible for a polyketide synthase."
  },
  "important_caveats": [
    "The UniProt cofactor annotation is computational (PROSITE-ProRule PRU00258), not direct experimental measurement, though the underlying biology (ACP phosphopantetheinylation) is extensively validated across PKS enzymes.",
    "The protein was integrated into Swiss-Prot in April 2025; the author's source snapshot is unknown but the sequence matches exactly.",
    "Identifying the KS 'GHSAG' motif and ACP signature from a 2121-aa raw sequence requires domain-level pattern recognition that is feasible but not trivial for all readers."
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

**Accession:** `Q2TXQ8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 122. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:41.744302+00:00.  

```json
"Q2TXQ8"
```

Source SHA-256: `b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:41.744302+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22447538","source":"PubMed"}],"value":"2.3.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22447538","source":"PubMed"}],"value":"Non-reducing polyketide synthase aoiG"}}}
```

Source SHA-256: `b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:41.744302+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:47942"},"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00258","source":"PROSITE-ProRule"}],"name":"pantetheine 4'-phosphate"}],"commentType":"COFACTOR"}
```

Source SHA-256: `b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:30:44.949915+00:00.  

```text
DE   RecName: Full=Non-reducing polyketide synthase aoiG {ECO:0000303|PubMed:22447538};
DE            EC=2.3.1.- {ECO:0000269|PubMed:22447538};
```

Source SHA-256: `cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)  
**Locator:** `lines 52-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:30:44.949915+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=pantetheine 4'-phosphate; Xref=ChEBI:CHEBI:47942;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00258};
```

Source SHA-256: `cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 134. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
