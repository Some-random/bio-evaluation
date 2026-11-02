# pathway_0093

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **A** — Antibiotic biosynthesis. .

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
A. Antibiotic biosynthesis. .
B. tetrahydrofolate biosynthesis
C. Glycan degradation
D. oxylipin biosynthesis. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence match is annotated as the spectinabilin polyketide synthase system protein NorC, with an Antibiotic biosynthesis pathway annotation. This supports choice A, though the annotation is not independently validated here by reviewing the underlying paper.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The unusually long sequence with repeated enzyme-like regions is consistent with a modular polyketide synthase, a bacterial secondary-metabolite biosynthetic system. Among the choices, antibiotic biosynthesis is a meaningful fit, unlike tetrahydrofolate biosynthesis or glycan degradation; oxylipin biosynthesis is also a poorer fit for this apparent bacterial megasynthase.


**Missing item-specific fact**

> The specific product and pathway assignment—NorC’s role in the spectinabilin system—are not given in the input. That fact would establish the precise annotation, but the sequence architecture and choices provide a defensible basis for selecting A.


**Reason**

> The sequence and alternatives support a broad biological inference toward polyketide/secondary-metabolite biosynthesis. The precise antibiotic assignment is protein-specific, so the inference is not conclusive, but it does not depend solely on recognizing a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No listed alternative is comparably supported by the sequence’s apparent modular biosynthetic architecture, although the sequence alone does not identify the specific antibiotic product.


### Important caveats

- The pathway annotation is reviewer-only information and was not supplied to the evaluated model.
- The UniProt pathway annotation cites a publication, but the underlying experimental evidence was not independently assessed.
- The annotation also identifies polyketide biosynthesis, a more specific pathway label not offered among the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The unusually long sequence with repeated enzyme-like regions is consistent with a modular polyketide synthase, a bacterial secondary-metabolite biosynthetic system. Among the choices, antibiotic biosynthesis is a meaningful fit, unlike tetrahydrofolate biosynthesis or glycan degradation; oxylipin biosynthesis is also a poorer fit for this apparent bacterial megasynthase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific product and pathway assignment—NorC’s role in the spectinabilin system—are not given in the input. That fact would establish the precise annotation, but the sequence architecture and choices provide a defensible basis for selecting A.",
    "reason": "The sequence and alternatives support a broad biological inference toward polyketide/secondary-metabolite biosynthesis. The precise antibiotic assignment is protein-specific, so the inference is not conclusive, but it does not depend solely on recognizing a database entry."
  },
  "case_id": "pathway_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as the spectinabilin polyketide synthase system protein NorC, with an Antibiotic biosynthesis pathway annotation. This supports choice A, though the annotation is not independently validated here by reviewing the underlying paper."
  },
  "important_caveats": [
    "The pathway annotation is reviewer-only information and was not supplied to the evaluated model.",
    "The UniProt pathway annotation cites a publication, but the underlying experimental evidence was not independently assessed.",
    "The annotation also identifies polyketide biosynthesis, a more specific pathway label not offered among the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No listed alternative is comparably supported by the sequence’s apparent modular biosynthetic architecture, although the sequence alone does not identify the specific antibiotic product."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as the spectinabilin polyketide synthase system protein NorC, with an Antibiotic biosynthesis pathway annotation. This supports choice A, though the annotation is not independently validated here by reviewing the underlying paper.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The unusually long sequence with repeated enzyme-like regions is consistent with a modular polyketide synthase, a bacterial secondary-metabolite biosynthetic system. Among the choices, antibiotic biosynthesis is a meaningful fit, unlike tetrahydrofolate biosynthesis or glycan degradation; oxylipin biosynthesis is also a poorer fit for this apparent bacterial megasynthase.",
    "missing_item_specific_fact": "The specific product and pathway assignment—NorC’s role in the spectinabilin system—are not given in the input. That fact would establish the precise annotation, but the sequence architecture and choices provide a defensible basis for selecting A.",
    "reason": "The sequence and alternatives support a broad biological inference toward polyketide/secondary-metabolite biosynthesis. The precise antibiotic assignment is protein-specific, so the inference is not conclusive, but it does not depend solely on recognizing a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No listed alternative is comparably supported by the sequence’s apparent modular biosynthetic architecture, although the sequence alone does not identify the specific antibiotic product."
  },
  "important_caveats": [
    "The pathway annotation is reviewer-only information and was not supplied to the evaluated model.",
    "The UniProt pathway annotation cites a publication, but the underlying experimental evidence was not independently assessed.",
    "The annotation also identifies polyketide biosynthesis, a more specific pathway label not offered among the choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B4ER97 (NORC_STRON), whose sequence exactly matches the benchmark input (2266 aa, SHA-256 confirmed), is annotated with 'PATHWAY: Antibiotic biosynthesis' (evidence ECO:0000305|PubMed:17763486) and 'PATHWAY: Polyketide biosynthesis'. The protein is named 'Spectinabilin polyketide synthase system protein NorC' (EC 2.3.1.290), a modular PKS from Streptomyces orinoci. Spectinabilin is a polyketide antibiotic, so the 'Antibiotic biosynthesis' pathway annotation is consistent with the protein's characterized function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 2266-aa sequence contains multiple copies of hallmark modular polyketide synthase (PKS) domain motifs: acyltransferase (AT) signatures ('MGCRFPGG' near position 50 and 'MGCRYPGE' near position 1100), ketosynthase (KS) 'GHSQGE'-type motifs, and repeated thioesterase-like C-terminal regions. This multi-domain, iterative architecture is diagnostic of a modular PKS and is fundamentally incompatible with glycosidases/cellulases (glycan degradation), GTP cyclohydrolase/dihydroneopterin aldolase (tetrahydrofolate biosynthesis), or lipoxygenases/cytochrome P450s (oxylipin biosynthesis). General knowledge that modular PKSs in Actinomycetes (the high-Ala/Gly/Arg/Pro composition is consistent with a high-GC Actinobacterium) produce polyketides, the majority of which are antibiotics, supports selecting 'Antibiotic biosynthesis' over the three unrelated distractors.


**Missing item-specific fact**

> None strictly required. The specific product (spectinabilin) and organism (Streptomyces orinoci) are not needed to eliminate B, C, and D; the PKS domain architecture alone is sufficient to rule out folate, glycan, and oxylipin pathways.


**Reason**

> The sequence itself encodes identifiable PKS domain motifs. A knowledgeable reader can recognize the modular PKS architecture, associate it with polyketide/antibiotic biosynthesis, and eliminate the three mechanistically unrelated distractors without needing to look up B4ER97 or recall the specific gene cluster.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (tetrahydrofolate biosynthesis), C (glycan degradation), and D (oxylipin biosynthesis) involve entirely different enzyme classes (GTP cyclohydrolases, glycosidases, lipoxygenases) that share no domain architecture with the supplied sequence. Only option A is compatible with a modular PKS. Minor formatting artifacts (double periods in A and D) do not create ambiguity.


### Important caveats

- The UniProt pathway annotation carries evidence code ECO:0000305 (curator inference from a single PubMed reference, PMID 17763486), not direct experimental validation of the pathway label itself. The underlying biochemical characterization of the PKS cluster is from that 2007 ChemBioChem paper.
- The reviewer-only UniProt accession and annotation were not available to the evaluated model; the reasoning-supported classification rests solely on sequence-recognizable PKS motifs and general pathway biology.
- The entry was first publicly released in 2025-02-05; the author's data-construction snapshot is unknown, though the sequence itself has been unchanged since 2008-09-23.
- 'Antibiotic biosynthesis' and 'Polyketide biosynthesis' are both listed as pathways for this entry; the question's option set does not include 'Polyketide biosynthesis' as a competing choice, so no intra-option ambiguity arises.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 2266-aa sequence contains multiple copies of hallmark modular polyketide synthase (PKS) domain motifs: acyltransferase (AT) signatures ('MGCRFPGG' near position 50 and 'MGCRYPGE' near position 1100), ketosynthase (KS) 'GHSQGE'-type motifs, and repeated thioesterase-like C-terminal regions. This multi-domain, iterative architecture is diagnostic of a modular PKS and is fundamentally incompatible with glycosidases/cellulases (glycan degradation), GTP cyclohydrolase/dihydroneopterin aldolase (tetrahydrofolate biosynthesis), or lipoxygenases/cytochrome P450s (oxylipin biosynthesis). General knowledge that modular PKSs in Actinomycetes (the high-Ala/Gly/Arg/Pro composition is consistent with a high-GC Actinobacterium) produce polyketides, the majority of which are antibiotics, supports selecting 'Antibiotic biosynthesis' over the three unrelated distractors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The specific product (spectinabilin) and organism (Streptomyces orinoci) are not needed to eliminate B, C, and D; the PKS domain architecture alone is sufficient to rule out folate, glycan, and oxylipin pathways.",
    "reason": "The sequence itself encodes identifiable PKS domain motifs. A knowledgeable reader can recognize the modular PKS architecture, associate it with polyketide/antibiotic biosynthesis, and eliminate the three mechanistically unrelated distractors without needing to look up B4ER97 or recall the specific gene cluster."
  },
  "case_id": "pathway_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B4ER97 (NORC_STRON), whose sequence exactly matches the benchmark input (2266 aa, SHA-256 confirmed), is annotated with 'PATHWAY: Antibiotic biosynthesis' (evidence ECO:0000305|PubMed:17763486) and 'PATHWAY: Polyketide biosynthesis'. The protein is named 'Spectinabilin polyketide synthase system protein NorC' (EC 2.3.1.290), a modular PKS from Streptomyces orinoci. Spectinabilin is a polyketide antibiotic, so the 'Antibiotic biosynthesis' pathway annotation is consistent with the protein's characterized function."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000305 (curator inference from a single PubMed reference, PMID 17763486), not direct experimental validation of the pathway label itself. The underlying biochemical characterization of the PKS cluster is from that 2007 ChemBioChem paper.",
    "The reviewer-only UniProt accession and annotation were not available to the evaluated model; the reasoning-supported classification rests solely on sequence-recognizable PKS motifs and general pathway biology.",
    "The entry was first publicly released in 2025-02-05; the author's data-construction snapshot is unknown, though the sequence itself has been unchanged since 2008-09-23.",
    "'Antibiotic biosynthesis' and 'Polyketide biosynthesis' are both listed as pathways for this entry; the question's option set does not include 'Polyketide biosynthesis' as a competing choice, so no intra-option ambiguity arises."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (tetrahydrofolate biosynthesis), C (glycan degradation), and D (oxylipin biosynthesis) involve entirely different enzyme classes (GTP cyclohydrolases, glycosidases, lipoxygenases) that share no domain architecture with the supplied sequence. Only option A is compatible with a modular PKS. Minor formatting artifacts (double periods in A and D) do not create ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B4ER97 (NORC_STRON), whose sequence exactly matches the benchmark input (2266 aa, SHA-256 confirmed), is annotated with 'PATHWAY: Antibiotic biosynthesis' (evidence ECO:0000305|PubMed:17763486) and 'PATHWAY: Polyketide biosynthesis'. The protein is named 'Spectinabilin polyketide synthase system protein NorC' (EC 2.3.1.290), a modular PKS from Streptomyces orinoci. Spectinabilin is a polyketide antibiotic, so the 'Antibiotic biosynthesis' pathway annotation is consistent with the protein's characterized function.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 2266-aa sequence contains multiple copies of hallmark modular polyketide synthase (PKS) domain motifs: acyltransferase (AT) signatures ('MGCRFPGG' near position 50 and 'MGCRYPGE' near position 1100), ketosynthase (KS) 'GHSQGE'-type motifs, and repeated thioesterase-like C-terminal regions. This multi-domain, iterative architecture is diagnostic of a modular PKS and is fundamentally incompatible with glycosidases/cellulases (glycan degradation), GTP cyclohydrolase/dihydroneopterin aldolase (tetrahydrofolate biosynthesis), or lipoxygenases/cytochrome P450s (oxylipin biosynthesis). General knowledge that modular PKSs in Actinomycetes (the high-Ala/Gly/Arg/Pro composition is consistent with a high-GC Actinobacterium) produce polyketides, the majority of which are antibiotics, supports selecting 'Antibiotic biosynthesis' over the three unrelated distractors.",
    "missing_item_specific_fact": "None strictly required. The specific product (spectinabilin) and organism (Streptomyces orinoci) are not needed to eliminate B, C, and D; the PKS domain architecture alone is sufficient to rule out folate, glycan, and oxylipin pathways.",
    "reason": "The sequence itself encodes identifiable PKS domain motifs. A knowledgeable reader can recognize the modular PKS architecture, associate it with polyketide/antibiotic biosynthesis, and eliminate the three mechanistically unrelated distractors without needing to look up B4ER97 or recall the specific gene cluster."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (tetrahydrofolate biosynthesis), C (glycan degradation), and D (oxylipin biosynthesis) involve entirely different enzyme classes (GTP cyclohydrolases, glycosidases, lipoxygenases) that share no domain architecture with the supplied sequence. Only option A is compatible with a modular PKS. Minor formatting artifacts (double periods in A and D) do not create ambiguity."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000305 (curator inference from a single PubMed reference, PMID 17763486), not direct experimental validation of the pathway label itself. The underlying biochemical characterization of the PKS cluster is from that 2007 ChemBioChem paper.",
    "The reviewer-only UniProt accession and annotation were not available to the evaluated model; the reasoning-supported classification rests solely on sequence-recognizable PKS motifs and general pathway biology.",
    "The entry was first publicly released in 2025-02-05; the author's data-construction snapshot is unknown, though the sequence itself has been unchanged since 2008-09-23.",
    "'Antibiotic biosynthesis' and 'Polyketide biosynthesis' are both listed as pathways for this entry; the question's option set does not include 'Polyketide biosynthesis' as a competing choice, so no intra-option ambiguity arises."
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
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:19.126101+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"17763486","source":"PubMed"}],"value":"Antibiotic biosynthesis"}]}
```

Source SHA-256: `4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:19.126101+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"17763486","source":"PubMed"}],"value":"Polyketide biosynthesis"}]}
```

Source SHA-256: `4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b`.

### Evidence C7

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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)  
**Locator:** `lines 43-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-02T04:27:21.445291+00:00.  

```text
CC   -!- PATHWAY: Antibiotic biosynthesis. {ECO:0000305|PubMed:17763486}.
```

Source SHA-256: `1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)  
**Locator:** `lines 44-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-02T04:27:21.445291+00:00.  

```text
CC   -!- PATHWAY: Polyketide biosynthesis. {ECO:0000305|PubMed:17763486}.
```

Source SHA-256: `1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 93. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
