# active_site_0118: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/active_site_0118.txt)

**Task:** `active_site`  
**Author key, unchanged:** **C** — Position 558 (For beta-ketoacyl synthase activity)

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches the annotated 2,121-residue protein, and both current and pre-cutoff UniProt records annotate position 558 as an active site for beta-ketoacyl synthase activity. This is PROSITE-ProRule computational annotation, not evidence of direct experimental validation.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence and choices may suggest a multidomain polyketide synthase, but general knowledge does not establish that this particular residue at position 558 has the stated role.


**Missing item-specific fact**

> The protein-specific mapping of residue 558 to the beta-ketoacyl synthase active site, supplied here by a PROSITE-ProRule annotation.


**Reason**

> Selecting the exact numbered residue and its function requires a protein-specific annotation or equivalent external analysis; recognizing the protein or relying on general catalytic-residue heuristics is not enough.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied matching annotation supports option C among the listed choices. Other active-site annotations exist at positions not offered, but they do not make another listed option defensible.


### Important caveats

- The matching historical record also annotates positions 693 and 735 for beta-ketoacyl synthase activity; option C is one supported residue, not an exhaustive active-site list.
- The author’s exact source snapshot is unknown, although the sequence matches the checked historical record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence and choices may suggest a multidomain polyketide synthase, but general knowledge does not establish that this particular residue at position 558 has the stated role.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific mapping of residue 558 to the beta-ketoacyl synthase active site, supplied here by a PROSITE-ProRule annotation.",
    "reason": "Selecting the exact numbered residue and its function requires a protein-specific annotation or equivalent external analysis; recognizing the protein or relying on general catalytic-residue heuristics is not enough."
  },
  "case_id": "active_site_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the annotated 2,121-residue protein, and both current and pre-cutoff UniProt records annotate position 558 as an active site for beta-ketoacyl synthase activity. This is PROSITE-ProRule computational annotation, not evidence of direct experimental validation."
  },
  "important_caveats": [
    "The matching historical record also annotates positions 693 and 735 for beta-ketoacyl synthase activity; option C is one supported residue, not an exhaustive active-site list.",
    "The author’s exact source snapshot is unknown, although the sequence matches the checked historical record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied matching annotation supports option C among the listed choices. Other active-site annotations exist at positions not offered, but they do not make another listed option defensible."
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
    "reason": "The sequence exactly matches the annotated 2,121-residue protein, and both current and pre-cutoff UniProt records annotate position 558 as an active site for beta-ketoacyl synthase activity. This is PROSITE-ProRule computational annotation, not evidence of direct experimental validation.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence and choices may suggest a multidomain polyketide synthase, but general knowledge does not establish that this particular residue at position 558 has the stated role.",
    "missing_item_specific_fact": "The protein-specific mapping of residue 558 to the beta-ketoacyl synthase active site, supplied here by a PROSITE-ProRule annotation.",
    "reason": "Selecting the exact numbered residue and its function requires a protein-specific annotation or equivalent external analysis; recognizing the protein or relying on general catalytic-residue heuristics is not enough."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied matching annotation supports option C among the listed choices. Other active-site annotations exist at positions not offered, but they do not make another listed option defensible."
  },
  "important_caveats": [
    "The matching historical record also annotates positions 693 and 735 for beta-ketoacyl synthase activity; option C is one supported residue, not an exhaustive active-site list.",
    "The author’s exact source snapshot is unknown, although the sequence matches the checked historical record."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q2TXQ8 (Non-reducing polyketide synthase aoiG, Aspergillus oryzae) annotates position 558 as an active site 'For beta-ketoacyl synthase activity' (evidence C5, H3). The annotation is based on PROSITE-ProRule PRU01348 (ECO:0000255), a computational profile-based assignment, but the protein's overall function as a polyketide synthase is experimentally supported (PubMed 22447538, ECO:0000269). The sequence matches exactly. The distractor positions (93, 109, 324) do not correspond to any annotated active sites in this entry; the actual proton donor is at 1519 and proton acceptor at 1334.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C10](#evidence-c10).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A knowledgeable person might recognize the sequence as a fungal non-reducing polyketide synthase and know that the KS domain contains a catalytic cysteine within a conserved Cys-His-His triad, and that the KS domain typically begins after a short N-terminal region. This could in principle exclude positions 93 and 109 (too early in the sequence for the KS catalytic residue in a 2121-residue PKS). However, distinguishing position 558 from position 324, or confirming 558 specifically, requires precise domain boundary identification or profile matching that cannot be reliably performed by mental inspection of a 2121-residue sequence.


**Missing item-specific fact**

> The exact domain boundaries of the KS domain within this specific 2121-residue protein, or the precise position of the catalytic cysteine within the KS active-site motif, which requires either recognition of this particular protein's database entry or running a domain-prediction/profile tool (e.g., PROSITE, InterProScan).


**Reason**

> While general PKS architecture knowledge provides a weak directional argument (KS domain is not in the extreme N-terminus), the task of selecting position 558 over 324 (or confirming 558 is the catalytic residue) from a raw 2121-residue sequence without computational tools depends on item-specific annotation or sequence recognition. The PROSITE-ProRule assignment itself is computational, and no motif context is provided in the question to enable position-level reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only position 558 matches an annotated active site among the four choices. Positions 93, 109, and 324 are not annotated as active sites in this entry. The functional labels attached to the distractors (Nucleophile at 109, Proton donor at 93, Proton acceptor at 324) do not correspond to any UniProt-annotated features at those positions. The question is unambiguous in that only one choice aligns with the annotation.


### Important caveats

- The active-site assignment at position 558 is based on PROSITE-ProRule (ECO:0000255), a computational profile-based annotation, not direct experimental mutagenesis or structural determination of this specific residue.
- The protein also has active sites at positions 693 and 735 (also for beta-ketoacyl synthase activity) and at 1334/1519 (dehydratase). The question only lists position 558 among the choices, avoiding ambiguity among multiple KS sites.
- The question does not identify the protein or provide domain annotations, making it effectively a sequence-recognition/lookup task for a 2121-residue protein.
- The evidence code ECO:0000269 (experimental) supports the overall enzyme function, but the specific residue-level assignment is ECO:0000255 (computational by rule/profile).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable person might recognize the sequence as a fungal non-reducing polyketide synthase and know that the KS domain contains a catalytic cysteine within a conserved Cys-His-His triad, and that the KS domain typically begins after a short N-terminal region. This could in principle exclude positions 93 and 109 (too early in the sequence for the KS catalytic residue in a 2121-residue PKS). However, distinguishing position 558 from position 324, or confirming 558 specifically, requires precise domain boundary identification or profile matching that cannot be reliably performed by mental inspection of a 2121-residue sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact domain boundaries of the KS domain within this specific 2121-residue protein, or the precise position of the catalytic cysteine within the KS active-site motif, which requires either recognition of this particular protein's database entry or running a domain-prediction/profile tool (e.g., PROSITE, InterProScan).",
    "reason": "While general PKS architecture knowledge provides a weak directional argument (KS domain is not in the extreme N-terminus), the task of selecting position 558 over 324 (or confirming 558 is the catalytic residue) from a raw 2121-residue sequence without computational tools depends on item-specific annotation or sequence recognition. The PROSITE-ProRule assignment itself is computational, and no motif context is provided in the question to enable position-level reasoning."
  },
  "case_id": "active_site_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C10"
    ],
    "judgment": "supported",
    "reason": "UniProt Q2TXQ8 (Non-reducing polyketide synthase aoiG, Aspergillus oryzae) annotates position 558 as an active site 'For beta-ketoacyl synthase activity' (evidence C5, H3). The annotation is based on PROSITE-ProRule PRU01348 (ECO:0000255), a computational profile-based assignment, but the protein's overall function as a polyketide synthase is experimentally supported (PubMed 22447538, ECO:0000269). The sequence matches exactly. The distractor positions (93, 109, 324) do not correspond to any annotated active sites in this entry; the actual proton donor is at 1519 and proton acceptor at 1334."
  },
  "important_caveats": [
    "The active-site assignment at position 558 is based on PROSITE-ProRule (ECO:0000255), a computational profile-based annotation, not direct experimental mutagenesis or structural determination of this specific residue.",
    "The protein also has active sites at positions 693 and 735 (also for beta-ketoacyl synthase activity) and at 1334/1519 (dehydratase). The question only lists position 558 among the choices, avoiding ambiguity among multiple KS sites.",
    "The question does not identify the protein or provide domain annotations, making it effectively a sequence-recognition/lookup task for a 2121-residue protein.",
    "The evidence code ECO:0000269 (experimental) supports the overall enzyme function, but the specific residue-level assignment is ECO:0000255 (computational by rule/profile)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 558 matches an annotated active site among the four choices. Positions 93, 109, and 324 are not annotated as active sites in this entry. The functional labels attached to the distractors (Nucleophile at 109, Proton donor at 93, Proton acceptor at 324) do not correspond to any UniProt-annotated features at those positions. The question is unambiguous in that only one choice aligns with the annotation."
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
    "reason": "UniProt Q2TXQ8 (Non-reducing polyketide synthase aoiG, Aspergillus oryzae) annotates position 558 as an active site 'For beta-ketoacyl synthase activity' (evidence C5, H3). The annotation is based on PROSITE-ProRule PRU01348 (ECO:0000255), a computational profile-based assignment, but the protein's overall function as a polyketide synthase is experimentally supported (PubMed 22447538, ECO:0000269). The sequence matches exactly. The distractor positions (93, 109, 324) do not correspond to any annotated active sites in this entry; the actual proton donor is at 1519 and proton acceptor at 1334.",
    "evidence_ids": ["C5", "H3", "C4", "C10"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A knowledgeable person might recognize the sequence as a fungal non-reducing polyketide synthase and know that the KS domain contains a catalytic cysteine within a conserved Cys-His-His triad, and that the KS domain typically begins after a short N-terminal region. This could in principle exclude positions 93 and 109 (too early in the sequence for the KS catalytic residue in a 2121-residue PKS). However, distinguishing position 558 from position 324, or confirming 558 specifically, requires precise domain boundary identification or profile matching that cannot be reliably performed by mental inspection of a 2121-residue sequence.",
    "missing_item_specific_fact": "The exact domain boundaries of the KS domain within this specific 2121-residue protein, or the precise position of the catalytic cysteine within the KS active-site motif, which requires either recognition of this particular protein's database entry or running a domain-prediction/profile tool (e.g., PROSITE, InterProScan).",
    "reason": "While general PKS architecture knowledge provides a weak directional argument (KS domain is not in the extreme N-terminus), the task of selecting position 558 over 324 (or confirming 558 is the catalytic residue) from a raw 2121-residue sequence without computational tools depends on item-specific annotation or sequence recognition. The PROSITE-ProRule assignment itself is computational, and no motif context is provided in the question to enable position-level reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only position 558 matches an annotated active site among the four choices. Positions 93, 109, and 324 are not annotated as active sites in this entry. The functional labels attached to the distractors (Nucleophile at 109, Proton donor at 93, Proton acceptor at 324) do not correspond to any UniProt-annotated features at those positions. The question is unambiguous in that only one choice aligns with the annotation."
  },
  "important_caveats": [
    "The active-site assignment at position 558 is based on PROSITE-ProRule (ECO:0000255), a computational profile-based annotation, not direct experimental mutagenesis or structural determination of this specific residue.",
    "The protein also has active sites at positions 693 and 735 (also for beta-ketoacyl synthase activity) and at 1334/1519 (dehydratase). The question only lists position 558 among the choices, avoiding ambiguity among multiple KS sites.",
    "The question does not identify the protein or provide domain annotations, making it effectively a sequence-recognition/lookup task for a 2121-residue protein.",
    "The evidence code ECO:0000269 (experimental) supports the overall enzyme function, but the specific residue-level assignment is ECO:0000255 (computational by rule/profile)."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "Q2TXQ8",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "76b2331851b384dacd64975284637f2321c70245db127da1fdb2db4370c8e5af",
  "benchmark_sequence_length": 2121,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 124,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-01-24",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "current_source_sequence_sha256": "76b2331851b384dacd64975284637f2321c70245db127da1fdb2db4370c8e5af",
  "current_source_sequence_length": 2121,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 122,
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
  },
  "selected_historical_record_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "selected_historical_source_sequence_sha256": "76b2331851b384dacd64975284637f2321c70245db127da1fdb2db4370c8e5af",
  "selected_historical_source_sequence_length": 2121,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 122,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q2TXQ8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":124,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-01-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Yellow koji mold\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus oryzae (strain ATCC 42149 / RIB 40)\",\"taxonId\":510516}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22447538\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22447538\",\"source\":\"PubMed\"}],\"value\":\"Non-reducing polyketide synthase aoiG\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "json_pointer": "/features/12",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":558},\"start\":{\"modifier\":\"EXACT\",\"value\":558}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "json_pointer": "/features/13",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":693},\"start\":{\"modifier\":\"EXACT\",\"value\":693}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "json_pointer": "/features/14",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":735},\"start\":{\"modifier\":\"EXACT\",\"value\":735}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "json_pointer": "/features/15",
  "excerpt": "{\"description\":\"Proton acceptor; for dehydratase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01363\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1334},\"start\":{\"modifier\":\"EXACT\",\"value\":1334}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "json_pointer": "/features/16",
  "excerpt": "{\"description\":\"Proton donor; for dehydratase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01363\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1519},\"start\":{\"modifier\":\"EXACT\",\"value\":1519}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ8.json",
  "source_sha256": "b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69",
  "retrieved_utc": "2026-11-02T04:30:41.744302+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Nakazawa T.\",\"Ishiuchi K.\",\"Praseuth A.\",\"Noguchi H.\",\"Hotta K.\",\"Watanabe K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22447538\"},{\"database\":\"DOI\",\"id\":\"10.1002/cbic.201200107\"}],\"citationType\":\"journal article\",\"firstPage\":\"855\",\"id\":\"22447538\",\"journal\":\"ChemBioChem\",\"lastPage\":\"861\",\"publicationDate\":\"2012\",\"title\":\"Overexpressing transcriptional regulator in Aspergillus oryzae activates a silent biosynthetic pathway to produce a novel polyketide.\",\"volume\":\"13\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"DOMAIN\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122",
  "source_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "retrieved_utc": "2026-11-02T04:30:44.949915+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   AOIG_ASPOR              Reviewed;        2121 AA.\nAC   Q2TXQ8;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JAN-2006, sequence version 1.\nDT   28-JAN-2026, entry version 122.\nDE   RecName: Full=Non-reducing polyketide synthase aoiG {ECO:0000303|PubMed:22447538};\nDE            EC=2.3.1.- {ECO:0000269|PubMed:22447538};\nGN   Name=aoiG {ECO:0000303|PubMed:22447538}; ORFNames=AO090010000048;\nOS   Aspergillus oryzae (strain ATCC 42149 / RIB 40) (Yellow koji mold).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=510516;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 122,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122",
  "source_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "retrieved_utc": "2026-11-02T04:30:44.949915+00:00",
  "source_locator": "lines 32-38",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, DOMAIN, AND INDUCTION.\nRX   PubMed=22447538; DOI=10.1002/cbic.201200107;\nRA   Nakazawa T., Ishiuchi K., Praseuth A., Noguchi H., Hotta K., Watanabe K.;\nRT   \"Overexpressing transcriptional regulator in Aspergillus oryzae activates a\nRT   silent biosynthetic pathway to produce a novel polyketide.\";\nRL   ChemBioChem 13:855-861(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 122,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122",
  "source_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "retrieved_utc": "2026-11-02T04:30:44.949915+00:00",
  "source_locator": "lines 186-188",
  "excerpt": "FT   ACT_SITE        558\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 122,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122",
  "source_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "retrieved_utc": "2026-11-02T04:30:44.949915+00:00",
  "source_locator": "lines 189-191",
  "excerpt": "FT   ACT_SITE        693\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 122,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122",
  "source_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "retrieved_utc": "2026-11-02T04:30:44.949915+00:00",
  "source_locator": "lines 192-194",
  "excerpt": "FT   ACT_SITE        735\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 122,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122",
  "source_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "retrieved_utc": "2026-11-02T04:30:44.949915+00:00",
  "source_locator": "lines 195-197",
  "excerpt": "FT   ACT_SITE        1334\nFT                   /note=\"Proton acceptor; for dehydratase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01363\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 122,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122",
  "source_sha256": "cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b",
  "retrieved_utc": "2026-11-02T04:30:44.949915+00:00",
  "source_locator": "lines 198-200",
  "excerpt": "FT   ACT_SITE        1519\nFT                   /note=\"Proton donor; for dehydratase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01363\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 122,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 118. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
