# EC_number_0013

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 2.7.11.24

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSKNIQRQRSISSISSRGVDRDRDPASGGLGLLSPYNSRSPLAGLHHSPGSLDATANQLSRPTFLLERKATEDIAKLDGVLFDDIPTLGSSNDHISSLGAGSPYPTINTSLAVTNPNYLSASSPGGPRRRANTASGPLSPAPPASPIDRLSKTTNRGSFVPSTARQPMNSQPPAPASSAPPPKQRTTSPSVASPPSQTRSQTVPYLSSNFGPTANMYGQRQPSGVDPSRPFHQVPLPPPPMSPPPAIGTINSIMTNIPPPPPRYPSAPAAAIHLPGPPGAPPPSGLPPPPGPPPNNTTNWQGTWIGAYGSYIPPPPPQQTHRPYNPQPYKTVNGQTIAIPPPPPPTESMQMSATYIPQGDSYGEGVGIPGLGMDDMAAWSATSQSSWLGGYNSIGSLAPTNASDTAASTPVDAYGSHNRDNSTTSNATSSGASGIPPELAAQWPLDRVLDWLQANNFSNDWRSTFRALDLHGNRFLEVGSANGGRGNFGMMHQLVYPRLAAECISSGTGWDQPREREEGKRMRRLIRHIVKGETPGTGMSSHTRKESISNTSLVPTSAGPDSGSPDTPIKAPGPGFSVGHPGGNHRKLLVGNFDDEGAHRRSPVASEPSEVGITFTERSSSNRGYSPAGSPAPTPGLFSSSTAPNLASSPGGRFGGHRNRNSTDSVSSNAAIYGSGVPPDASQVLRSQMNFGDMAKDTRRYGHDGGNRPSPLGDNASNGDRSAGASEPPGSAKEGKSFLSIFNHRKKKHHDDPDSPTSPMQHKSHSLGSRGNASETSLERPGSSVSTSHEHNTPASSMRSRRITTGRIFILATLDYWNYRMVDVSDVESASDLRQLICINLGLPDADGAQVYLTELGKFDHEDPLDDSQLVANKKVRADAAGSLKVFVRPGNMAGLAVNIGQSQNALSPAHLPAGAKMDEDTYARLNGQRRRSSSSPPASRQNTLTGGEHGKPTSTGADDDENKDPKSDDIAQQAEAHRIEMERKQQAYLAKRKHARENGNSPSENGTGSYTGIVGPKVIDFDEPRNSPFEDKKPFDSAFAPQRRAPAAPLDPSATLIKANSLSKRGSHQRNSQGSVDGFPSKRQGTGMTESPKHISEKRKPTNERQALGGIGAALAGMGRGLGGIAHPGGAGQRGTSPNRSSPGSAGESAGVASSTTDRGEDAKSRKPISSGNVSPTSSARTVSDEPPQLPKVVIKPRIFDGDSSSDEDSDDDSDDGLFAKPLAGRGGDDAAAKGKEPATKPVAKSPMSKHGTFWNDADSDGDEDPISESASNLNKRPSLTVNTKRGRKGLSVTFTSPDLPSSAGSKTAAGDEDDRSSRGSKRTPNTPHSEGWDSNNDKDVKLSRRKSFMEKDTSIWANRPPTDALINNLEDFFPNLDVDQPVLEEGELPGDLPPSPIAEAEEPHDQQQAKSMTTSRISNLYNDSDTLGSDESTLKALERPASIVSVARKNTRRSGGLGRMKSIREVAHKRYTQGAGAPPPVPAAPNNSNNSSSSGSKNSNLMRRKSTKMFNANIVQIRPERGSMILPQIPQDHLPSLPHNANNQIPKRQTTFRWFKGQLIGKGTYGRVYLGMNATTGEFLAVKEVEVNPKAAGGDKNKMKELVAALDQEIDTMQHLDHVNIVQYLGCERKETSISIFLEYIPGGSIGSCLRKHGKFEESVVSSLTRQTLSGLAYLHREGILHRDLKADNILLDVDGTAKISDFGISKKTDNIYGNDKTNSMQGSVFWMAPEVIRSQGEGYSAKVDIWSLGCVVLEMFAGRRPWSKDEAVGAIYKIANGETPPIPEEVSAAVTPVALSFMWDCFSVNPEERPTATKLLAEHPFCVFRDDYDFDQTELYAKIKGTWNTK

[Multiple Choices]
A. 2.7.13.3
B. 2.3.1.318
C. 2.1.1.353
D. 2.7.11.24
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact sequence matches UniProt entry A0A194W8T8, annotated as MAP kinase kinase kinase mkh1 with EC 2.7.11.24. The entry also assigns that EC to the serine- and threonine-phosphorylation reactions and cites PubMed 39631571. This supports D as a literature-backed database annotation, though the excerpts do not independently establish the experimental methods behind it.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a eukaryotic protein-kinase domain, including characteristic catalytic-region motifs, which favors a protein kinase over the transferases in B and C and the histidine-kinase class in A. That supports a broad kinase classification, but does not establish the specific MAP kinase kinase kinase function denoted by EC 2.7.11.24.


**Missing item-specific fact**

> The protein-specific identification or functional annotation as MAPKKK Mkh1; the sequence alone does not establish that specific kinase role.


**Reason**

> The sequence offers useful grounds for recognizing a protein kinase, but the requested complete EC number is more specific than that inference. Distinguishing this MAPKKK EC from other serine/threonine protein kinases depends on protein-specific functional information absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other listed option is comparably supported by the sequence’s eukaryotic protein-kinase features. The limitation is the need for protein-specific evidence for the exact EC, not a clear tie among the choices.


### Important caveats

- The reviewer-only database evidence applies to an exact sequence match, but the author's source snapshot is unknown.
- The cited UniProt evidence codes and paper support the annotation; the supplied excerpts are not an independent review of the primary experimental data.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a eukaryotic protein-kinase domain, including characteristic catalytic-region motifs, which favors a protein kinase over the transferases in B and C and the histidine-kinase class in A. That supports a broad kinase classification, but does not establish the specific MAP kinase kinase kinase function denoted by EC 2.7.11.24.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification or functional annotation as MAPKKK Mkh1; the sequence alone does not establish that specific kinase role.",
    "reason": "The sequence offers useful grounds for recognizing a protein kinase, but the requested complete EC number is more specific than that inference. Distinguishing this MAPKKK EC from other serine/threonine protein kinases depends on protein-specific functional information absent from the input."
  },
  "case_id": "EC_number_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry A0A194W8T8, annotated as MAP kinase kinase kinase mkh1 with EC 2.7.11.24. The entry also assigns that EC to the serine- and threonine-phosphorylation reactions and cites PubMed 39631571. This supports D as a literature-backed database annotation, though the excerpts do not independently establish the experimental methods behind it."
  },
  "important_caveats": [
    "The reviewer-only database evidence applies to an exact sequence match, but the author's source snapshot is unknown.",
    "The cited UniProt evidence codes and paper support the annotation; the supplied excerpts are not an independent review of the primary experimental data."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported by the sequence’s eukaryotic protein-kinase features. The limitation is the need for protein-specific evidence for the exact EC, not a clear tie among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry A0A194W8T8, annotated as MAP kinase kinase kinase mkh1 with EC 2.7.11.24. The entry also assigns that EC to the serine- and threonine-phosphorylation reactions and cites PubMed 39631571. This supports D as a literature-backed database annotation, though the excerpts do not independently establish the experimental methods behind it.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a eukaryotic protein-kinase domain, including characteristic catalytic-region motifs, which favors a protein kinase over the transferases in B and C and the histidine-kinase class in A. That supports a broad kinase classification, but does not establish the specific MAP kinase kinase kinase function denoted by EC 2.7.11.24.",
    "missing_item_specific_fact": "The protein-specific identification or functional annotation as MAPKKK Mkh1; the sequence alone does not establish that specific kinase role.",
    "reason": "The sequence offers useful grounds for recognizing a protein kinase, but the requested complete EC number is more specific than that inference. Distinguishing this MAPKKK EC from other serine/threonine protein kinases depends on protein-specific functional information absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported by the sequence’s eukaryotic protein-kinase features. The limitation is the need for protein-specific evidence for the exact EC, not a clear tie among the choices."
  },
  "important_caveats": [
    "The reviewer-only database evidence applies to an exact sequence match, but the author's source snapshot is unknown.",
    "The cited UniProt evidence codes and paper support the annotation; the supplied excerpts are not an independent review of the primary experimental data."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A194W8T8 (MKH1_CYTMA) annotates EC=2.7.11.24 with evidence code ECO:0000305 (curator inference from PubMed:39631571). The catalytic activities listed (L-seryl-&#91;protein&#93; + ATP → O-phospho-L-seryl-&#91;protein&#93; + ADP + H+; L-threonyl-&#91;protein&#93; + ATP → O-phospho-L-threonyl-&#91;protein&#93; + ADP + H+) are consistent with EC 2.7.11.24 (MAP kinase kinase kinase). The sequence contains a canonical eukaryotic protein kinase domain with HRD motif (HRDLKADNILL), activation segment (MAPEVIRSQGEGYSAKVDIWSLGCVVLEMFAGRRPWSKDEAVGAIYKIANGETPPIPEEVSAAVTPVALSFMWDCFSVNPEERPTATKLLAEHPFCVFRDDYDFDQTELYAKIKGTWNTK), and Ser/Thr specificity features. The annotation is curator-inferred from a functional study (Diao et al. 2025) rather than direct in vitro kinetics, but the sequence evidence is fully consistent.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the sequence contains a canonical eukaryotic protein kinase domain identifiable by conserved motifs: the HRD catalytic loop (HRDLKADNILL), the DFG-equivalent activation segment, and the substrate-binding pocket (WSLGCVVLEMFAGRRPWSKDEAVGAIYKIANGETPPIPEEVSAAVTPVALSFMWDCFSVNPEERPTATKLLAEHPFCVFRDDYDFDQTELYAKIKGTWNTK). This fold is diagnostic of EC 2.7.11.x (protein kinase), immediately eliminating B (acyltransferase, EC 2.3.x) and C (methyltransferase, EC 2.1.x). Furthermore, the kinase uses a Ser/Thr phosphoryl-transfer mechanism (evidenced by the activation segment and absence of His-Asp phosphorelay domains such as HisKA or HATPase_c), eliminating A (histidine kinase, EC 2.7.13.x). Among the four choices, only D (2.7.11.24) belongs to the protein kinase class, making it the uniquely defensible answer.


**Missing item-specific fact**

> The specific 4th-digit assignment '24' (MAPKKK rather than another 2.7.11.x subtype) would require knowledge of the protein's position in the MAPK cascade or its specific substrate. However, since no other 2.7.11.x option is offered, this precision is not needed to select the correct answer from the given choices.


**Reason**

> The sequence provides clear, identifiable protein kinase domain architecture that distinguishes D from all three distractors through general enzymology knowledge (kinase fold vs. acyltransferase/methyltransferase/histidine kinase). No memorization of the specific UniProt entry is required to arrive at D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and C represent entirely different enzyme classes (histidine kinase, acyltransferase, methyltransferase) whose catalytic mechanisms and structural folds are incompatible with the observed protein kinase domain. Only D is a protein kinase (EC 2.7.11.x), leaving no ambiguity among the choices.


### Important caveats

- The EC annotation carries evidence code ECO:0000305 (inferred by curator from PubMed:39631571), not direct in vitro kinetic characterization. The functional paper describes genetic/biochemical pathway evidence rather than purified-enzyme kinetics.
- The annotation was first added in June 2025 (entry version 32, first public date 2025-06-18); the historical snapshot at entry version 30 (January 2026) already contains the EC assignment, so the benchmark likely used a post-2025 annotation.
- The 4th digit '24' specifically denotes MAPKKK; distinguishing this from other 2.7.11.x kinases (e.g., 2.7.11.1, 2.7.11.22) would require cascade-position knowledge, but this is not needed here as no competing 2.7.11.x option is presented.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the sequence contains a canonical eukaryotic protein kinase domain identifiable by conserved motifs: the HRD catalytic loop (HRDLKADNILL), the DFG-equivalent activation segment, and the substrate-binding pocket (WSLGCVVLEMFAGRRPWSKDEAVGAIYKIANGETPPIPEEVSAAVTPVALSFMWDCFSVNPEERPTATKLLAEHPFCVFRDDYDFDQTELYAKIKGTWNTK). This fold is diagnostic of EC 2.7.11.x (protein kinase), immediately eliminating B (acyltransferase, EC 2.3.x) and C (methyltransferase, EC 2.1.x). Furthermore, the kinase uses a Ser/Thr phosphoryl-transfer mechanism (evidenced by the activation segment and absence of His-Asp phosphorelay domains such as HisKA or HATPase_c), eliminating A (histidine kinase, EC 2.7.13.x). Among the four choices, only D (2.7.11.24) belongs to the protein kinase class, making it the uniquely defensible answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific 4th-digit assignment '24' (MAPKKK rather than another 2.7.11.x subtype) would require knowledge of the protein's position in the MAPK cascade or its specific substrate. However, since no other 2.7.11.x option is offered, this precision is not needed to select the correct answer from the given choices.",
    "reason": "The sequence provides clear, identifiable protein kinase domain architecture that distinguishes D from all three distractors through general enzymology knowledge (kinase fold vs. acyltransferase/methyltransferase/histidine kinase). No memorization of the specific UniProt entry is required to arrive at D."
  },
  "case_id": "EC_number_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A194W8T8 (MKH1_CYTMA) annotates EC=2.7.11.24 with evidence code ECO:0000305 (curator inference from PubMed:39631571). The catalytic activities listed (L-seryl-[protein] + ATP → O-phospho-L-seryl-[protein] + ADP + H+; L-threonyl-[protein] + ATP → O-phospho-L-threonyl-[protein] + ADP + H+) are consistent with EC 2.7.11.24 (MAP kinase kinase kinase). The sequence contains a canonical eukaryotic protein kinase domain with HRD motif (HRDLKADNILL), activation segment (MAPEVIRSQGEGYSAKVDIWSLGCVVLEMFAGRRPWSKDEAVGAIYKIANGETPPIPEEVSAAVTPVALSFMWDCFSVNPEERPTATKLLAEHPFCVFRDDYDFDQTELYAKIKGTWNTK), and Ser/Thr specificity features. The annotation is curator-inferred from a functional study (Diao et al. 2025) rather than direct in vitro kinetics, but the sequence evidence is fully consistent."
  },
  "important_caveats": [
    "The EC annotation carries evidence code ECO:0000305 (inferred by curator from PubMed:39631571), not direct in vitro kinetic characterization. The functional paper describes genetic/biochemical pathway evidence rather than purified-enzyme kinetics.",
    "The annotation was first added in June 2025 (entry version 32, first public date 2025-06-18); the historical snapshot at entry version 30 (January 2026) already contains the EC assignment, so the benchmark likely used a post-2025 annotation.",
    "The 4th digit '24' specifically denotes MAPKKK; distinguishing this from other 2.7.11.x kinases (e.g., 2.7.11.1, 2.7.11.22) would require cascade-position knowledge, but this is not needed here as no competing 2.7.11.x option is presented."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C represent entirely different enzyme classes (histidine kinase, acyltransferase, methyltransferase) whose catalytic mechanisms and structural folds are incompatible with the observed protein kinase domain. Only D is a protein kinase (EC 2.7.11.x), leaving no ambiguity among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A194W8T8 (MKH1_CYTMA) annotates EC=2.7.11.24 with evidence code ECO:0000305 (curator inference from PubMed:39631571). The catalytic activities listed (L-seryl-[protein] + ATP → O-phospho-L-seryl-[protein] + ADP + H+; L-threonyl-[protein] + ATP → O-phospho-L-threonyl-[protein] + ADP + H+) are consistent with EC 2.7.11.24 (MAP kinase kinase kinase). The sequence contains a canonical eukaryotic protein kinase domain with HRD motif (HRDLKADNILL), activation segment (MAPEVIRSQGEGYSAKVDIWSLGCVVLEMFAGRRPWSKDEAVGAIYKIANGETPPIPEEVSAAVTPVALSFMWDCFSVNPEERPTATKLLAEHPFCVFRDDYDFDQTELYAKIKGTWNTK), and Ser/Thr specificity features. The annotation is curator-inferred from a functional study (Diao et al. 2025) rather than direct in vitro kinetics, but the sequence evidence is fully consistent.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the sequence contains a canonical eukaryotic protein kinase domain identifiable by conserved motifs: the HRD catalytic loop (HRDLKADNILL), the DFG-equivalent activation segment, and the substrate-binding pocket (WSLGCVVLEMFAGRRPWSKDEAVGAIYKIANGETPPIPEEVSAAVTPVALSFMWDCFSVNPEERPTATKLLAEHPFCVFRDDYDFDQTELYAKIKGTWNTK). This fold is diagnostic of EC 2.7.11.x (protein kinase), immediately eliminating B (acyltransferase, EC 2.3.x) and C (methyltransferase, EC 2.1.x). Furthermore, the kinase uses a Ser/Thr phosphoryl-transfer mechanism (evidenced by the activation segment and absence of His-Asp phosphorelay domains such as HisKA or HATPase_c), eliminating A (histidine kinase, EC 2.7.13.x). Among the four choices, only D (2.7.11.24) belongs to the protein kinase class, making it the uniquely defensible answer.",
    "missing_item_specific_fact": "The specific 4th-digit assignment '24' (MAPKKK rather than another 2.7.11.x subtype) would require knowledge of the protein's position in the MAPK cascade or its specific substrate. However, since no other 2.7.11.x option is offered, this precision is not needed to select the correct answer from the given choices.",
    "reason": "The sequence provides clear, identifiable protein kinase domain architecture that distinguishes D from all three distractors through general enzymology knowledge (kinase fold vs. acyltransferase/methyltransferase/histidine kinase). No memorization of the specific UniProt entry is required to arrive at D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and C represent entirely different enzyme classes (histidine kinase, acyltransferase, methyltransferase) whose catalytic mechanisms and structural folds are incompatible with the observed protein kinase domain. Only D is a protein kinase (EC 2.7.11.x), leaving no ambiguity among the choices."
  },
  "important_caveats": [
    "The EC annotation carries evidence code ECO:0000305 (inferred by curator from PubMed:39631571), not direct in vitro kinetic characterization. The functional paper describes genetic/biochemical pathway evidence rather than purified-enzyme kinetics.",
    "The annotation was first added in June 2025 (entry version 32, first public date 2025-06-18); the historical snapshot at entry version 30 (January 2026) already contains the EC assignment, so the benchmark likely used a post-2025 annotation.",
    "The 4th digit '24' specifically denotes MAPKKK; distinguishing this from other 2.7.11.x kinases (e.g., 2.7.11.1, 2.7.11.22) would require cascade-position knowledge, but this is not needed here as no competing 2.7.11.x option is presented."
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

**Accession:** `A0A194W8T8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.396358+00:00.  

```json
"A0A194W8T8"
```

Source SHA-256: `1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.396358+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39631571","source":"PubMed"}],"value":"2.7.11.24"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39631571","source":"PubMed"}],"value":"Mitogen-activated protein kinase kinase kinase mkh1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39631571","source":"PubMed"}],"value":"MAP kinase kinase kinase mkh1"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"39631571","source":"PubMed"}],"value":"MAPKKK mkh1"}]}}
```

Source SHA-256: `1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.396358+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"39631571","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:17990"}}],"reaction":{"ecNumber":"2.7.11.24","evidences":[{"evidenceCode":"ECO:0000305","id":"39631571","source":"PubMed"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.396358+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"39631571","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:46609"}}],"reaction":{"ecNumber":"2.7.11.24","evidences":[{"evidenceCode":"ECO:0000305","id":"39631571","source":"PubMed"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.396358+00:00.  

```json
{"citation":{"authors":["Diao Y.","Xiong X.","Jin J.","Yu C.","Tian Y.","Zhao C.","Wu Y.","Liu H."],"citationCrossReferences":[{"database":"PubMed","id":"39631571"},{"database":"DOI","id":"10.1016/j.micpath.2024.107194"}],"citationType":"journal article","firstPage":"107194","id":"39631571","journal":"Microb. Pathog.","lastPage":"107194","publicationDate":"2025","title":"Mitogen-activated protein (MAP) kinase signalling pathway VmMkh1-VmMkk1-VmSpm1 regulates cell wall integrity in Valsamali.","volume":"198"},"referenceNumber":2,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:22.695404+00:00.  

```text
DE   RecName: Full=Mitogen-activated protein kinase kinase kinase mkh1 {ECO:0000303|PubMed:39631571};
DE            Short=MAP kinase kinase kinase mkh1 {ECO:0000303|PubMed:39631571};
DE            Short=MAPKKK mkh1 {ECO:0000303|PubMed:39631571};
DE            EC=2.7.11.24 {ECO:0000305|PubMed:39631571};
```

Source SHA-256: `d8496e59b0240fb2d9db3c0360daa33c12604e1a19d07fbf3a81c8ec7bbcdb1a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30)  
**Locator:** `lines 37-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:22.695404+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.24;
CC         Evidence={ECO:0000305|PubMed:39631571};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:17990;
CC         Evidence={ECO:0000305|PubMed:39631571};
```

Source SHA-256: `d8496e59b0240fb2d9db3c0360daa33c12604e1a19d07fbf3a81c8ec7bbcdb1a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30)  
**Locator:** `lines 45-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:22.695404+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.24;
CC         Evidence={ECO:0000305|PubMed:39631571};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:46609;
CC         Evidence={ECO:0000305|PubMed:39631571};
```

Source SHA-256: `d8496e59b0240fb2d9db3c0360daa33c12604e1a19d07fbf3a81c8ec7bbcdb1a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 13. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
