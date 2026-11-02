# cofactor_0014

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **D** — pantetheine 4&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASSALTPVAIVGYACKLPGDVSSPDDLWELCSRGRTGWGPTPSTRYSKDAYYHPAPGKHGCINTEGGYFLKEDPARFDAPFFNMTIQEATALDPQQRLLLECTFEAFENSGMTKEGIAGKDIGVFVGGSFADYEVNNTRDIDTAPTYQATGCAPAMQSNRLSYYFDLRGPSMTVDTACSSSLVALHSAMQSLRNGESSSAVVAAAHLNLTPDFFVTMSNTQLLNDAGKTFAFDHRAISGFARGEGAGSMILKPLDAAIRDGDVIRAVIHNSGVNQDGKTNGITVPNGRAQSDLIKQVYSKAGLDPAECGFSECHGTGTKVGDPIEVAGIHEALGAGRSPRNPLFIGSVKSNVGHLEGASGIVSVIKAAMMLEKGMVLPNANFETANPNIPLEQYNMKVPTSTRPWPRGKKYVSVSNYGFGGANAHVVLGAAPKGLKTTMTTIRSLEDAPEEPLCKLFVLSAHDSQALQKEITDLGVFLEQRPEVFEKLLAGNVAYTLGERRSHLPCRLAIAAVSSDELGQSLATTKVPTFRARNEPTLGFVFTGQGAQWATMGAELARDYPIFAAALDTADDTLKALGADFSLKEEMLKPADISLINAAHISQPACTALQIALTMLLSSWGIHPAAVVGHSSGEIGCAFAAGIIGLEDAMKIAYYRGQCMLSLKKKAVGKPQGTMMAVGTSAENVRPLLDAVSKGYITVACINSPASVTLSGDVEAVEELQPILTEKSIFNRQLKVGVAYHSAHLEPVVDEYLDLIKNIQPASTATATFYSSLLGRVAEASELTPEYWVQNLTSPVRFSGGLSAMARETGSKTIDHLVELGPHSALQGPIRDTLATIDAAKGKMHYVSVLARGQNASECALRMAGALYMKGLSLTFGEINFPRTKSVNQKLITDLPRYPFNHETRYWHESRLAQKHCFKEGGRNDLLGSLADWSNDLEPTWRNIVKLDDLPFLRSHKMQDMPVFPMAGYMGMALEAAARRAIARGVQFDRFEIREFVVSSALVFNEDTDVEMTITLKPYSEGLRGAASDLWDDYKICSWDAKRGWLQHCHGLVGVRNSPAANAVDAHRIQSASKAFEACKASIISASTETVDVQAMYNTLTTIGAGYGPVFTGLEPCQASDTTAHAQLVVPDTKSLMPKGYETELIVHPALLDQIIQIVWPIFGAGRQGLDTLYMPTFVKNFSISRNFASMLGNGLEVFGAGAPNNEAPEPTKFGFFVVGSSDASEPLVQFDGLTMTPLRESSGSSGPQARELCYKIDWQTVSDEDIGLEKSSSDASDTPIKADSLVSTPFTRDEAVCVVYNKATEKDLAAEVADNVWKTSGVQAELVTLSKVIPADKRVIFVSTGNNVLSGIDATMFGTLRQMLLSARKVLWIYKEGPDVDDVDGSMVVGFTRAIRSETSANIVTLGLQQATGKTLVENIFTVLTKTSADSPSTFKDDKEFILKGDDLLVPKVVDDEELNVRLHQESQDSVIYQQPFAQSDRRLKMVIATLGSLDSFYFVDDEPKPLNDNEVEIEVKATGMNFKDVVVSMGQLNQPYIGVECAGVIAAVGKKVTDVKVGQSVMAMTEGAYSTYARCLSTSVAPLPEKMDFTAASTIPVVFCTAYYGLFDLGRLTEGESVLIHAAAGGVGQAAIMLAQTCGAEIFATVGSLDKKQHIVKEYGIPEDHIFYSRDTAFGPAIRQVTGGKGVDVVLNSLGGDFLRESWDCLAPFGRFIEIGKADITKNSRLEMAQFEYNVSFASVDLTKVAAYKPKLMKRLLNDVEKLMSSGSIRPVGPITSYGINDVEAAFRSLQSGKSMGKLVIAPQSGDSVQAIAPKKTATLFKEDASYLIVGGTGGLGCSIARWMASRGAKHICLSSRRANITPRLEALITDLSILGTKVSVRACDVADAGSVETLVKDLKKESPIRGVIQGAMVLKDVLYEQMTLDDFSAVVNPKVAGTLNLHNSLGTSELDFFIALSSVAGVVGNRGQAAYAAANVFLDTFMAHRKAQGLPGTSLDLTAVSDVGYLADNSERAADVLRNLGGETIEESEILGLLTAAVTGKITASNNHVITGLKINPGSEPFWCHDAKFSNLLAAAASQSSAEGGNANIPLPQALKSAANGEKALEVLYGALVTKLAAVLMLSVEEMEPSAAVASYSLDSLAAIEVRNWIAREADANVQVLELLTSPSLMELAKLISKKSKLVSFE

[Multiple Choices]
A. Na(+)
B. [2Fe-2S] cluster
C. pyridoxal 5'-phosphate
D. pantetheine 4'-phosphate
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

> The sequence matches the annotated PKS1 entry, which assigns pantetheine 4'-phosphate as a cofactor. The assignment is supported by a PROSITE-ProRule annotation, rather than direct experimental evidence in the supplied material. This is biologically consistent with the phosphopantetheine-modified ACP domain of a polyketide synthase.

Citations as saved: [C1](#evidence-c1), [H1](#evidence-h1), [H4](#evidence-h4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, multidomain sequence is consistent with a highly reducing polyketide synthase containing an ACP carrier domain. ACP domains require a 4'-phosphopantetheine arm for acyl-group transfer, distinguishing choice D from sodium, an iron-sulfur cluster, and PLP.


**Missing item-specific fact**

> No protein-specific external annotation is strictly needed for this biological inference. Direct evidence that this particular protein is modified or experimentally requires the cofactor is not supplied.


**Reason**

> Recognizing the PKS/ACP architecture and applying the general phosphopantetheinylation requirement provides a concrete basis for choosing D; the external annotation corroborates the choice but is not the only basis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, pantetheine 4'-phosphate is the relevant cofactor for an ACP-containing polyketide synthase.


### Important caveats

- The sequence-matched UniProt cofactor annotation is computational, based on a PROSITE-ProRule; the supplied evidence does not establish direct experimental verification for this protein.
- The cited database entry and sequence identity are reviewer-only evidence, not information provided to the original model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, multidomain sequence is consistent with a highly reducing polyketide synthase containing an ACP carrier domain. ACP domains require a 4'-phosphopantetheine arm for acyl-group transfer, distinguishing choice D from sodium, an iron-sulfur cluster, and PLP.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific external annotation is strictly needed for this biological inference. Direct evidence that this particular protein is modified or experimentally requires the cofactor is not supplied.",
    "reason": "Recognizing the PKS/ACP architecture and applying the general phosphopantetheinylation requirement provides a concrete basis for choosing D; the external annotation corroborates the choice but is not the only basis."
  },
  "case_id": "cofactor_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "H1",
      "H4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated PKS1 entry, which assigns pantetheine 4'-phosphate as a cofactor. The assignment is supported by a PROSITE-ProRule annotation, rather than direct experimental evidence in the supplied material. This is biologically consistent with the phosphopantetheine-modified ACP domain of a polyketide synthase."
  },
  "important_caveats": [
    "The sequence-matched UniProt cofactor annotation is computational, based on a PROSITE-ProRule; the supplied evidence does not establish direct experimental verification for this protein.",
    "The cited database entry and sequence identity are reviewer-only evidence, not information provided to the original model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, pantetheine 4'-phosphate is the relevant cofactor for an ACP-containing polyketide synthase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated PKS1 entry, which assigns pantetheine 4'-phosphate as a cofactor. The assignment is supported by a PROSITE-ProRule annotation, rather than direct experimental evidence in the supplied material. This is biologically consistent with the phosphopantetheine-modified ACP domain of a polyketide synthase.",
    "evidence_ids": ["C1", "H1", "H4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, multidomain sequence is consistent with a highly reducing polyketide synthase containing an ACP carrier domain. ACP domains require a 4'-phosphopantetheine arm for acyl-group transfer, distinguishing choice D from sodium, an iron-sulfur cluster, and PLP.",
    "missing_item_specific_fact": "No protein-specific external annotation is strictly needed for this biological inference. Direct evidence that this particular protein is modified or experimentally requires the cofactor is not supplied.",
    "reason": "Recognizing the PKS/ACP architecture and applying the general phosphopantetheinylation requirement provides a concrete basis for choosing D; the external annotation corroborates the choice but is not the only basis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, pantetheine 4'-phosphate is the relevant cofactor for an ACP-containing polyketide synthase."
  },
  "important_caveats": [
    "The sequence-matched UniProt cofactor annotation is computational, based on a PROSITE-ProRule; the supplied evidence does not establish direct experimental verification for this protein.",
    "The cited database entry and sequence identity are reviewer-only evidence, not information provided to the original model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5, H4) explicitly lists pantetheine 4'-phosphate (ChEBI:CHEBI:47942) as the cofactor for this protein (A0A172QE52, Highly-reducing polyketide synthase 1 from Aureobasidium melanogenum). The evidence code is ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule PRU00258), meaning the annotation is computational/profiler-based rather than direct experimental measurement on this specific protein. However, the requirement of 4'-phosphopantetheine as a prosthetic group in polyketide synthases is one of the most well-established facts in biochemistry, demonstrated experimentally across dozens of PKS and FAS systems. The protein is a 2190-AA multi-domain fungal HR-PKS with EC 2.3.1.- (acyltransferase), consistent with phosphopantetheine-dependent thioester chemistry. The answer is strongly supported by both the database annotation and the universal biochemistry of the enzyme class.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 2190-AA sequence exhibits a multi-domain architecture characteristic of fungal polyketide synthases (or fatty acid synthases): recognizable acyltransferase motifs (GGS near N-terminus), ketosynthase, ketoreductase, dehydratase, enoylreductase, acyl-carrier protein (GGTGGLGCSIARW with serine attachment site), and thioesterase domains. All PKS and FAS enzymes universally require 4'-phosphopantetheine as a prosthetic group covalently attached to the ACP serine to carry the growing acyl chain. Among the four choices, only pantetheine 4'-phosphate is consistent with a multi-domain (~2000+ AA) acyl-transferase/thioesterase enzyme. Na+ is not a cofactor for this enzyme class; &#91;2Fe-2S&#93; clusters belong to small electron-transfer proteins; PLP is the cofactor for single-domain aminotransferases/decarboxylases (~400-500 AA). The protein size and domain architecture allow elimination of A, B, and C through general enzymological knowledge.


**Missing item-specific fact**

> None critical. Identifying the exact domain boundaries from a raw 2190-AA sequence without bioinformatics tools is challenging, but the overall multi-domain architecture, protein length, and presence of recognizable motifs (GGS, GGTGGLGCSIARW, HHH-motif TE domain) provide sufficient grounds for a trained biochemist to infer PKS/FAS identity and thus phosphopantetheine dependence.


**Reason**

> The reasoning chain—large multi-domain sequence → PKS/FAS architecture → universal phosphopantetheine requirement—is grounded in well-established general biochemistry. The distractors are eliminated by protein size, domain count, and enzyme-class logic. No protein-specific experimental measurement or obscure database fact is needed beyond recognizing the enzyme class.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent mechanistically distinct cofactor classes (monovalent cation, iron-sulfur cluster, vitamin B6 derivative, phosphopantetheine arm). A 2190-AA multi-domain acyltransferase/thioesterase enzyme is incompatible with Na+, &#91;2Fe-2S&#93;, or PLP. Only pantetheine 4'-phosphate fits the enzyme class. No ambiguity among options.


### Important caveats

- The UniProt cofactor annotation carries evidence code ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule PRU00258), not direct experimental evidence on this specific protein. However, phosphopantetheine in PKS is experimentally validated across many homologous systems.
- The protein was integrated into Swiss-Prot only on 2025-02-05; the benchmark author's source snapshot date is unknown. The sequence (version 1, unchanged since 2016) matches in all checked versions.
- Identifying domain architecture from a raw 2190-AA sequence without computational tools is non-trivial but feasible for an expert; the question does not provide domain annotations or functional context beyond the sequence itself.
- The identity origin (accession A0A172QE52) was inferred from dataset metadata and was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 2190-AA sequence exhibits a multi-domain architecture characteristic of fungal polyketide synthases (or fatty acid synthases): recognizable acyltransferase motifs (GGS near N-terminus), ketosynthase, ketoreductase, dehydratase, enoylreductase, acyl-carrier protein (GGTGGLGCSIARW with serine attachment site), and thioesterase domains. All PKS and FAS enzymes universally require 4'-phosphopantetheine as a prosthetic group covalently attached to the ACP serine to carry the growing acyl chain. Among the four choices, only pantetheine 4'-phosphate is consistent with a multi-domain (~2000+ AA) acyl-transferase/thioesterase enzyme. Na+ is not a cofactor for this enzyme class; [2Fe-2S] clusters belong to small electron-transfer proteins; PLP is the cofactor for single-domain aminotransferases/decarboxylases (~400-500 AA). The protein size and domain architecture allow elimination of A, B, and C through general enzymological knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Identifying the exact domain boundaries from a raw 2190-AA sequence without bioinformatics tools is challenging, but the overall multi-domain architecture, protein length, and presence of recognizable motifs (GGS, GGTGGLGCSIARW, HHH-motif TE domain) provide sufficient grounds for a trained biochemist to infer PKS/FAS identity and thus phosphopantetheine dependence.",
    "reason": "The reasoning chain—large multi-domain sequence → PKS/FAS architecture → universal phosphopantetheine requirement—is grounded in well-established general biochemistry. The distractors are eliminated by protein size, domain count, and enzyme-class logic. No protein-specific experimental measurement or obscure database fact is needed beyond recognizing the enzyme class."
  },
  "case_id": "cofactor_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H4) explicitly lists pantetheine 4'-phosphate (ChEBI:CHEBI:47942) as the cofactor for this protein (A0A172QE52, Highly-reducing polyketide synthase 1 from Aureobasidium melanogenum). The evidence code is ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule PRU00258), meaning the annotation is computational/profiler-based rather than direct experimental measurement on this specific protein. However, the requirement of 4'-phosphopantetheine as a prosthetic group in polyketide synthases is one of the most well-established facts in biochemistry, demonstrated experimentally across dozens of PKS and FAS systems. The protein is a 2190-AA multi-domain fungal HR-PKS with EC 2.3.1.- (acyltransferase), consistent with phosphopantetheine-dependent thioester chemistry. The answer is strongly supported by both the database annotation and the universal biochemistry of the enzyme class."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule PRU00258), not direct experimental evidence on this specific protein. However, phosphopantetheine in PKS is experimentally validated across many homologous systems.",
    "The protein was integrated into Swiss-Prot only on 2025-02-05; the benchmark author's source snapshot date is unknown. The sequence (version 1, unchanged since 2016) matches in all checked versions.",
    "Identifying domain architecture from a raw 2190-AA sequence without computational tools is non-trivial but feasible for an expert; the question does not provide domain annotations or functional context beyond the sequence itself.",
    "The identity origin (accession A0A172QE52) was inferred from dataset metadata and was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct cofactor classes (monovalent cation, iron-sulfur cluster, vitamin B6 derivative, phosphopantetheine arm). A 2190-AA multi-domain acyltransferase/thioesterase enzyme is incompatible with Na+, [2Fe-2S], or PLP. Only pantetheine 4'-phosphate fits the enzyme class. No ambiguity among options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5, H4) explicitly lists pantetheine 4'-phosphate (ChEBI:CHEBI:47942) as the cofactor for this protein (A0A172QE52, Highly-reducing polyketide synthase 1 from Aureobasidium melanogenum). The evidence code is ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule PRU00258), meaning the annotation is computational/profiler-based rather than direct experimental measurement on this specific protein. However, the requirement of 4'-phosphopantetheine as a prosthetic group in polyketide synthases is one of the most well-established facts in biochemistry, demonstrated experimentally across dozens of PKS and FAS systems. The protein is a 2190-AA multi-domain fungal HR-PKS with EC 2.3.1.- (acyltransferase), consistent with phosphopantetheine-dependent thioester chemistry. The answer is strongly supported by both the database annotation and the universal biochemistry of the enzyme class.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 2190-AA sequence exhibits a multi-domain architecture characteristic of fungal polyketide synthases (or fatty acid synthases): recognizable acyltransferase motifs (GGS near N-terminus), ketosynthase, ketoreductase, dehydratase, enoylreductase, acyl-carrier protein (GGTGGLGCSIARW with serine attachment site), and thioesterase domains. All PKS and FAS enzymes universally require 4'-phosphopantetheine as a prosthetic group covalently attached to the ACP serine to carry the growing acyl chain. Among the four choices, only pantetheine 4'-phosphate is consistent with a multi-domain (~2000+ AA) acyl-transferase/thioesterase enzyme. Na+ is not a cofactor for this enzyme class; [2Fe-2S] clusters belong to small electron-transfer proteins; PLP is the cofactor for single-domain aminotransferases/decarboxylases (~400-500 AA). The protein size and domain architecture allow elimination of A, B, and C through general enzymological knowledge.",
    "missing_item_specific_fact": "None critical. Identifying the exact domain boundaries from a raw 2190-AA sequence without bioinformatics tools is challenging, but the overall multi-domain architecture, protein length, and presence of recognizable motifs (GGS, GGTGGLGCSIARW, HHH-motif TE domain) provide sufficient grounds for a trained biochemist to infer PKS/FAS identity and thus phosphopantetheine dependence.",
    "reason": "The reasoning chain—large multi-domain sequence → PKS/FAS architecture → universal phosphopantetheine requirement—is grounded in well-established general biochemistry. The distractors are eliminated by protein size, domain count, and enzyme-class logic. No protein-specific experimental measurement or obscure database fact is needed beyond recognizing the enzyme class."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct cofactor classes (monovalent cation, iron-sulfur cluster, vitamin B6 derivative, phosphopantetheine arm). A 2190-AA multi-domain acyltransferase/thioesterase enzyme is incompatible with Na+, [2Fe-2S], or PLP. Only pantetheine 4'-phosphate fits the enzyme class. No ambiguity among options."
  },
  "important_caveats": [
    "The UniProt cofactor annotation carries evidence code ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule PRU00258), not direct experimental evidence on this specific protein. However, phosphopantetheine in PKS is experimentally validated across many homologous systems.",
    "The protein was integrated into Swiss-Prot only on 2025-02-05; the benchmark author's source snapshot date is unknown. The sequence (version 1, unchanged since 2016) matches in all checked versions.",
    "Identifying domain architecture from a raw 2190-AA sequence without computational tools is non-trivial but feasible for an expert; the question does not provide domain annotations or functional context beyond the sequence itself.",
    "The identity origin (accession A0A172QE52) was inferred from dataset metadata and was not available to the evaluated model."
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

**Accession:** `A0A172QE52` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:28.395908+00:00.  

```json
"A0A172QE52"
```

Source SHA-256: `16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:28.395908+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"Liamocins biosynthesis cluster protein PKS1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"32003433","source":"PubMed"}],"value":"1.-.-.-"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"32003433","source":"PubMed"}],"value":"2.3.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"Highly-reducing polyketide synthase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"32003433","source":"PubMed"}],"value":"HR-PKS PKS1"}]}}
```

Source SHA-256: `16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:28.395908+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:47942"},"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00258","source":"PROSITE-ProRule"}],"name":"pantetheine 4'-phosphate"}],"commentType":"COFACTOR"}
```

Source SHA-256: `16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:31.251331+00:00.  

```text
ID   PKS1_AURME              Reviewed;        2190 AA.
AC   A0A172QE52;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   07-SEP-2016, sequence version 1.
DT   28-JAN-2026, entry version 38.
DE   RecName: Full=Highly-reducing polyketide synthase 1 {ECO:0000303|PubMed:32003433};
DE            Short=HR-PKS PKS1 {ECO:0000303|PubMed:32003433};
DE            EC=1.-.-.- {ECO:0000269|PubMed:32003433};
DE            EC=2.3.1.- {ECO:0000269|PubMed:32003433};
DE   AltName: Full=Liamocins biosynthesis cluster protein PKS1 {ECO:0000303|PubMed:32003433};
GN   Name=PKS1 {ECO:0000303|PubMed:32003433};
OS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.
OX   NCBI_TaxID=46634;
```

Source SHA-256: `52e514130a97f47329d9a3516f69b151be6460d3cc32144e6d797ab41a405440`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:31.251331+00:00.  

```text
DE   RecName: Full=Highly-reducing polyketide synthase 1 {ECO:0000303|PubMed:32003433};
DE            Short=HR-PKS PKS1 {ECO:0000303|PubMed:32003433};
DE            EC=1.-.-.- {ECO:0000269|PubMed:32003433};
DE            EC=2.3.1.- {ECO:0000269|PubMed:32003433};
DE   AltName: Full=Liamocins biosynthesis cluster protein PKS1 {ECO:0000303|PubMed:32003433};
```

Source SHA-256: `52e514130a97f47329d9a3516f69b151be6460d3cc32144e6d797ab41a405440`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38)  
**Locator:** `lines 70-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:31.251331+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=pantetheine 4'-phosphate; Xref=ChEBI:CHEBI:47942;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00258};
```

Source SHA-256: `52e514130a97f47329d9a3516f69b151be6460d3cc32144e6d797ab41a405440`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 14. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
