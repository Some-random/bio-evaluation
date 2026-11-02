# pathway_0025

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MPSHTFNPQAGYDLAVDRNLGLGEIFYNRAQKSHQAIAVCDGGAVLTYGQLHAKAYRLAQELSQWLRLTEKPVGIVVQHGMADVVAQMAVIYAGGSCAPMDPTLPDNQIQGRLKRLDAVCVLTDQANRHRDLGADVLCIDDFDIADLAPEDTLYPVATNLEHCAYLIHTSGTTAEPKAVQIAARSILHVAFYAPLEPVYDTDVVAHANNSSFDVSLFDIWVPLLRGAQIAVINKAVLLDPPMMAREIDRLGITVMATTTAVLNLAAFIYPKAFAKLRLVTIGGEAANVAAIRIILKNGPPAMLFNAYGPTECCVFCLAHQITPADVEHGSIGVSIGKPVGRTITYIAGDEGGESDQGELWIGGPGVSPGYFRQPEKNLAAFSDLGEAMTSLENPVRFYRTGDIVRRRPNGALEYVGRRDHQVKVRGFRIELEAVEAGLLKTGLFSDAVAMRIEMPQNGAGSILAAYVVPTDVSKPPTMDEALESAKSILPHYMVPQLELVPRLPLNRHLKVDRKQLAELFGRRWEDVSPAQPENASQDVRSALVSLWATVLASPLSTYGDDDDFLHLGGTSLQAAMLINQIRHKFDIEVSLLTLYDNTTLGALTSIIKQRLSGQSETLHNEKDSWVADSEIADDLSCPLDRPIDWCRDTEGRVFLTGGTGFVGAFLLADLLHMPQTSQVRCLVRATDAAVGQERLRAALDKYGLWEDGFADKLVAIAGLLEDDYLGMGREQFEEAASWASVVFHLGARVNYAQPYSLHRASNTLGTRNMVRFACAGRTKAIHYVSSIGCFGPTGSILGTTSVREDEPLLPHITALPYDHGYAQSQWVADALLRRLMDRGFPIAIYRPGFIVGHSQTGACNPDDFLSRLIDACREIGCYPQLPNQRKEFVPVDYVNAAILHIAASPASLGHAYHIVPPTRAVSIDMDNSMALVDRAGNSPMRPVSYKEWVERLAATSPKRLLPLQPMLAERVKDGLTRWELYENMPVYETTNTARALQNYPGGLQFPVLDTSLMKRYLDFLEAKG

[Multiple Choices]
A. L-threonine from L-aspartate: step 5/5. .
B. Secondary metabolite biosynthesis. .
C. L-valine biosynthesis
D. L-methionine biosynthesis via de novo pathway. .
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

> The exact sequence matches the UniProt record for FrzA, which annotates its pathway as secondary metabolite biosynthesis and cites a study on FR901483 biosynthesis. The annotation carries experimental-evidence code ECO:0000269, though the primary paper was not independently reviewed here.

Citations as saved: [H3](#evidence-h3), [H2](#evidence-h2), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a long fungal enzyme, but its length and general sequence features do not meaningfully distinguish a role in secondary-metabolite biosynthesis from the listed amino-acid biosynthesis pathways.


**Missing item-specific fact**

> The protein-specific identification and functional assignment of FrzA to the FR901483 biosynthetic pathway are absent from the input.


**Reason**

> Selecting B depends on knowing this protein's specific function or pathway annotation; recognizing the sequence or relying on a generic sequence heuristic would not provide that information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports B; the other choices name specific amino-acid biosynthesis pathways and are not supported for this protein by the available record.


### Important caveats

- The reviewer-only database evidence confirms a sequence match but was not available to the evaluated model.
- The author’s exact source snapshot is unknown; the historical record also matches the sequence and contains the pathway annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a long fungal enzyme, but its length and general sequence features do not meaningfully distinguish a role in secondary-metabolite biosynthesis from the listed amino-acid biosynthesis pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and functional assignment of FrzA to the FR901483 biosynthetic pathway are absent from the input.",
    "reason": "Selecting B depends on knowing this protein's specific function or pathway annotation; recognizing the sequence or relying on a generic sequence heuristic would not provide that information."
  },
  "case_id": "pathway_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H2",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record for FrzA, which annotates its pathway as secondary metabolite biosynthesis and cites a study on FR901483 biosynthesis. The annotation carries experimental-evidence code ECO:0000269, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only database evidence confirms a sequence match but was not available to the evaluated model.",
    "The author’s exact source snapshot is unknown; the historical record also matches the sequence and contains the pathway annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B; the other choices name specific amino-acid biosynthesis pathways and are not supported for this protein by the available record."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record for FrzA, which annotates its pathway as secondary metabolite biosynthesis and cites a study on FR901483 biosynthesis. The annotation carries experimental-evidence code ECO:0000269, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["H3", "H2", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a long fungal enzyme, but its length and general sequence features do not meaningfully distinguish a role in secondary-metabolite biosynthesis from the listed amino-acid biosynthesis pathways.",
    "missing_item_specific_fact": "The protein-specific identification and functional assignment of FrzA to the FR901483 biosynthetic pathway are absent from the input.",
    "reason": "Selecting B depends on knowing this protein's specific function or pathway annotation; recognizing the sequence or relying on a generic sequence heuristic would not provide that information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B; the other choices name specific amino-acid biosynthesis pathways and are not supported for this protein by the available record."
  },
  "important_caveats": [
    "The reviewer-only database evidence confirms a sequence match but was not available to the evaluated model.",
    "The author’s exact source snapshot is unknown; the historical record also matches the sequence and contains the pathway annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A7T8F1L4 annotates this protein as 'Non-canonical nonribosomal peptide synthetase FrzA' (EC 1.2.1.101) with pathway 'Secondary metabolite biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:33372776). The protein is part of the FR901483 immunosuppressant biosynthesis cluster in Cladobotryum sp., a fungal secondary metabolite. The sequence matches exactly (SHA-256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 1024-aa sequence exhibits unmistakable multi-domain NRPS architecture: a PCP domain with the conserved 'GGSC' phosphopantetheinylation serine motif, adenylation (A) domain signatures (including 'GGxxxDG' and 'GELWIGGPGVSPGYFRQPEKNLAAFSDLGEAMTSLENPVRFYRTGDIVRRRPNGALEYVGRRDHQVKVRGFRIELEAVEAGLLKTGLFSDAVAMRIEMPQNGAGSILAAYVVPTDVSKPPTMDEALESAKSILPHYMVPQLELVPRLPLNRHLKVDRKQLAELFGRRWEDVSPAQPENASQDVRSALVSLWATVLASPLSTYGDDDDFLHLGGTSLQAAMLINQIRHKFDIEVSLLTLYDNTTLGALTSIIKQRLSGQSETLHNEKDSWVADSEIADDLSCPLDRPIDWCRDTEGRVFLTGGTGFVGAFLLADLLHMPQTSQVRCLVRATDAAVGQERLRAALDKYGLWEDGFADKLVAIAGLLEDDYLGMGREQFEEAASWASVVFHLGARVNYAQPYSLHRASNTLGTRNMVRFACAGRTKAIHYVSSIGCFGPTGSILGTTSVREDEPLLPHITALPYDHGYAQSQWVADALLRRLMDRGFPIAIYRPGFIVGHSQTGACNPDDFLSRLIDACREIGCYPQLPNQRKEFVPVDYVNAAILHIAASPASLGHAYHIVPPTRAVSIDMDNSMALVDRAGNSPMRPVSYKEWVERLAATSPKRLLPLQPMLAERVKDGLTRWELYENMPVYETTNTARALQNYPGGLQFPVLDTSLMKRYLDFLEAKG' patterns), a condensation (C) domain with 'HHxxxDG' motif, and a terminal reductase (R) domain with NAD(P)-binding 'GxGxxG' pattern. NRPS enzymes are by definition dedicated to secondary metabolite (e.g., antibiotic, immunosuppressant, siderophore) biosynthesis and are never involved in primary amino acid biosynthesis. The distractors (threonine, valine, methionine biosynthesis) are primary metabolic pathways catalyzed by small monofunctional enzymes (~200-400 aa), incompatible with a 1024-aa multi-domain NRPS.


**Missing item-specific fact**

> None required. Recognition of NRPS domain architecture from sequence motifs and the general biological principle that NRPS enzymes produce secondary metabolites is sufficient to select B over the primary amino acid biosynthesis distractors.


**Reason**

> A model with knowledge of NRPS domain signatures (PCP 'GGSC' serine, C-domain 'HHxxxDG', A-domain core motifs, terminal reductase) can identify the protein as a non-ribosomal peptide synthetase from the sequence alone. The fundamental biological fact that NRPS enzymes exclusively participate in secondary metabolite biosynthesis—not primary amino acid metabolism—allows elimination of all three distractors without needing to know the specific FR901483 pathway or the protein's exact name.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The NRPS architecture is unambiguous and incompatible with primary amino acid biosynthesis pathways (A, C, D). Only option B (Secondary metabolite biosynthesis) is consistent with a multi-domain NRPS enzyme. No other choice is defensible.


### Important caveats

- The UniProt annotation carries experimental evidence (ECO:0000269, direct assay from PubMed:33372776), not merely computational inference.
- The entry was first public in June 2025; the author's source snapshot date is unknown, though the sequence has been stable since 2021.
- The term 'non-canonical' in the protein name refers to unusual NRPS domain organization (lacking a TE domain, using a reductase instead), not to a different pathway class.
- The question asks for the 'primary pathway'—the UniProt pathway comment states 'Secondary metabolite biosynthesis' without further specificity, matching option B verbatim.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 1024-aa sequence exhibits unmistakable multi-domain NRPS architecture: a PCP domain with the conserved 'GGSC' phosphopantetheinylation serine motif, adenylation (A) domain signatures (including 'GGxxxDG' and 'GELWIGGPGVSPGYFRQPEKNLAAFSDLGEAMTSLENPVRFYRTGDIVRRRPNGALEYVGRRDHQVKVRGFRIELEAVEAGLLKTGLFSDAVAMRIEMPQNGAGSILAAYVVPTDVSKPPTMDEALESAKSILPHYMVPQLELVPRLPLNRHLKVDRKQLAELFGRRWEDVSPAQPENASQDVRSALVSLWATVLASPLSTYGDDDDFLHLGGTSLQAAMLINQIRHKFDIEVSLLTLYDNTTLGALTSIIKQRLSGQSETLHNEKDSWVADSEIADDLSCPLDRPIDWCRDTEGRVFLTGGTGFVGAFLLADLLHMPQTSQVRCLVRATDAAVGQERLRAALDKYGLWEDGFADKLVAIAGLLEDDYLGMGREQFEEAASWASVVFHLGARVNYAQPYSLHRASNTLGTRNMVRFACAGRTKAIHYVSSIGCFGPTGSILGTTSVREDEPLLPHITALPYDHGYAQSQWVADALLRRLMDRGFPIAIYRPGFIVGHSQTGACNPDDFLSRLIDACREIGCYPQLPNQRKEFVPVDYVNAAILHIAASPASLGHAYHIVPPTRAVSIDMDNSMALVDRAGNSPMRPVSYKEWVERLAATSPKRLLPLQPMLAERVKDGLTRWELYENMPVYETTNTARALQNYPGGLQFPVLDTSLMKRYLDFLEAKG' patterns), a condensation (C) domain with 'HHxxxDG' motif, and a terminal reductase (R) domain with NAD(P)-binding 'GxGxxG' pattern. NRPS enzymes are by definition dedicated to secondary metabolite (e.g., antibiotic, immunosuppressant, siderophore) biosynthesis and are never involved in primary amino acid biosynthesis. The distractors (threonine, valine, methionine biosynthesis) are primary metabolic pathways catalyzed by small monofunctional enzymes (~200-400 aa), incompatible with a 1024-aa multi-domain NRPS.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. Recognition of NRPS domain architecture from sequence motifs and the general biological principle that NRPS enzymes produce secondary metabolites is sufficient to select B over the primary amino acid biosynthesis distractors.",
    "reason": "A model with knowledge of NRPS domain signatures (PCP 'GGSC' serine, C-domain 'HHxxxDG', A-domain core motifs, terminal reductase) can identify the protein as a non-ribosomal peptide synthetase from the sequence alone. The fundamental biological fact that NRPS enzymes exclusively participate in secondary metabolite biosynthesis—not primary amino acid metabolism—allows elimination of all three distractors without needing to know the specific FR901483 pathway or the protein's exact name."
  },
  "case_id": "pathway_0025",
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
    "reason": "UniProt entry A0A7T8F1L4 annotates this protein as 'Non-canonical nonribosomal peptide synthetase FrzA' (EC 1.2.1.101) with pathway 'Secondary metabolite biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:33372776). The protein is part of the FR901483 immunosuppressant biosynthesis cluster in Cladobotryum sp., a fungal secondary metabolite. The sequence matches exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269, direct assay from PubMed:33372776), not merely computational inference.",
    "The entry was first public in June 2025; the author's source snapshot date is unknown, though the sequence has been stable since 2021.",
    "The term 'non-canonical' in the protein name refers to unusual NRPS domain organization (lacking a TE domain, using a reductase instead), not to a different pathway class.",
    "The question asks for the 'primary pathway'—the UniProt pathway comment states 'Secondary metabolite biosynthesis' without further specificity, matching option B verbatim."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The NRPS architecture is unambiguous and incompatible with primary amino acid biosynthesis pathways (A, C, D). Only option B (Secondary metabolite biosynthesis) is consistent with a multi-domain NRPS enzyme. No other choice is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8F1L4 annotates this protein as 'Non-canonical nonribosomal peptide synthetase FrzA' (EC 1.2.1.101) with pathway 'Secondary metabolite biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:33372776). The protein is part of the FR901483 immunosuppressant biosynthesis cluster in Cladobotryum sp., a fungal secondary metabolite. The sequence matches exactly (SHA-256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 1024-aa sequence exhibits unmistakable multi-domain NRPS architecture: a PCP domain with the conserved 'GGSC' phosphopantetheinylation serine motif, adenylation (A) domain signatures (including 'GGxxxDG' and 'GELWIGGPGVSPGYFRQPEKNLAAFSDLGEAMTSLENPVRFYRTGDIVRRRPNGALEYVGRRDHQVKVRGFRIELEAVEAGLLKTGLFSDAVAMRIEMPQNGAGSILAAYVVPTDVSKPPTMDEALESAKSILPHYMVPQLELVPRLPLNRHLKVDRKQLAELFGRRWEDVSPAQPENASQDVRSALVSLWATVLASPLSTYGDDDDFLHLGGTSLQAAMLINQIRHKFDIEVSLLTLYDNTTLGALTSIIKQRLSGQSETLHNEKDSWVADSEIADDLSCPLDRPIDWCRDTEGRVFLTGGTGFVGAFLLADLLHMPQTSQVRCLVRATDAAVGQERLRAALDKYGLWEDGFADKLVAIAGLLEDDYLGMGREQFEEAASWASVVFHLGARVNYAQPYSLHRASNTLGTRNMVRFACAGRTKAIHYVSSIGCFGPTGSILGTTSVREDEPLLPHITALPYDHGYAQSQWVADALLRRLMDRGFPIAIYRPGFIVGHSQTGACNPDDFLSRLIDACREIGCYPQLPNQRKEFVPVDYVNAAILHIAASPASLGHAYHIVPPTRAVSIDMDNSMALVDRAGNSPMRPVSYKEWVERLAATSPKRLLPLQPMLAERVKDGLTRWELYENMPVYETTNTARALQNYPGGLQFPVLDTSLMKRYLDFLEAKG' patterns), a condensation (C) domain with 'HHxxxDG' motif, and a terminal reductase (R) domain with NAD(P)-binding 'GxGxxG' pattern. NRPS enzymes are by definition dedicated to secondary metabolite (e.g., antibiotic, immunosuppressant, siderophore) biosynthesis and are never involved in primary amino acid biosynthesis. The distractors (threonine, valine, methionine biosynthesis) are primary metabolic pathways catalyzed by small monofunctional enzymes (~200-400 aa), incompatible with a 1024-aa multi-domain NRPS.",
    "missing_item_specific_fact": "None required. Recognition of NRPS domain architecture from sequence motifs and the general biological principle that NRPS enzymes produce secondary metabolites is sufficient to select B over the primary amino acid biosynthesis distractors.",
    "reason": "A model with knowledge of NRPS domain signatures (PCP 'GGSC' serine, C-domain 'HHxxxDG', A-domain core motifs, terminal reductase) can identify the protein as a non-ribosomal peptide synthetase from the sequence alone. The fundamental biological fact that NRPS enzymes exclusively participate in secondary metabolite biosynthesis—not primary amino acid metabolism—allows elimination of all three distractors without needing to know the specific FR901483 pathway or the protein's exact name."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The NRPS architecture is unambiguous and incompatible with primary amino acid biosynthesis pathways (A, C, D). Only option B (Secondary metabolite biosynthesis) is consistent with a multi-domain NRPS enzyme. No other choice is defensible."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269, direct assay from PubMed:33372776), not merely computational inference.",
    "The entry was first public in June 2025; the author's source snapshot date is unknown, though the sequence has been stable since 2021.",
    "The term 'non-canonical' in the protein name refers to unusual NRPS domain organization (lacking a TE domain, using a reductase instead), not to a different pathway class.",
    "The question asks for the 'primary pathway'—the UniProt pathway comment states 'Secondary metabolite biosynthesis' without further specificity, matching option B verbatim."
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

**Accession:** `A0A7T8F1L4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 18. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:48.509506+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"FR901483 biosynthesis cluster protein A"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"1.2.1.101"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33372776","source":"PubMed"}],"value":"Non-canonical nonribosomal peptide synthetase FrzA"}}}
```

Source SHA-256: `4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:48.509506+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"33372776","source":"PubMed"}],"value":"Secondary metabolite biosynthesis"}]}
```

Source SHA-256: `4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:48.509506+00:00.  

```json
{"citation":{"authors":["Zhang Z.","Tamura Y.","Tang M.","Qiao T.","Sato M.","Otsu Y.","Sasamura S.","Taniguchi M.","Watanabe K.","Tang Y."],"citationCrossReferences":[{"database":"PubMed","id":"33372776"},{"database":"DOI","id":"10.1021/jacs.0c12352"}],"citationType":"journal article","firstPage":"132","id":"33372776","journal":"J. Am. Chem. Soc.","lastPage":"136","publicationDate":"2021","title":"Biosynthesis of the Immunosuppressant (-)-FR901483.","volume":"143"},"referenceComments":[{"type":"STRAIN","value":"11231"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","PATHWAY"]}
```

Source SHA-256: `4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:50.375049+00:00.  

```text
ID   FRZA_CLASX              Reviewed;        1024 AA.
AC   A0A7T8F1L4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   02-JUN-2021, sequence version 1.
DT   28-JAN-2026, entry version 18.
DE   RecName: Full=Non-canonical nonribosomal peptide synthetase FrzA {ECO:0000303|PubMed:33372776};
DE            EC=1.2.1.101 {ECO:0000269|PubMed:33372776};
DE   AltName: Full=FR901483 biosynthesis cluster protein A {ECO:0000303|PubMed:33372776};
GN   Name=FrzA {ECO:0000303|PubMed:33372776};
OS   Cladobotryum sp.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.
OX   NCBI_TaxID=2040732;
```

Source SHA-256: `dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)  
**Locator:** `lines 14-22`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:50.375049+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND
RP   PATHWAY.
RC   STRAIN=11231;
RX   PubMed=33372776; DOI=10.1021/jacs.0c12352;
RA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,
RA   Taniguchi M., Watanabe K., Tang Y.;
RT   "Biosynthesis of the Immunosuppressant (-)-FR901483.";
RL   J. Am. Chem. Soc. 143:132-136(2021).
```

Source SHA-256: `dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)  
**Locator:** `lines 65-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 18 / 1.  
**Retrieved:** 2026-11-02T04:25:50.375049+00:00.  

```text
CC   -!- PATHWAY: Secondary metabolite biosynthesis.
CC       {ECO:0000269|PubMed:33372776}.
```

Source SHA-256: `dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
