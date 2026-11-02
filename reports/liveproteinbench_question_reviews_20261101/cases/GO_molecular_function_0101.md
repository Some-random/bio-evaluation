# GO_molecular_function_0101

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — 3-oxoacyl-&#91;acyl-carrier-protein&#93; synthase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSGRGVSQMVTDDKLRYFLKKVTADLHETRGRLRELEEAAGEPIAVVAMGCRFPGGVRSPEDLWHLVASGRDAITPFPADRGWETAGLYDPDPDRPGKSCAREGGFLDDVASFDAGLFGVSPREALALDPQQRLLLEVTWETFERAGLTPAALRGTRTGVFVGTSSQEYAMLVHNARENFEGYSTGYLASVISGRLAYNFGLQGPAVTVDTACSSSLVALHQAAQALRAGDCTLALAGGVAVLATPSMFVEFSRQRGLAPDGRCKAFAAAADGTGWGEGVGLLLLERLSEARREGHPVLAVVRGSAVNQDGASNGLTAPNGPAQQRVIRRALAACRAVGGPGGRGGGPWHRDPAGRSHRGPGAAGHLRPRASRPTSFVARVVEVQYRPHPGRRRRRRCDQDGDGPAPRRTAAHPAYRRPHSTGGLVGGHRAAAHRGEGVAGDRPTPPGRRVLLRHQRHQRPCGAGTSRAGRLPRPRRTAGTAPGGDTAAALGALRPHRARPAGTGRPAARPYPRPPAPLPADTAHSLLVSRTLFGHRAVVLGDDRDELLTGLDALAGGGNAPGVLTGVAGEPRKPVLVFPGQGAQWEGMAAELYRESAVFRDRLRQCAEALAPHTGFSLVDVVCGAEGAAALDRVDVVQPALWAMLVSLAALWRSHGVEPGAVVGHSQGEIAAACVAGALSLEDGARIVALRSRLIAERLSGRGGMAFLGLPAGRAREWLAAWETRLGVAAVNGPSSVVVSGDAEALDGMLAAAEEEGVRAIRVAVDYASHSAQVATLEDELLAALPGITPRTAEIPFFSTVNGALIDTSALDPAYWYRNLRQTVRFESTVRRLLEAGHRGFVEVSPHPVLAVSVQEILDATATEGVVLASLRRGEGGLRRFLTSVGEAHVHGIPADFALPPGRLVDLPTLAFERRRYWLDAQPAAPAHQAEGSAGESAGESAGESAEESEAALFRQRLAGLPESERERAVLHTVCEQAAVVLNLTSAADLDTGKAFTDLGFVSMTAMELRNRLATATGIRLTPTAAFDHPTPEKLAAHLLSRLTGTAEPIAQPVAAPPAAGEPIAIVAMGCRYPGEVASPEELWELLAAGRDATSSFPANRGWNTDELYDPNPGRPGRTYVRRGGFLHDADQFDPQLFGISPREALAMDPQQRLLLEVAWEVLERARLSPASVRGSRTGVFMGISGQDYLPVLTASPDGGAGHLMTGTSTSVASGRIAYTFGLRGPAVTVDTACSSSLVALHLAIQALRQGDCSAALVGGATVLSTPGAFVEFSQQRALAPDGRCKAFAAGADGTGWGEGAGMLLVEPLSEARRQGHPVLALIRGSATNQDGASNGLSAPNGQAQQQVIRQALANSGLTTRDVDAVEAHGTGTALGDPIEAEALLATYGQDRPAQRPLWLGSLKSNIGHTAAAAGVGGVIKMVLALRRGVLPPTLHAADPTPHVDWSAGAVELLTEAREWPETGRPRRAGVSAFGISGTNAHVVLEQAPDPDPAPGSGLPHPAATLPAVPWPLSGRTAAALRAQAGRLHRFVLAHPGLAPADIGRSLAAGRAGLEHRAVVLGRDRDQLLAELATLAEGEGDDAGAAVRGTVRARSRMACLFTAGPGARSGPGRELYARMPVYAAAVDEAGAAFQALPARPLGETMALDEAPADPVLAQVLHFAEQVALFRLLDHWGTAPSHLLGHGPGEAAAAHCAGVLSLSDAAALLPALRATEDDIRRTVKELTFHPPRIPLVSGRTGRPLTPGELRSPEHWIALARETGTPAEGLRWLLADGVHHCLLPVPVDTAGIPGDLAEDGLLLLPDPSRDGTGATALLRALARLYVRGVAVGWDRMLADCGARLVELPTYAFQRGRYWPELAALPAAGPRPAGRADGQGGREFQERLAGASEEEREALLAALVRTHAAAALRLPDADAIDERTPLPELGFDSLTAVDLRNRLGADTGLRLAPSLVFQHPTVTALARHLLAAWTAAGGADRAAEDTTGAGTTLGPLLARAGELGRSEEFQELMHRMAAFRPAFDTPRAEHRIPPVRLSRGPAAPGLVCFPTFAGSSGPQQYARLAAAARGERDLWVLPAPGFSWDQPLPASVDALARLQADGVQECAEGQPVVLLGYSAGGWIAHATAAALEARGAGPSGVVLLDTYWPDSAMLPRLHARIDQDRKSGSSEAHWTEEIRDDAGLTAMAHYSRLFQTWRPAPITAPTLLVRAAEPAVAEPPRDWRPHWRLPHTAVDAPGTHFTLIREHGPAALGSVHHWLNGLQKKEH

[Multiple Choices]
A. 3-oxoacyl-[acyl-carrier-protein] synthase activity
B. FAD binding
C. 2 iron, 2 sulfur cluster binding
D. peptidyl-tRNA hydrolase activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The exact sequence matches the NorC polyketide-synthase protein. Its archived GO annotation assigns 3-oxoacyl-&#91;acyl-carrier-protein&#93; synthase activity by InterPro inference; the cited functional record also describes its role in a modular PKS. This supports A as an annotation-level molecular function, though it is not a direct assay of that specific activity.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is exceptionally long and has repeated enzyme-module-like regions consistent with a modular polyketide synthase. That architecture supports a chain-elongation synthase activity and distinguishes A from the unrelated FAD-binding, iron-sulfur-cluster-binding, and peptidyl-tRNA-hydrolase choices.


**Missing item-specific fact**

> No item-specific database identity or experimental measurement is required to make this broad distinction, although confirming the precise GO annotation would require a protein-specific source.


**Reason**

> The sequence and choices provide meaningful biological grounds to favor a modular PKS activity. This is an inference from architecture, not a claim that sequence alone establishes the protein's precise experimental substrate specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices are sufficiently distinct for the PKS-like sequence architecture to favor A; no other option is comparably supported by the supplied sequence.


### Important caveats

- The GO assignment is computational (IEA:InterPro), while the cited functional evidence concerns the PKS system's overall role; neither alone demonstrates an isolated assay of this exact activity.
- The sequence match and historical annotation support the key, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is exceptionally long and has repeated enzyme-module-like regions consistent with a modular polyketide synthase. That architecture supports a chain-elongation synthase activity and distinguishes A from the unrelated FAD-binding, iron-sulfur-cluster-binding, and peptidyl-tRNA-hydrolase choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No item-specific database identity or experimental measurement is required to make this broad distinction, although confirming the precise GO annotation would require a protein-specific source.",
    "reason": "The sequence and choices provide meaningful biological grounds to favor a modular PKS activity. This is an inference from architecture, not a claim that sequence alone establishes the protein's precise experimental substrate specificity."
  },
  "case_id": "GO_molecular_function_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the NorC polyketide-synthase protein. Its archived GO annotation assigns 3-oxoacyl-[acyl-carrier-protein] synthase activity by InterPro inference; the cited functional record also describes its role in a modular PKS. This supports A as an annotation-level molecular function, though it is not a direct assay of that specific activity."
  },
  "important_caveats": [
    "The GO assignment is computational (IEA:InterPro), while the cited functional evidence concerns the PKS system's overall role; neither alone demonstrates an isolated assay of this exact activity.",
    "The sequence match and historical annotation support the key, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are sufficiently distinct for the PKS-like sequence architecture to favor A; no other option is comparably supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the NorC polyketide-synthase protein. Its archived GO annotation assigns 3-oxoacyl-[acyl-carrier-protein] synthase activity by InterPro inference; the cited functional record also describes its role in a modular PKS. This supports A as an annotation-level molecular function, though it is not a direct assay of that specific activity.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is exceptionally long and has repeated enzyme-module-like regions consistent with a modular polyketide synthase. That architecture supports a chain-elongation synthase activity and distinguishes A from the unrelated FAD-binding, iron-sulfur-cluster-binding, and peptidyl-tRNA-hydrolase choices.",
    "missing_item_specific_fact": "No item-specific database identity or experimental measurement is required to make this broad distinction, although confirming the precise GO annotation would require a protein-specific source.",
    "reason": "The sequence and choices provide meaningful biological grounds to favor a modular PKS activity. This is an inference from architecture, not a claim that sequence alone establishes the protein's precise experimental substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices are sufficiently distinct for the PKS-like sequence architecture to favor A; no other option is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "The GO assignment is computational (IEA:InterPro), while the cited functional evidence concerns the PKS system's overall role; neither alone demonstrates an isolated assay of this exact activity.",
    "The sequence match and historical annotation support the key, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B4ER97 (NorC, spectinabilin PKS) carries GO:0004315 (3-oxoacyl-&#91;acyl-carrier-protein&#93; synthase activity) annotated with IEA:InterPro (C7/H5). The protein is a type I modular PKS whose ketosynthase (KS) domain catalyzes a condensation reaction mechanistically analogous to 3-oxoacyl-ACP synthase (EC 2.3.1.41). The annotation is computationally inferred (IEA) via domain-similarity to the FAS II β-ketoacyl-ACP synthase family, not directly experimental, but the mechanistic equivalence is well-established. The actual EC for the full PKS system is 2.3.1.290 (C4/C6), but the KS domain activity is the closest match among the given options.

Citations as saved: [C7](#evidence-c7), [H5](#evidence-h5), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 2266-aa sequence displays a large multi-domain architecture with repeated catalytic units characteristic of a modular PKS. Recognizable KS-domain motifs (e.g., 'GCRFPGG' near residue 37 and 'GCRYPGE' near residue ~1130) indicate condensation (ketoacyl synthase) activity. KR-domain motifs ('GHSQGE', 'HHCLL') and ACP-like regions further confirm PKS architecture. Distractor elimination: (B) FAD binding requires a Rossmann-fold flavin-binding motif (GxGxxG followed by a hydrophobic pocket), absent here; (C) 2Fe-2S cluster binding requires a CxxCxxC-type cysteine cluster, not present; (D) peptidyl-tRNA hydrolase is a small (~20 kDa) enzyme with a completely different fold and active-site architecture, incompatible with a 2266-aa multi-domain protein. The condensation/synthase activity (A) is the only option consistent with the observed KS motifs and overall domain organization.


**Missing item-specific fact**

> None critical. The specific GO term GO:0004315 is technically defined for type II FAS (ACP-dependent), while this is a type I modular PKS (CoA-dependent); recognizing the mechanistic equivalence requires specialized PKS/FAS knowledge but is standard biochemistry.


**Reason**

> A model with general knowledge of enzyme domain motifs can identify KS-domain signatures, recognize the multi-domain PKS architecture, and eliminate the three distractors by absence of their characteristic structural/sequence features. The path to answer A is supported by sequence-level reasoning rather than pure memorization of a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (FAD binding), C (2Fe-2S cluster binding), and D (peptidyl-tRNA hydrolase) are clearly incompatible with a 2266-aa multi-domain PKS. Option A is the only mechanistically plausible choice despite the technical GO-term imprecision (type II FAS term applied to a type I PKS KS domain via IEA:InterPro). No ambiguity among the four choices.


### Important caveats

- The GO:0004315 annotation is IEA:InterPro (computational inference by domain similarity), not an experimental measurement. The protein's actual EC is 2.3.1.290, specific to the spectinabilin PKS system.
- GO:0004315 is formally defined for type II FAS using ACP thioesters; the modular PKS uses CoA thioesters. The annotation reflects mechanistic analogy at the KS domain level.
- The sequence contains a second internal copy of KS-like motifs (GCRYPGE region), consistent with a multi-module PKS, reinforcing the condensation-activity interpretation.
- The protein was first publicly released in UniProt on 2025-02-05; the benchmark's exact author snapshot is unknown but the sequence matches at all checked versions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 2266-aa sequence displays a large multi-domain architecture with repeated catalytic units characteristic of a modular PKS. Recognizable KS-domain motifs (e.g., 'GCRFPGG' near residue 37 and 'GCRYPGE' near residue ~1130) indicate condensation (ketoacyl synthase) activity. KR-domain motifs ('GHSQGE', 'HHCLL') and ACP-like regions further confirm PKS architecture. Distractor elimination: (B) FAD binding requires a Rossmann-fold flavin-binding motif (GxGxxG followed by a hydrophobic pocket), absent here; (C) 2Fe-2S cluster binding requires a CxxCxxC-type cysteine cluster, not present; (D) peptidyl-tRNA hydrolase is a small (~20 kDa) enzyme with a completely different fold and active-site architecture, incompatible with a 2266-aa multi-domain protein. The condensation/synthase activity (A) is the only option consistent with the observed KS motifs and overall domain organization.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific GO term GO:0004315 is technically defined for type II FAS (ACP-dependent), while this is a type I modular PKS (CoA-dependent); recognizing the mechanistic equivalence requires specialized PKS/FAS knowledge but is standard biochemistry.",
    "reason": "A model with general knowledge of enzyme domain motifs can identify KS-domain signatures, recognize the multi-domain PKS architecture, and eliminate the three distractors by absence of their characteristic structural/sequence features. The path to answer A is supported by sequence-level reasoning rather than pure memorization of a database entry."
  },
  "case_id": "GO_molecular_function_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H5",
      "C4",
      "C5",
      "C6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B4ER97 (NorC, spectinabilin PKS) carries GO:0004315 (3-oxoacyl-[acyl-carrier-protein] synthase activity) annotated with IEA:InterPro (C7/H5). The protein is a type I modular PKS whose ketosynthase (KS) domain catalyzes a condensation reaction mechanistically analogous to 3-oxoacyl-ACP synthase (EC 2.3.1.41). The annotation is computationally inferred (IEA) via domain-similarity to the FAS II β-ketoacyl-ACP synthase family, not directly experimental, but the mechanistic equivalence is well-established. The actual EC for the full PKS system is 2.3.1.290 (C4/C6), but the KS domain activity is the closest match among the given options."
  },
  "important_caveats": [
    "The GO:0004315 annotation is IEA:InterPro (computational inference by domain similarity), not an experimental measurement. The protein's actual EC is 2.3.1.290, specific to the spectinabilin PKS system.",
    "GO:0004315 is formally defined for type II FAS using ACP thioesters; the modular PKS uses CoA thioesters. The annotation reflects mechanistic analogy at the KS domain level.",
    "The sequence contains a second internal copy of KS-like motifs (GCRYPGE region), consistent with a multi-module PKS, reinforcing the condensation-activity interpretation.",
    "The protein was first publicly released in UniProt on 2025-02-05; the benchmark's exact author snapshot is unknown but the sequence matches at all checked versions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (FAD binding), C (2Fe-2S cluster binding), and D (peptidyl-tRNA hydrolase) are clearly incompatible with a 2266-aa multi-domain PKS. Option A is the only mechanistically plausible choice despite the technical GO-term imprecision (type II FAS term applied to a type I PKS KS domain via IEA:InterPro). No ambiguity among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B4ER97 (NorC, spectinabilin PKS) carries GO:0004315 (3-oxoacyl-[acyl-carrier-protein] synthase activity) annotated with IEA:InterPro (C7/H5). The protein is a type I modular PKS whose ketosynthase (KS) domain catalyzes a condensation reaction mechanistically analogous to 3-oxoacyl-ACP synthase (EC 2.3.1.41). The annotation is computationally inferred (IEA) via domain-similarity to the FAS II β-ketoacyl-ACP synthase family, not directly experimental, but the mechanistic equivalence is well-established. The actual EC for the full PKS system is 2.3.1.290 (C4/C6), but the KS domain activity is the closest match among the given options.",
    "evidence_ids": ["C7", "H5", "C4", "C5", "C6", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 2266-aa sequence displays a large multi-domain architecture with repeated catalytic units characteristic of a modular PKS. Recognizable KS-domain motifs (e.g., 'GCRFPGG' near residue 37 and 'GCRYPGE' near residue ~1130) indicate condensation (ketoacyl synthase) activity. KR-domain motifs ('GHSQGE', 'HHCLL') and ACP-like regions further confirm PKS architecture. Distractor elimination: (B) FAD binding requires a Rossmann-fold flavin-binding motif (GxGxxG followed by a hydrophobic pocket), absent here; (C) 2Fe-2S cluster binding requires a CxxCxxC-type cysteine cluster, not present; (D) peptidyl-tRNA hydrolase is a small (~20 kDa) enzyme with a completely different fold and active-site architecture, incompatible with a 2266-aa multi-domain protein. The condensation/synthase activity (A) is the only option consistent with the observed KS motifs and overall domain organization.",
    "missing_item_specific_fact": "None critical. The specific GO term GO:0004315 is technically defined for type II FAS (ACP-dependent), while this is a type I modular PKS (CoA-dependent); recognizing the mechanistic equivalence requires specialized PKS/FAS knowledge but is standard biochemistry.",
    "reason": "A model with general knowledge of enzyme domain motifs can identify KS-domain signatures, recognize the multi-domain PKS architecture, and eliminate the three distractors by absence of their characteristic structural/sequence features. The path to answer A is supported by sequence-level reasoning rather than pure memorization of a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (FAD binding), C (2Fe-2S cluster binding), and D (peptidyl-tRNA hydrolase) are clearly incompatible with a 2266-aa multi-domain PKS. Option A is the only mechanistically plausible choice despite the technical GO-term imprecision (type II FAS term applied to a type I PKS KS domain via IEA:InterPro). No ambiguity among the four choices."
  },
  "important_caveats": [
    "The GO:0004315 annotation is IEA:InterPro (computational inference by domain similarity), not an experimental measurement. The protein's actual EC is 2.3.1.290, specific to the spectinabilin PKS system.",
    "GO:0004315 is formally defined for type II FAS using ACP thioesters; the modular PKS uses CoA thioesters. The annotation reflects mechanistic analogy at the KS domain level.",
    "The sequence contains a second internal copy of KS-like motifs (GCRYPGE region), consistent with a multi-module PKS, reinforcing the condensation-activity interpretation.",
    "The protein was first publicly released in UniProt on 2025-02-05; the benchmark's exact author snapshot is unknown but the sequence matches at all checked versions."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:19.126101+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"17763486","source":"PubMed"}],"value":"Component of a type I modular polyketide synthase (PKS) that generates the backbone of the antibiotic spectinabilin (also known as neoaureothin), a nitroaryl-substituted polyketide metabolite (PubMed:17763486). This PKS system accepts the unusual starter unit 4-nitrobenzoyl-CoA and extends it by 6 molecules of (S)-methylmalonyl-CoA and a single molecule of malonyl-CoA (PubMed:17763486)"}]}
```

Source SHA-256: `4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:19.126101+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"17763486","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:58945"}}],"reaction":{"ecNumber":"2.3.1.290","evidences":[{"evidenceCode":"ECO:0000305","id":"17763486","source":"PubMed"}],"name":"4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:58944"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:16526"},{"database":"ChEBI","id":"CHEBI:57287"},{"database":"ChEBI","id":"CHEBI:57327"},{"database":"ChEBI","id":"CHEBI:57384"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:142871"},{"database":"ChEBI","id":"CHEBI:142872"}]}}
```

Source SHA-256: `4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)  
**Locator:** `/uniProtKBCrossReferences/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:19.126101+00:00.  

```json
{"database":"GO","id":"GO:0004315","properties":[{"key":"GoTerm","value":"F:3-oxoacyl-[acyl-carrier-protein] synthase activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)  
**Locator:** `lines 23-29`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-02T04:27:21.445291+00:00.  

```text
CC   -!- FUNCTION: Component of a type I modular polyketide synthase (PKS) that
CC       generates the backbone of the antibiotic spectinabilin (also known as
CC       neoaureothin), a nitroaryl-substituted polyketide metabolite
CC       (PubMed:17763486). This PKS system accepts the unusual starter unit 4-
CC       nitrobenzoyl-CoA and extends it by 6 molecules of (S)-methylmalonyl-CoA
CC       and a single molecule of malonyl-CoA (PubMed:17763486).
CC       {ECO:0000269|PubMed:17763486}.
```

Source SHA-256: `1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)  
**Locator:** `lines 60-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-02T04:27:21.445291+00:00.  

```text
DR   GO; GO:0004315; F:3-oxoacyl-[acyl-carrier-protein] synthase activity; IEA:InterPro.
```

Source SHA-256: `1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 39629-39711`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004315
name: 3-oxoacyl-[acyl-carrier-protein] synthase activity
namespace: molecular_function
alt_id: GO:0033817
def: "Catalysis of the reaction: acyl-[acyl-carrier protein] + malonyl-[acyl-carrier protein] = 3-oxoacyl-[acyl-carrier protein] + CO2 + [acyl-carrier protein]." [RHEA:22836]
comment: Note that this activity is responsible for the chain-elongation step of dissociated (type II) fatty-acid biosynthesis, i.e. the addition of two C atoms to the fatty-acid chain. Can use fatty acyl thioesters of ACP (C2 to C16) as substrates, as well as fatty acyl thioesters of Co-A (C4 to C16).
synonym: "3-ketoacyl-acyl carrier protein synthase activity" RELATED [EC:2.3.1.41]
synonym: "3-oxoacyl-[acyl-carrier protein] synthase activity" EXACT []
synonym: "3-oxoacyl-ACP synthase activity" EXACT []
synonym: "3-oxoacyl-acyl carrier protein synthase I activity" NARROW [EC:2.3.1.179]
synonym: "3-oxoacyl-acyl-carrier-protein synthase activity" RELATED [EC:2.3.1.41]
synonym: "acyl-acyl-carrier-protein:malonyl-acyl-carrier-protein C-acyltransferase (decarboxylating)" RELATED [EC:2.3.1.41]
synonym: "acyl-malonyl acyl carrier protein-condensing enzyme activity" RELATED [EC:2.3.1.41]
synonym: "acyl-malonyl(acyl-carrier-protein)-condensing enzyme activity" RELATED [EC:2.3.1.41]
synonym: "beta-ketoacyl acyl carrier protein synthase activity" RELATED [EC:2.3.1.41]
synonym: "beta-ketoacyl synthetase activity" RELATED [EC:2.3.1.41]
synonym: "beta-ketoacyl-[acyl carrier protein] synthase activity" RELATED [EC:2.3.1.41]
synonym: "beta-ketoacyl-ACP synthase I activity" NARROW [EC:2.3.1.41]
synonym: "beta-ketoacyl-ACP synthase II activity" NARROW [EC:2.3.1.179]
synonym: "beta-ketoacyl-ACP synthetase activity" RELATED [EC:2.3.1.41]
synonym: "beta-ketoacyl-acyl carrier protein synthase activity" RELATED [EC:2.3.1.41]
synonym: "beta-ketoacyl-acyl carrier protein synthetase activity" RELATED [EC:2.3.1.41]
synonym: "beta-ketoacyl-acyl-carrier-protein synthase I" NARROW [EC:2.3.1.41]
synonym: "beta-ketoacyl-acyl-carrier-protein synthase II activity" NARROW []
synonym: "beta-ketoacylsynthase activity" RELATED [EC:2.3.1.41]
synonym: "condensing enzyme activity" BROAD [EC:2.3.1.41]
synonym: "fatty acid condensing enzyme activity" BROAD [EC:2.3.1.41]
synonym: "ketoacyl-ACP synthase activity" EXACT []
xref: EC:2.3.1.179
xref: EC:2.3.1.41
xref: MetaCyc:2.3.1.179-RXN
xref: MetaCyc:3-OXOACYL-ACP-SYNTH-RXN
xref: RHEA:14565
xref: RHEA:22836
xref: RHEA:41800
xref: RHEA:41820
xref: RHEA:41836
xref: RHEA:41852
xref: RHEA:41868
xref: RHEA:41884
xref: RHEA:41900
xref: RHEA:41916
xref: RHEA:42248
xref: RHEA:42252
xref: RHEA:42260
xref: RHEA:42268
xref: RHEA:42272
xref: RHEA:42276
xref: RHEA:47824
xref: RHEA:54924
xref: RHEA:54940
xref: RHEA:55040
xref: RHEA:65308
xref: RHEA:65312
is_a: GO:0016747 ! acyltransferase activity, transferring groups other than amino-acyl groups
property_value: skos:exactMatch EC:2.3.1.41
property_value: skos:exactMatch MetaCyc:3-OXOACYL-ACP-SYNTH-RXN
property_value: skos:exactMatch RHEA:22836
property_value: skos:narrowMatch EC:2.3.1.179
property_value: skos:narrowMatch MetaCyc:2.3.1.179-RXN
property_value: skos:narrowMatch RHEA:14565
property_value: skos:narrowMatch RHEA:41800
property_value: skos:narrowMatch RHEA:41820
property_value: skos:narrowMatch RHEA:41836
property_value: skos:narrowMatch RHEA:41852
property_value: skos:narrowMatch RHEA:41868
property_value: skos:narrowMatch RHEA:41884
property_value: skos:narrowMatch RHEA:41900
property_value: skos:narrowMatch RHEA:41916
property_value: skos:narrowMatch RHEA:42248
property_value: skos:narrowMatch RHEA:42252
property_value: skos:narrowMatch RHEA:42260
property_value: skos:narrowMatch RHEA:42268
property_value: skos:narrowMatch RHEA:42272
property_value: skos:narrowMatch RHEA:42276
property_value: skos:narrowMatch RHEA:47824
property_value: skos:narrowMatch RHEA:54924
property_value: skos:narrowMatch RHEA:54940
property_value: skos:narrowMatch RHEA:55040
property_value: skos:narrowMatch RHEA:65308
property_value: skos:narrowMatch RHEA:65312

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 101. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
