# cofactor_0076

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — pantetheine 4&#x27;-phosphate

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
A. Zn(2+)
B. pantetheine 4'-phosphate
C. NAD(+)
D. [4Fe-4S] cluster
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

> The exact sequence matches the UniProt NorC entry, which annotates pantetheine 4'-phosphate as a cofactor. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, repeated sequence architecture is consistent with a modular polyketide synthase containing acyl-carrier-protein domains. Such carrier domains require a covalently attached 4'-phosphopantetheine group, distinguishing this option from Zn(2+), NAD(+), and an iron-sulfur cluster.


**Missing item-specific fact**

> No essential protein-specific annotation is needed for this broad inference; identifying the exact NorC accession would be additional lookup information, not information supplied to the model.


**Reason**

> The sequence's repeated modular architecture supports a defensible polyketide-synthase/carrier-domain inference, and carrier domains use the phosphopantetheine cofactor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The PKS carrier-domain interpretation specifically favors pantetheine 4'-phosphate among the listed options.


### Important caveats

- The reviewer-only database annotation is computational and does not establish experimental confirmation.
- The annotation and sequence match apply to the 2266-residue NorC entry; the precise author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, repeated sequence architecture is consistent with a modular polyketide synthase containing acyl-carrier-protein domains. Such carrier domains require a covalently attached 4'-phosphopantetheine group, distinguishing this option from Zn(2+), NAD(+), and an iron-sulfur cluster.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No essential protein-specific annotation is needed for this broad inference; identifying the exact NorC accession would be additional lookup information, not information supplied to the model.",
    "reason": "The sequence's repeated modular architecture supports a defensible polyketide-synthase/carrier-domain inference, and carrier domains use the phosphopantetheine cofactor."
  },
  "case_id": "cofactor_0076",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt NorC entry, which annotates pantetheine 4'-phosphate as a cofactor. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The reviewer-only database annotation is computational and does not establish experimental confirmation.",
    "The annotation and sequence match apply to the 2266-residue NorC entry; the precise author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PKS carrier-domain interpretation specifically favors pantetheine 4'-phosphate among the listed options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0076",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt NorC entry, which annotates pantetheine 4'-phosphate as a cofactor. The annotation is based on a PROSITE-ProRule computational inference, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, repeated sequence architecture is consistent with a modular polyketide synthase containing acyl-carrier-protein domains. Such carrier domains require a covalently attached 4'-phosphopantetheine group, distinguishing this option from Zn(2+), NAD(+), and an iron-sulfur cluster.",
    "missing_item_specific_fact": "No essential protein-specific annotation is needed for this broad inference; identifying the exact NorC accession would be additional lookup information, not information supplied to the model.",
    "reason": "The sequence's repeated modular architecture supports a defensible polyketide-synthase/carrier-domain inference, and carrier domains use the phosphopantetheine cofactor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PKS carrier-domain interpretation specifically favors pantetheine 4'-phosphate among the listed options."
  },
  "important_caveats": [
    "The reviewer-only database annotation is computational and does not establish experimental confirmation.",
    "The annotation and sequence match apply to the 2266-residue NorC entry; the precise author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B4ER97 (Spectinabilin polyketide synthase system protein NorC, EC 2.3.1.290) explicitly annotates pantetheine 4'-phosphate (ChEBI:47942) as the cofactor (evidence_id C5, H4). The evidence code is ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule PRU00258), i.e., computational inference from ACP domain signature rather than direct experimental measurement. However, the underlying biochemistry—that acyl carrier protein (ACP) domains universally carry pantetheine 4'-phosphate as a prosthetic group—is well-established. The sequence contains recognizable ACP domain motifs (e.g., 'GHSQGE' in 'VGHSQGEIAAACVAG', 'GCRFPGG' appearing twice, 'GCRYPGE' appearing once), consistent with the annotation. The protein is a modular PKS with EC 2.3.1.290, for which pantetheine 4'-phosphate on ACP domains is the defining cofactor.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 2266-aa sequence contains multiple recognizable ACP domain signatures: the canonical 'GHSQGE' motif (with the critical serine for pantetheine attachment) in 'VGHSQGEIAAACVAG', and the conserved 'GCRFPGG'/'GCRYPGE' motifs flanking the ACP β-sheet. These are among the most well-known sequence signatures in biochemistry, taught in standard enzymology courses. The well-established rule that ACP domains in PKS/FAS enzymes carry pantetheine 4'-phosphate as their prosthetic group allows a knowledgeable biologist to identify option B from the sequence motifs alone. The modular PKS architecture (repeated KS-AT-DH-ER-KR-ACP-like domain organization across the long sequence) further supports this. Zn(2+) (metalloproteases, alcohol dehydrogenases), &#91;4Fe-4S&#93; (radical SAM, ferredoxins), and NAD(+) (dehydrogenases) lack corresponding domain signatures in this sequence.


**Missing item-specific fact**

> None critical. Recognition of the ACP domain signature (GHSQGE, GCRFPGG/GCRYPGE) and the universal ACP–pantetheine 4'-phosphate linkage are general biochemistry facts. One could argue that identifying the exact protein as a PKS rather than FAS requires domain-architecture knowledge, but the ACP–pantetheine link holds for both.


**Reason**

> The ACP domain motif is a concrete, identifiable feature in the supplied sequence. The biochemical rule linking ACP to pantetheine 4'-phosphate is textbook knowledge, not an item-specific database lookup. A model trained on general biochemistry can reason from the visible motifs to the correct cofactor without needing to know the specific UniProt accession.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While modular PKSs contain KR and DH subdomains that transiently use NAD(P)H/NAD+, the question asks for 'the specific cofactor required for catalytic activity' of the protein. Pantetheine 4'-phosphate on ACP domains is the central, defining cofactor that shuttles intermediates across all catalytic domains. NAD(+) (option C) is a co-substrate for specific subdomains, not the protein's defining cofactor. Zn(2+) and &#91;4Fe-4S&#93; have no structural or functional basis in this sequence. Option B is clearly the best answer.


### Important caveats

- The UniProt cofactor annotation uses evidence code ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule), meaning it is a computational inference from domain signature rather than a direct experimental measurement of pantetheine attachment on this specific protein.
- The EC number 2.3.1.290 is annotated with ECO:0000305 (inferred from sequence or structural similarity), not from direct enzymatic assay of this specific protein.
- The protein is a modular PKS with multiple domains; some subdomains (KR, DH) could transiently involve NAD(P) cofactors, but the question's phrasing and the ACP-centric architecture make pantetheine 4'-phosphate the unambiguous intended answer.
- Sequence identity is confirmed (SHA-256 match) between the benchmark sequence and UniProt B4ER97 (2266 aa, sequence version 1).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 2266-aa sequence contains multiple recognizable ACP domain signatures: the canonical 'GHSQGE' motif (with the critical serine for pantetheine attachment) in 'VGHSQGEIAAACVAG', and the conserved 'GCRFPGG'/'GCRYPGE' motifs flanking the ACP β-sheet. These are among the most well-known sequence signatures in biochemistry, taught in standard enzymology courses. The well-established rule that ACP domains in PKS/FAS enzymes carry pantetheine 4'-phosphate as their prosthetic group allows a knowledgeable biologist to identify option B from the sequence motifs alone. The modular PKS architecture (repeated KS-AT-DH-ER-KR-ACP-like domain organization across the long sequence) further supports this. Zn(2+) (metalloproteases, alcohol dehydrogenases), [4Fe-4S] (radical SAM, ferredoxins), and NAD(+) (dehydrogenases) lack corresponding domain signatures in this sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognition of the ACP domain signature (GHSQGE, GCRFPGG/GCRYPGE) and the universal ACP–pantetheine 4'-phosphate linkage are general biochemistry facts. One could argue that identifying the exact protein as a PKS rather than FAS requires domain-architecture knowledge, but the ACP–pantetheine link holds for both.",
    "reason": "The ACP domain motif is a concrete, identifiable feature in the supplied sequence. The biochemical rule linking ACP to pantetheine 4'-phosphate is textbook knowledge, not an item-specific database lookup. A model trained on general biochemistry can reason from the visible motifs to the correct cofactor without needing to know the specific UniProt accession."
  },
  "case_id": "cofactor_0076",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B4ER97 (Spectinabilin polyketide synthase system protein NorC, EC 2.3.1.290) explicitly annotates pantetheine 4'-phosphate (ChEBI:47942) as the cofactor (evidence_id C5, H4). The evidence code is ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule PRU00258), i.e., computational inference from ACP domain signature rather than direct experimental measurement. However, the underlying biochemistry—that acyl carrier protein (ACP) domains universally carry pantetheine 4'-phosphate as a prosthetic group—is well-established. The sequence contains recognizable ACP domain motifs (e.g., 'GHSQGE' in 'VGHSQGEIAAACVAG', 'GCRFPGG' appearing twice, 'GCRYPGE' appearing once), consistent with the annotation. The protein is a modular PKS with EC 2.3.1.290, for which pantetheine 4'-phosphate on ACP domains is the defining cofactor."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses evidence code ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule), meaning it is a computational inference from domain signature rather than a direct experimental measurement of pantetheine attachment on this specific protein.",
    "The EC number 2.3.1.290 is annotated with ECO:0000305 (inferred from sequence or structural similarity), not from direct enzymatic assay of this specific protein.",
    "The protein is a modular PKS with multiple domains; some subdomains (KR, DH) could transiently involve NAD(P) cofactors, but the question's phrasing and the ACP-centric architecture make pantetheine 4'-phosphate the unambiguous intended answer.",
    "Sequence identity is confirmed (SHA-256 match) between the benchmark sequence and UniProt B4ER97 (2266 aa, sequence version 1)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While modular PKSs contain KR and DH subdomains that transiently use NAD(P)H/NAD+, the question asks for 'the specific cofactor required for catalytic activity' of the protein. Pantetheine 4'-phosphate on ACP domains is the central, defining cofactor that shuttles intermediates across all catalytic domains. NAD(+) (option C) is a co-substrate for specific subdomains, not the protein's defining cofactor. Zn(2+) and [4Fe-4S] have no structural or functional basis in this sequence. Option B is clearly the best answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0076",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B4ER97 (Spectinabilin polyketide synthase system protein NorC, EC 2.3.1.290) explicitly annotates pantetheine 4'-phosphate (ChEBI:47942) as the cofactor (evidence_id C5, H4). The evidence code is ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule PRU00258), i.e., computational inference from ACP domain signature rather than direct experimental measurement. However, the underlying biochemistry—that acyl carrier protein (ACP) domains universally carry pantetheine 4'-phosphate as a prosthetic group—is well-established. The sequence contains recognizable ACP domain motifs (e.g., 'GHSQGE' in 'VGHSQGEIAAACVAG', 'GCRFPGG' appearing twice, 'GCRYPGE' appearing once), consistent with the annotation. The protein is a modular PKS with EC 2.3.1.290, for which pantetheine 4'-phosphate on ACP domains is the defining cofactor.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 2266-aa sequence contains multiple recognizable ACP domain signatures: the canonical 'GHSQGE' motif (with the critical serine for pantetheine attachment) in 'VGHSQGEIAAACVAG', and the conserved 'GCRFPGG'/'GCRYPGE' motifs flanking the ACP β-sheet. These are among the most well-known sequence signatures in biochemistry, taught in standard enzymology courses. The well-established rule that ACP domains in PKS/FAS enzymes carry pantetheine 4'-phosphate as their prosthetic group allows a knowledgeable biologist to identify option B from the sequence motifs alone. The modular PKS architecture (repeated KS-AT-DH-ER-KR-ACP-like domain organization across the long sequence) further supports this. Zn(2+) (metalloproteases, alcohol dehydrogenases), [4Fe-4S] (radical SAM, ferredoxins), and NAD(+) (dehydrogenases) lack corresponding domain signatures in this sequence.",
    "missing_item_specific_fact": "None critical. Recognition of the ACP domain signature (GHSQGE, GCRFPGG/GCRYPGE) and the universal ACP–pantetheine 4'-phosphate linkage are general biochemistry facts. One could argue that identifying the exact protein as a PKS rather than FAS requires domain-architecture knowledge, but the ACP–pantetheine link holds for both.",
    "reason": "The ACP domain motif is a concrete, identifiable feature in the supplied sequence. The biochemical rule linking ACP to pantetheine 4'-phosphate is textbook knowledge, not an item-specific database lookup. A model trained on general biochemistry can reason from the visible motifs to the correct cofactor without needing to know the specific UniProt accession."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While modular PKSs contain KR and DH subdomains that transiently use NAD(P)H/NAD+, the question asks for 'the specific cofactor required for catalytic activity' of the protein. Pantetheine 4'-phosphate on ACP domains is the central, defining cofactor that shuttles intermediates across all catalytic domains. NAD(+) (option C) is a co-substrate for specific subdomains, not the protein's defining cofactor. Zn(2+) and [4Fe-4S] have no structural or functional basis in this sequence. Option B is clearly the best answer."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses evidence code ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule), meaning it is a computational inference from domain signature rather than a direct experimental measurement of pantetheine attachment on this specific protein.",
    "The EC number 2.3.1.290 is annotated with ECO:0000305 (inferred from sequence or structural similarity), not from direct enzymatic assay of this specific protein.",
    "The protein is a modular PKS with multiple domains; some subdomains (KR, DH) could transiently involve NAD(P) cofactors, but the question's phrasing and the ACP-centric architecture make pantetheine 4'-phosphate the unambiguous intended answer.",
    "Sequence identity is confirmed (SHA-256 match) between the benchmark sequence and UniProt B4ER97 (2266 aa, sequence version 1)."
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
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:19.126101+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:47942"},"evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00258","source":"PROSITE-ProRule"}],"name":"pantetheine 4'-phosphate"}],"commentType":"COFACTOR"}
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)  
**Locator:** `lines 40-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-02T04:27:21.445291+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=pantetheine 4'-phosphate; Xref=ChEBI:CHEBI:47942;
CC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00258};
```

Source SHA-256: `1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 76. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
