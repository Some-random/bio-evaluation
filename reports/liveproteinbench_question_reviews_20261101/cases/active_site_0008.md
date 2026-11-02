# active_site_0008

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **A** — Position 179 (For beta-ketoacyl synthase activity)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASSALTPVAIVGYACKLPGDVSSPDDLWELCSRGRTGWGPTPSTRYSKDAYYHPAPGKHGCINTEGGYFLKEDPARFDAPFFNMTIQEATALDPQQRLLLECTFEAFENSGMTKEGIAGKDIGVFVGGSFADYEVNNTRDIDTAPTYQATGCAPAMQSNRLSYYFDLRGPSMTVDTACSSSLVALHSAMQSLRNGESSSAVVAAAHLNLTPDFFVTMSNTQLLNDAGKTFAFDHRAISGFARGEGAGSMILKPLDAAIRDGDVIRAVIHNSGVNQDGKTNGITVPNGRAQSDLIKQVYSKAGLDPAECGFSECHGTGTKVGDPIEVAGIHEALGAGRSPRNPLFIGSVKSNVGHLEGASGIVSVIKAAMMLEKGMVLPNANFETANPNIPLEQYNMKVPTSTRPWPRGKKYVSVSNYGFGGANAHVVLGAAPKGLKTTMTTIRSLEDAPEEPLCKLFVLSAHDSQALQKEITDLGVFLEQRPEVFEKLLAGNVAYTLGERRSHLPCRLAIAAVSSDELGQSLATTKVPTFRARNEPTLGFVFTGQGAQWATMGAELARDYPIFAAALDTADDTLKALGADFSLKEEMLKPADISLINAAHISQPACTALQIALTMLLSSWGIHPAAVVGHSSGEIGCAFAAGIIGLEDAMKIAYYRGQCMLSLKKKAVGKPQGTMMAVGTSAENVRPLLDAVSKGYITVACINSPASVTLSGDVEAVEELQPILTEKSIFNRQLKVGVAYHSAHLEPVVDEYLDLIKNIQPASTATATFYSSLLGRVAEASELTPEYWVQNLTSPVRFSGGLSAMARETGSKTIDHLVELGPHSALQGPIRDTLATIDAAKGKMHYVSVLARGQNASECALRMAGALYMKGLSLTFGEINFPRTKSVNQKLITDLPRYPFNHETRYWHESRLAQKHCFKEGGRNDLLGSLADWSNDLEPTWRNIVKLDDLPFLRSHKMQDMPVFPMAGYMGMALEAAARRAIARGVQFDRFEIREFVVSSALVFNEDTDVEMTITLKPYSEGLRGAASDLWDDYKICSWDAKRGWLQHCHGLVGVRNSPAANAVDAHRIQSASKAFEACKASIISASTETVDVQAMYNTLTTIGAGYGPVFTGLEPCQASDTTAHAQLVVPDTKSLMPKGYETELIVHPALLDQIIQIVWPIFGAGRQGLDTLYMPTFVKNFSISRNFASMLGNGLEVFGAGAPNNEAPEPTKFGFFVVGSSDASEPLVQFDGLTMTPLRESSGSSGPQARELCYKIDWQTVSDEDIGLEKSSSDASDTPIKADSLVSTPFTRDEAVCVVYNKATEKDLAAEVADNVWKTSGVQAELVTLSKVIPADKRVIFVSTGNNVLSGIDATMFGTLRQMLLSARKVLWIYKEGPDVDDVDGSMVVGFTRAIRSETSANIVTLGLQQATGKTLVENIFTVLTKTSADSPSTFKDDKEFILKGDDLLVPKVVDDEELNVRLHQESQDSVIYQQPFAQSDRRLKMVIATLGSLDSFYFVDDEPKPLNDNEVEIEVKATGMNFKDVVVSMGQLNQPYIGVECAGVIAAVGKKVTDVKVGQSVMAMTEGAYSTYARCLSTSVAPLPEKMDFTAASTIPVVFCTAYYGLFDLGRLTEGESVLIHAAAGGVGQAAIMLAQTCGAEIFATVGSLDKKQHIVKEYGIPEDHIFYSRDTAFGPAIRQVTGGKGVDVVLNSLGGDFLRESWDCLAPFGRFIEIGKADITKNSRLEMAQFEYNVSFASVDLTKVAAYKPKLMKRLLNDVEKLMSSGSIRPVGPITSYGINDVEAAFRSLQSGKSMGKLVIAPQSGDSVQAIAPKKTATLFKEDASYLIVGGTGGLGCSIARWMASRGAKHICLSSRRANITPRLEALITDLSILGTKVSVRACDVADAGSVETLVKDLKKESPIRGVIQGAMVLKDVLYEQMTLDDFSAVVNPKVAGTLNLHNSLGTSELDFFIALSSVAGVVGNRGQAAYAAANVFLDTFMAHRKAQGLPGTSLDLTAVSDVGYLADNSERAADVLRNLGGETIEESEILGLLTAAVTGKITASNNHVITGLKINPGSEPFWCHDAKFSNLLAAAASQSSAEGGNANIPLPQALKSAANGEKALEVLYGALVTKLAAVLMLSVEEMEPSAAVASYSLDSLAAIEVRNWIAREADANVQVLELLTSPSLMELAKLISKKSKLVSFE

[Multiple Choices]
A. Position 179 (For beta-ketoacyl synthase activity)
B. Position 157 (Proton acceptor)
C. Position 968 (For acyl/malonyl transferase activity)
D. Position 1045 (Proton acceptor; for dehydratase activity)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The exact supplied sequence matches the annotated PKS1 sequence. UniProt records position 179 as an active site for beta-ketoacyl synthase activity, supporting choice A. This is a PROSITE-ProRule computational annotation, not evidence of direct experimental measurement.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices suggest a multidomain polyketide synthase, so the listed catalytic functions are biologically plausible; that alone does not establish the exact active-site position or distinguish position 179 from the alternatives.


**Missing item-specific fact**

> The protein-specific active-site annotation mapping residue 179 to beta-ketoacyl synthase activity.


**Reason**

> Selecting the keyed residue requires a specific residue-to-function assignment absent from the input. Recognizing the protein or recalling its database annotation would be lookup or memorization, not sequence-based reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed options, the matching annotation supports A; the other positions and functions do not match the cited active-site annotation.


### Important caveats

- The supporting active-site assignment is computationally annotated by PROSITE-ProRule; the supplied evidence does not establish experimental validation.
- The protein has other annotated catalytic residues, but they are not listed as matching options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices suggest a multidomain polyketide synthase, so the listed catalytic functions are biologically plausible; that alone does not establish the exact active-site position or distinguish position 179 from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific active-site annotation mapping residue 179 to beta-ketoacyl synthase activity.",
    "reason": "Selecting the keyed residue requires a specific residue-to-function assignment absent from the input. Recognizing the protein or recalling its database annotation would be lookup or memorization, not sequence-based reasoning."
  },
  "case_id": "active_site_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the annotated PKS1 sequence. UniProt records position 179 as an active site for beta-ketoacyl synthase activity, supporting choice A. This is a PROSITE-ProRule computational annotation, not evidence of direct experimental measurement."
  },
  "important_caveats": [
    "The supporting active-site assignment is computationally annotated by PROSITE-ProRule; the supplied evidence does not establish experimental validation.",
    "The protein has other annotated catalytic residues, but they are not listed as matching options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the matching annotation supports A; the other positions and functions do not match the cited active-site annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the annotated PKS1 sequence. UniProt records position 179 as an active site for beta-ketoacyl synthase activity, supporting choice A. This is a PROSITE-ProRule computational annotation, not evidence of direct experimental measurement.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices suggest a multidomain polyketide synthase, so the listed catalytic functions are biologically plausible; that alone does not establish the exact active-site position or distinguish position 179 from the alternatives.",
    "missing_item_specific_fact": "The protein-specific active-site annotation mapping residue 179 to beta-ketoacyl synthase activity.",
    "reason": "Selecting the keyed residue requires a specific residue-to-function assignment absent from the input. Recognizing the protein or recalling its database annotation would be lookup or memorization, not sequence-based reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed options, the matching annotation supports A; the other positions and functions do not match the cited active-site annotation."
  },
  "important_caveats": [
    "The supporting active-site assignment is computationally annotated by PROSITE-ProRule; the supplied evidence does not establish experimental validation.",
    "The protein has other annotated catalytic residues, but they are not listed as matching options."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5/H3) explicitly lists position 179 as an Active site with description 'For beta-ketoacyl synthase activity', matching Choice A exactly. The evidence code is ECO:0000255 (PROSITE-ProRule PRU01348), indicating computational/pattern-based inference rather than direct experimental validation, but it is the authoritative database annotation. The distractors do not match any annotated active site: no annotation exists at positions 157, 968, or 1045. The actual dehydratase proton acceptor is at 957 (not 1045), and the dehydratase proton donor is at 1154.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C8](#evidence-c8), [H6](#evidence-h6), [C9](#evidence-c9), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Fungal highly-reducing polyketide synthases (HR-PKS) have a conserved N-terminal KS domain whose catalytic residue is a cysteine acting as a nucleophile (not a proton acceptor). The domain order KS-AT-DH-ER-KR-ACP-TE places the KS active site near the N-terminus (typically positions 100–300). Choice B assigns 'Proton acceptor' to position 157, which is inconsistent with KS catalytic chemistry (the KS uses a cysteine thiol nucleophile, not a proton-accepting mechanism). Choices C and D assign functions (acyl transferase, DH proton acceptor) to positions (968, 1045) that are inconsistent with the expected domain architecture of a fungal HR-PKS. A model with general PKS domain architecture knowledge can eliminate B (wrong catalytic mechanism for N-terminal KS region), C (AT domain position atypical), and D (DH proton acceptor position inconsistent), leaving A.


**Missing item-specific fact**

> The exact residue number 179 (vs. 157 or another nearby position) is a database annotation fact. Distinguishing position 179 from 157 within the N-terminal region would require precise domain boundary knowledge or motif-finding tools, but the functional description 'For beta-ketoacyl synthase activity' combined with 'Proton acceptor' inconsistency provides sufficient discrimination among the four choices.


**Reason**

> The functional descriptions embedded in the choices provide meaningful biological discriminators rooted in general PKS enzymology: KS uses a cysteine nucleophile (not a proton acceptor), KS is N-terminal, DH uses histidine proton transfer. This allows elimination of B, C, and D through general domain-architecture reasoning without needing to look up this specific protein's entry. The exact position number is a database fact, but the question is answerable because only one choice has both a correct function and a plausible domain position.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice A is the only option with a function description consistent with the N-terminal KS domain of a fungal HR-PKS. B misassigns catalytic mechanism, C misplaces the AT domain, and D misplaces the DH proton acceptor. No other choice is defensible given the functional descriptions provided.


### Important caveats

- The active site annotation at position 179 is based on PROSITE-ProRule (ECO:0000255), a computational pattern-matching inference, not direct experimental mutagenesis or structural evidence.
- The protein was identified from the sequence by the reviewer; the evaluated model received only the raw 2190-aa sequence with no protein name, organism, or domain annotation.
- The exact position number (179 vs. 157) within the N-terminal region cannot be pinpointed by general reasoning alone; the question is answerable primarily because the functional descriptions in the distractors are biologically inconsistent, not because the model can count to residue 179 in a raw sequence.
- The UniProt entry was first publicly released 2025-02-05; the benchmark author's source snapshot is unknown but the sequence matches across versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Fungal highly-reducing polyketide synthases (HR-PKS) have a conserved N-terminal KS domain whose catalytic residue is a cysteine acting as a nucleophile (not a proton acceptor). The domain order KS-AT-DH-ER-KR-ACP-TE places the KS active site near the N-terminus (typically positions 100–300). Choice B assigns 'Proton acceptor' to position 157, which is inconsistent with KS catalytic chemistry (the KS uses a cysteine thiol nucleophile, not a proton-accepting mechanism). Choices C and D assign functions (acyl transferase, DH proton acceptor) to positions (968, 1045) that are inconsistent with the expected domain architecture of a fungal HR-PKS. A model with general PKS domain architecture knowledge can eliminate B (wrong catalytic mechanism for N-terminal KS region), C (AT domain position atypical), and D (DH proton acceptor position inconsistent), leaving A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact residue number 179 (vs. 157 or another nearby position) is a database annotation fact. Distinguishing position 179 from 157 within the N-terminal region would require precise domain boundary knowledge or motif-finding tools, but the functional description 'For beta-ketoacyl synthase activity' combined with 'Proton acceptor' inconsistency provides sufficient discrimination among the four choices.",
    "reason": "The functional descriptions embedded in the choices provide meaningful biological discriminators rooted in general PKS enzymology: KS uses a cysteine nucleophile (not a proton acceptor), KS is N-terminal, DH uses histidine proton transfer. This allows elimination of B, C, and D through general domain-architecture reasoning without needing to look up this specific protein's entry. The exact position number is a database fact, but the question is answerable because only one choice has both a correct function and a plausible domain position."
  },
  "case_id": "active_site_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C8",
      "H6",
      "C9",
      "H7"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (C5/H3) explicitly lists position 179 as an Active site with description 'For beta-ketoacyl synthase activity', matching Choice A exactly. The evidence code is ECO:0000255 (PROSITE-ProRule PRU01348), indicating computational/pattern-based inference rather than direct experimental validation, but it is the authoritative database annotation. The distractors do not match any annotated active site: no annotation exists at positions 157, 968, or 1045. The actual dehydratase proton acceptor is at 957 (not 1045), and the dehydratase proton donor is at 1154."
  },
  "important_caveats": [
    "The active site annotation at position 179 is based on PROSITE-ProRule (ECO:0000255), a computational pattern-matching inference, not direct experimental mutagenesis or structural evidence.",
    "The protein was identified from the sequence by the reviewer; the evaluated model received only the raw 2190-aa sequence with no protein name, organism, or domain annotation.",
    "The exact position number (179 vs. 157) within the N-terminal region cannot be pinpointed by general reasoning alone; the question is answerable primarily because the functional descriptions in the distractors are biologically inconsistent, not because the model can count to residue 179 in a raw sequence.",
    "The UniProt entry was first publicly released 2025-02-05; the benchmark author's source snapshot is unknown but the sequence matches across versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A is the only option with a function description consistent with the N-terminal KS domain of a fungal HR-PKS. B misassigns catalytic mechanism, C misplaces the AT domain, and D misplaces the DH proton acceptor. No other choice is defensible given the functional descriptions provided."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5/H3) explicitly lists position 179 as an Active site with description 'For beta-ketoacyl synthase activity', matching Choice A exactly. The evidence code is ECO:0000255 (PROSITE-ProRule PRU01348), indicating computational/pattern-based inference rather than direct experimental validation, but it is the authoritative database annotation. The distractors do not match any annotated active site: no annotation exists at positions 157, 968, or 1045. The actual dehydratase proton acceptor is at 957 (not 1045), and the dehydratase proton donor is at 1154.",
    "evidence_ids": ["C5", "H3", "C8", "H6", "C9", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Fungal highly-reducing polyketide synthases (HR-PKS) have a conserved N-terminal KS domain whose catalytic residue is a cysteine acting as a nucleophile (not a proton acceptor). The domain order KS-AT-DH-ER-KR-ACP-TE places the KS active site near the N-terminus (typically positions 100–300). Choice B assigns 'Proton acceptor' to position 157, which is inconsistent with KS catalytic chemistry (the KS uses a cysteine thiol nucleophile, not a proton-accepting mechanism). Choices C and D assign functions (acyl transferase, DH proton acceptor) to positions (968, 1045) that are inconsistent with the expected domain architecture of a fungal HR-PKS. A model with general PKS domain architecture knowledge can eliminate B (wrong catalytic mechanism for N-terminal KS region), C (AT domain position atypical), and D (DH proton acceptor position inconsistent), leaving A.",
    "missing_item_specific_fact": "The exact residue number 179 (vs. 157 or another nearby position) is a database annotation fact. Distinguishing position 179 from 157 within the N-terminal region would require precise domain boundary knowledge or motif-finding tools, but the functional description 'For beta-ketoacyl synthase activity' combined with 'Proton acceptor' inconsistency provides sufficient discrimination among the four choices.",
    "reason": "The functional descriptions embedded in the choices provide meaningful biological discriminators rooted in general PKS enzymology: KS uses a cysteine nucleophile (not a proton acceptor), KS is N-terminal, DH uses histidine proton transfer. This allows elimination of B, C, and D through general domain-architecture reasoning without needing to look up this specific protein's entry. The exact position number is a database fact, but the question is answerable because only one choice has both a correct function and a plausible domain position."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A is the only option with a function description consistent with the N-terminal KS domain of a fungal HR-PKS. B misassigns catalytic mechanism, C misplaces the AT domain, and D misplaces the DH proton acceptor. No other choice is defensible given the functional descriptions provided."
  },
  "important_caveats": [
    "The active site annotation at position 179 is based on PROSITE-ProRule (ECO:0000255), a computational pattern-matching inference, not direct experimental mutagenesis or structural evidence.",
    "The protein was identified from the sequence by the reviewer; the evaluated model received only the raw 2190-aa sequence with no protein name, organism, or domain annotation.",
    "The exact position number (179 vs. 157) within the N-terminal region cannot be pinpointed by general reasoning alone; the question is answerable primarily because the functional descriptions in the distractors are biologically inconsistent, not because the model can count to residue 179 in a raw sequence.",
    "The UniProt entry was first publicly released 2025-02-05; the benchmark author's source snapshot is unknown but the sequence matches across versions."
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

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:28.395908+00:00.  

```json
{"description":"For beta-ketoacyl synthase activity","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01348","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":179},"start":{"modifier":"EXACT","value":179}},"type":"Active site"}
```

Source SHA-256: `16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:28.395908+00:00.  

```json
{"description":"Proton acceptor; for dehydratase activity","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01363","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":957},"start":{"modifier":"EXACT","value":957}},"type":"Active site"}
```

Source SHA-256: `16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)  
**Locator:** `/features/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:28.395908+00:00.  

```json
{"description":"Proton donor; for dehydratase activity","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01363","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":1154},"start":{"modifier":"EXACT","value":1154}},"type":"Active site"}
```

Source SHA-256: `16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38)  
**Locator:** `lines 210-212`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:31.251331+00:00.  

```text
FT   ACT_SITE        179
FT                   /note="For beta-ketoacyl synthase activity"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01348"
```

Source SHA-256: `52e514130a97f47329d9a3516f69b151be6460d3cc32144e6d797ab41a405440`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38)  
**Locator:** `lines 219-221`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:31.251331+00:00.  

```text
FT   ACT_SITE        957
FT                   /note="Proton acceptor; for dehydratase activity"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01363"
```

Source SHA-256: `52e514130a97f47329d9a3516f69b151be6460d3cc32144e6d797ab41a405440`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38)  
**Locator:** `lines 222-224`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:24:31.251331+00:00.  

```text
FT   ACT_SITE        1154
FT                   /note="Proton donor; for dehydratase activity"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01363"
```

Source SHA-256: `52e514130a97f47329d9a3516f69b151be6460d3cc32144e6d797ab41a405440`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 8. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
