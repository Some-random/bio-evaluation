# catalytic_activity_0187

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0187.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — 4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MELNGIRRRLATAKEAERHRLLLELIRAAAAEALDRPGPLPLDPGRAFGAQGVRGRAAGRLRERLSEATGLPLPATVVFDYPTPGALAGRLCALLLDEPAGPGGANGQMEAEEPIAIVGMGCRLPGDVRSPEGLWRLVHNGTDAISEFPEDRGWTVQQHPDPDHLGTTVTRHAGFLYDAPDFDAGFFAISPGEAVTIDPQHRLLLETTWKAVEDARIDPTSLRGSRTGVFVGLMYSEYGARIRRVPPGAEGYRVVGSMPSVASGRLAYTFGFEGPAVTVDTACSSSLVAMHLAAQSLRKGECTLAVAGGATVMATPWGYIEFSRQRGLAPDGRCRSFSADAAGSSWSEGVGVLLLERLSDARRHGHRVLAVVRGSAVNQDGASNGLTAPNGPAQQRVIRQALAHAGLTTAEVDAVDAHGAGTRLGDPIEAQALLATYGQGRPAGRPLWLGSLKSNIGHTQAAAGAAGVIKMVMAMRHGVLPRSLHITEPTPHVDWTSGAVELLTEARDWPADGRPRRAAVSSFGVGGTNAHIILEQAAPEPERPHAPEADGEPRPLPWPVSGHGAAGLRAQARRLADFLRAGPAAPDADLAYSLATTRATLTDRAVVVAADRAEAIARLTALAEGDQGPRVARATAVPRDRLAFVFPGQGSQWPGMAAELMSCYPVFRESIKECGRSLAPHTDWSLAKVLRGESGAPTLDRVDVVQPALFAVMVSLAALWRSFGVEPSAVAGHSQGEIAAARVAGALSLEDAARVVALRSRALRVLSGRGGMVSVAAPAGQVLRTLERWGGAVSVAAVNGPRSLVISGDPGALGEALAAFEAEGIRARRIPVDYASHSAQVEEIRDTLLTELSGIRPRPATVPFYSTVSGEPLDTTALDTGYWVRNLRDTVQFDRTVRRLLADGHTTFLEMSPHPVLTPGIQETAEEAGADEVLTVESLRRNEGGPARLLTAVAEAHVHGVAVDWSPAFAPHRSPARRPAVLRLSSGAATGLRTRPRPPPMFTTAGLDGIDHPLLGAAIPLADGGGGTLFTGTLSLATHPWLADHAVADVLVVPGTALVEAALRAGAECTGRAMLEELVLQAPLILPEQGTVRIQLSVGGPDGTGRRALILSSRPEDAGADEPWTRHAEGTLAPGGGHPRQDPGPWPPTGAREIDLDDCYRQLAKTGLHYGPAFQGLKRLWRLADDLCLEAELPDSAGESGRYGLHPALFDAALHAAALAGPSGAEPLTRLPFSWSGVALYTAGATRLRARLSFTGPQSLTLTAMDPLGHPVLSVGTLGMRPVTAEALHRAAGTAGTALLRLEWRRQAPEHPAGPDLTGWAWVGAGAPPAQPPDGRPYRDLAALRAELDAGAAVPPVIVLAEPATPEGTDPFTAARAALHRTLAAIQDWAAEERLAGTRLVVLTQGAVAATPGALPDPALAAVWGLVRSAQAEYPDRIGLVDTDDPGRSRAAVAAAVHAGEAQAAVRDGALLVPRLARVTATDGPGGPAWPADGTVLVTGGLGTLGRLVVRHLVTTHGARRLVILSRSGGDSAEVREFVGELLAQGANVQVVKGDAADPAVLERVLDGIPQEHPLAAVAHLAGALDDGVLAAQTPQRLDRVLRPKAEAAWQLHRLTARARVPLLAFSSLSGVLGPAGQAGYAAANAFVDALVQRRRGTGLPGVSMGWGMWATRSGLTGALSDTDARLIARTGVRPLTDEEGLALFDQARATGEPVVFPLGLDITALNSGAPDGIPPLLRGLTARTPARRAGAAEAPEPAGEDLAARLAATPEAERDALLLGVVRGHIAAVLGYDDPRAVAERRPFSDIGFDSLRALQLRNRLGAATGRRLPATLVFDHPNPAALSRYLRTLLLPDPAPAPTAPDGQPGPDQADQVIERLNSASLEEVLDFIDHQLGE

[Multiple Choices]
A. UTP + H2O = UDP + phosphate + H(+)
B. 4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O
C. n ATP + n H2O + a microtubule = n ADP + n phosphate + (n+1) alpha/beta tubulin heterodimers.
D. UDP-N-acetyl-alpha-D-glucosamine + H2O = aldehydo-N-acetyl-D-mannosamine + UDP + H(+)
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches a UniProt entry whose catalytic-activity annotation gives the reaction in choice B; the same reaction is present in the archived entry for the matching sequence. This is database annotation supported by a cited publication, not independent verification here of the underlying experiment.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1,897-residue sequence has the scale and repeated catalytic-domain character expected of a modular type I polyketide synthase. Such enzymes assemble polyketide chains from extender units and can use reducing cofactors, making the polyketide-producing reaction in B a much better fit than the nucleotide hydrolysis, tubulin polymerization, or sugar-nucleotide transformation in A, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of modular polyketide synthases meaningfully distinguishes B among these choices. The sequence and general enzyme-family pattern do not independently establish the exact named product or full reaction stoichiometry, but that finer identification is not necessary to favor B over the offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe substantially different biological processes, and the sequence's large modular-enzyme architecture favors the polyketide synthase reaction.


### Important caveats

- The source annotation is tied to a publication, but the primary paper was not independently retrieved or assessed here.
- The sequence-family inference supports choosing B among these options; it does not by itself prove every substrate, product, or stoichiometric detail.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1,897-residue sequence has the scale and repeated catalytic-domain character expected of a modular type I polyketide synthase. Such enzymes assemble polyketide chains from extender units and can use reducing cofactors, making the polyketide-producing reaction in B a much better fit than the nucleotide hydrolysis, tubulin polymerization, or sugar-nucleotide transformation in A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of modular polyketide synthases meaningfully distinguishes B among these choices. The sequence and general enzyme-family pattern do not independently establish the exact named product or full reaction stoichiometry, but that finer identification is not necessary to favor B over the offered alternatives."
  },
  "case_id": "catalytic_activity_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry whose catalytic-activity annotation gives the reaction in choice B; the same reaction is present in the archived entry for the matching sequence. This is database annotation supported by a cited publication, not independent verification here of the underlying experiment."
  },
  "important_caveats": [
    "The source annotation is tied to a publication, but the primary paper was not independently retrieved or assessed here.",
    "The sequence-family inference supports choosing B among these options; it does not by itself prove every substrate, product, or stoichiometric detail."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe substantially different biological processes, and the sequence's large modular-enzyme architecture favors the polyketide synthase reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry whose catalytic-activity annotation gives the reaction in choice B; the same reaction is present in the archived entry for the matching sequence. This is database annotation supported by a cited publication, not independent verification here of the underlying experiment.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1,897-residue sequence has the scale and repeated catalytic-domain character expected of a modular type I polyketide synthase. Such enzymes assemble polyketide chains from extender units and can use reducing cofactors, making the polyketide-producing reaction in B a much better fit than the nucleotide hydrolysis, tubulin polymerization, or sugar-nucleotide transformation in A, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of modular polyketide synthases meaningfully distinguishes B among these choices. The sequence and general enzyme-family pattern do not independently establish the exact named product or full reaction stoichiometry, but that finer identification is not necessary to favor B over the offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe substantially different biological processes, and the sequence's large modular-enzyme architecture favors the polyketide synthase reaction."
  },
  "important_caveats": [
    "The source annotation is tied to a publication, but the primary paper was not independently retrieved or assessed here.",
    "The sequence-family inference supports choosing B among these options; it does not by itself prove every substrate, product, or stoichiometric detail."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B4ER92 (sequence matched) annotates this protein as 'Spectinabilin polyketide synthase system protein NorA' (EC 2.3.1.290) with the exact catalytic reaction listed in option B. The evidence code is ECO:0000305 (inferred by curator) based on PubMed:17763486. The reaction text in C5/H4 matches option B verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1897-residue sequence contains multiple conserved modular polyketide synthase (type I PKS) domain signatures identifiable by comparison with other well-characterized PKSs (DEBS, 6-dEB synthase, erythromycin PKS): (1) 'MGCRLPGDV' is the KS (ketosynthase) active-site motif; (2) 'GATVMATPWGY' is the AT (acyltransferase) domain 'GxSxG/GAT' signature; (3) 'GGDSAEVREFVGELLAQ' is the KR (ketoreductase) NAD(P)H-binding Rossmann motif; (4) repeated occurrences of these motifs indicate a multi-module iterative architecture. A knowledgeable model recognizes that modular PKSs catalyze iterative Claisen condensations of CoA-thioester extender units (malonyl-CoA, methylmalonyl-CoA) with NADPH-dependent ketoreductions. Among the four choices, only option B describes a polyketide condensation/reduction reaction using CoA thioesters and NADPH. Options A (nucleotide hydrolase), C (microtubule depolymerase), and D (glycoside hydrolase/epimerase) are mechanistically incompatible with the KS/AT/KR domain architecture. The domain signatures are highly conserved across the entire modular PKS superfamily, so this inference transfers directly from knowledge of other PKS proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The modular PKS domain architecture (KS, AT, KR motifs) is directly readable from the sequence and is shared across all type I modular PKSs. This family-level knowledge uniquely identifies option B as the only polyketide synthase reaction among the four choices. No target-specific database lookup is required; the conserved motifs and the incompatibility of the other three options with PKS biochemistry provide a clear, transferable discrimination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The PKS domain architecture unambiguously selects option B. The other three options describe entirely unrelated enzyme classes (nucleotide phosphatase, microtubule depolymerase, glycoside hydrolase) with no mechanistic overlap with polyketide synthesis.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (inferred by curator from literature), not direct in vitro experimental validation of the full multi-subunit reaction. NorA is one component of a multi-enzyme PKS system; the full reaction likely requires other PKS proteins in the operon.
- The specific product 'demethyldeoxyspectinabilin' and the precise stoichiometry (6 methylmalonyl-CoA + 1 malonyl-CoA) are pathway-specific details; however, the general reaction class (CoA-thioester condensation with NADPH reduction) is what the domain architecture predicts.
- Reviewer-only evidence was not available to the evaluated model; the reasoning above relies solely on sequence motifs and general PKS family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1897-residue sequence contains multiple conserved modular polyketide synthase (type I PKS) domain signatures identifiable by comparison with other well-characterized PKSs (DEBS, 6-dEB synthase, erythromycin PKS): (1) 'MGCRLPGDV' is the KS (ketosynthase) active-site motif; (2) 'GATVMATPWGY' is the AT (acyltransferase) domain 'GxSxG/GAT' signature; (3) 'GGDSAEVREFVGELLAQ' is the KR (ketoreductase) NAD(P)H-binding Rossmann motif; (4) repeated occurrences of these motifs indicate a multi-module iterative architecture. A knowledgeable model recognizes that modular PKSs catalyze iterative Claisen condensations of CoA-thioester extender units (malonyl-CoA, methylmalonyl-CoA) with NADPH-dependent ketoreductions. Among the four choices, only option B describes a polyketide condensation/reduction reaction using CoA thioesters and NADPH. Options A (nucleotide hydrolase), C (microtubule depolymerase), and D (glycoside hydrolase/epimerase) are mechanistically incompatible with the KS/AT/KR domain architecture. The domain signatures are highly conserved across the entire modular PKS superfamily, so this inference transfers directly from knowledge of other PKS proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The modular PKS domain architecture (KS, AT, KR motifs) is directly readable from the sequence and is shared across all type I modular PKSs. This family-level knowledge uniquely identifies option B as the only polyketide synthase reaction among the four choices. No target-specific database lookup is required; the conserved motifs and the incompatibility of the other three options with PKS biochemistry provide a clear, transferable discrimination."
  },
  "case_id": "catalytic_activity_0187",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B4ER92 (sequence matched) annotates this protein as 'Spectinabilin polyketide synthase system protein NorA' (EC 2.3.1.290) with the exact catalytic reaction listed in option B. The evidence code is ECO:0000305 (inferred by curator) based on PubMed:17763486. The reaction text in C5/H4 matches option B verbatim."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by curator from literature), not direct in vitro experimental validation of the full multi-subunit reaction. NorA is one component of a multi-enzyme PKS system; the full reaction likely requires other PKS proteins in the operon.",
    "The specific product 'demethyldeoxyspectinabilin' and the precise stoichiometry (6 methylmalonyl-CoA + 1 malonyl-CoA) are pathway-specific details; however, the general reaction class (CoA-thioester condensation with NADPH reduction) is what the domain architecture predicts.",
    "Reviewer-only evidence was not available to the evaluated model; the reasoning above relies solely on sequence motifs and general PKS family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PKS domain architecture unambiguously selects option B. The other three options describe entirely unrelated enzyme classes (nucleotide phosphatase, microtubule depolymerase, glycoside hydrolase) with no mechanistic overlap with polyketide synthesis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0187",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B4ER92 (sequence matched) annotates this protein as 'Spectinabilin polyketide synthase system protein NorA' (EC 2.3.1.290) with the exact catalytic reaction listed in option B. The evidence code is ECO:0000305 (inferred by curator) based on PubMed:17763486. The reaction text in C5/H4 matches option B verbatim.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1897-residue sequence contains multiple conserved modular polyketide synthase (type I PKS) domain signatures identifiable by comparison with other well-characterized PKSs (DEBS, 6-dEB synthase, erythromycin PKS): (1) 'MGCRLPGDV' is the KS (ketosynthase) active-site motif; (2) 'GATVMATPWGY' is the AT (acyltransferase) domain 'GxSxG/GAT' signature; (3) 'GGDSAEVREFVGELLAQ' is the KR (ketoreductase) NAD(P)H-binding Rossmann motif; (4) repeated occurrences of these motifs indicate a multi-module iterative architecture. A knowledgeable model recognizes that modular PKSs catalyze iterative Claisen condensations of CoA-thioester extender units (malonyl-CoA, methylmalonyl-CoA) with NADPH-dependent ketoreductions. Among the four choices, only option B describes a polyketide condensation/reduction reaction using CoA thioesters and NADPH. Options A (nucleotide hydrolase), C (microtubule depolymerase), and D (glycoside hydrolase/epimerase) are mechanistically incompatible with the KS/AT/KR domain architecture. The domain signatures are highly conserved across the entire modular PKS superfamily, so this inference transfers directly from knowledge of other PKS proteins.",
    "missing_item_specific_fact": "",
    "reason": "The modular PKS domain architecture (KS, AT, KR motifs) is directly readable from the sequence and is shared across all type I modular PKSs. This family-level knowledge uniquely identifies option B as the only polyketide synthase reaction among the four choices. No target-specific database lookup is required; the conserved motifs and the incompatibility of the other three options with PKS biochemistry provide a clear, transferable discrimination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PKS domain architecture unambiguously selects option B. The other three options describe entirely unrelated enzyme classes (nucleotide phosphatase, microtubule depolymerase, glycoside hydrolase) with no mechanistic overlap with polyketide synthesis."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by curator from literature), not direct in vitro experimental validation of the full multi-subunit reaction. NorA is one component of a multi-enzyme PKS system; the full reaction likely requires other PKS proteins in the operon.",
    "The specific product 'demethyldeoxyspectinabilin' and the precise stoichiometry (6 methylmalonyl-CoA + 1 malonyl-CoA) are pathway-specific details; however, the general reaction class (CoA-thioester condensation with NADPH reduction) is what the domain architecture predicts.",
    "Reviewer-only evidence was not available to the evaluated model; the reasoning above relies solely on sequence motifs and general PKS family knowledge."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 1897,
  "benchmark_sequence_sha256": "7a2b43eb4693bca9c8e214b8ce966e5161f55926389724de9065d4baf60d4ff1",
  "current_entry_audit": {
    "entryVersion": 85,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2008-09-23",
    "sequenceVersion": 1
  },
  "current_record_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1897,
  "current_source_sequence_sha256": "7a2b43eb4693bca9c8e214b8ce966e5161f55926389724de9065d4baf60d4ff1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 83,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B4ER92",
  "selected_historical_entry_version": 83,
  "selected_historical_record_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "selected_historical_source_sequence_length": 1897,
  "selected_historical_source_sequence_sha256": "7a2b43eb4693bca9c8e214b8ce966e5161f55926389724de9065d4baf60d4ff1",
  "selected_historical_version": {
    "accession": "B4ER92",
    "database": "Swiss-Prot",
    "entryVersion": 83,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NORA_STRON",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B4ER92\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":85,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2008-09-23\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Streptoverticillium orinoci\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces orinoci\",\"taxonId\":67339}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAO85893.1\",\"source\":\"EMBL\"}],\"value\":\"Modular polyketide synthase NorA\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17763486\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.290\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Spectinabilin polyketide synthase system protein NorA\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Spectinabilin PKS system protein NorA\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17763486\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:58945\"}}],\"reaction\":{\"ecNumber\":\"2.3.1.290\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17763486\",\"source\":\"PubMed\"}],\"name\":\"4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:58944\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57327\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57384\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142871\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142872\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER92.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Traitcheva N.\",\"Jenke-Kodama H.\",\"He J.\",\"Dittmann E.\",\"Hertweck C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17763486\"},{\"database\":\"DOI\",\"id\":\"10.1002/cbic.200700309\"}],\"citationType\":\"journal article\",\"firstPage\":\"1841\",\"id\":\"17763486\",\"journal\":\"ChemBioChem\",\"lastPage\":\"1849\",\"publicationDate\":\"2007\",\"title\":\"Non-colinear polyketide biosynthesis in the aureothin and neoaureothin pathways: an evolutionary perspective.\",\"volume\":\"8\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAO85893.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"HKI-0260\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:00.659517+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5eeaeb37c4ffac30774fcace62eb9d316998cb9ebef04f688b171413d879c5c3",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER92.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H1",
  "excerpt": "ID   NORA_STRON              Reviewed;        1897 AA.\nAC   B4ER92;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   23-SEP-2008, sequence version 1.\nDT   28-JAN-2026, entry version 83.\nDE   RecName: Full=Spectinabilin polyketide synthase system protein NorA {ECO:0000305};\nDE            Short=Spectinabilin PKS system protein NorA {ECO:0000305};\nDE            EC=2.3.1.290 {ECO:0000305|PubMed:17763486};\nDE   AltName: Full=Modular polyketide synthase NorA {ECO:0000312|EMBL:CAO85893.1};\nGN   Name=norA {ECO:0000303|PubMed:17763486};\nOS   Streptomyces orinoci (Streptoverticillium orinoci).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=67339;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Spectinabilin polyketide synthase system protein NorA {ECO:0000305};\nDE            Short=Spectinabilin PKS system protein NorA {ECO:0000305};\nDE            EC=2.3.1.290 {ECO:0000305|PubMed:17763486};\nDE   AltName: Full=Modular polyketide synthase NorA {ECO:0000312|EMBL:CAO85893.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAO85893.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND SUBUNIT.\nRC   STRAIN=HKI-0260;\nRX   PubMed=17763486; DOI=10.1002/cbic.200700309;\nRA   Traitcheva N., Jenke-Kodama H., He J., Dittmann E., Hertweck C.;\nRT   \"Non-colinear polyketide biosynthesis in the aureothin and neoaureothin\nRT   pathways: an evolutionary perspective.\";\nRL   ChemBioChem 8:1841-1849(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6\nCC         NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8\nCC         CoA + 5 H2O; Xref=Rhea:RHEA:58944, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:57287,\nCC         ChEBI:CHEBI:57327, ChEBI:CHEBI:57384, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:142871, ChEBI:CHEBI:142872;\nCC         EC=2.3.1.290; Evidence={ECO:0000305|PubMed:17763486};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:58945;\nCC         Evidence={ECO:0000305|PubMed:17763486};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 187. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
