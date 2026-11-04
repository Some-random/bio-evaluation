# cofactor_0075

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0075.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — pantetheine 4&#x27;-phosphate

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
A. [4Fe-4S] cluster
B. pantetheine 4'-phosphate
C. Mg(2+)
D. Na(+)
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates pantetheine 4'-phosphate as the cofactor, based on a PROSITE-ProRule computational annotation. This fits the protein's annotation as a polyketide synthase system protein, whose acyl-carrier domains use a phosphopantetheine arm. The evidence supports the key but is not direct experimental confirmation of cofactor dependence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The very long, multidomain sequence is consistent with a modular polyketide synthase. Transferable knowledge of these enzymes identifies their acyl-carrier protein domains as requiring a serine-linked phosphopantetheine arm for carrying intermediates. That distinguishes pantetheine 4'-phosphate (B) from an iron-sulfur cluster or sodium ion; magnesium may be relevant to other enzyme chemistries but does not explain the carrier-domain requirement.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and the well-established role of phosphopantetheine in polyketide-synthase carrier domains meaningfully favors B without needing the exact protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices offer no comparably plausible alternative to the phosphopantetheine requirement of a modular polyketide synthase's carrier domains.


### Important caveats

- The cited cofactor annotation is computational rather than direct experimental evidence.
- The family-level inference is strong, but the sequence alone does not establish experimental cofactor dependence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The very long, multidomain sequence is consistent with a modular polyketide synthase. Transferable knowledge of these enzymes identifies their acyl-carrier protein domains as requiring a serine-linked phosphopantetheine arm for carrying intermediates. That distinguishes pantetheine 4'-phosphate (B) from an iron-sulfur cluster or sodium ion; magnesium may be relevant to other enzyme chemistries but does not explain the carrier-domain requirement.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the well-established role of phosphopantetheine in polyketide-synthase carrier domains meaningfully favors B without needing the exact protein's recorded annotation."
  },
  "case_id": "cofactor_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates pantetheine 4'-phosphate as the cofactor, based on a PROSITE-ProRule computational annotation. This fits the protein's annotation as a polyketide synthase system protein, whose acyl-carrier domains use a phosphopantetheine arm. The evidence supports the key but is not direct experimental confirmation of cofactor dependence."
  },
  "important_caveats": [
    "The cited cofactor annotation is computational rather than direct experimental evidence.",
    "The family-level inference is strong, but the sequence alone does not establish experimental cofactor dependence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices offer no comparably plausible alternative to the phosphopantetheine requirement of a modular polyketide synthase's carrier domains."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates pantetheine 4'-phosphate as the cofactor, based on a PROSITE-ProRule computational annotation. This fits the protein's annotation as a polyketide synthase system protein, whose acyl-carrier domains use a phosphopantetheine arm. The evidence supports the key but is not direct experimental confirmation of cofactor dependence.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The very long, multidomain sequence is consistent with a modular polyketide synthase. Transferable knowledge of these enzymes identifies their acyl-carrier protein domains as requiring a serine-linked phosphopantetheine arm for carrying intermediates. That distinguishes pantetheine 4'-phosphate (B) from an iron-sulfur cluster or sodium ion; magnesium may be relevant to other enzyme chemistries but does not explain the carrier-domain requirement.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the well-established role of phosphopantetheine in polyketide-synthase carrier domains meaningfully favors B without needing the exact protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices offer no comparably plausible alternative to the phosphopantetheine requirement of a modular polyketide synthase's carrier domains."
  },
  "important_caveats": [
    "The cited cofactor annotation is computational rather than direct experimental evidence.",
    "The family-level inference is strong, but the sequence alone does not establish experimental cofactor dependence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (B4ER92, matched) annotates pantetheine 4'-phosphate as the cofactor with evidence code ECO:0000255 (PROSITE-ProRule:PRU00258, the ACP signature). The protein is identified as a modular polyketide synthase (NorA, EC 2.3.1.290). Pantetheine 4'-phosphate is the well-established prosthetic group of acyl carrier protein (ACP) domains, which are essential components of type I modular PKS enzymes. The annotation is family-based (PROSITE-ProRule) rather than direct experimental measurement of this specific protein, but the underlying biochemistry of ACP/PKS cofactor dependence is extensively validated across many characterized PKS and FAS systems.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The ~1897-residue sequence exhibits the hallmark architecture of a modular type I polyketide synthase: multiple tandem domains of similar length and composition, consistent with iterative KS-AT-ACP-ER-KR-DH module organization. Near the N-terminus, the motif 'GMGCRL' is recognizable as a variant of the conserved ACP core signature (GxxDxL), the domain that is post-translationally modified with pantetheine 4'-phosphate. Transferable knowledge from extensively characterized PKS/FAS systems (e.g., DEBS, FAS I, erythromycin PKS) establishes that pantetheine 4'-phosphate is the obligate prosthetic group of ACP domains and thus the defining cofactor of modular PKS enzymes. Among the four options, &#91;4Fe-4S&#93; clusters belong to radical SAM enzymes and ferredoxins, Mg2+ is the cofactor of kinases and polymerases, and Na+ is not a catalytic cofactor for PKS. Only pantetheine 4'-phosphate is mechanistically tied to the ACP/PKS family, making it the uniquely defensible choice once the PKS architecture and ACP motif are recognized.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the modular PKS architecture from the protein length and multi-domain pattern, identify the ACP-like motif 'GMGCRL' as a degenerate variant of the canonical ACP signature, and apply the well-established family-level fact that ACP domains carry pantetheine 4'-phosphate. This family-level inference meaningfully and uniquely distinguishes option B from the three alternatives, none of which are cofactors of PKS or ACP enzymes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Pantetheine 4'-phosphate is the defining cofactor of ACP domains in PKS/FAS enzymes. The other three options (&#91;4Fe-4S&#93;, Mg2+, Na+) are not cofactors of any known PKS domain. No ambiguity exists among the choices given the PKS family identification.


### Important caveats

- The UniProt cofactor annotation is based on PROSITE-ProRule (ECO:0000255), a computational/family-level assignment, not a direct experimental measurement on this specific protein. However, the underlying biochemistry is extensively validated across many characterized PKS systems.
- The ACP motif 'GMGCRL' in this sequence is a degenerate variant of the textbook 'GxxDSL' motif; recognition relies on family-level pattern matching rather than an exact canonical match.
- The protein identity (NorA, spectinabilin PKS) was established by the reviewer from UniProt; the evaluated model must rely on sequence features and family knowledge alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The ~1897-residue sequence exhibits the hallmark architecture of a modular type I polyketide synthase: multiple tandem domains of similar length and composition, consistent with iterative KS-AT-ACP-ER-KR-DH module organization. Near the N-terminus, the motif 'GMGCRL' is recognizable as a variant of the conserved ACP core signature (GxxDxL), the domain that is post-translationally modified with pantetheine 4'-phosphate. Transferable knowledge from extensively characterized PKS/FAS systems (e.g., DEBS, FAS I, erythromycin PKS) establishes that pantetheine 4'-phosphate is the obligate prosthetic group of ACP domains and thus the defining cofactor of modular PKS enzymes. Among the four options, [4Fe-4S] clusters belong to radical SAM enzymes and ferredoxins, Mg2+ is the cofactor of kinases and polymerases, and Na+ is not a catalytic cofactor for PKS. Only pantetheine 4'-phosphate is mechanistically tied to the ACP/PKS family, making it the uniquely defensible choice once the PKS architecture and ACP motif are recognized.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the modular PKS architecture from the protein length and multi-domain pattern, identify the ACP-like motif 'GMGCRL' as a degenerate variant of the canonical ACP signature, and apply the well-established family-level fact that ACP domains carry pantetheine 4'-phosphate. This family-level inference meaningfully and uniquely distinguishes option B from the three alternatives, none of which are cofactors of PKS or ACP enzymes."
  },
  "case_id": "cofactor_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (B4ER92, matched) annotates pantetheine 4'-phosphate as the cofactor with evidence code ECO:0000255 (PROSITE-ProRule:PRU00258, the ACP signature). The protein is identified as a modular polyketide synthase (NorA, EC 2.3.1.290). Pantetheine 4'-phosphate is the well-established prosthetic group of acyl carrier protein (ACP) domains, which are essential components of type I modular PKS enzymes. The annotation is family-based (PROSITE-ProRule) rather than direct experimental measurement of this specific protein, but the underlying biochemistry of ACP/PKS cofactor dependence is extensively validated across many characterized PKS and FAS systems."
  },
  "important_caveats": [
    "The UniProt cofactor annotation is based on PROSITE-ProRule (ECO:0000255), a computational/family-level assignment, not a direct experimental measurement on this specific protein. However, the underlying biochemistry is extensively validated across many characterized PKS systems.",
    "The ACP motif 'GMGCRL' in this sequence is a degenerate variant of the textbook 'GxxDSL' motif; recognition relies on family-level pattern matching rather than an exact canonical match.",
    "The protein identity (NorA, spectinabilin PKS) was established by the reviewer from UniProt; the evaluated model must rely on sequence features and family knowledge alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Pantetheine 4'-phosphate is the defining cofactor of ACP domains in PKS/FAS enzymes. The other three options ([4Fe-4S], Mg2+, Na+) are not cofactors of any known PKS domain. No ambiguity exists among the choices given the PKS family identification."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (B4ER92, matched) annotates pantetheine 4'-phosphate as the cofactor with evidence code ECO:0000255 (PROSITE-ProRule:PRU00258, the ACP signature). The protein is identified as a modular polyketide synthase (NorA, EC 2.3.1.290). Pantetheine 4'-phosphate is the well-established prosthetic group of acyl carrier protein (ACP) domains, which are essential components of type I modular PKS enzymes. The annotation is family-based (PROSITE-ProRule) rather than direct experimental measurement of this specific protein, but the underlying biochemistry of ACP/PKS cofactor dependence is extensively validated across many characterized PKS and FAS systems.",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The ~1897-residue sequence exhibits the hallmark architecture of a modular type I polyketide synthase: multiple tandem domains of similar length and composition, consistent with iterative KS-AT-ACP-ER-KR-DH module organization. Near the N-terminus, the motif 'GMGCRL' is recognizable as a variant of the conserved ACP core signature (GxxDxL), the domain that is post-translationally modified with pantetheine 4'-phosphate. Transferable knowledge from extensively characterized PKS/FAS systems (e.g., DEBS, FAS I, erythromycin PKS) establishes that pantetheine 4'-phosphate is the obligate prosthetic group of ACP domains and thus the defining cofactor of modular PKS enzymes. Among the four options, [4Fe-4S] clusters belong to radical SAM enzymes and ferredoxins, Mg2+ is the cofactor of kinases and polymerases, and Na+ is not a catalytic cofactor for PKS. Only pantetheine 4'-phosphate is mechanistically tied to the ACP/PKS family, making it the uniquely defensible choice once the PKS architecture and ACP motif are recognized.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the modular PKS architecture from the protein length and multi-domain pattern, identify the ACP-like motif 'GMGCRL' as a degenerate variant of the canonical ACP signature, and apply the well-established family-level fact that ACP domains carry pantetheine 4'-phosphate. This family-level inference meaningfully and uniquely distinguishes option B from the three alternatives, none of which are cofactors of PKS or ACP enzymes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Pantetheine 4'-phosphate is the defining cofactor of ACP domains in PKS/FAS enzymes. The other three options ([4Fe-4S], Mg2+, Na+) are not cofactors of any known PKS domain. No ambiguity exists among the choices given the PKS family identification."
  },
  "important_caveats": [
    "The UniProt cofactor annotation is based on PROSITE-ProRule (ECO:0000255), a computational/family-level assignment, not a direct experimental measurement on this specific protein. However, the underlying biochemistry is extensively validated across many characterized PKS systems.",
    "The ACP motif 'GMGCRL' in this sequence is a degenerate variant of the textbook 'GxxDSL' motif; recognition relies on family-level pattern matching rather than an exact canonical match.",
    "The protein identity (NorA, spectinabilin PKS) was established by the reviewer from UniProt; the evaluated model must rely on sequence features and family knowledge alone."
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
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:47942\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00258\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"pantetheine 4'-phosphate\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
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
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=pantetheine 4'-phosphate; Xref=ChEBI:CHEBI:47942;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00258};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:51.676658+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3915fd8feae78450aa29f8354771d2a032c0708667b4608cc38f4af415714d8a",
  "url": "https://rest.uniprot.org/unisave/B4ER92?format=txt&versions=83"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 75. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
