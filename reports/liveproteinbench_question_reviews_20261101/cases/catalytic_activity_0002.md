# catalytic_activity_0002

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — 4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSGRGVSQMVTDDKLRYFLKKVTADLHETRGRLRELEEAAGEPIAVVAMGCRFPGGVRSPEDLWHLVASGRDAITPFPADRGWETAGLYDPDPDRPGKSCAREGGFLDDVASFDAGLFGVSPREALALDPQQRLLLEVTWETFERAGLTPAALRGTRTGVFVGTSSQEYAMLVHNARENFEGYSTGYLASVISGRLAYNFGLQGPAVTVDTACSSSLVALHQAAQALRAGDCTLALAGGVAVLATPSMFVEFSRQRGLAPDGRCKAFAAAADGTGWGEGVGLLLLERLSEARREGHPVLAVVRGSAVNQDGASNGLTAPNGPAQQRVIRRALAACRAVGGPGGRGGGPWHRDPAGRSHRGPGAAGHLRPRASRPTSFVARVVEVQYRPHPGRRRRRRCDQDGDGPAPRRTAAHPAYRRPHSTGGLVGGHRAAAHRGEGVAGDRPTPPGRRVLLRHQRHQRPCGAGTSRAGRLPRPRRTAGTAPGGDTAAALGALRPHRARPAGTGRPAARPYPRPPAPLPADTAHSLLVSRTLFGHRAVVLGDDRDELLTGLDALAGGGNAPGVLTGVAGEPRKPVLVFPGQGAQWEGMAAELYRESAVFRDRLRQCAEALAPHTGFSLVDVVCGAEGAAALDRVDVVQPALWAMLVSLAALWRSHGVEPGAVVGHSQGEIAAACVAGALSLEDGARIVALRSRLIAERLSGRGGMAFLGLPAGRAREWLAAWETRLGVAAVNGPSSVVVSGDAEALDGMLAAAEEEGVRAIRVAVDYASHSAQVATLEDELLAALPGITPRTAEIPFFSTVNGALIDTSALDPAYWYRNLRQTVRFESTVRRLLEAGHRGFVEVSPHPVLAVSVQEILDATATEGVVLASLRRGEGGLRRFLTSVGEAHVHGIPADFALPPGRLVDLPTLAFERRRYWLDAQPAAPAHQAEGSAGESAGESAGESAEESEAALFRQRLAGLPESERERAVLHTVCEQAAVVLNLTSAADLDTGKAFTDLGFVSMTAMELRNRLATATGIRLTPTAAFDHPTPEKLAAHLLSRLTGTAEPIAQPVAAPPAAGEPIAIVAMGCRYPGEVASPEELWELLAAGRDATSSFPANRGWNTDELYDPNPGRPGRTYVRRGGFLHDADQFDPQLFGISPREALAMDPQQRLLLEVAWEVLERARLSPASVRGSRTGVFMGISGQDYLPVLTASPDGGAGHLMTGTSTSVASGRIAYTFGLRGPAVTVDTACSSSLVALHLAIQALRQGDCSAALVGGATVLSTPGAFVEFSQQRALAPDGRCKAFAAGADGTGWGEGAGMLLVEPLSEARRQGHPVLALIRGSATNQDGASNGLSAPNGQAQQQVIRQALANSGLTTRDVDAVEAHGTGTALGDPIEAEALLATYGQDRPAQRPLWLGSLKSNIGHTAAAAGVGGVIKMVLALRRGVLPPTLHAADPTPHVDWSAGAVELLTEAREWPETGRPRRAGVSAFGISGTNAHVVLEQAPDPDPAPGSGLPHPAATLPAVPWPLSGRTAAALRAQAGRLHRFVLAHPGLAPADIGRSLAAGRAGLEHRAVVLGRDRDQLLAELATLAEGEGDDAGAAVRGTVRARSRMACLFTAGPGARSGPGRELYARMPVYAAAVDEAGAAFQALPARPLGETMALDEAPADPVLAQVLHFAEQVALFRLLDHWGTAPSHLLGHGPGEAAAAHCAGVLSLSDAAALLPALRATEDDIRRTVKELTFHPPRIPLVSGRTGRPLTPGELRSPEHWIALARETGTPAEGLRWLLADGVHHCLLPVPVDTAGIPGDLAEDGLLLLPDPSRDGTGATALLRALARLYVRGVAVGWDRMLADCGARLVELPTYAFQRGRYWPELAALPAAGPRPAGRADGQGGREFQERLAGASEEEREALLAALVRTHAAAALRLPDADAIDERTPLPELGFDSLTAVDLRNRLGADTGLRLAPSLVFQHPTVTALARHLLAAWTAAGGADRAAEDTTGAGTTLGPLLARAGELGRSEEFQELMHRMAAFRPAFDTPRAEHRIPPVRLSRGPAAPGLVCFPTFAGSSGPQQYARLAAAARGERDLWVLPAPGFSWDQPLPASVDALARLQADGVQECAEGQPVVLLGYSAGGWIAHATAAALEARGAGPSGVVLLDTYWPDSAMLPRLHARIDQDRKSGSSEAHWTEEIRDDAGLTAMAHYSRLFQTWRPAPITAPTLLVRAAEPAVAEPPRDWRPHWRLPHTAVDAPGTHFTLIREHGPAALGSVHHWLNGLQKKEH

[Multiple Choices]
A. restrictinol + glycine + H(+) = restricticin + H2O
B. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
C. (S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate
D. 4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence matches UniProt entry B4ER97, annotated as the NorC spectinabilin polyketide synthase system protein. Its catalytic-activity annotation gives the exact reaction in choice D and cites PubMed 17763486. This supports the key, though the cited annotation is not itself independent validation of the underlying experiment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence with repeated enzyme-domain-like regions is compatible with a modular polyketide synthase, making D a better broad-class match than the other choices.


**Missing item-specific fact**

> The sequence and prompt do not establish the specific NorC pathway assignment or that its reaction uses 4-nitrobenzoyl-CoA to produce demethyldeoxyspectinabilin; that substrate/product specificity is needed to choose the exact reaction.


**Reason**

> Sequence architecture can suggest a polyketide synthase, but it does not by itself identify this particular pathway reaction or its exact stoichiometry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe substantially different reaction classes; D is the matching polyketide-synthase reaction, although its exact specificity is not derivable from the supplied input alone.


### Important caveats

- Reviewer-only UniProt evidence establishes the sequence match and annotation, but was not available in the original question.
- The UniProt catalytic-activity annotation cites a publication; the supplied evidence does not independently establish the experimental basis or scope of that publication.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence with repeated enzyme-domain-like regions is compatible with a modular polyketide synthase, making D a better broad-class match than the other choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence and prompt do not establish the specific NorC pathway assignment or that its reaction uses 4-nitrobenzoyl-CoA to produce demethyldeoxyspectinabilin; that substrate/product specificity is needed to choose the exact reaction.",
    "reason": "Sequence architecture can suggest a polyketide synthase, but it does not by itself identify this particular pathway reaction or its exact stoichiometry."
  },
  "case_id": "catalytic_activity_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry B4ER97, annotated as the NorC spectinabilin polyketide synthase system protein. Its catalytic-activity annotation gives the exact reaction in choice D and cites PubMed 17763486. This supports the key, though the cited annotation is not itself independent validation of the underlying experiment."
  },
  "important_caveats": [
    "Reviewer-only UniProt evidence establishes the sequence match and annotation, but was not available in the original question.",
    "The UniProt catalytic-activity annotation cites a publication; the supplied evidence does not independently establish the experimental basis or scope of that publication."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe substantially different reaction classes; D is the matching polyketide-synthase reaction, although its exact specificity is not derivable from the supplied input alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry B4ER97, annotated as the NorC spectinabilin polyketide synthase system protein. Its catalytic-activity annotation gives the exact reaction in choice D and cites PubMed 17763486. This supports the key, though the cited annotation is not itself independent validation of the underlying experiment.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence with repeated enzyme-domain-like regions is compatible with a modular polyketide synthase, making D a better broad-class match than the other choices.",
    "missing_item_specific_fact": "The sequence and prompt do not establish the specific NorC pathway assignment or that its reaction uses 4-nitrobenzoyl-CoA to produce demethyldeoxyspectinabilin; that substrate/product specificity is needed to choose the exact reaction.",
    "reason": "Sequence architecture can suggest a polyketide synthase, but it does not by itself identify this particular pathway reaction or its exact stoichiometry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe substantially different reaction classes; D is the matching polyketide-synthase reaction, although its exact specificity is not derivable from the supplied input alone."
  },
  "important_caveats": [
    "Reviewer-only UniProt evidence establishes the sequence match and annotation, but was not available in the original question.",
    "The UniProt catalytic-activity annotation cites a publication; the supplied evidence does not independently establish the experimental basis or scope of that publication."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 2266-aa sequence matches UniProt B4ER97 exactly (SHA256 confirmed). The entry is annotated as 'Spectinabilin polyketide synthase system protein NorC' (EC 2.3.1.290) with the catalytic activity reaction exactly matching option D. The evidence code ECO:0000305 references PubMed:17763486 (Traitcheva et al., ChemBioChem 2007), indicating experimental support for the reaction assignment. Both current (v82) and historical (v80) UniProt snapshots confirm the same annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 2266-residue protein contains multiple tandem domain motifs characteristic of modular polyketide synthases: KS catalytic motifs (e.g., GHSQGE with the active-site Cys-His-Glu triad), AT domain motifs (e.g., GCRxPGG), and apparent module duplication (PIAVVAMGCRFPGG / PIAIVAMGCRYPGE). This architecture is diagnostic of a modular PKS, not an NRPS (option A), glycoside hydrolase (option B, typically 300-600 aa), or terpene cyclase (option C, typically 300-500 aa). Among the four choices, only D describes a polyketide synthase reaction. Thus, identifying the enzyme class from domain-level sequence features is sufficient to select D.


**Missing item-specific fact**

> The exact stoichiometry (4-nitrobenzoyl-CoA starter, 6 methylmalonyl-CoA + 1 malonyl-CoA, product 'demethyldeoxyspectinabilin') is not derivable from sequence alone; however, it is not needed to distinguish D from the non-PKS distractors.


**Reason**

> A model with knowledge of PKS domain signatures can reason from the sequence to 'this is a modular PKS' and then select D as the only PKS reaction among the options. This is a concrete biological argument based on domain architecture, not a lookup of a specific database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span four distinct enzyme classes (NRPS, glycoside hydrolase, terpene cyclase, PKS). Once the protein is identified as a modular PKS via domain motifs, D is the uniquely matching option. No other choice describes a polyketide synthase reaction.


### Important caveats

- The specific reaction stoichiometry and product name (demethyldeoxyspectinabilin) in option D cannot be derived from sequence alone; only the enzyme-class identification is sequence-reasonable.
- The evidence code ECO:0000305 indicates inference from a single published study (PubMed:17763486); independent biochemical reconstitution of the full reaction with all listed substrates may not have been performed in isolation.
- The UniProt entry was first publicly released in Feb 2025; the author's construction date is unknown, but the sequence itself dates to 2008 and the functional annotation to 2007.
- Distractors A, B, and C are from entirely different enzyme classes and protein families, making them straightforwardly eliminable for a model familiar with domain signatures.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 2266-residue protein contains multiple tandem domain motifs characteristic of modular polyketide synthases: KS catalytic motifs (e.g., GHSQGE with the active-site Cys-His-Glu triad), AT domain motifs (e.g., GCRxPGG), and apparent module duplication (PIAVVAMGCRFPGG / PIAIVAMGCRYPGE). This architecture is diagnostic of a modular PKS, not an NRPS (option A), glycoside hydrolase (option B, typically 300-600 aa), or terpene cyclase (option C, typically 300-500 aa). Among the four choices, only D describes a polyketide synthase reaction. Thus, identifying the enzyme class from domain-level sequence features is sufficient to select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact stoichiometry (4-nitrobenzoyl-CoA starter, 6 methylmalonyl-CoA + 1 malonyl-CoA, product 'demethyldeoxyspectinabilin') is not derivable from sequence alone; however, it is not needed to distinguish D from the non-PKS distractors.",
    "reason": "A model with knowledge of PKS domain signatures can reason from the sequence to 'this is a modular PKS' and then select D as the only PKS reaction among the options. This is a concrete biological argument based on domain architecture, not a lookup of a specific database entry."
  },
  "case_id": "catalytic_activity_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied 2266-aa sequence matches UniProt B4ER97 exactly (SHA256 confirmed). The entry is annotated as 'Spectinabilin polyketide synthase system protein NorC' (EC 2.3.1.290) with the catalytic activity reaction exactly matching option D. The evidence code ECO:0000305 references PubMed:17763486 (Traitcheva et al., ChemBioChem 2007), indicating experimental support for the reaction assignment. Both current (v82) and historical (v80) UniProt snapshots confirm the same annotation."
  },
  "important_caveats": [
    "The specific reaction stoichiometry and product name (demethyldeoxyspectinabilin) in option D cannot be derived from sequence alone; only the enzyme-class identification is sequence-reasonable.",
    "The evidence code ECO:0000305 indicates inference from a single published study (PubMed:17763486); independent biochemical reconstitution of the full reaction with all listed substrates may not have been performed in isolation.",
    "The UniProt entry was first publicly released in Feb 2025; the author's construction date is unknown, but the sequence itself dates to 2008 and the functional annotation to 2007.",
    "Distractors A, B, and C are from entirely different enzyme classes and protein families, making them straightforwardly eliminable for a model familiar with domain signatures."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct enzyme classes (NRPS, glycoside hydrolase, terpene cyclase, PKS). Once the protein is identified as a modular PKS via domain motifs, D is the uniquely matching option. No other choice describes a polyketide synthase reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 2266-aa sequence matches UniProt B4ER97 exactly (SHA256 confirmed). The entry is annotated as 'Spectinabilin polyketide synthase system protein NorC' (EC 2.3.1.290) with the catalytic activity reaction exactly matching option D. The evidence code ECO:0000305 references PubMed:17763486 (Traitcheva et al., ChemBioChem 2007), indicating experimental support for the reaction assignment. Both current (v82) and historical (v80) UniProt snapshots confirm the same annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 2266-residue protein contains multiple tandem domain motifs characteristic of modular polyketide synthases: KS catalytic motifs (e.g., GHSQGE with the active-site Cys-His-Glu triad), AT domain motifs (e.g., GCRxPGG), and apparent module duplication (PIAVVAMGCRFPGG / PIAIVAMGCRYPGE). This architecture is diagnostic of a modular PKS, not an NRPS (option A), glycoside hydrolase (option B, typically 300-600 aa), or terpene cyclase (option C, typically 300-500 aa). Among the four choices, only D describes a polyketide synthase reaction. Thus, identifying the enzyme class from domain-level sequence features is sufficient to select D.",
    "missing_item_specific_fact": "The exact stoichiometry (4-nitrobenzoyl-CoA starter, 6 methylmalonyl-CoA + 1 malonyl-CoA, product 'demethyldeoxyspectinabilin') is not derivable from sequence alone; however, it is not needed to distinguish D from the non-PKS distractors.",
    "reason": "A model with knowledge of PKS domain signatures can reason from the sequence to 'this is a modular PKS' and then select D as the only PKS reaction among the options. This is a concrete biological argument based on domain architecture, not a lookup of a specific database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct enzyme classes (NRPS, glycoside hydrolase, terpene cyclase, PKS). Once the protein is identified as a modular PKS via domain motifs, D is the uniquely matching option. No other choice describes a polyketide synthase reaction."
  },
  "important_caveats": [
    "The specific reaction stoichiometry and product name (demethyldeoxyspectinabilin) in option D cannot be derived from sequence alone; only the enzyme-class identification is sequence-reasonable.",
    "The evidence code ECO:0000305 indicates inference from a single published study (PubMed:17763486); independent biochemical reconstitution of the full reaction with all listed substrates may not have been performed in isolation.",
    "The UniProt entry was first publicly released in Feb 2025; the author's construction date is unknown, but the sequence itself dates to 2008 and the functional annotation to 2007.",
    "Distractors A, B, and C are from entirely different enzyme classes and protein families, making them straightforwardly eliminable for a model familiar with domain signatures."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 2. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
