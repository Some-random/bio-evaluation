# GO_molecular_function_0027

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — phosphopantetheine binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSHSSHYSPVDSGMVPSSSSTEDHLSPTLSASIVLPAQLNPFAKAYDIPPSSIVQLGWALLLRCHLAIPSPCWSTIDDKTMPRGSDTHALQWESLHLEEGRSISWILQRWEDPSVHWYLSSDQLPGSKSPTLTTMLFLVKEYGLFDPVTPIDPGMGTIIYFYPSDEQPRLHISWNPDVVSSGHAFHLTRSLEHALQTIFLAPSVDIRDVNLFGIWDHQQLLQWNSYCPDPVDRLVQEMFQDVVAATPEASAVAAWDGELNYRELDRLSSRLAGVLQSDFGVVSETIVALCFEKSVWAIVAMLAVVKAGGAFLHIDPQHPPARHQAMIKSTASKLFLCSEQTRDTVVRSVPDCPSLVIHREMFAAQPDHAQQDTVISSGNLGPTNAAYVVCTSGSTGTPKAIVVEHVSLCSSVTAQAKAMDITAGSRVLQYAAYTFDVSIGDIFAALTHGACICIPSNWERAHDLSGAINRLGVNQACLTSTVASLLTPVEVPKLKKLTLGGEPATQQCINMWVDKVALKNIYGPAECTVWCIIQPDVSSGIAVSNIGHAIGARAWIVHPENHDRLMPIGAVGELLIEGPLVARGYLNDPVRTNAVFLAQPPIWLASFGPPPPRSRFYKTGDLARYGPGGALLFEGRKDTQVKLRGQRIELGEVEYRLHQALSDLSPSAAVELVHPKESTAPLLCAFITWDEGIDLDLQPAKPPLSACLTPNARKRFNHTVSLLQTEMERTLPAYMIPGLCIPVHKLPLTTSGKLDRKALRYFCTQHSLAFLSTFENNNVNSPTDGATDSFAAPLETVSPAESTLAQLWAQVLGRKTDSIGRKDNFLSLGGDSLAAMRLVNRAARDAQLTLTVADVFKCPVLADQASLVRPLVQTRNLVPFELMAPGDLQIEDLVAYVAEKCGVLHDQVEDIYPCTPLQDEMMRDSLSGDRTQMGQEVILLAEDLDIPRYLSACARVFQRFPILRTRFVQHSDRLIQVVIRENLGWQRPESLTEYVEADAKEAPALNKPLTRWALTSDSTHCILTMHHSIFDGISLGHILGAIYAVYQSIPLPPDSVSFAAFLAQINEHTSGLSDDSKQFWRSYLRPSPGSGDLPLPIVDSTYRPCANRGTQRLVTFQSGVVPALQQHGLTEATLIRGAWACTLAQLQTSSSTPSDVVFGTILTGRNLHLPGVDALVAPTLTHAPIRIRMSAASNEKPASFLARVQADATAMIPFEHDGMDRIRAIDAQVRAVCDQMQTLLVIQPIPEGLTSASTSPFPGPILSGPRVEAREMRHFHWYGLLVECTLLPTNGFFVRMCYDDKLFSSEDVERLLDDYSQALHELGGGLTEGEEVHLPTERKLDTLTLPGLVAPSGAEDMV

[Multiple Choices]
A. endo-1,4-beta-xylanase activity
B. mannose-6-phosphate isomerase activity
C. phosphopantetheine binding
D. methylated histone binding
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

> The exact sequence is annotated for phosphopantetheine binding by InterPro (computational evidence), and the matched protein is identified as an NRPS-like enzyme. Its experimentally described catalytic activity is esterification, which supports the NRPS context but is not direct experimental evidence of phosphopantetheine binding.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H3](#evidence-h3), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, multidomain sequence is consistent with an NRPS-like enzyme. NRPS carrier-protein domains bind phosphopantetheine, making C a biologically motivated choice over the unrelated xylanase, mannose-isomerase, and methylated-histone-binding options.


**Missing item-specific fact**

> The precise InterPro assignment of a phosphopantetheine-binding domain is not supplied; direct experimental confirmation of that binding is also absent.


**Reason**

> A defensible family/domain-level inference from the sequence and the choices distinguishes C, although the specific GO annotation is computational and would be easier to establish with an external domain annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C is the only option that fits the NRPS-like sequence. The wording calls for a primary function, while the reported experimentally characterized activity is catalytic esterification, but that catalytic function is not among the choices.


### Important caveats

- The sequence matches the reviewed UniProt record, but the phosphopantetheine-binding annotation is IEA:InterPro rather than direct experimental evidence.
- The experimental evidence supports NRPS-like catalytic activity, not specifically phosphopantetheine binding.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, multidomain sequence is consistent with an NRPS-like enzyme. NRPS carrier-protein domains bind phosphopantetheine, making C a biologically motivated choice over the unrelated xylanase, mannose-isomerase, and methylated-histone-binding options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise InterPro assignment of a phosphopantetheine-binding domain is not supplied; direct experimental confirmation of that binding is also absent.",
    "reason": "A defensible family/domain-level inference from the sequence and the choices distinguishes C, although the specific GO annotation is computational and would be easier to establish with an external domain annotation."
  },
  "case_id": "GO_molecular_function_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H3",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence is annotated for phosphopantetheine binding by InterPro (computational evidence), and the matched protein is identified as an NRPS-like enzyme. Its experimentally described catalytic activity is esterification, which supports the NRPS context but is not direct experimental evidence of phosphopantetheine binding."
  },
  "important_caveats": [
    "The sequence matches the reviewed UniProt record, but the phosphopantetheine-binding annotation is IEA:InterPro rather than direct experimental evidence.",
    "The experimental evidence supports NRPS-like catalytic activity, not specifically phosphopantetheine binding."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is the only option that fits the NRPS-like sequence. The wording calls for a primary function, while the reported experimentally characterized activity is catalytic esterification, but that catalytic function is not among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence is annotated for phosphopantetheine binding by InterPro (computational evidence), and the matched protein is identified as an NRPS-like enzyme. Its experimentally described catalytic activity is esterification, which supports the NRPS context but is not direct experimental evidence of phosphopantetheine binding.",
    "evidence_ids": ["C4", "C5", "C8", "H3", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, multidomain sequence is consistent with an NRPS-like enzyme. NRPS carrier-protein domains bind phosphopantetheine, making C a biologically motivated choice over the unrelated xylanase, mannose-isomerase, and methylated-histone-binding options.",
    "missing_item_specific_fact": "The precise InterPro assignment of a phosphopantetheine-binding domain is not supplied; direct experimental confirmation of that binding is also absent.",
    "reason": "A defensible family/domain-level inference from the sequence and the choices distinguishes C, although the specific GO annotation is computational and would be easier to establish with an external domain annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is the only option that fits the NRPS-like sequence. The wording calls for a primary function, while the reported experimentally characterized activity is catalytic esterification, but that catalytic function is not among the choices."
  },
  "important_caveats": [
    "The sequence matches the reviewed UniProt record, but the phosphopantetheine-binding annotation is IEA:InterPro rather than direct experimental evidence.",
    "The experimental evidence supports NRPS-like catalytic activity, not specifically phosphopantetheine binding."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0L1JF11 (RSTN8_ASPN3) is annotated with GO:0031177 'phosphopantetheine binding' (evidence C8, H7; IEA:InterPro). The protein is a single-module NRPS-like enzyme (nonribosomal peptide synthetase rstn8) that catalyzes esterification of restrictinol with glycine. NRPS enzymes obligately carry a phosphopantetheine prosthetic group on their PCP domain, making phosphopantetheine binding a genuine molecular function annotation. Among the four options, C is the only one annotated on this protein; options A (glycoside hydrolase), B (TIM-barrel isomerase), and D (chromodomain protein) are entirely incompatible with the NRPS architecture. The evidence code is IEA:InterPro (computational), not experimental, but the biochemical link between PCP domains and phosphopantetheine is well-established.

Citations as saved: [C8](#evidence-c8), [H7](#evidence-h7), [C5](#evidence-c5), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The ~1358-aa sequence contains recognizable NRPS domain signatures: the adenylation-domain motif 'KAGGA' (present at ~residue 430), the PCP-domain 'GDSL' motif with the phosphopantetheinylation serine ('GDSLA' at ~residue 1100), and condensation-domain 'HH' motifs. These multi-domain features are hallmarks of NRPS enzymes and are absent from glycoside hydrolases (GH families have distinct beta-sandwich or TIM-barrel folds), mannose-6-phosphate isomerase (a compact ~250-aa TIM barrel), or chromodomain-containing histone readers (~40-aa chromodomain). Once the NRPS architecture is recognized, general biochemistry dictates that the PCP domain binds phosphopantetheine as its essential prosthetic group, making option C the only applicable choice.


**Missing item-specific fact**

> None strictly required. The NRPS-to-phosphopantetheine link is general enzymology knowledge, and the domain motifs are extractable from the sequence. However, a model unfamiliar with NRPS domain signatures might struggle to positively identify the enzyme class from sequence alone without a domain predictor.


**Reason**

> A knowledgeable biologist can identify NRPS A/PCP/C domain motifs in the sequence and eliminate the three incompatible options (glycoside hydrolase, isomerase, histone reader) based on gross architecture mismatch. The connection between PCP domains and phosphopantetheine binding is standard biochemistry, not an item-specific database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, B, and D describe functions with entirely different domain architectures (GH fold, TIM barrel, chromodomain) that are clearly absent from this NRPS sequence. Only C is compatible. One minor wording concern: the prompt asks for 'primary molecular function,' and the primary catalytic activity of rstn8 is NRPS/ligase activity (GO:1904091, GO:0016874), not phosphopantetheine binding per se. However, since NRPS activity is not among the choices, C is the only defensible answer among the four provided.


### Important caveats

- The GO:0031177 annotation is IEA:InterPro (computational inference from domain match), not experimentally verified binding of phosphopantetheine to this specific protein.
- The protein's primary catalytic function is non-ribosomal peptide synthetase / ligase activity (esterification of restrictinol with glycine, ECO:0000269 PubMed:33857369). 'Phosphopantetheine binding' is a secondary structural/cofactor-association function, not the primary catalytic activity. The question's phrasing 'primary molecular function' slightly misaligns with the correct answer, but among the four choices C is the only valid annotation.
- The sequence match is confirmed (SHA-256 identical to both current and historical UniProt entries).
- The protein was first released in Swiss-Prot on 2025-02-05; the benchmark author's data-construction date is unknown, so the annotation may or may not have been available at benchmark creation time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The ~1358-aa sequence contains recognizable NRPS domain signatures: the adenylation-domain motif 'KAGGA' (present at ~residue 430), the PCP-domain 'GDSL' motif with the phosphopantetheinylation serine ('GDSLA' at ~residue 1100), and condensation-domain 'HH' motifs. These multi-domain features are hallmarks of NRPS enzymes and are absent from glycoside hydrolases (GH families have distinct beta-sandwich or TIM-barrel folds), mannose-6-phosphate isomerase (a compact ~250-aa TIM barrel), or chromodomain-containing histone readers (~40-aa chromodomain). Once the NRPS architecture is recognized, general biochemistry dictates that the PCP domain binds phosphopantetheine as its essential prosthetic group, making option C the only applicable choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The NRPS-to-phosphopantetheine link is general enzymology knowledge, and the domain motifs are extractable from the sequence. However, a model unfamiliar with NRPS domain signatures might struggle to positively identify the enzyme class from sequence alone without a domain predictor.",
    "reason": "A knowledgeable biologist can identify NRPS A/PCP/C domain motifs in the sequence and eliminate the three incompatible options (glycoside hydrolase, isomerase, histone reader) based on gross architecture mismatch. The connection between PCP domains and phosphopantetheine binding is standard biochemistry, not an item-specific database lookup."
  },
  "case_id": "GO_molecular_function_0027",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "H7",
      "C5",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0L1JF11 (RSTN8_ASPN3) is annotated with GO:0031177 'phosphopantetheine binding' (evidence C8, H7; IEA:InterPro). The protein is a single-module NRPS-like enzyme (nonribosomal peptide synthetase rstn8) that catalyzes esterification of restrictinol with glycine. NRPS enzymes obligately carry a phosphopantetheine prosthetic group on their PCP domain, making phosphopantetheine binding a genuine molecular function annotation. Among the four options, C is the only one annotated on this protein; options A (glycoside hydrolase), B (TIM-barrel isomerase), and D (chromodomain protein) are entirely incompatible with the NRPS architecture. The evidence code is IEA:InterPro (computational), not experimental, but the biochemical link between PCP domains and phosphopantetheine is well-established."
  },
  "important_caveats": [
    "The GO:0031177 annotation is IEA:InterPro (computational inference from domain match), not experimentally verified binding of phosphopantetheine to this specific protein.",
    "The protein's primary catalytic function is non-ribosomal peptide synthetase / ligase activity (esterification of restrictinol with glycine, ECO:0000269 PubMed:33857369). 'Phosphopantetheine binding' is a secondary structural/cofactor-association function, not the primary catalytic activity. The question's phrasing 'primary molecular function' slightly misaligns with the correct answer, but among the four choices C is the only valid annotation.",
    "The sequence match is confirmed (SHA-256 identical to both current and historical UniProt entries).",
    "The protein was first released in Swiss-Prot on 2025-02-05; the benchmark author's data-construction date is unknown, so the annotation may or may not have been available at benchmark creation time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe functions with entirely different domain architectures (GH fold, TIM barrel, chromodomain) that are clearly absent from this NRPS sequence. Only C is compatible. One minor wording concern: the prompt asks for 'primary molecular function,' and the primary catalytic activity of rstn8 is NRPS/ligase activity (GO:1904091, GO:0016874), not phosphopantetheine binding per se. However, since NRPS activity is not among the choices, C is the only defensible answer among the four provided."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0L1JF11 (RSTN8_ASPN3) is annotated with GO:0031177 'phosphopantetheine binding' (evidence C8, H7; IEA:InterPro). The protein is a single-module NRPS-like enzyme (nonribosomal peptide synthetase rstn8) that catalyzes esterification of restrictinol with glycine. NRPS enzymes obligately carry a phosphopantetheine prosthetic group on their PCP domain, making phosphopantetheine binding a genuine molecular function annotation. Among the four options, C is the only one annotated on this protein; options A (glycoside hydrolase), B (TIM-barrel isomerase), and D (chromodomain protein) are entirely incompatible with the NRPS architecture. The evidence code is IEA:InterPro (computational), not experimental, but the biochemical link between PCP domains and phosphopantetheine is well-established.",
    "evidence_ids": ["C8", "H7", "C5", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The ~1358-aa sequence contains recognizable NRPS domain signatures: the adenylation-domain motif 'KAGGA' (present at ~residue 430), the PCP-domain 'GDSL' motif with the phosphopantetheinylation serine ('GDSLA' at ~residue 1100), and condensation-domain 'HH' motifs. These multi-domain features are hallmarks of NRPS enzymes and are absent from glycoside hydrolases (GH families have distinct beta-sandwich or TIM-barrel folds), mannose-6-phosphate isomerase (a compact ~250-aa TIM barrel), or chromodomain-containing histone readers (~40-aa chromodomain). Once the NRPS architecture is recognized, general biochemistry dictates that the PCP domain binds phosphopantetheine as its essential prosthetic group, making option C the only applicable choice.",
    "missing_item_specific_fact": "None strictly required. The NRPS-to-phosphopantetheine link is general enzymology knowledge, and the domain motifs are extractable from the sequence. However, a model unfamiliar with NRPS domain signatures might struggle to positively identify the enzyme class from sequence alone without a domain predictor.",
    "reason": "A knowledgeable biologist can identify NRPS A/PCP/C domain motifs in the sequence and eliminate the three incompatible options (glycoside hydrolase, isomerase, histone reader) based on gross architecture mismatch. The connection between PCP domains and phosphopantetheine binding is standard biochemistry, not an item-specific database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, B, and D describe functions with entirely different domain architectures (GH fold, TIM barrel, chromodomain) that are clearly absent from this NRPS sequence. Only C is compatible. One minor wording concern: the prompt asks for 'primary molecular function,' and the primary catalytic activity of rstn8 is NRPS/ligase activity (GO:1904091, GO:0016874), not phosphopantetheine binding per se. However, since NRPS activity is not among the choices, C is the only defensible answer among the four provided."
  },
  "important_caveats": [
    "The GO:0031177 annotation is IEA:InterPro (computational inference from domain match), not experimentally verified binding of phosphopantetheine to this specific protein.",
    "The protein's primary catalytic function is non-ribosomal peptide synthetase / ligase activity (esterification of restrictinol with glycine, ECO:0000269 PubMed:33857369). 'Phosphopantetheine binding' is a secondary structural/cofactor-association function, not the primary catalytic activity. The question's phrasing 'primary molecular function' slightly misaligns with the correct answer, but among the four choices C is the only valid annotation.",
    "The sequence match is confirmed (SHA-256 identical to both current and historical UniProt entries).",
    "The protein was first released in Swiss-Prot on 2025-02-05; the benchmark author's data-construction date is unknown, so the annotation may or may not have been available at benchmark creation time."
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

**Accession:** `A0A0L1JF11` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 41. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF11.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.345446+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein 8"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"6.3.2.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33857369","source":"PubMed"}],"value":"Nonribosomal peptide synthetase rstn8"}}}
```

Source SHA-256: `c4747f7695d004ff8ea5a8c179d271c3d96bfd468ffd19f64a22f32b7d7896f2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF11.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.345446+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33857369","source":"PubMed"}],"value":"Nonribosomal peptide synthetase; part of the gene cluster that mediates the biosynthesis of the tetrahydropyranyl antifungal agent restricticin that acts as an inhibitor of CYP51 and blocks the ergosterol biosynthesis (PubMed:33857369). Within the pathway, rstn8 catalyzes the C3 esterification of restrictinol with glycine to yield restricticin. Rstn8 represents an example of the emerging class of single-module NRPS-like enzymes that perform esterification reactions. Rstn8 displays strict substrate specificity toward glycine as no other natural amino acid is accepted. Rstn8 does not recognize desmethylrestrictinol as a substrate, demonstrating that rstn1-catalyzed methylation, possibly protecting the C4-OH, must precede the final esterification step (PubMed:33857369). The highly reducing polyketide synthase rstn3, the short chain dehydrogenase rstn4, the cyclase rstn5, the FAD-dependent monooxygenase rstn6 and the enoylreductase rstn7 are required to generate the first stable intermediate desmethylrestrictinol. Rstn3 with rstn7 biosynthesize the first polyketide chain intermediate that is reduced by rstn4, followed by epoxidation by rstn6 before 6-endo cyclization via epoxide opening by rstn5 leads to desmethylrestrictinol. The methyltransferase rstn1 then catalyzes the C4 O-methylation of desmethylrestrictinol to produce restrictinol, and the nonribosomal peptide synthetase rstn8 catalyzes the C3 esterification of restrictinol with glycine that leads to restricticin (PubMed:33857369)"}]}
```

Source SHA-256: `c4747f7695d004ff8ea5a8c179d271c3d96bfd468ffd19f64a22f32b7d7896f2`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0L1JF11.json)  
**Locator:** `/uniProtKBCrossReferences/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:40.345446+00:00.  

```json
{"database":"GO","id":"GO:0031177","properties":[{"key":"GoTerm","value":"F:phosphopantetheine binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `c4747f7695d004ff8ea5a8c179d271c3d96bfd468ffd19f64a22f32b7d7896f2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JF11?format=txt&versions=41)  
**Locator:** `lines 32-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:19.711233+00:00.  

```text
CC   -!- FUNCTION: Nonribosomal peptide synthetase; part of the gene cluster
CC       that mediates the biosynthesis of the tetrahydropyranyl antifungal
CC       agent restricticin that acts as an inhibitor of CYP51 and blocks the
CC       ergosterol biosynthesis (PubMed:33857369). Within the pathway, rstn8
CC       catalyzes the C3 esterification of restrictinol with glycine to yield
CC       restricticin. Rstn8 represents an example of the emerging class of
CC       single-module NRPS-like enzymes that perform esterification reactions.
CC       Rstn8 displays strict substrate specificity toward glycine as no other
CC       natural amino acid is accepted. Rstn8 does not recognize
CC       desmethylrestrictinol as a substrate, demonstrating that rstn1-
CC       catalyzed methylation, possibly protecting the C4-OH, must precede the
CC       final esterification step (PubMed:33857369). The highly reducing
CC       polyketide synthase rstn3, the short chain dehydrogenase rstn4, the
CC       cyclase rstn5, the FAD-dependent monooxygenase rstn6 and the
CC       enoylreductase rstn7 are required to generate the first stable
CC       intermediate desmethylrestrictinol. Rstn3 with rstn7 biosynthesize the
CC       first polyketide chain intermediate that is reduced by rstn4, followed
CC       by epoxidation by rstn6 before 6-endo cyclization via epoxide opening
CC       by rstn5 leads to desmethylrestrictinol. The methyltransferase rstn1
CC       then catalyzes the C4 O-methylation of desmethylrestrictinol to produce
CC       restrictinol, and the nonribosomal peptide synthetase rstn8 catalyzes
CC       the C3 esterification of restrictinol with glycine that leads to
CC       restricticin (PubMed:33857369). {ECO:0000269|PubMed:33857369}.
```

Source SHA-256: `d90784deda82bb78af24fa1babc1da69e6ef26f5a77034ba845f02029dbced6d`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0L1JF11?format=txt&versions=41)  
**Locator:** `lines 92-92`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 41 / 1.  
**Retrieved:** 2026-11-01T06:27:19.711233+00:00.  

```text
DR   GO; GO:0031177; F:phosphopantetheine binding; IEA:InterPro.
```

Source SHA-256: `d90784deda82bb78af24fa1babc1da69e6ef26f5a77034ba845f02029dbced6d`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 27. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
