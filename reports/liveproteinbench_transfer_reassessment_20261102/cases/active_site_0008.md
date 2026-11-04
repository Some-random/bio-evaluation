# active_site_0008

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0008.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 179 (For beta-ketoacyl synthase activity)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASSALTPVAIVGYACKLPGDVSSPDDLWELCSRGRTGWGPTPSTRYSKDAYYHPAPGKHGCINTEGGYFLKEDPARFDAPFFNMTIQEATALDPQQRLLLECTFEAFENSGMTKEGIAGKDIGVFVGGSFADYEVNNTRDIDTAPTYQATGCAPAMQSNRLSYYFDLRGPSMTVDTACSSSLVALHSAMQSLRNGESSSAVVAAAHLNLTPDFFVTMSNTQLLNDAGKTFAFDHRAISGFARGEGAGSMILKPLDAAIRDGDVIRAVIHNSGVNQDGKTNGITVPNGRAQSDLIKQVYSKAGLDPAECGFSECHGTGTKVGDPIEVAGIHEALGAGRSPRNPLFIGSVKSNVGHLEGASGIVSVIKAAMMLEKGMVLPNANFETANPNIPLEQYNMKVPTSTRPWPRGKKYVSVSNYGFGGANAHVVLGAAPKGLKTTMTTIRSLEDAPEEPLCKLFVLSAHDSQALQKEITDLGVFLEQRPEVFEKLLAGNVAYTLGERRSHLPCRLAIAAVSSDELGQSLATTKVPTFRARNEPTLGFVFTGQGAQWATMGAELARDYPIFAAALDTADDTLKALGADFSLKEEMLKPADISLINAAHISQPACTALQIALTMLLSSWGIHPAAVVGHSSGEIGCAFAAGIIGLEDAMKIAYYRGQCMLSLKKKAVGKPQGTMMAVGTSAENVRPLLDAVSKGYITVACINSPASVTLSGDVEAVEELQPILTEKSIFNRQLKVGVAYHSAHLEPVVDEYLDLIKNIQPASTATATFYSSLLGRVAEASELTPEYWVQNLTSPVRFSGGLSAMARETGSKTIDHLVELGPHSALQGPIRDTLATIDAAKGKMHYVSVLARGQNASECALRMAGALYMKGLSLTFGEINFPRTKSVNQKLITDLPRYPFNHETRYWHESRLAQKHCFKEGGRNDLLGSLADWSNDLEPTWRNIVKLDDLPFLRSHKMQDMPVFPMAGYMGMALEAAARRAIARGVQFDRFEIREFVVSSALVFNEDTDVEMTITLKPYSEGLRGAASDLWDDYKICSWDAKRGWLQHCHGLVGVRNSPAANAVDAHRIQSASKAFEACKASIISASTETVDVQAMYNTLTTIGAGYGPVFTGLEPCQASDTTAHAQLVVPDTKSLMPKGYETELIVHPALLDQIIQIVWPIFGAGRQGLDTLYMPTFVKNFSISRNFASMLGNGLEVFGAGAPNNEAPEPTKFGFFVVGSSDASEPLVQFDGLTMTPLRESSGSSGPQARELCYKIDWQTVSDEDIGLEKSSSDASDTPIKADSLVSTPFTRDEAVCVVYNKATEKDLAAEVADNVWKTSGVQAELVTLSKVIPADKRVIFVSTGNNVLSGIDATMFGTLRQMLLSARKVLWIYKEGPDVDDVDGSMVVGFTRAIRSETSANIVTLGLQQATGKTLVENIFTVLTKTSADSPSTFKDDKEFILKGDDLLVPKVVDDEELNVRLHQESQDSVIYQQPFAQSDRRLKMVIATLGSLDSFYFVDDEPKPLNDNEVEIEVKATGMNFKDVVVSMGQLNQPYIGVECAGVIAAVGKKVTDVKVGQSVMAMTEGAYSTYARCLSTSVAPLPEKMDFTAASTIPVVFCTAYYGLFDLGRLTEGESVLIHAAAGGVGQAAIMLAQTCGAEIFATVGSLDKKQHIVKEYGIPEDHIFYSRDTAFGPAIRQVTGGKGVDVVLNSLGGDFLRESWDCLAPFGRFIEIGKADITKNSRLEMAQFEYNVSFASVDLTKVAAYKPKLMKRLLNDVEKLMSSGSIRPVGPITSYGINDVEAAFRSLQSGKSMGKLVIAPQSGDSVQAIAPKKTATLFKEDASYLIVGGTGGLGCSIARWMASRGAKHICLSSRRANITPRLEALITDLSILGTKVSVRACDVADAGSVETLVKDLKKESPIRGVIQGAMVLKDVLYEQMTLDDFSAVVNPKVAGTLNLHNSLGTSELDFFIALSSVAGVVGNRGQAAYAAANVFLDTFMAHRKAQGLPGTSLDLTAVSDVGYLADNSERAADVLRNLGGETIEESEILGLLTAAVTGKITASNNHVITGLKINPGSEPFWCHDAKFSNLLAAAASQSSAEGGNANIPLPQALKSAANGEKALEVLYGALVTKLAAVLMLSVEEMEPSAAVASYSLDSLAAIEVRNWIAREADANVQVLELLTSPSLMELAKLISKKSKLVSFE

[Multiple Choices]
A. Position 179 (For beta-ketoacyl synthase activity)
B. Position 157 (Proton acceptor)
C. Position 968 (For acyl/malonyl transferase activity)
D. Position 1045 (Proton acceptor; for dehydratase activity)
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation identifies position 179 as an active site for beta-ketoacyl synthase activity. This is computational annotation evidence, not direct experimental validation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence is consistent with a polyketide synthase, whose N-terminal beta-ketoacyl synthase domain uses a conserved catalytic cysteine. Position 179 is cysteine, making choice A a credible family-based inference; position 157 is methionine, while the later choices point to other activities or regions.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognizing the polyketide synthase architecture and the conserved KS catalytic-cysteine feature meaningfully distinguishes A among the offered choices without needing the exact protein's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A matches the conserved KS catalytic-cysteine inference among these alternatives.


### Important caveats

- The supporting source annotation is based on a PROSITE-ProRule computational inference rather than cited experimental evidence.
- The prompt describes residues in the plural, but each option offers a single residue.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is consistent with a polyketide synthase, whose N-terminal beta-ketoacyl synthase domain uses a conserved catalytic cysteine. Position 179 is cysteine, making choice A a credible family-based inference; position 157 is methionine, while the later choices point to other activities or regions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the polyketide synthase architecture and the conserved KS catalytic-cysteine feature meaningfully distinguishes A among the offered choices without needing the exact protein's recorded annotation."
  },
  "case_id": "active_site_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 179 as an active site for beta-ketoacyl synthase activity. This is computational annotation evidence, not direct experimental validation."
  },
  "important_caveats": [
    "The supporting source annotation is based on a PROSITE-ProRule computational inference rather than cited experimental evidence.",
    "The prompt describes residues in the plural, but each option offers a single residue."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A matches the conserved KS catalytic-cysteine inference among these alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 179 as an active site for beta-ketoacyl synthase activity. This is computational annotation evidence, not direct experimental validation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence is consistent with a polyketide synthase, whose N-terminal beta-ketoacyl synthase domain uses a conserved catalytic cysteine. Position 179 is cysteine, making choice A a credible family-based inference; position 157 is methionine, while the later choices point to other activities or regions.",
    "missing_item_specific_fact": "",
    "reason": "Recognizing the polyketide synthase architecture and the conserved KS catalytic-cysteine feature meaningfully distinguishes A among the offered choices without needing the exact protein's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A matches the conserved KS catalytic-cysteine inference among these alternatives."
  },
  "important_caveats": [
    "The supporting source annotation is based on a PROSITE-ProRule computational inference rather than cited experimental evidence.",
    "The prompt describes residues in the plural, but each option offers a single residue."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5/H3) explicitly lists position 179 as an Active site with description 'For beta-ketoacyl synthase activity,' matching option A exactly. The residue at position 179 in the supplied sequence is Cys (verified by manual counting: positions 171-180 = PSMTVDTACS), consistent with the KS catalytic cysteine. The annotation is computational (ECO:0000255, PROSITE-ProRule PRU01348), not experimental, but it is a recognized and consistent annotation. The other options do not match any annotated active site: position 157 has no annotation, position 968 has no annotation, and the dehydratase proton acceptor is annotated at 957 (not 1045 as in option D).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 2190-residue protein is recognizable as a fungal type I polyketide synthase (HR-PKS) by its large multi-domain architecture. In all fungal PKSs, the KS (ketoacyl synthase) domain is the first catalytic module, placing its catalytic Cys within the first ~200-400 residues. The KS catalytic Cys sits in a conserved motif (GHS or variants like ACS) and is one of the most well-characterized active-site residues in PKS biochemistry. Counting to position 179 in the supplied sequence yields Cys (in the context 'DTACS'), matching the expected KS catalytic cysteine. Option B (position 157, 'Proton acceptor') is eliminated because position 157 is Met, which cannot serve as a proton acceptor. Option D (position 1045, 'Proton acceptor; for dehydratase activity') is a plausible-sounding DH-domain description but the actual DH proton acceptor (a His) in fungal PKSs is typically ~100 residues earlier; moreover, the residue at 1045 does not match a typical His proton acceptor. Option C (position 968, 'acyl/malonyl transferase') would correspond to an AT-domain Ser, but the AT domain in fungal PKSs follows the KS and its catalytic Ser is at a different position. Thus, family-level knowledge of fungal PKS domain order (KS first) and the conserved Cys-His-His catalytic triad of KS domains meaningfully distinguishes option A from the others.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model familiar with fungal PKS domain architecture and the KS catalytic Cys motif can identify the correct answer by: (1) recognizing the protein as a fungal PKS from its size and domain features, (2) knowing the KS domain is the first catalytic module, (3) identifying the Cys at position 179 as the KS catalytic residue, and (4) eliminating options with chemically implausible residues (Met as proton acceptor) or positions inconsistent with known domain boundaries. This is legitimate transferable knowledge from other fungal PKSs (e.g., 6-MSAS, yeast FAS) rather than memorization of this specific entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options differ in both position and functional description. Only position 179 with 'beta-ketoacyl synthase activity' matches a Cys residue in the expected KS catalytic context. The other options either assign catalytic roles to non-catalytic residues (Met at 157) or give positions that do not correspond to the actual annotated active sites for the described activities.


### Important caveats

- The active-site annotation is computational (PROSITE-ProRule PRU01348), not experimentally validated. No crystal structure or mutagenesis data for this exact protein confirms position 179.
- The UniProt entry also annotates positions 315 and 355 as additional KS active sites (likely the His residues of the Cys-His-His triad or a second KS-like motif), but these are not offered as options, so they do not create ambiguity among the given choices.
- The protein identity (Aureobasidium melanogenum HR-PKS PKS1) was inferred by the reviewer from metadata, not from the original model input. The model must work from sequence features alone.
- Manual residue counting in a 2190-aa sequence is error-prone; the Cys at 179 was verified but small counting errors could shift the identified residue by one or two positions.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 2190-residue protein is recognizable as a fungal type I polyketide synthase (HR-PKS) by its large multi-domain architecture. In all fungal PKSs, the KS (ketoacyl synthase) domain is the first catalytic module, placing its catalytic Cys within the first ~200-400 residues. The KS catalytic Cys sits in a conserved motif (GHS or variants like ACS) and is one of the most well-characterized active-site residues in PKS biochemistry. Counting to position 179 in the supplied sequence yields Cys (in the context 'DTACS'), matching the expected KS catalytic cysteine. Option B (position 157, 'Proton acceptor') is eliminated because position 157 is Met, which cannot serve as a proton acceptor. Option D (position 1045, 'Proton acceptor; for dehydratase activity') is a plausible-sounding DH-domain description but the actual DH proton acceptor (a His) in fungal PKSs is typically ~100 residues earlier; moreover, the residue at 1045 does not match a typical His proton acceptor. Option C (position 968, 'acyl/malonyl transferase') would correspond to an AT-domain Ser, but the AT domain in fungal PKSs follows the KS and its catalytic Ser is at a different position. Thus, family-level knowledge of fungal PKS domain order (KS first) and the conserved Cys-His-His catalytic triad of KS domains meaningfully distinguishes option A from the others.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with fungal PKS domain architecture and the KS catalytic Cys motif can identify the correct answer by: (1) recognizing the protein as a fungal PKS from its size and domain features, (2) knowing the KS domain is the first catalytic module, (3) identifying the Cys at position 179 as the KS catalytic residue, and (4) eliminating options with chemically implausible residues (Met as proton acceptor) or positions inconsistent with known domain boundaries. This is legitimate transferable knowledge from other fungal PKSs (e.g., 6-MSAS, yeast FAS) rather than memorization of this specific entry."
  },
  "case_id": "active_site_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H3) explicitly lists position 179 as an Active site with description 'For beta-ketoacyl synthase activity,' matching option A exactly. The residue at position 179 in the supplied sequence is Cys (verified by manual counting: positions 171-180 = PSMTVDTACS), consistent with the KS catalytic cysteine. The annotation is computational (ECO:0000255, PROSITE-ProRule PRU01348), not experimental, but it is a recognized and consistent annotation. The other options do not match any annotated active site: position 157 has no annotation, position 968 has no annotation, and the dehydratase proton acceptor is annotated at 957 (not 1045 as in option D)."
  },
  "important_caveats": [
    "The active-site annotation is computational (PROSITE-ProRule PRU01348), not experimentally validated. No crystal structure or mutagenesis data for this exact protein confirms position 179.",
    "The UniProt entry also annotates positions 315 and 355 as additional KS active sites (likely the His residues of the Cys-His-His triad or a second KS-like motif), but these are not offered as options, so they do not create ambiguity among the given choices.",
    "The protein identity (Aureobasidium melanogenum HR-PKS PKS1) was inferred by the reviewer from metadata, not from the original model input. The model must work from sequence features alone.",
    "Manual residue counting in a 2190-aa sequence is error-prone; the Cys at 179 was verified but small counting errors could shift the identified residue by one or two positions."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options differ in both position and functional description. Only position 179 with 'beta-ketoacyl synthase activity' matches a Cys residue in the expected KS catalytic context. The other options either assign catalytic roles to non-catalytic residues (Met at 157) or give positions that do not correspond to the actual annotated active sites for the described activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5/H3) explicitly lists position 179 as an Active site with description 'For beta-ketoacyl synthase activity,' matching option A exactly. The residue at position 179 in the supplied sequence is Cys (verified by manual counting: positions 171-180 = PSMTVDTACS), consistent with the KS catalytic cysteine. The annotation is computational (ECO:0000255, PROSITE-ProRule PRU01348), not experimental, but it is a recognized and consistent annotation. The other options do not match any annotated active site: position 157 has no annotation, position 968 has no annotation, and the dehydratase proton acceptor is annotated at 957 (not 1045 as in option D).",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 2190-residue protein is recognizable as a fungal type I polyketide synthase (HR-PKS) by its large multi-domain architecture. In all fungal PKSs, the KS (ketoacyl synthase) domain is the first catalytic module, placing its catalytic Cys within the first ~200-400 residues. The KS catalytic Cys sits in a conserved motif (GHS or variants like ACS) and is one of the most well-characterized active-site residues in PKS biochemistry. Counting to position 179 in the supplied sequence yields Cys (in the context 'DTACS'), matching the expected KS catalytic cysteine. Option B (position 157, 'Proton acceptor') is eliminated because position 157 is Met, which cannot serve as a proton acceptor. Option D (position 1045, 'Proton acceptor; for dehydratase activity') is a plausible-sounding DH-domain description but the actual DH proton acceptor (a His) in fungal PKSs is typically ~100 residues earlier; moreover, the residue at 1045 does not match a typical His proton acceptor. Option C (position 968, 'acyl/malonyl transferase') would correspond to an AT-domain Ser, but the AT domain in fungal PKSs follows the KS and its catalytic Ser is at a different position. Thus, family-level knowledge of fungal PKS domain order (KS first) and the conserved Cys-His-His catalytic triad of KS domains meaningfully distinguishes option A from the others.",
    "missing_item_specific_fact": "",
    "reason": "A model familiar with fungal PKS domain architecture and the KS catalytic Cys motif can identify the correct answer by: (1) recognizing the protein as a fungal PKS from its size and domain features, (2) knowing the KS domain is the first catalytic module, (3) identifying the Cys at position 179 as the KS catalytic residue, and (4) eliminating options with chemically implausible residues (Met as proton acceptor) or positions inconsistent with known domain boundaries. This is legitimate transferable knowledge from other fungal PKSs (e.g., 6-MSAS, yeast FAS) rather than memorization of this specific entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options differ in both position and functional description. Only position 179 with 'beta-ketoacyl synthase activity' matches a Cys residue in the expected KS catalytic context. The other options either assign catalytic roles to non-catalytic residues (Met at 157) or give positions that do not correspond to the actual annotated active sites for the described activities."
  },
  "important_caveats": [
    "The active-site annotation is computational (PROSITE-ProRule PRU01348), not experimentally validated. No crystal structure or mutagenesis data for this exact protein confirms position 179.",
    "The UniProt entry also annotates positions 315 and 355 as additional KS active sites (likely the His residues of the Cys-His-His triad or a second KS-like motif), but these are not offered as options, so they do not create ambiguity among the given choices.",
    "The protein identity (Aureobasidium melanogenum HR-PKS PKS1) was inferred by the reviewer from metadata, not from the original model input. The model must work from sequence features alone.",
    "Manual residue counting in a 2190-aa sequence is error-prone; the Cys at 179 was verified but small counting errors could shift the identified residue by one or two positions."
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
  "benchmark_sequence_length": 2190,
  "benchmark_sequence_sha256": "54c6293388ffbabb04893b3f34a510ee9be7b0611db234b260e42f3c643855c0",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-09-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 2190,
  "current_source_sequence_sha256": "54c6293388ffbabb04893b3f34a510ee9be7b0611db234b260e42f3c643855c0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A172QE52",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "52e514130a97f47329d9a3516f69b151be6460d3cc32144e6d797ab41a405440",
  "selected_historical_source_sequence_length": 2190,
  "selected_historical_source_sequence_sha256": "54c6293388ffbabb04893b3f34a510ee9be7b0611db234b260e42f3c643855c0",
  "selected_historical_version": {
    "accession": "A0A172QE52",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PKS1_AURME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A172QE52\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:28.395908+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf",
  "url": "https://rest.uniprot.org/uniprotkb/A0A172QE52.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-09-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:28.395908+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf",
  "url": "https://rest.uniprot.org/uniprotkb/A0A172QE52.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Aureobasidium pullulans var. melanogenum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetidae\",\"Dothideales\",\"Saccotheciaceae\",\"Aureobasidium\"],\"scientificName\":\"Aureobasidium melanogenum\",\"taxonId\":46634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:28.395908+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf",
  "url": "https://rest.uniprot.org/uniprotkb/A0A172QE52.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"Liamocins biosynthesis cluster protein PKS1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"Highly-reducing polyketide synthase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"HR-PKS PKS1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:28.395908+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf",
  "url": "https://rest.uniprot.org/uniprotkb/A0A172QE52.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":179},\"start\":{\"modifier\":\"EXACT\",\"value\":179}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:24:28.395908+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf",
  "url": "https://rest.uniprot.org/uniprotkb/A0A172QE52.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":315},\"start\":{\"modifier\":\"EXACT\",\"value\":315}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:24:28.395908+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf",
  "url": "https://rest.uniprot.org/uniprotkb/A0A172QE52.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":355},\"start\":{\"modifier\":\"EXACT\",\"value\":355}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:24:28.395908+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf",
  "url": "https://rest.uniprot.org/uniprotkb/A0A172QE52.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Proton acceptor; for dehydratase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01363\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":957},\"start\":{\"modifier\":\"EXACT\",\"value\":957}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:24:28.395908+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf",
  "url": "https://rest.uniprot.org/uniprotkb/A0A172QE52.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Proton donor; for dehydratase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01363\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1154},\"start\":{\"modifier\":\"EXACT\",\"value\":1154}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:24:28.395908+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf",
  "url": "https://rest.uniprot.org/uniprotkb/A0A172QE52.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A172QE52.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Xue S.J.\",\"Liu G.L.\",\"Chi Z.\",\"Gao Z.C.\",\"Hu Z.\",\"Chi Z.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32003433\"},{\"database\":\"DOI\",\"id\":\"10.1042/bcj20190922\"}],\"citationType\":\"journal article\",\"firstPage\":\"887\",\"id\":\"32003433\",\"journal\":\"Biochem. J.\",\"lastPage\":\"903\",\"publicationDate\":\"2020\",\"title\":\"Genetic evidences for the core biosynthesis pathway, regulation, transport and secretion of liamocins in yeast-like fungal cells.\",\"volume\":\"477\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"DOMAIN\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:28.395908+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "16a30a77ee9823820a479e1b4a3663d71e8a84512c7e8f13a6d2e372aec007bf",
  "url": "https://rest.uniprot.org/uniprotkb/A0A172QE52.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   PKS1_AURME              Reviewed;        2190 AA.\nAC   A0A172QE52;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-SEP-2016, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=Highly-reducing polyketide synthase 1 {ECO:0000303|PubMed:32003433};\nDE            Short=HR-PKS PKS1 {ECO:0000303|PubMed:32003433};\nDE            EC=1.-.-.- {ECO:0000269|PubMed:32003433};\nDE            EC=2.3.1.- {ECO:0000269|PubMed:32003433};\nDE   AltName: Full=Liamocins biosynthesis cluster protein PKS1 {ECO:0000303|PubMed:32003433};\nGN   Name=PKS1 {ECO:0000303|PubMed:32003433};\nOS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.\nOX   NCBI_TaxID=46634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:31.251331+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52e514130a97f47329d9a3516f69b151be6460d3cc32144e6d797ab41a405440",
  "url": "https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, DISRUPTION PHENOTYPE, DOMAIN, AND INDUCTION.\nRX   PubMed=32003433; DOI=10.1042/bcj20190922;\nRA   Xue S.J., Liu G.L., Chi Z., Gao Z.C., Hu Z., Chi Z.M.;\nRT   \"Genetic evidences for the core biosynthesis pathway, regulation, transport\nRT   and secretion of liamocins in yeast-like fungal cells.\";\nRL   Biochem. J. 477:887-903(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:31.251331+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52e514130a97f47329d9a3516f69b151be6460d3cc32144e6d797ab41a405440",
  "url": "https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        179\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:31.251331+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 210-212",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52e514130a97f47329d9a3516f69b151be6460d3cc32144e6d797ab41a405440",
  "url": "https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        315\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:31.251331+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 213-215",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52e514130a97f47329d9a3516f69b151be6460d3cc32144e6d797ab41a405440",
  "url": "https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H5",
  "excerpt": "FT   ACT_SITE        355\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:31.251331+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 216-218",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52e514130a97f47329d9a3516f69b151be6460d3cc32144e6d797ab41a405440",
  "url": "https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H6",
  "excerpt": "FT   ACT_SITE        957\nFT                   /note=\"Proton acceptor; for dehydratase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01363\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:31.251331+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 219-221",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52e514130a97f47329d9a3516f69b151be6460d3cc32144e6d797ab41a405440",
  "url": "https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H7",
  "excerpt": "FT   ACT_SITE        1154\nFT                   /note=\"Proton donor; for dehydratase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01363\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:31.251331+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 222-224",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52e514130a97f47329d9a3516f69b151be6460d3cc32144e6d797ab41a405440",
  "url": "https://rest.uniprot.org/unisave/A0A172QE52?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 8. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
