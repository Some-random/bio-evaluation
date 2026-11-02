# active_site_0079

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 205 (For beta-ketoacyl synthase activity)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTDEAKLLSYLKRVTADLDRTTRRLREAEEQRYEAIAIVGMACRYPGGVRSPEELWRLVADEADAVSHFPQNRGWDLDTLFDPERAGGTSLTQEGGFLYDADQFDAGFFGIGPREATAMDPQQRLLLETSWEALERAGIDPATLRGSATGVFAGVMYHDYGARVVEVPEEVEGYLGNGNAGSIASGRVAFTFGFEGPAVTLDTACSSSLVALHLAAQALRQGECSLALAGGVTVMATPGVFTEFTRQGGLAADGRCKSFSTTADGTGWSEGAGMLLLERLSDAERNGHLVLAVVRGSAVNQDGASSGLTAPNGPAQQRVIRQALANARLSASEVDVVEAHGTGTKLGDPIEAQALLATYGQDRAEDRPLWLGSVKSNLGHTQAAAGVAGIIKSVMAMRHGVLPATLHVDEPTSEVDWSAGAVELLTKSRSWPETGRPRRAAVSGFGVSGTNAHVILEQAADLDVPDAAPVPEGVPVPWVVSARSADALRAQARRLRGHMAAEPGAAVVDVGHSLATARSCFEHRAVVIGRTTDDLLAGLEALAEGRGDSRVRVGAGLAGGRTGFVFAGQGSQRLGMGGRLREMFPVFGEAWDEVVAELDGRLGRPLGEVVFAEEGSEQASLVDRTEFTQPALFAFEVALFRLLESWGVVPDVVAGHSIGELAAAYVAGVLSLSDACALVVARGRLMQALPAGGAMVAVQVTEAEARRLVEGEPSGAVDIAAVNGPESVVIAGDEDVVLRVQEIVRGRGRKTKRLTVSHAFHSPRMEPMLDEFRRVAETVTYHEPRIAVVSAVSGEVAGAELRSAEYWTRHVREAVRFYDAVRCLRSEGVSTFVEVGPDGALSALGQDCLVGEEARGTEFVSTVRAGRDEAESVVAAVGAAHVRGVPVDWAAYYAPYGPRRAGLPTYAFEHQRYWLDASVRTVGDLAGLGLGSAEHPLLGAAVALADGDGVLLTGRLSLATHPWLADHRVQGAVLFPGTAFVELALRAGEQVGADCVEELTLEVPLVLPERGGVQVQVVVGAADEQGGRPVTVYSRPDEDVEDEPWARHAIGMLVPFAASAAVPAEDADFAVWPPQDAVAVDTDGMYDRLAEGGLEYGPVFQGLRSVWRRGSEVFAEVALDDTHRDGAEHDVSAVSAPETTAPVWRLEATGGGTLDALALVAYEETDRPLRANEVRVEVHAAGLNFRDVLITLGMLETKDKLGWELSGVVLETGPDVTGLAPGDRVMGVALGSFAQQAVADHRMLAKIPDGWSYAEAASVPLVFLTAYYSLVDLADLRAGQSVLIHAAAGGVGMAAVQLARHLGAEVFGTASTGKWDALRAQGLDETHIASSRDLEFEPRVLEATDGRGVDVVLDALAGEFVDASLRTLTHGGRFIEMGKTDIRDAEEVAARYPGVHYRAFDLIEAGPERVGQMLAEVLRLFDDGALTVLPVTTWDLLSAPDAFRHLSQARHIGKVVLTVPRTIDPYDTELAVVTRSRSRWRTGRSSARLTANPNSAGEFGLHPALLDAALHAIGFGEFVSDGGAGVLPFSWSGVRLLASGADALRVRVSGVGVGANEVALVVADGSGRPVASVDSLALRPVSADGIGAGRSGASRQSLFRVGWRQVAVPDQAGAGEWVALDRGAGWAQGEGCEVLPDLAALGSAVSAGRSVPRLVVAHFAADREVPVTAGVRGVTAEGLELIQSWLADERFADSRLVIMTRQAVAVDAGEGVFDLGAAALWGLVRTAQSEQPGRVVLVDVDDLDAVSRVVGIGDEPQLAVRDGRVFVPRLMRAEAIDGVPVWDPEGTLLITGASGALGGVVARHVVREWGVRHLVLASRRGAEAPGMTELVAELGELGASAAPVACDVADRDALAAVLAGIPAVHRLAGVVHAAGVLDDGVVGSLTPERLETVLAPKADAAWHLHELAAELDLSVFVLFSSAASVFGGAGQGNYAAANAFLDALAARRRADGLVATSLSWGLWDQAGGMTGQLGEADVARMSRSGVLPISVGEALPLLDAGVTGGDAWLAPVRLDLAALRQQAIATGGVPALLRDLVRVPNRRKAETGGSGAGSRSSLTDKLAGLPQEERAQELLDFVCEHTAAVLGHSGAGMVDPGRNFRELGIDSLAAVELRNRIGGVLGIRLSATLVFDYPSPVLLAGHIGEQLALDEPAPRLPVVAELERLEAAVSAARFDEDSRDDVAARLRKLLSHLDALAASPKREADDGELASASVEELFALVDQELEDL

[Multiple Choices]
A. Position 458 (For beta-ketoacyl synthase activity)
B. Position 315 (For beta-ketoacyl synthase activity)
C. Position 205 (For beta-ketoacyl synthase activity)
D. Position 93 (Proton donor)
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

> The sequence matches the UniProt entry, which annotates position 205 for beta-ketoacyl synthase activity. This is computational annotation from PROSITE-ProRule, not evidence of direct experimental validation; the historical record also annotates positions 340 and 380 for the same activity.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a large polyketide synthase, but general knowledge of this enzyme class does not establish which specific numbered residue is annotated for beta-ketoacyl synthase activity.


**Missing item-specific fact**

> The sequence-specific active-site annotation identifying residue 205 (and the additional annotated residues 340 and 380) is needed to select among the numbered positions.


**Reason**

> The key is supported by a sequence-matched database annotation, but that annotation is reviewer-only and absent from the input. Inferring an exact residue number from broad enzyme-class knowledge would not meaningfully distinguish these choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the supplied evidence supports position 205. However, the wording refers to residues constituting the catalytic center while each option names just one position; the annotation also identifies positions 340 and 380 for the same activity, neither of which is offered.


### Important caveats

- The active-site annotation is computationally assigned by PROSITE-ProRule, not shown here to be experimentally verified.
- The historical source entry and current entry both match the supplied sequence; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a large polyketide synthase, but general knowledge of this enzyme class does not establish which specific numbered residue is annotated for beta-ketoacyl synthase activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-specific active-site annotation identifying residue 205 (and the additional annotated residues 340 and 380) is needed to select among the numbered positions.",
    "reason": "The key is supported by a sequence-matched database annotation, but that annotation is reviewer-only and absent from the input. Inferring an exact residue number from broad enzyme-class knowledge would not meaningfully distinguish these choices."
  },
  "case_id": "active_site_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, which annotates position 205 for beta-ketoacyl synthase activity. This is computational annotation from PROSITE-ProRule, not evidence of direct experimental validation; the historical record also annotates positions 340 and 380 for the same activity."
  },
  "important_caveats": [
    "The active-site annotation is computationally assigned by PROSITE-ProRule, not shown here to be experimentally verified.",
    "The historical source entry and current entry both match the supplied sequence; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the supplied evidence supports position 205. However, the wording refers to residues constituting the catalytic center while each option names just one position; the annotation also identifies positions 340 and 380 for the same activity, neither of which is offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, which annotates position 205 for beta-ketoacyl synthase activity. This is computational annotation from PROSITE-ProRule, not evidence of direct experimental validation; the historical record also annotates positions 340 and 380 for the same activity.",
    "evidence_ids": ["C1", "C5", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a large polyketide synthase, but general knowledge of this enzyme class does not establish which specific numbered residue is annotated for beta-ketoacyl synthase activity.",
    "missing_item_specific_fact": "The sequence-specific active-site annotation identifying residue 205 (and the additional annotated residues 340 and 380) is needed to select among the numbered positions.",
    "reason": "The key is supported by a sequence-matched database annotation, but that annotation is reviewer-only and absent from the input. Inferring an exact residue number from broad enzyme-class knowledge would not meaningfully distinguish these choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the supplied evidence supports position 205. However, the wording refers to residues constituting the catalytic center while each option names just one position; the annotation also identifies positions 340 and 380 for the same activity, neither of which is offered."
  },
  "important_caveats": [
    "The active-site annotation is computationally assigned by PROSITE-ProRule, not shown here to be experimentally verified.",
    "The historical source entry and current entry both match the supplied sequence; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E0D204 (GFSC_STRHA, Polyketide synthase GfsC, module 8) annotates position 205 as an Active site with description 'For beta-ketoacyl synthase activity' (evidence ECO:0000255|PROSITE-ProRule:PRU01348). The benchmark sequence SHA256 matches the UniProt sequence exactly. The annotation is computational (PROSITE-ProRule pattern-based), not experimental, but it is the canonical database annotation. Among the four choices (458, 315, 205, 93), only position 205 corresponds to an annotated active site. Positions 340 and 380 are also annotated as active sites for the same activity but are not offered as options.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C1](#evidence-c1), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> In principle, beta-ketoacyl synthase (KS) domains in type I polyketide synthases contain a conserved catalytic cysteine within a GxSxG-like motif, and the KS domain typically occupies the N-terminal region of a PKS module. One could attempt to locate the KS domain and its catalytic Cys by pattern recognition. However, in a 2228-residue multi-domain PKS protein, distinguishing position 205 from positions 315 or 458 requires precise identification of domain boundaries and the exact catalytic motif residue, which is not feasible from raw sequence alone without computational domain prediction or prior knowledge of this specific protein's architecture.


**Missing item-specific fact**

> The specific domain architecture of GfsC (module 8 of FD-891 PKS) and the exact location of the KS catalytic cysteine within the 2228-residue sequence. The PROSITE-ProRule PRU01348 pattern match that assigns position 205 is an item-specific annotation not derivable from general biological reasoning applied to the raw sequence.


**Reason**

> While general PKS biology (KS domains have a catalytic Cys, KS is typically N-terminal) provides a weak prior, selecting position 205 over 315 or 458 in a 2228 AA protein requires either recognizing this exact sequence and recalling its annotation, or running a domain/motif prediction tool. No concrete biological argument from the sequence text alone meaningfully distinguishes 205 from the other KS-labeled positions.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only position 205 corresponds to any annotated active site in the UniProt entry. Positions 458 and 315 are not annotated as active sites, and position 93 is labeled 'Proton donor' which does not match any annotation for this protein. The UniProt entry does annotate positions 340 and 380 as additional active sites for beta-ketoacyl synthase activity, but these are not among the choices, so no ambiguity exists within the provided options.


### Important caveats

- The active site annotation is based on PROSITE-ProRule (ECO:0000255), a computational pattern-matching inference, not direct experimental evidence such as mutagenesis or crystallography.
- The UniProt entry annotates three positions (205, 340, 380) as active sites for beta-ketoacyl synthase activity; the question selects only one of these (205) as the correct answer while omitting the others from the choices.
- The protein is identified as 'module 8' of the FD-891 PKS (GfsC), implying it is one component of a multi-module assembly; the KS domain context is specific to this module.
- The UniProt accession E0D204 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "In principle, beta-ketoacyl synthase (KS) domains in type I polyketide synthases contain a conserved catalytic cysteine within a GxSxG-like motif, and the KS domain typically occupies the N-terminal region of a PKS module. One could attempt to locate the KS domain and its catalytic Cys by pattern recognition. However, in a 2228-residue multi-domain PKS protein, distinguishing position 205 from positions 315 or 458 requires precise identification of domain boundaries and the exact catalytic motif residue, which is not feasible from raw sequence alone without computational domain prediction or prior knowledge of this specific protein's architecture.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific domain architecture of GfsC (module 8 of FD-891 PKS) and the exact location of the KS catalytic cysteine within the 2228-residue sequence. The PROSITE-ProRule PRU01348 pattern match that assigns position 205 is an item-specific annotation not derivable from general biological reasoning applied to the raw sequence.",
    "reason": "While general PKS biology (KS domains have a catalytic Cys, KS is typically N-terminal) provides a weak prior, selecting position 205 over 315 or 458 in a 2228 AA protein requires either recognizing this exact sequence and recalling its annotation, or running a domain/motif prediction tool. No concrete biological argument from the sequence text alone meaningfully distinguishes 205 from the other KS-labeled positions."
  },
  "case_id": "active_site_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C1",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E0D204 (GFSC_STRHA, Polyketide synthase GfsC, module 8) annotates position 205 as an Active site with description 'For beta-ketoacyl synthase activity' (evidence ECO:0000255|PROSITE-ProRule:PRU01348). The benchmark sequence SHA256 matches the UniProt sequence exactly. The annotation is computational (PROSITE-ProRule pattern-based), not experimental, but it is the canonical database annotation. Among the four choices (458, 315, 205, 93), only position 205 corresponds to an annotated active site. Positions 340 and 380 are also annotated as active sites for the same activity but are not offered as options."
  },
  "important_caveats": [
    "The active site annotation is based on PROSITE-ProRule (ECO:0000255), a computational pattern-matching inference, not direct experimental evidence such as mutagenesis or crystallography.",
    "The UniProt entry annotates three positions (205, 340, 380) as active sites for beta-ketoacyl synthase activity; the question selects only one of these (205) as the correct answer while omitting the others from the choices.",
    "The protein is identified as 'module 8' of the FD-891 PKS (GfsC), implying it is one component of a multi-module assembly; the KS domain context is specific to this module.",
    "The UniProt accession E0D204 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only position 205 corresponds to any annotated active site in the UniProt entry. Positions 458 and 315 are not annotated as active sites, and position 93 is labeled 'Proton donor' which does not match any annotation for this protein. The UniProt entry does annotate positions 340 and 380 as additional active sites for beta-ketoacyl synthase activity, but these are not among the choices, so no ambiguity exists within the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E0D204 (GFSC_STRHA, Polyketide synthase GfsC, module 8) annotates position 205 as an Active site with description 'For beta-ketoacyl synthase activity' (evidence ECO:0000255|PROSITE-ProRule:PRU01348). The benchmark sequence SHA256 matches the UniProt sequence exactly. The annotation is computational (PROSITE-ProRule pattern-based), not experimental, but it is the canonical database annotation. Among the four choices (458, 315, 205, 93), only position 205 corresponds to an annotated active site. Positions 340 and 380 are also annotated as active sites for the same activity but are not offered as options.",
    "evidence_ids": ["C5", "H3", "C1", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "In principle, beta-ketoacyl synthase (KS) domains in type I polyketide synthases contain a conserved catalytic cysteine within a GxSxG-like motif, and the KS domain typically occupies the N-terminal region of a PKS module. One could attempt to locate the KS domain and its catalytic Cys by pattern recognition. However, in a 2228-residue multi-domain PKS protein, distinguishing position 205 from positions 315 or 458 requires precise identification of domain boundaries and the exact catalytic motif residue, which is not feasible from raw sequence alone without computational domain prediction or prior knowledge of this specific protein's architecture.",
    "missing_item_specific_fact": "The specific domain architecture of GfsC (module 8 of FD-891 PKS) and the exact location of the KS catalytic cysteine within the 2228-residue sequence. The PROSITE-ProRule PRU01348 pattern match that assigns position 205 is an item-specific annotation not derivable from general biological reasoning applied to the raw sequence.",
    "reason": "While general PKS biology (KS domains have a catalytic Cys, KS is typically N-terminal) provides a weak prior, selecting position 205 over 315 or 458 in a 2228 AA protein requires either recognizing this exact sequence and recalling its annotation, or running a domain/motif prediction tool. No concrete biological argument from the sequence text alone meaningfully distinguishes 205 from the other KS-labeled positions."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only position 205 corresponds to any annotated active site in the UniProt entry. Positions 458 and 315 are not annotated as active sites, and position 93 is labeled 'Proton donor' which does not match any annotation for this protein. The UniProt entry does annotate positions 340 and 380 as additional active sites for beta-ketoacyl synthase activity, but these are not among the choices, so no ambiguity exists within the provided options."
  },
  "important_caveats": [
    "The active site annotation is based on PROSITE-ProRule (ECO:0000255), a computational pattern-matching inference, not direct experimental evidence such as mutagenesis or crystallography.",
    "The UniProt entry annotates three positions (205, 340, 380) as active sites for beta-ketoacyl synthase activity; the question selects only one of these (205) as the correct answer while omitting the others from the choices.",
    "The protein is identified as 'module 8' of the FD-891 PKS (GfsC), implying it is one component of a multi-module assembly; the KS domain context is specific to this module.",
    "The UniProt accession E0D204 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
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
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:54.215687+00:00.  

```json
{"description":"For beta-ketoacyl synthase activity","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01348","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":205},"start":{"modifier":"EXACT","value":205}},"type":"Active site"}
```

Source SHA-256: `d3e6081dd33f462787c1460e2e3378a99c0a32a901c3c620f20a536cd944ba11`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69)  
**Locator:** `lines 200-202`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-02T04:27:56.450911+00:00.  

```text
FT   ACT_SITE        205
FT                   /note="For beta-ketoacyl synthase activity"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01348"
```

Source SHA-256: `d63277a07d00eb0d9fd8538c01445bcef958bf5e5584852732f178b8f77295cd`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69)  
**Locator:** `lines 203-205`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-02T04:27:56.450911+00:00.  

```text
FT   ACT_SITE        340
FT                   /note="For beta-ketoacyl synthase activity"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01348"
```

Source SHA-256: `d63277a07d00eb0d9fd8538c01445bcef958bf5e5584852732f178b8f77295cd`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E0D204?format=txt&versions=69)  
**Locator:** `lines 206-208`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 69 / 1.  
**Retrieved:** 2026-11-02T04:27:56.450911+00:00.  

```text
FT   ACT_SITE        380
FT                   /note="For beta-ketoacyl synthase activity"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01348"
```

Source SHA-256: `d63277a07d00eb0d9fd8538c01445bcef958bf5e5584852732f178b8f77295cd`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 79. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
