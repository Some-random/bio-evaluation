# active_site_0118

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0118.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 558 (For beta-ketoacyl synthase activity)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVNIYIFGDQTVRVDDAVHKLLHVKNNPILKSFLDGSFAAIRKQIFLLPANERTSLPDAHTLPLLLEAVRRGRRHVALESALVCLCEIGQYIALLQTTDLCHPPTGSILVGFCTGSLAAAAVSCVRTSIDLLTLGIEAVVVAFRVGMHVARRANALGGDGGSQWKPWSLAVTDGSESETEKILEEFTRDEVSGVHVANRHDAYILAKGLPAIMKPYVSAAGSNTLTISGTPRVLEALKASPHLRGTKSLPVSIYAPYHAAHLYNEADVESIFACKPVESALFHRELRTPLISCATGTVLKEKTFGDLLRALVMEILTCQIRFDKVEESIVQHTPGATAQLIPIHTNIAPRMKTSLTQVGLQVECFKAIANQEPAAEALSESPSNDSSKIAIIGFSGRFPEADGLNEFWELLQQGLDVHKPIPADRFDLEAHYDATLREKNTSRIKHGCWIRSPGSFDARFFQMSPREACQTDPAQRLALLTAYEAMEMAGFVPDRTPSSQRDRVGVYYGMTSDDWREVNSSQDIDTYFIPGGIRAFVPGRINYFFKFSGPSITVDTACSSSLAAIHTACNALLNSDCDTALAGGTNILTNPDNFAGLDRGHFLSSTGNCKTFDDDADGYCRADGVGTVILKRLQDAIADNDPIFGVIVGARTSHSAEAVSITRPLADAQAHLFRKLLAESGIHPHEISYIEMHGTGTQAGDAVEMKSVLDSFARDDSRAPDRPLHLGSVKANVGHGESASGVTALIKVLLMMQKNRIPPHCGIKGRINRHFPTDMEYRNVHIPFMETDWTRPQEGKRRSFINNFSAAGGNTAVLVEDAPLLEQSRAISSPDPQRYHVITLSARSVRSLSKNMRALGEFIGSETSPGLLARIAYTTTARRMHHSYRVAFVGNDLQEVKRRFLDTDVTEAIKPCPTKSPGVGFLFTGQGAQQTAMARELYDRFTSFRADILEFEAVGRGHGFPSILPLITGAVDVEELSPMIVQLGTVVIQIAMARLWQTWGLTPEYALGHSLGEYAALQIAGVLSISDTIYLAGSRAALLEKRCTAGSHGMLAVKASVAHLEEALKGMQVEVSCINGFDDTVLSGTNDEIDRASKELSELKVTFKRLILPFAFHSSQVDPILEELEHIASQLSFQPPRIPIVSPTVGHIITDEGTIGAQYIRRHCREPVNFLGAIQAAQGSGICNSGALAVEIGAHPILTRMMKAAVGSSVTVCSTLSHREDMFKTLTESLSVLHLAGVRLNWDEYHRDFNNQVVMLPAYSWDYQDYWIQYQNNFCLTKGSPERSESVDAIQPMSTRLSPSVQKILEEEMTAAQASIIIESDITDPELLPVALDHKVNGVTLCPSSLYADIGHTLGTYLLGKKEDVTDYKIDVSNMAVEKALVVKGTGPQLFRASLDMDWNMLRGMMKVYSVNNMGTLTTHHAQCTIELQRPHQWQEGWNRQLYLIQRSIEQLKKGVEEGWTHKMRRGVAYRLFSSMMQYGPSYQAMEEVIFDSSGLEATAQVRLQSTTGRYSFNPVWSDSLGHITGFVTNCNDSIDLTENLFVNHGWGFMRCVEPFSPDTVYQTHVKMQPVDGNNGFYVGDVYVLNDHRIIAQYGAVTFQKVARRVLEMLLPATTSKGRSSNIRPRNVGTAQSAKIVQSKRRTQTPHVEDAWQQVLEMIARELGVDPGQLTEDVNFTDMGVDSLMSLTIIGNFREFLSLDVPWSLFEDCPSVQSLRIYLNMSSLSESDSIETSSYPTPDESTTTTITSPSGSDRNVGRNSGIDGVGTTVGLVLSILAEEIGVNVRDLSNADGLSELGLDSLLSITALGRVRDETDLDLPSDFFLEHSSVAAITAALHAIFGSTEQGPEQSLITSHPPAMSINLQGDEGCPQTLFLFPDGSGSSTSYSALPTISKDVRVYAMDCPYLKRPNELAKCQLQDLTPVYVAEIRRRQLRGPYSLGGWSAGGIAAYEAAQYLVDQGERVERLILIDSPNPMGLGKCPPHFYRFLEEAGVFGVHGGRKPPAWLLQHFQAFNDVLSQYTLEPFRPADATPNTTLIYAQDGVCKSPRDPRPERHPGDPEVFSWLLENRVDMSCNGWDQLLGEDNIHLGTVFDANHFTIVRTPAVVRLSEIVRMAMSRKFQ

[Multiple Choices]
A. Position 109 (Nucleophile)
B. Position 93 (Proton donor)
C. Position 558 (For beta-ketoacyl synthase activity)
D. Position 324 (Proton acceptor)
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

> The sequence-matched UniProt annotation identifies position 558 as an active-site residue for beta-ketoacyl synthase activity. This is computational PROSITE-ProRule evidence, not direct experimental validation. The record also annotates positions 693 and 735 for that activity, but neither is an offered choice.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 2121-residue sequence has the architecture and conserved features of a large polyketide synthase. In this enzyme family, the beta-ketoacyl synthase domain uses conserved catalytic residues, including a nucleophilic cysteine; the sequence contains a cysteine-containing motif consistent with that role near the region represented by position 558. Choice C explicitly identifies beta-ketoacyl synthase activity, distinguishing it from the alternatives’ unrelated positions and labels.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level knowledge of polyketide synthases and their conserved catalytic machinery provides a meaningful basis for preferring C from the sequence and choices. It does not independently establish every residue annotation or experimental activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C among the offered choices matches the beta-ketoacyl synthase active-site inference. The annotation lists additional residues for that activity, but those positions are not offered.


### Important caveats

- The supporting active-site annotation is rule-based computational evidence; the supplied excerpts do not establish direct experimental validation of position 558.
- The prompt’s wording may suggest a complete catalytic center, whereas choice C gives one residue and the source annotates other beta-ketoacyl synthase residues as well.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 2121-residue sequence has the architecture and conserved features of a large polyketide synthase. In this enzyme family, the beta-ketoacyl synthase domain uses conserved catalytic residues, including a nucleophilic cysteine; the sequence contains a cysteine-containing motif consistent with that role near the region represented by position 558. Choice C explicitly identifies beta-ketoacyl synthase activity, distinguishing it from the alternatives’ unrelated positions and labels.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of polyketide synthases and their conserved catalytic machinery provides a meaningful basis for preferring C from the sequence and choices. It does not independently establish every residue annotation or experimental activity."
  },
  "case_id": "active_site_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 558 as an active-site residue for beta-ketoacyl synthase activity. This is computational PROSITE-ProRule evidence, not direct experimental validation. The record also annotates positions 693 and 735 for that activity, but neither is an offered choice."
  },
  "important_caveats": [
    "The supporting active-site annotation is rule-based computational evidence; the supplied excerpts do not establish direct experimental validation of position 558.",
    "The prompt’s wording may suggest a complete catalytic center, whereas choice C gives one residue and the source annotates other beta-ketoacyl synthase residues as well."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the offered choices matches the beta-ketoacyl synthase active-site inference. The annotation lists additional residues for that activity, but those positions are not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 558 as an active-site residue for beta-ketoacyl synthase activity. This is computational PROSITE-ProRule evidence, not direct experimental validation. The record also annotates positions 693 and 735 for that activity, but neither is an offered choice.",
    "evidence_ids": ["C5", "H3", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 2121-residue sequence has the architecture and conserved features of a large polyketide synthase. In this enzyme family, the beta-ketoacyl synthase domain uses conserved catalytic residues, including a nucleophilic cysteine; the sequence contains a cysteine-containing motif consistent with that role near the region represented by position 558. Choice C explicitly identifies beta-ketoacyl synthase activity, distinguishing it from the alternatives’ unrelated positions and labels.",
    "missing_item_specific_fact": "",
    "reason": "Family-level knowledge of polyketide synthases and their conserved catalytic machinery provides a meaningful basis for preferring C from the sequence and choices. It does not independently establish every residue annotation or experimental activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the offered choices matches the beta-ketoacyl synthase active-site inference. The annotation lists additional residues for that activity, but those positions are not offered."
  },
  "important_caveats": [
    "The supporting active-site annotation is rule-based computational evidence; the supplied excerpts do not establish direct experimental validation of position 558.",
    "The prompt’s wording may suggest a complete catalytic center, whereas choice C gives one residue and the source annotates other beta-ketoacyl synthase residues as well."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q2TXQ8, Non-reducing polyketide synthase aoiG from Aspergillus oryzae) annotates position 558 as an Active site with description 'For beta-ketoacyl synthase activity' (evidence ECO:0000255, PROSITE-ProRule PRU01348). The sequence at position 558 is Cysteine, consistent with the KS-domain catalytic nucleophile. The annotation is computational (PROSITE pattern-based), not direct experimental evidence, but it is the recorded annotation that the author key reproduces verbatim. The other options (positions 109, 93, 324) are not annotated as active sites in this entry.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can verify the amino acid identity at each proposed position directly from the supplied 2121-AA sequence: position 558 is Cys, position 109 is Leu, position 93 is Ala, and position 324 is Lys. General enzyme chemistry immediately eliminates Leu (option A, 'Nucleophile') and Ala (option B, 'Proton donor') as catalytic residues—neither possesses a reactive side chain capable of nucleophilic attack or proton donation. The protein's large size (~2121 AA) and the presence of a GxSxG motif near position 393 are hallmarks of a modular polyketide/fatty-acid synthase architecture. In KS (ketoacyl synthase) domains of PKS/FAS, the catalytic residue is a well-conserved Cysteine that forms a thioester intermediate; recognizing position 558 as Cys in a KS-like context matches the 'beta-ketoacyl synthase activity' label in option C. For option D, Lys at position 324 is not the canonical proton acceptor in PKS/FAS dehydratase domains (which use His/Asp triads), making it a weaker fit. Thus, amino-acid chemistry plus transferable PKS/FAS domain knowledge meaningfully distinguishes C from A, B, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The model can check residue identity at each position from the sequence and apply general knowledge of catalytic residue chemistry (Leu/Ala are not catalytic; Cys is the KS nucleophile; Lys is not the standard dehydratase proton acceptor in PKS/FAS). No target-specific database lookup is strictly required to eliminate the clearly wrong options and select C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (Leu as nucleophile) and B (Ala as proton donor) are eliminated by basic amino-acid chemistry. Option D (Lys as proton acceptor) is a weak distractor but does not match the canonical PKS/FAS dehydratase chemistry. Option C (Cys for beta-ketoacyl synthase) is the only chemically and structurally consistent choice.


### Important caveats

- The UniProt annotation for position 558 is based on PROSITE-ProRule PRU01348 (computational/pattern-based, ECO:0000255), not direct experimental mutagenesis or structural data. The evidence supports the annotation as recorded but does not constitute independent experimental proof of catalysis at that residue in this specific protein.
- The NR-PKS has multiple annotated active sites (positions 558, 693, 735 for KS; 1334 for dehydratase proton acceptor; 1519 for dehydratase proton donor). The question asks for 'the catalytic center' (singular) and offers only one correct choice, which is acceptable for a single-answer MCQ.
- The protein identity (Non-reducing PKS aoiG, Aspergillus oryzae) is not stated in the model input; the model must infer the enzyme class from sequence features (size, GxSxG motif, domain architecture). This is permitted transferable knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can verify the amino acid identity at each proposed position directly from the supplied 2121-AA sequence: position 558 is Cys, position 109 is Leu, position 93 is Ala, and position 324 is Lys. General enzyme chemistry immediately eliminates Leu (option A, 'Nucleophile') and Ala (option B, 'Proton donor') as catalytic residues—neither possesses a reactive side chain capable of nucleophilic attack or proton donation. The protein's large size (~2121 AA) and the presence of a GxSxG motif near position 393 are hallmarks of a modular polyketide/fatty-acid synthase architecture. In KS (ketoacyl synthase) domains of PKS/FAS, the catalytic residue is a well-conserved Cysteine that forms a thioester intermediate; recognizing position 558 as Cys in a KS-like context matches the 'beta-ketoacyl synthase activity' label in option C. For option D, Lys at position 324 is not the canonical proton acceptor in PKS/FAS dehydratase domains (which use His/Asp triads), making it a weaker fit. Thus, amino-acid chemistry plus transferable PKS/FAS domain knowledge meaningfully distinguishes C from A, B, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The model can check residue identity at each position from the sequence and apply general knowledge of catalytic residue chemistry (Leu/Ala are not catalytic; Cys is the KS nucleophile; Lys is not the standard dehydratase proton acceptor in PKS/FAS). No target-specific database lookup is strictly required to eliminate the clearly wrong options and select C."
  },
  "case_id": "active_site_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q2TXQ8, Non-reducing polyketide synthase aoiG from Aspergillus oryzae) annotates position 558 as an Active site with description 'For beta-ketoacyl synthase activity' (evidence ECO:0000255, PROSITE-ProRule PRU01348). The sequence at position 558 is Cysteine, consistent with the KS-domain catalytic nucleophile. The annotation is computational (PROSITE pattern-based), not direct experimental evidence, but it is the recorded annotation that the author key reproduces verbatim. The other options (positions 109, 93, 324) are not annotated as active sites in this entry."
  },
  "important_caveats": [
    "The UniProt annotation for position 558 is based on PROSITE-ProRule PRU01348 (computational/pattern-based, ECO:0000255), not direct experimental mutagenesis or structural data. The evidence supports the annotation as recorded but does not constitute independent experimental proof of catalysis at that residue in this specific protein.",
    "The NR-PKS has multiple annotated active sites (positions 558, 693, 735 for KS; 1334 for dehydratase proton acceptor; 1519 for dehydratase proton donor). The question asks for 'the catalytic center' (singular) and offers only one correct choice, which is acceptable for a single-answer MCQ.",
    "The protein identity (Non-reducing PKS aoiG, Aspergillus oryzae) is not stated in the model input; the model must infer the enzyme class from sequence features (size, GxSxG motif, domain architecture). This is permitted transferable knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (Leu as nucleophile) and B (Ala as proton donor) are eliminated by basic amino-acid chemistry. Option D (Lys as proton acceptor) is a weak distractor but does not match the canonical PKS/FAS dehydratase chemistry. Option C (Cys for beta-ketoacyl synthase) is the only chemically and structurally consistent choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q2TXQ8, Non-reducing polyketide synthase aoiG from Aspergillus oryzae) annotates position 558 as an Active site with description 'For beta-ketoacyl synthase activity' (evidence ECO:0000255, PROSITE-ProRule PRU01348). The sequence at position 558 is Cysteine, consistent with the KS-domain catalytic nucleophile. The annotation is computational (PROSITE pattern-based), not direct experimental evidence, but it is the recorded annotation that the author key reproduces verbatim. The other options (positions 109, 93, 324) are not annotated as active sites in this entry.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can verify the amino acid identity at each proposed position directly from the supplied 2121-AA sequence: position 558 is Cys, position 109 is Leu, position 93 is Ala, and position 324 is Lys. General enzyme chemistry immediately eliminates Leu (option A, 'Nucleophile') and Ala (option B, 'Proton donor') as catalytic residues—neither possesses a reactive side chain capable of nucleophilic attack or proton donation. The protein's large size (~2121 AA) and the presence of a GxSxG motif near position 393 are hallmarks of a modular polyketide/fatty-acid synthase architecture. In KS (ketoacyl synthase) domains of PKS/FAS, the catalytic residue is a well-conserved Cysteine that forms a thioester intermediate; recognizing position 558 as Cys in a KS-like context matches the 'beta-ketoacyl synthase activity' label in option C. For option D, Lys at position 324 is not the canonical proton acceptor in PKS/FAS dehydratase domains (which use His/Asp triads), making it a weaker fit. Thus, amino-acid chemistry plus transferable PKS/FAS domain knowledge meaningfully distinguishes C from A, B, and D.",
    "missing_item_specific_fact": "",
    "reason": "The model can check residue identity at each position from the sequence and apply general knowledge of catalytic residue chemistry (Leu/Ala are not catalytic; Cys is the KS nucleophile; Lys is not the standard dehydratase proton acceptor in PKS/FAS). No target-specific database lookup is strictly required to eliminate the clearly wrong options and select C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (Leu as nucleophile) and B (Ala as proton donor) are eliminated by basic amino-acid chemistry. Option D (Lys as proton acceptor) is a weak distractor but does not match the canonical PKS/FAS dehydratase chemistry. Option C (Cys for beta-ketoacyl synthase) is the only chemically and structurally consistent choice."
  },
  "important_caveats": [
    "The UniProt annotation for position 558 is based on PROSITE-ProRule PRU01348 (computational/pattern-based, ECO:0000255), not direct experimental mutagenesis or structural data. The evidence supports the annotation as recorded but does not constitute independent experimental proof of catalysis at that residue in this specific protein.",
    "The NR-PKS has multiple annotated active sites (positions 558, 693, 735 for KS; 1334 for dehydratase proton acceptor; 1519 for dehydratase proton donor). The question asks for 'the catalytic center' (singular) and offers only one correct choice, which is acceptable for a single-answer MCQ.",
    "The protein identity (Non-reducing PKS aoiG, Aspergillus oryzae) is not stated in the model input; the model must infer the enzyme class from sequence features (size, GxSxG motif, domain architecture). This is permitted transferable knowledge."
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
  "benchmark_sequence_length": 2121,
  "benchmark_sequence_sha256": "76b2331851b384dacd64975284637f2321c70245db127da1fdb2db4370c8e5af",
  "current_entry_audit": {
    "entryVersion": 124,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-01-24",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 2121,
  "current_source_sequence_sha256": "76b2331851b384dacd64975284637f2321c70245db127da1fdb2db4370c8e5af",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 122,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q2TXQ8",
  "selected_historical_entry_version": 122,
  "selected_historical_record_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "selected_historical_source_sequence_length": 2121,
  "selected_historical_source_sequence_sha256": "76b2331851b384dacd64975284637f2321c70245db127da1fdb2db4370c8e5af",
  "selected_historical_version": {
    "accession": "Q2TXQ8",
    "database": "Swiss-Prot",
    "entryVersion": 122,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AOIG_ASPOR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q2TXQ8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":124,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-01-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yellow koji mold\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus oryzae (strain ATCC 42149 / RIB 40)\",\"taxonId\":510516}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22447538\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22447538\",\"source\":\"PubMed\"}],\"value\":\"Non-reducing polyketide synthase aoiG\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":558},\"start\":{\"modifier\":\"EXACT\",\"value\":558}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":693},\"start\":{\"modifier\":\"EXACT\",\"value\":693}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":735},\"start\":{\"modifier\":\"EXACT\",\"value\":735}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Proton acceptor; for dehydratase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01363\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1334},\"start\":{\"modifier\":\"EXACT\",\"value\":1334}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Proton donor; for dehydratase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01363\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1519},\"start\":{\"modifier\":\"EXACT\",\"value\":1519}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Nakazawa T.\",\"Ishiuchi K.\",\"Praseuth A.\",\"Noguchi H.\",\"Hotta K.\",\"Watanabe K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22447538\"},{\"database\":\"DOI\",\"id\":\"10.1002/cbic.201200107\"}],\"citationType\":\"journal article\",\"firstPage\":\"855\",\"id\":\"22447538\",\"journal\":\"ChemBioChem\",\"lastPage\":\"861\",\"publicationDate\":\"2012\",\"title\":\"Overexpressing transcriptional regulator in Aspergillus oryzae activates a silent biosynthetic pathway to produce a novel polyketide.\",\"volume\":\"13\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"DOMAIN\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H1",
  "excerpt": "ID   AOIG_ASPOR              Reviewed;        2121 AA.\nAC   Q2TXQ8;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JAN-2006, sequence version 1.\nDT   28-JAN-2026, entry version 122.\nDE   RecName: Full=Non-reducing polyketide synthase aoiG {ECO:0000303|PubMed:22447538};\nDE            EC=2.3.1.- {ECO:0000269|PubMed:22447538};\nGN   Name=aoiG {ECO:0000303|PubMed:22447538}; ORFNames=AO090010000048;\nOS   Aspergillus oryzae (strain ATCC 42149 / RIB 40) (Yellow koji mold).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=510516;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:44.949915+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, DOMAIN, AND INDUCTION.\nRX   PubMed=22447538; DOI=10.1002/cbic.201200107;\nRA   Nakazawa T., Ishiuchi K., Praseuth A., Noguchi H., Hotta K., Watanabe K.;\nRT   \"Overexpressing transcriptional regulator in Aspergillus oryzae activates a\nRT   silent biosynthetic pathway to produce a novel polyketide.\";\nRL   ChemBioChem 13:855-861(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:44.949915+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        558\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:44.949915+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 186-188",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        693\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:44.949915+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 189-191",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H5",
  "excerpt": "FT   ACT_SITE        735\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:44.949915+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 192-194",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H6",
  "excerpt": "FT   ACT_SITE        1334\nFT                   /note=\"Proton acceptor; for dehydratase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01363\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:44.949915+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 195-197",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H7",
  "excerpt": "FT   ACT_SITE        1519\nFT                   /note=\"Proton donor; for dehydratase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01363\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:44.949915+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 198-200",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 118. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
