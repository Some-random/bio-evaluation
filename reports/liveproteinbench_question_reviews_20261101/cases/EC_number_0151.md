# EC_number_0151

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 2.3.1.290

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSGRGVSQMVTDDKLRYFLKKVTADLHETRGRLRELEEAAGEPIAVVAMGCRFPGGVRSPEDLWHLVASGRDAITPFPADRGWETAGLYDPDPDRPGKSCAREGGFLDDVASFDAGLFGVSPREALALDPQQRLLLEVTWETFERAGLTPAALRGTRTGVFVGTSSQEYAMLVHNARENFEGYSTGYLASVISGRLAYNFGLQGPAVTVDTACSSSLVALHQAAQALRAGDCTLALAGGVAVLATPSMFVEFSRQRGLAPDGRCKAFAAAADGTGWGEGVGLLLLERLSEARREGHPVLAVVRGSAVNQDGASNGLTAPNGPAQQRVIRRALAACRAVGGPGGRGGGPWHRDPAGRSHRGPGAAGHLRPRASRPTSFVARVVEVQYRPHPGRRRRRRCDQDGDGPAPRRTAAHPAYRRPHSTGGLVGGHRAAAHRGEGVAGDRPTPPGRRVLLRHQRHQRPCGAGTSRAGRLPRPRRTAGTAPGGDTAAALGALRPHRARPAGTGRPAARPYPRPPAPLPADTAHSLLVSRTLFGHRAVVLGDDRDELLTGLDALAGGGNAPGVLTGVAGEPRKPVLVFPGQGAQWEGMAAELYRESAVFRDRLRQCAEALAPHTGFSLVDVVCGAEGAAALDRVDVVQPALWAMLVSLAALWRSHGVEPGAVVGHSQGEIAAACVAGALSLEDGARIVALRSRLIAERLSGRGGMAFLGLPAGRAREWLAAWETRLGVAAVNGPSSVVVSGDAEALDGMLAAAEEEGVRAIRVAVDYASHSAQVATLEDELLAALPGITPRTAEIPFFSTVNGALIDTSALDPAYWYRNLRQTVRFESTVRRLLEAGHRGFVEVSPHPVLAVSVQEILDATATEGVVLASLRRGEGGLRRFLTSVGEAHVHGIPADFALPPGRLVDLPTLAFERRRYWLDAQPAAPAHQAEGSAGESAGESAGESAEESEAALFRQRLAGLPESERERAVLHTVCEQAAVVLNLTSAADLDTGKAFTDLGFVSMTAMELRNRLATATGIRLTPTAAFDHPTPEKLAAHLLSRLTGTAEPIAQPVAAPPAAGEPIAIVAMGCRYPGEVASPEELWELLAAGRDATSSFPANRGWNTDELYDPNPGRPGRTYVRRGGFLHDADQFDPQLFGISPREALAMDPQQRLLLEVAWEVLERARLSPASVRGSRTGVFMGISGQDYLPVLTASPDGGAGHLMTGTSTSVASGRIAYTFGLRGPAVTVDTACSSSLVALHLAIQALRQGDCSAALVGGATVLSTPGAFVEFSQQRALAPDGRCKAFAAGADGTGWGEGAGMLLVEPLSEARRQGHPVLALIRGSATNQDGASNGLSAPNGQAQQQVIRQALANSGLTTRDVDAVEAHGTGTALGDPIEAEALLATYGQDRPAQRPLWLGSLKSNIGHTAAAAGVGGVIKMVLALRRGVLPPTLHAADPTPHVDWSAGAVELLTEAREWPETGRPRRAGVSAFGISGTNAHVVLEQAPDPDPAPGSGLPHPAATLPAVPWPLSGRTAAALRAQAGRLHRFVLAHPGLAPADIGRSLAAGRAGLEHRAVVLGRDRDQLLAELATLAEGEGDDAGAAVRGTVRARSRMACLFTAGPGARSGPGRELYARMPVYAAAVDEAGAAFQALPARPLGETMALDEAPADPVLAQVLHFAEQVALFRLLDHWGTAPSHLLGHGPGEAAAAHCAGVLSLSDAAALLPALRATEDDIRRTVKELTFHPPRIPLVSGRTGRPLTPGELRSPEHWIALARETGTPAEGLRWLLADGVHHCLLPVPVDTAGIPGDLAEDGLLLLPDPSRDGTGATALLRALARLYVRGVAVGWDRMLADCGARLVELPTYAFQRGRYWPELAALPAAGPRPAGRADGQGGREFQERLAGASEEEREALLAALVRTHAAAALRLPDADAIDERTPLPELGFDSLTAVDLRNRLGADTGLRLAPSLVFQHPTVTALARHLLAAWTAAGGADRAAEDTTGAGTTLGPLLARAGELGRSEEFQELMHRMAAFRPAFDTPRAEHRIPPVRLSRGPAAPGLVCFPTFAGSSGPQQYARLAAAARGERDLWVLPAPGFSWDQPLPASVDALARLQADGVQECAEGQPVVLLGYSAGGWIAHATAAALEARGAGPSGVVLLDTYWPDSAMLPRLHARIDQDRKSGSSEAHWTEEIRDDAGLTAMAHYSRLFQTWRPAPITAPTLLVRAAEPAVAEPPRDWRPHWRLPHTAVDAPGTHFTLIREHGPAALGSVHHWLNGLQKKEH

[Multiple Choices]
A. 2.3.1.319
B. 2.5.1.56
C. 2.7.1.39
D. 2.3.1.290
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

> The supplied 2266-aa sequence exactly matches the UniProt NorC record, which assigns EC 2.3.1.290 and describes the corresponding catalytic reaction. The annotation cites PubMed 17763486; this supports the key, though the excerpts do not independently establish the experimental basis or details of that study.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long, modular sequence is consistent with a polyketide synthase, which can broadly favor an acyltransferase EC class over the kinase option. That general inference does not identify the particular pathway reaction needed to distinguish the two 2.3.1 choices.


**Missing item-specific fact**

> The protein's identity as NorC in the spectinabilin polyketide synthase system and its pathway-specific substrate/product reaction, which assigns EC 2.3.1.290.


**Reason**

> The exact EC choice depends on protein- and pathway-specific functional annotation not supplied in the question. Recognizing the broad enzyme family from sequence does not establish the complete four-part EC number.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence's cited annotation supports D; the other choices are not supported by the supplied sequence alone.


### Important caveats

- The UniProt evidence is reviewer-only and was not available to the evaluated model.
- The current and archived records match the benchmark sequence, but the benchmark author's exact source snapshot is unknown.
- The cited annotation supports the expected answer but is not, by itself, an independent review of the underlying primary study.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, modular sequence is consistent with a polyketide synthase, which can broadly favor an acyltransferase EC class over the kinase option. That general inference does not identify the particular pathway reaction needed to distinguish the two 2.3.1 choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as NorC in the spectinabilin polyketide synthase system and its pathway-specific substrate/product reaction, which assigns EC 2.3.1.290.",
    "reason": "The exact EC choice depends on protein- and pathway-specific functional annotation not supplied in the question. Recognizing the broad enzyme family from sequence does not establish the complete four-part EC number."
  },
  "case_id": "EC_number_0151",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied 2266-aa sequence exactly matches the UniProt NorC record, which assigns EC 2.3.1.290 and describes the corresponding catalytic reaction. The annotation cites PubMed 17763486; this supports the key, though the excerpts do not independently establish the experimental basis or details of that study."
  },
  "important_caveats": [
    "The UniProt evidence is reviewer-only and was not available to the evaluated model.",
    "The current and archived records match the benchmark sequence, but the benchmark author's exact source snapshot is unknown.",
    "The cited annotation supports the expected answer but is not, by itself, an independent review of the underlying primary study."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's cited annotation supports D; the other choices are not supported by the supplied sequence alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0151",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 2266-aa sequence exactly matches the UniProt NorC record, which assigns EC 2.3.1.290 and describes the corresponding catalytic reaction. The annotation cites PubMed 17763486; this supports the key, though the excerpts do not independently establish the experimental basis or details of that study.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long, modular sequence is consistent with a polyketide synthase, which can broadly favor an acyltransferase EC class over the kinase option. That general inference does not identify the particular pathway reaction needed to distinguish the two 2.3.1 choices.",
    "missing_item_specific_fact": "The protein's identity as NorC in the spectinabilin polyketide synthase system and its pathway-specific substrate/product reaction, which assigns EC 2.3.1.290.",
    "reason": "The exact EC choice depends on protein- and pathway-specific functional annotation not supplied in the question. Recognizing the broad enzyme family from sequence does not establish the complete four-part EC number."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence's cited annotation supports D; the other choices are not supported by the supplied sequence alone."
  },
  "important_caveats": [
    "The UniProt evidence is reviewer-only and was not available to the evaluated model.",
    "The current and archived records match the benchmark sequence, but the benchmark author's exact source snapshot is unknown.",
    "The cited annotation supports the expected answer but is not, by itself, an independent review of the underlying primary study."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry B4ER97 (NORC_STRON, 2266 aa, sequence SHA256 matched in both current and historical snapshots). The entry is annotated as 'Spectinabilin polyketide synthase system protein NorC' with EC 2.3.1.290, supported by evidence code ECO:0000305 (inferred by curator) referencing PubMed:17763486 (Traitcheva et al. 2007, ChemBioChem). The catalytic activity is the condensation of 4-nitrobenzoyl-CoA with methylmalonyl-CoA and malonyl-CoA to form demethyldeoxyspectinabilin. The annotation is a curator inference from published literature rather than direct enzymatic assay of this specific protein, but it is a well-supported database assignment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The 2266-aa sequence contains multiple recognizable modular PKS domains: ketosynthase (KS) motifs ('MGCRFPGG', 'MGCRYPGE'), acyltransferase (AT) motifs ('GYSAGGW', 'GHSQGE'), ketoreductase (KR) motifs ('GPAVTVDTACSSSLVAL', 'GDSLTAVDLRNRL'), and ACP-like regions. This multi-domain architecture clearly identifies the protein as a type I modular polyketide synthase, which logically places it in EC 2.3.1.x (acyltransferases involved in PKS reactions) and eliminates 2.5.1.56 (alkyl/aryl transferase) and 2.7.1.39 (phosphotransferase/kinase). However, distinguishing between the remaining 2.3.1.x options (2.3.1.319 vs 2.3.1.290) requires knowing the specific starter unit (4-nitrobenzoyl-CoA for spectinabilin vs. whatever substrate 2.3.1.319 uses) and the exact product, which is a protein-specific substrate-specificity fact not derivable from domain architecture alone.


**Missing item-specific fact**

> The specific substrate/product identity that distinguishes EC 2.3.1.319 from EC 2.3.1.290. Both are 2.3.1.x acyltransferases; the fourth digit encodes the particular reaction (spectinabilin PKS vs. whatever reaction 2.3.1.319 represents). Identifying this requires either recognizing the exact protein sequence (NorC from Streptomyces orinoci) or knowing the substrate-specificity of each EC number, neither of which follows from general domain-architecture reasoning.


**Reason**

> General reasoning from the sequence can narrow the EC class to 2.3.1.x (modular PKS acyltransferase) and eliminate options B and C. However, the final distinction between two 2.3.1.x EC numbers depends on the specific chemical reaction catalyzed, which is an item-specific annotation fact. Recognizing the exact sequence and recalling its database entry is what ultimately determines the answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While both A and D fall in the 2.3.1.x class, only D (2.3.1.290) corresponds to the spectinabilin modular PKS architecture present in this sequence. If 2.3.1.319 represents a structurally distinct acyltransferase (e.g., a smaller, non-modular enzyme), the 2266-aa multi-domain architecture would eliminate it. The options are sufficiently distinct at the class level (2.3 vs 2.5 vs 2.7), though the final 2.3.1.x distinction is fine-grained.


### Important caveats

- The EC 2.3.1.290 annotation carries evidence code ECO:0000305 (inferred by curator) based on PubMed:17763486, not a direct in vitro enzymatic characterization of NorC alone. The underlying study examined the aureothin/neoaureothin pathway evolution.
- The UniProt entry was first public on 2025-02-05 and integrated into Swiss-Prot on 2025-02-05; the sequence itself dates to 2008. The author's source snapshot is unknown.
- The sequence identity origin (accession B4ER97) was inferred mechanically from dataset metadata and was not available to the evaluated model.
- The domain assignments (KS, AT, KR, ACP) are based on well-known conserved motifs visible in the sequence and are not reviewer-only information.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 2266-aa sequence contains multiple recognizable modular PKS domains: ketosynthase (KS) motifs ('MGCRFPGG', 'MGCRYPGE'), acyltransferase (AT) motifs ('GYSAGGW', 'GHSQGE'), ketoreductase (KR) motifs ('GPAVTVDTACSSSLVAL', 'GDSLTAVDLRNRL'), and ACP-like regions. This multi-domain architecture clearly identifies the protein as a type I modular polyketide synthase, which logically places it in EC 2.3.1.x (acyltransferases involved in PKS reactions) and eliminates 2.5.1.56 (alkyl/aryl transferase) and 2.7.1.39 (phosphotransferase/kinase). However, distinguishing between the remaining 2.3.1.x options (2.3.1.319 vs 2.3.1.290) requires knowing the specific starter unit (4-nitrobenzoyl-CoA for spectinabilin vs. whatever substrate 2.3.1.319 uses) and the exact product, which is a protein-specific substrate-specificity fact not derivable from domain architecture alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate/product identity that distinguishes EC 2.3.1.319 from EC 2.3.1.290. Both are 2.3.1.x acyltransferases; the fourth digit encodes the particular reaction (spectinabilin PKS vs. whatever reaction 2.3.1.319 represents). Identifying this requires either recognizing the exact protein sequence (NorC from Streptomyces orinoci) or knowing the substrate-specificity of each EC number, neither of which follows from general domain-architecture reasoning.",
    "reason": "General reasoning from the sequence can narrow the EC class to 2.3.1.x (modular PKS acyltransferase) and eliminate options B and C. However, the final distinction between two 2.3.1.x EC numbers depends on the specific chemical reaction catalyzed, which is an item-specific annotation fact. Recognizing the exact sequence and recalling its database entry is what ultimately determines the answer."
  },
  "case_id": "EC_number_0151",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry B4ER97 (NORC_STRON, 2266 aa, sequence SHA256 matched in both current and historical snapshots). The entry is annotated as 'Spectinabilin polyketide synthase system protein NorC' with EC 2.3.1.290, supported by evidence code ECO:0000305 (inferred by curator) referencing PubMed:17763486 (Traitcheva et al. 2007, ChemBioChem). The catalytic activity is the condensation of 4-nitrobenzoyl-CoA with methylmalonyl-CoA and malonyl-CoA to form demethyldeoxyspectinabilin. The annotation is a curator inference from published literature rather than direct enzymatic assay of this specific protein, but it is a well-supported database assignment."
  },
  "important_caveats": [
    "The EC 2.3.1.290 annotation carries evidence code ECO:0000305 (inferred by curator) based on PubMed:17763486, not a direct in vitro enzymatic characterization of NorC alone. The underlying study examined the aureothin/neoaureothin pathway evolution.",
    "The UniProt entry was first public on 2025-02-05 and integrated into Swiss-Prot on 2025-02-05; the sequence itself dates to 2008. The author's source snapshot is unknown.",
    "The sequence identity origin (accession B4ER97) was inferred mechanically from dataset metadata and was not available to the evaluated model.",
    "The domain assignments (KS, AT, KR, ACP) are based on well-known conserved motifs visible in the sequence and are not reviewer-only information."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While both A and D fall in the 2.3.1.x class, only D (2.3.1.290) corresponds to the spectinabilin modular PKS architecture present in this sequence. If 2.3.1.319 represents a structurally distinct acyltransferase (e.g., a smaller, non-modular enzyme), the 2266-aa multi-domain architecture would eliminate it. The options are sufficiently distinct at the class level (2.3 vs 2.5 vs 2.7), though the final 2.3.1.x distinction is fine-grained."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0151",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry B4ER97 (NORC_STRON, 2266 aa, sequence SHA256 matched in both current and historical snapshots). The entry is annotated as 'Spectinabilin polyketide synthase system protein NorC' with EC 2.3.1.290, supported by evidence code ECO:0000305 (inferred by curator) referencing PubMed:17763486 (Traitcheva et al. 2007, ChemBioChem). The catalytic activity is the condensation of 4-nitrobenzoyl-CoA with methylmalonyl-CoA and malonyl-CoA to form demethyldeoxyspectinabilin. The annotation is a curator inference from published literature rather than direct enzymatic assay of this specific protein, but it is a well-supported database assignment.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The 2266-aa sequence contains multiple recognizable modular PKS domains: ketosynthase (KS) motifs ('MGCRFPGG', 'MGCRYPGE'), acyltransferase (AT) motifs ('GYSAGGW', 'GHSQGE'), ketoreductase (KR) motifs ('GPAVTVDTACSSSLVAL', 'GDSLTAVDLRNRL'), and ACP-like regions. This multi-domain architecture clearly identifies the protein as a type I modular polyketide synthase, which logically places it in EC 2.3.1.x (acyltransferases involved in PKS reactions) and eliminates 2.5.1.56 (alkyl/aryl transferase) and 2.7.1.39 (phosphotransferase/kinase). However, distinguishing between the remaining 2.3.1.x options (2.3.1.319 vs 2.3.1.290) requires knowing the specific starter unit (4-nitrobenzoyl-CoA for spectinabilin vs. whatever substrate 2.3.1.319 uses) and the exact product, which is a protein-specific substrate-specificity fact not derivable from domain architecture alone.",
    "missing_item_specific_fact": "The specific substrate/product identity that distinguishes EC 2.3.1.319 from EC 2.3.1.290. Both are 2.3.1.x acyltransferases; the fourth digit encodes the particular reaction (spectinabilin PKS vs. whatever reaction 2.3.1.319 represents). Identifying this requires either recognizing the exact protein sequence (NorC from Streptomyces orinoci) or knowing the substrate-specificity of each EC number, neither of which follows from general domain-architecture reasoning.",
    "reason": "General reasoning from the sequence can narrow the EC class to 2.3.1.x (modular PKS acyltransferase) and eliminate options B and C. However, the final distinction between two 2.3.1.x EC numbers depends on the specific chemical reaction catalyzed, which is an item-specific annotation fact. Recognizing the exact sequence and recalling its database entry is what ultimately determines the answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While both A and D fall in the 2.3.1.x class, only D (2.3.1.290) corresponds to the spectinabilin modular PKS architecture present in this sequence. If 2.3.1.319 represents a structurally distinct acyltransferase (e.g., a smaller, non-modular enzyme), the 2266-aa multi-domain architecture would eliminate it. The options are sufficiently distinct at the class level (2.3 vs 2.5 vs 2.7), though the final 2.3.1.x distinction is fine-grained."
  },
  "important_caveats": [
    "The EC 2.3.1.290 annotation carries evidence code ECO:0000305 (inferred by curator) based on PubMed:17763486, not a direct in vitro enzymatic characterization of NorC alone. The underlying study examined the aureothin/neoaureothin pathway evolution.",
    "The UniProt entry was first public on 2025-02-05 and integrated into Swiss-Prot on 2025-02-05; the sequence itself dates to 2008. The author's source snapshot is unknown.",
    "The sequence identity origin (accession B4ER97) was inferred mechanically from dataset metadata and was not available to the evaluated model.",
    "The domain assignments (KS, AT, KR, ACP) are based on well-known conserved motifs visible in the sequence and are not reviewer-only information."
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

**Accession:** `B4ER97` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 80. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:19.126101+00:00.  

```json
"B4ER97"
```

Source SHA-256: `4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:19.126101+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"CAO85898.1","source":"EMBL"}],"value":"Modular polyketide synthase NorC"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"17763486","source":"PubMed"}],"value":"2.3.1.290"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Spectinabilin polyketide synthase system protein NorC"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Spectinabilin PKS system protein NorC"}]}}
```

Source SHA-256: `4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:19.126101+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"17763486","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:58945"}}],"reaction":{"ecNumber":"2.3.1.290","evidences":[{"evidenceCode":"ECO:0000305","id":"17763486","source":"PubMed"}],"name":"4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:58944"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57327"},{"database":"ChEBI","id":"CHEBI:57384"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:142871"},{"database":"ChEBI","id":"CHEBI:142872"}]}}
```

Source SHA-256: `4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:19.126101+00:00.  

```json
{"citation":{"authors":["Traitcheva N.","Jenke-Kodama H.","He J.","Dittmann E.","Hertweck C."],"citationCrossReferences":[{"database":"PubMed","id":"17763486"},{"database":"DOI","id":"10.1002/cbic.200700309"}],"citationType":"journal article","firstPage":"1841","id":"17763486","journal":"ChemBioChem","lastPage":"1849","publicationDate":"2007","title":"Non-colinear polyketide biosynthesis in the aureothin and neoaureothin pathways: an evolutionary perspective.","volume":"8"},"evidences":[{"evidenceCode":"ECO:0000312","id":"CAO85898.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"HKI-0260"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","SUBUNIT"]}
```

Source SHA-256: `4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-02T04:27:21.445291+00:00.  

```text
ID   NORC_STRON              Reviewed;        2266 AA.
AC   B4ER97;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   23-SEP-2008, sequence version 1.
DT   28-JAN-2026, entry version 80.
DE   RecName: Full=Spectinabilin polyketide synthase system protein NorC {ECO:0000305};
DE            Short=Spectinabilin PKS system protein NorC {ECO:0000305};
DE            EC=2.3.1.290 {ECO:0000305|PubMed:17763486};
DE   AltName: Full=Modular polyketide synthase NorC {ECO:0000312|EMBL:CAO85898.1};
GN   Name=norC {ECO:0000303|PubMed:17763486};
OS   Streptomyces orinoci (Streptoverticillium orinoci).
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=67339;
```

Source SHA-256: `1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-02T04:27:21.445291+00:00.  

```text
DE   RecName: Full=Spectinabilin polyketide synthase system protein NorC {ECO:0000305};
DE            Short=Spectinabilin PKS system protein NorC {ECO:0000305};
DE            EC=2.3.1.290 {ECO:0000305|PubMed:17763486};
DE   AltName: Full=Modular polyketide synthase NorC {ECO:0000312|EMBL:CAO85898.1};
```

Source SHA-256: `1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)  
**Locator:** `lines 15-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-02T04:27:21.445291+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:CAO85898.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND SUBUNIT.
RC   STRAIN=HKI-0260;
RX   PubMed=17763486; DOI=10.1002/cbic.200700309;
RA   Traitcheva N., Jenke-Kodama H., He J., Dittmann E., Hertweck C.;
RT   "Non-colinear polyketide biosynthesis in the aureothin and neoaureothin
RT   pathways: an evolutionary perspective.";
RL   ChemBioChem 8:1841-1849(2007).
```

Source SHA-256: `1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)  
**Locator:** `lines 30-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-02T04:27:21.445291+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6
CC         NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8
CC         CoA + 5 H2O; Xref=Rhea:RHEA:58944, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:57287,
CC         ChEBI:CHEBI:57327, ChEBI:CHEBI:57384, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58349, ChEBI:CHEBI:142871, ChEBI:CHEBI:142872;
CC         EC=2.3.1.290; Evidence={ECO:0000305|PubMed:17763486};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:58945;
CC         Evidence={ECO:0000305|PubMed:17763486};
```

Source SHA-256: `1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 151. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
