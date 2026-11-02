# pathway_0071

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Antibiotic biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTDEAKLLSYLKRVTADLDRTTRRLREAEEQRYEAIAIVGMACRYPGGVRSPEELWRLVADEADAVSHFPQNRGWDLDTLFDPERAGGTSLTQEGGFLYDADQFDAGFFGIGPREATAMDPQQRLLLETSWEALERAGIDPATLRGSATGVFAGVMYHDYGARVVEVPEEVEGYLGNGNAGSIASGRVAFTFGFEGPAVTLDTACSSSLVALHLAAQALRQGECSLALAGGVTVMATPGVFTEFTRQGGLAADGRCKSFSTTADGTGWSEGAGMLLLERLSDAERNGHLVLAVVRGSAVNQDGASSGLTAPNGPAQQRVIRQALANARLSASEVDVVEAHGTGTKLGDPIEAQALLATYGQDRAEDRPLWLGSVKSNLGHTQAAAGVAGIIKSVMAMRHGVLPATLHVDEPTSEVDWSAGAVELLTKSRSWPETGRPRRAAVSGFGVSGTNAHVILEQAADLDVPDAAPVPEGVPVPWVVSARSADALRAQARRLRGHMAAEPGAAVVDVGHSLATARSCFEHRAVVIGRTTDDLLAGLEALAEGRGDSRVRVGAGLAGGRTGFVFAGQGSQRLGMGGRLREMFPVFGEAWDEVVAELDGRLGRPLGEVVFAEEGSEQASLVDRTEFTQPALFAFEVALFRLLESWGVVPDVVAGHSIGELAAAYVAGVLSLSDACALVVARGRLMQALPAGGAMVAVQVTEAEARRLVEGEPSGAVDIAAVNGPESVVIAGDEDVVLRVQEIVRGRGRKTKRLTVSHAFHSPRMEPMLDEFRRVAETVTYHEPRIAVVSAVSGEVAGAELRSAEYWTRHVREAVRFYDAVRCLRSEGVSTFVEVGPDGALSALGQDCLVGEEARGTEFVSTVRAGRDEAESVVAAVGAAHVRGVPVDWAAYYAPYGPRRAGLPTYAFEHQRYWLDASVRTVGDLAGLGLGSAEHPLLGAAVALADGDGVLLTGRLSLATHPWLADHRVQGAVLFPGTAFVELALRAGEQVGADCVEELTLEVPLVLPERGGVQVQVVVGAADEQGGRPVTVYSRPDEDVEDEPWARHAIGMLVPFAASAAVPAEDADFAVWPPQDAVAVDTDGMYDRLAEGGLEYGPVFQGLRSVWRRGSEVFAEVALDDTHRDGAEHDVSAVSAPETTAPVWRLEATGGGTLDALALVAYEETDRPLRANEVRVEVHAAGLNFRDVLITLGMLETKDKLGWELSGVVLETGPDVTGLAPGDRVMGVALGSFAQQAVADHRMLAKIPDGWSYAEAASVPLVFLTAYYSLVDLADLRAGQSVLIHAAAGGVGMAAVQLARHLGAEVFGTASTGKWDALRAQGLDETHIASSRDLEFEPRVLEATDGRGVDVVLDALAGEFVDASLRTLTHGGRFIEMGKTDIRDAEEVAARYPGVHYRAFDLIEAGPERVGQMLAEVLRLFDDGALTVLPVTTWDLLSAPDAFRHLSQARHIGKVVLTVPRTIDPYDTELAVVTRSRSRWRTGRSSARLTANPNSAGEFGLHPALLDAALHAIGFGEFVSDGGAGVLPFSWSGVRLLASGADALRVRVSGVGVGANEVALVVADGSGRPVASVDSLALRPVSADGIGAGRSGASRQSLFRVGWRQVAVPDQAGAGEWVALDRGAGWAQGEGCEVLPDLAALGSAVSAGRSVPRLVVAHFAADREVPVTAGVRGVTAEGLELIQSWLADERFADSRLVIMTRQAVAVDAGEGVFDLGAAALWGLVRTAQSEQPGRVVLVDVDDLDAVSRVVGIGDEPQLAVRDGRVFVPRLMRAEAIDGVPVWDPEGTLLITGASGALGGVVARHVVREWGVRHLVLASRRGAEAPGMTELVAELGELGASAAPVACDVADRDALAAVLAGIPAVHRLAGVVHAAGVLDDGVVGSLTPERLETVLAPKADAAWHLHELAAELDLSVFVLFSSAASVFGGAGQGNYAAANAFLDALAARRRADGLVATSLSWGLWDQAGGMTGQLGEADVARMSRSGVLPISVGEALPLLDAGVTGGDAWLAPVRLDLAALRQQAIATGGVPALLRDLVRVPNRRKAETGGSGAGSRSSLTDKLAGLPQEERAQELLDFVCEHTAAVLGHSGAGMVDPGRNFRELGIDSLAAVELRNRIGGVLGIRLSATLVFDYPSPVLLAGHIGEQLALDEPAPRLPVVAELERLEAAVSAARFDEDSRDDVAARLRKLLSHLDALAASPKREADDGELASASVEELFALVDQELEDL

[Multiple Choices]
A. Cell wall biogenesis
B. Antibiotic biosynthesis. .
C. tRNA modification
D. tetrahydrofolate interconversion. .
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

> The exact sequence matches a UniProt entry identifying the protein as polyketide synthase GfsC and annotating its pathway as antibiotic biosynthesis. The pathway annotation cites a study of the FD-891 antibiotic biosynthetic gene cluster; this supports the key, though the supplied evidence is an annotation and citation rather than an independently reviewed experimental report.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, multidomain enzyme sequence is consistent with a modular polyketide synthase, which supports secondary-metabolite biosynthesis. Of the listed choices, antibiotic biosynthesis is the fitting pathway; the other choices concern distinct enzyme systems.


**Missing item-specific fact**

> The sequence alone does not establish that this particular polyketide product is an antibiotic; that protein-specific pathway assignment is supplied by the external annotation and cited study.


**Reason**

> Recognizable polyketide-synthase architecture provides a meaningful basis for choosing among these broadly distinct pathway options, although the exact antibiotic-biosynthesis assignment depends on item-specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other listed option is comparably supported by the sequence's polyketide-synthase-like architecture.


### Important caveats

- The reviewer-only database evidence was not available in the original question and is used only to assess whether the expected answer is supported.
- A polyketide synthase can make products other than antibiotics, so the sequence-level inference is less specific than the annotated pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, multidomain enzyme sequence is consistent with a modular polyketide synthase, which supports secondary-metabolite biosynthesis. Of the listed choices, antibiotic biosynthesis is the fitting pathway; the other choices concern distinct enzyme systems.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The sequence alone does not establish that this particular polyketide product is an antibiotic; that protein-specific pathway assignment is supplied by the external annotation and cited study.",
    "reason": "Recognizable polyketide-synthase architecture provides a meaningful basis for choosing among these broadly distinct pathway options, although the exact antibiotic-biosynthesis assignment depends on item-specific annotation."
  },
  "case_id": "pathway_0071",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry identifying the protein as polyketide synthase GfsC and annotating its pathway as antibiotic biosynthesis. The pathway annotation cites a study of the FD-891 antibiotic biosynthetic gene cluster; this supports the key, though the supplied evidence is an annotation and citation rather than an independently reviewed experimental report."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not available in the original question and is used only to assess whether the expected answer is supported.",
    "A polyketide synthase can make products other than antibiotics, so the sequence-level inference is less specific than the annotated pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported by the sequence's polyketide-synthase-like architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0071",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry identifying the protein as polyketide synthase GfsC and annotating its pathway as antibiotic biosynthesis. The pathway annotation cites a study of the FD-891 antibiotic biosynthetic gene cluster; this supports the key, though the supplied evidence is an annotation and citation rather than an independently reviewed experimental report.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, multidomain enzyme sequence is consistent with a modular polyketide synthase, which supports secondary-metabolite biosynthesis. Of the listed choices, antibiotic biosynthesis is the fitting pathway; the other choices concern distinct enzyme systems.",
    "missing_item_specific_fact": "The sequence alone does not establish that this particular polyketide product is an antibiotic; that protein-specific pathway assignment is supplied by the external annotation and cited study.",
    "reason": "Recognizable polyketide-synthase architecture provides a meaningful basis for choosing among these broadly distinct pathway options, although the exact antibiotic-biosynthesis assignment depends on item-specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other listed option is comparably supported by the sequence's polyketide-synthase-like architecture."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not available in the original question and is used only to assess whether the expected answer is supported.",
    "A polyketide synthase can make products other than antibiotics, so the sequence-level inference is less specific than the annotated pathway."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E0D204 (GFSC_STRHA) annotates this protein as 'Polyketide synthase GfsC' / 'FD-891 synthase GfsC, module 8' from Streptomyces halstedii, with the explicit pathway annotation 'Antibiotic biosynthesis' (ECO:0000305, curated from PubMed:20589823, Kudo et al. 2010, characterizing the 16-membered macrolide antibiotic FD-891 gene cluster). The sequence matches exactly (SHA256 confirmed). The annotation is curator-inferred from a published gene-cluster characterization, not direct enzymatic assay, but the pathway assignment is well-established.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 2228 amino acids long, far exceeding the size of tRNA modification enzymes (~200–400 aa), tetrahydrofolate interconversion enzymes (~250–350 aa), or typical cell-wall biosynthesis enzymes. The sequence contains recognizable type I modular polyketide synthase (PKS) domain signatures: the ketosynthase (KS) catalytic motif 'GHSIG' appears (e.g., 'GHSIGELAAAYVAGVLSLSDACALVVARGRLMQ'), acyltransferase (AT) domain motifs ('GAGLAGGRTGFVFAGQGSQRLGMGGRLREMFP'), and a tandem multi-domain architecture spanning the full length. Modular type I PKS proteins in Streptomyces are overwhelmingly dedicated to polyketide antibiotic biosynthesis. Among the four choices, only 'Antibiotic biosynthesis' is compatible with a ~2200-aa multi-domain PKS. The other three options involve enzymes that are an order of magnitude smaller and structurally unrelated.


**Missing item-specific fact**

> None strictly required. Identifying the exact protein (GfsC, module 8 of FD-891 synthase) would require database lookup, but the pathway can be inferred from domain architecture, size, and elimination of incompatible choices.


**Reason**

> A knowledgeable model can reason from the extreme protein length, the presence of KS/AT/ACP domain motifs, and the modular tandem architecture to conclude this is a type I modular PKS, which maps to antibiotic biosynthesis. The three distractors (cell wall biogenesis, tRNA modification, THF interconversion) involve enzymes that are far smaller and mechanistically unrelated to polyketide assembly. This constitutes a concrete biological argument distinguishing the answer without requiring memorization of this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are mutually exclusive in terms of enzyme class and size. A 2228-aa multi-domain PKS is incompatible with tRNA modification (small nucleotidyltransferases/methyltransferases), THF interconversion (small dehydrogenases/cyclohydrolases), or cell wall biogenesis (glycosyltransferases, transpeptidases of different architecture). Only antibiotic biosynthesis fits.


### Important caveats

- The UniProt pathway annotation carries evidence code ECO:0000305 (inferred by curator from literature), not a direct in-vitro enzymatic assay for GfsC module 8 specifically; the evidence is the published gene-cluster characterization (PubMed:20589823).
- Recognizing PKS domain motifs (GHSxG, GxGxxGxGAG) within a 2228-aa raw sequence is specialized bioinformatics knowledge; a general-purpose model may struggle to locate these motifs without alignment tools, though the extreme size alone provides a strong prior against the three small-enzyme distractors.
- The reviewer-only evidence (accession E0D204, UniProt annotations) was not available to the evaluated model; the reasoning assessment is based solely on what the sequence and choices provide.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 2228 amino acids long, far exceeding the size of tRNA modification enzymes (~200–400 aa), tetrahydrofolate interconversion enzymes (~250–350 aa), or typical cell-wall biosynthesis enzymes. The sequence contains recognizable type I modular polyketide synthase (PKS) domain signatures: the ketosynthase (KS) catalytic motif 'GHSIG' appears (e.g., 'GHSIGELAAAYVAGVLSLSDACALVVARGRLMQ'), acyltransferase (AT) domain motifs ('GAGLAGGRTGFVFAGQGSQRLGMGGRLREMFP'), and a tandem multi-domain architecture spanning the full length. Modular type I PKS proteins in Streptomyces are overwhelmingly dedicated to polyketide antibiotic biosynthesis. Among the four choices, only 'Antibiotic biosynthesis' is compatible with a ~2200-aa multi-domain PKS. The other three options involve enzymes that are an order of magnitude smaller and structurally unrelated.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Identifying the exact protein (GfsC, module 8 of FD-891 synthase) would require database lookup, but the pathway can be inferred from domain architecture, size, and elimination of incompatible choices.",
    "reason": "A knowledgeable model can reason from the extreme protein length, the presence of KS/AT/ACP domain motifs, and the modular tandem architecture to conclude this is a type I modular PKS, which maps to antibiotic biosynthesis. The three distractors (cell wall biogenesis, tRNA modification, THF interconversion) involve enzymes that are far smaller and mechanistically unrelated to polyketide assembly. This constitutes a concrete biological argument distinguishing the answer without requiring memorization of this specific UniProt entry."
  },
  "case_id": "pathway_0071",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E0D204 (GFSC_STRHA) annotates this protein as 'Polyketide synthase GfsC' / 'FD-891 synthase GfsC, module 8' from Streptomyces halstedii, with the explicit pathway annotation 'Antibiotic biosynthesis' (ECO:0000305, curated from PubMed:20589823, Kudo et al. 2010, characterizing the 16-membered macrolide antibiotic FD-891 gene cluster). The sequence matches exactly (SHA256 confirmed). The annotation is curator-inferred from a published gene-cluster characterization, not direct enzymatic assay, but the pathway assignment is well-established."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000305 (inferred by curator from literature), not a direct in-vitro enzymatic assay for GfsC module 8 specifically; the evidence is the published gene-cluster characterization (PubMed:20589823).",
    "Recognizing PKS domain motifs (GHSxG, GxGxxGxGAG) within a 2228-aa raw sequence is specialized bioinformatics knowledge; a general-purpose model may struggle to locate these motifs without alignment tools, though the extreme size alone provides a strong prior against the three small-enzyme distractors.",
    "The reviewer-only evidence (accession E0D204, UniProt annotations) was not available to the evaluated model; the reasoning assessment is based solely on what the sequence and choices provide."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mutually exclusive in terms of enzyme class and size. A 2228-aa multi-domain PKS is incompatible with tRNA modification (small nucleotidyltransferases/methyltransferases), THF interconversion (small dehydrogenases/cyclohydrolases), or cell wall biogenesis (glycosyltransferases, transpeptidases of different architecture). Only antibiotic biosynthesis fits."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0071",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E0D204 (GFSC_STRHA) annotates this protein as 'Polyketide synthase GfsC' / 'FD-891 synthase GfsC, module 8' from Streptomyces halstedii, with the explicit pathway annotation 'Antibiotic biosynthesis' (ECO:0000305, curated from PubMed:20589823, Kudo et al. 2010, characterizing the 16-membered macrolide antibiotic FD-891 gene cluster). The sequence matches exactly (SHA256 confirmed). The annotation is curator-inferred from a published gene-cluster characterization, not direct enzymatic assay, but the pathway assignment is well-established.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 2228 amino acids long, far exceeding the size of tRNA modification enzymes (~200–400 aa), tetrahydrofolate interconversion enzymes (~250–350 aa), or typical cell-wall biosynthesis enzymes. The sequence contains recognizable type I modular polyketide synthase (PKS) domain signatures: the ketosynthase (KS) catalytic motif 'GHSIG' appears (e.g., 'GHSIGELAAAYVAGVLSLSDACALVVARGRLMQ'), acyltransferase (AT) domain motifs ('GAGLAGGRTGFVFAGQGSQRLGMGGRLREMFP'), and a tandem multi-domain architecture spanning the full length. Modular type I PKS proteins in Streptomyces are overwhelmingly dedicated to polyketide antibiotic biosynthesis. Among the four choices, only 'Antibiotic biosynthesis' is compatible with a ~2200-aa multi-domain PKS. The other three options involve enzymes that are an order of magnitude smaller and structurally unrelated.",
    "missing_item_specific_fact": "None strictly required. Identifying the exact protein (GfsC, module 8 of FD-891 synthase) would require database lookup, but the pathway can be inferred from domain architecture, size, and elimination of incompatible choices.",
    "reason": "A knowledgeable model can reason from the extreme protein length, the presence of KS/AT/ACP domain motifs, and the modular tandem architecture to conclude this is a type I modular PKS, which maps to antibiotic biosynthesis. The three distractors (cell wall biogenesis, tRNA modification, THF interconversion) involve enzymes that are far smaller and mechanistically unrelated to polyketide assembly. This constitutes a concrete biological argument distinguishing the answer without requiring memorization of this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mutually exclusive in terms of enzyme class and size. A 2228-aa multi-domain PKS is incompatible with tRNA modification (small nucleotidyltransferases/methyltransferases), THF interconversion (small dehydrogenases/cyclohydrolases), or cell wall biogenesis (glycosyltransferases, transpeptidases of different architecture). Only antibiotic biosynthesis fits."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000305 (inferred by curator from literature), not a direct in-vitro enzymatic assay for GfsC module 8 specifically; the evidence is the published gene-cluster characterization (PubMed:20589823).",
    "Recognizing PKS domain motifs (GHSxG, GxGxxGxGAG) within a 2228-aa raw sequence is specialized bioinformatics knowledge; a general-purpose model may struggle to locate these motifs without alignment tools, though the extreme size alone provides a strong prior against the three small-enzyme distractors.",
    "The reviewer-only evidence (accession E0D204, UniProt annotations) was not available to the evaluated model; the reasoning assessment is based solely on what the sequence and choices provide."
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

**Accession:** `E0D204` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 69. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D204.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.215687+00:00.  

```json
"E0D204"
```

Source SHA-256: `d3e6081dd33f462787c1460e2e3378a99c0a32a901c3c620f20a536cd944ba11`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D204.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.215687+00:00.  

```json
{"lineage":["Bacteria","Bacillati","Actinomycetota","Actinomycetes","Kitasatosporales","Streptomycetaceae","Streptomyces"],"scientificName":"Streptomyces halstedii","taxonId":1944}
```

Source SHA-256: `d3e6081dd33f462787c1460e2e3378a99c0a32a901c3c620f20a536cd944ba11`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D204.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.215687+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"FD-891 synthase GfsC, module 8"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"I6XD69","source":"UniProtKB"}],"value":"2.3.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Polyketide synthase GfsC"}}}
```

Source SHA-256: `d3e6081dd33f462787c1460e2e3378a99c0a32a901c3c620f20a536cd944ba11`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D204.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.215687+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"20589823","source":"PubMed"}],"value":"Antibiotic biosynthesis"}]}
```

Source SHA-256: `d3e6081dd33f462787c1460e2e3378a99c0a32a901c3c620f20a536cd944ba11`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E0D204.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.215687+00:00.  

```json
{"citation":{"authors":["Kudo F.","Motegi A.","Mizoue K.","Eguchi T."],"citationCrossReferences":[{"database":"PubMed","id":"20589823"},{"database":"DOI","id":"10.1002/cbic.201000214"}],"citationType":"journal article","firstPage":"1574","id":"20589823","journal":"ChemBioChem","lastPage":"1582","publicationDate":"2010","title":"Cloning and characterization of the biosynthetic gene cluster of 16-membered macrolide antibiotic FD-891: involvement of a dual functional cytochrome P450 monooxygenase catalyzing epoxidation and hydroxylation.","volume":"11"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAJ16469.1","source":"EMBL"}],"referenceComments":[{"type":"STRAIN","value":"A-8890"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","PATHWAY","DOMAIN"]}
```

Source SHA-256: `d3e6081dd33f462787c1460e2e3378a99c0a32a901c3c620f20a536cd944ba11`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-02T04:27:56.450911+00:00.  

```text
ID   GFSC_STRHA              Reviewed;        2228 AA.
AC   E0D204;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   02-NOV-2010, sequence version 1.
DT   28-JAN-2026, entry version 69.
DE   RecName: Full=Polyketide synthase GfsC {ECO:0000305};
DE            EC=2.3.1.- {ECO:0000250|UniProtKB:I6XD69};
DE   AltName: Full=FD-891 synthase GfsC, module 8;
GN   Name=gfsC {ECO:0000303|PubMed:20589823};
OS   Streptomyces halstedii.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=1944;
```

Source SHA-256: `d63277a07d00eb0d9fd8538c01445bcef958bf5e5584852732f178b8f77295cd`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69)  
**Locator:** `lines 14-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-02T04:27:56.450911+00:00.  

```text
RN   [1] {ECO:0000312|EMBL:BAJ16469.1}
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], PATHWAY, AND DOMAIN.
RC   STRAIN=A-8890;
RX   PubMed=20589823; DOI=10.1002/cbic.201000214;
RA   Kudo F., Motegi A., Mizoue K., Eguchi T.;
RT   "Cloning and characterization of the biosynthetic gene cluster of 16-
RT   membered macrolide antibiotic FD-891: involvement of a dual functional
RT   cytochrome P450 monooxygenase catalyzing epoxidation and hydroxylation.";
RL   ChemBioChem 11:1574-1582(2010).
```

Source SHA-256: `d63277a07d00eb0d9fd8538c01445bcef958bf5e5584852732f178b8f77295cd`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69)  
**Locator:** `lines 55-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-02T04:27:56.450911+00:00.  

```text
CC   -!- PATHWAY: Antibiotic biosynthesis. {ECO:0000305|PubMed:20589823}.
```

Source SHA-256: `d63277a07d00eb0d9fd8538c01445bcef958bf5e5584852732f178b8f77295cd`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 71. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
