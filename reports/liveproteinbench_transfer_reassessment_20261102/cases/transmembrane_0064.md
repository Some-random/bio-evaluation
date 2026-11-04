# transmembrane_0064

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0064.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 308..328; 344..364; 474..494; 533..553; 640..660; 670..690; 731..751; 771..791; 807..827; 851..871; 937..957; 1162..1182; 1209..1229; 1244..1264; 1306..1326; 1381..1401; 1422..1442; 1498..1518; 1532..1552; 1561..1581; 1633..1653; 1671..1691; 1722..1742

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSHFRNHSLAISTSASIHTSASPSPVSPASPASASAGLSRRHSWNVTDESQEIPTFNDPSNASRHVDDNLTPRRAVPLHSTPLGKSGTVHSHRLSERDIIWADVNDGRDIGGDPNETTPTKSHNRPFFDSYQSTTSLHSTISPLDVNGRSSDDRERLTTGPSHVMHYNGIGKGTPRRSPRKPYNESGSSLRRSSTLRNVSQSLRKASVRVVNIMGTERGDGRERLGSDDEGEEVLQDVEIDGDQAFAMSSTNDNPGTVPSPRQLPTRSQREEVDHGRLRGRTMCLFGPMSRVRKSMDRLMRYPWTEPVILLLIITNVVVLAIQSAPALDSPRIDNGYFQGWEDFVLLVLFIVFTLEMFARIVVTGLLLDPETSLRESLFGQDGAVPILKQYLLITKFNIQSNLRRNATKRRAPWRSQGQNDAAHNKDSKTPANSALRSLTGLSEAPFQKAMARQKGLSDQGRPYLRHSWHRIDMIAVFAFWITFFLALTGYEATADRHVYIFRALSVLRAGRLLVITSGTTTILHSLKRAGPMLITVSYFLVFAACIFSIIGVQSFRGSFRRACVLTDPHNSSNVIQLETQCGGWLDPTSFKSMSYLSLDGTSSAVPPKGYICPLGQICMTTDENPNNNVNSFDNVFSSLVQVIIVISINTWAPVMYMAMDSDFFGSSLFFIAGVIVLNFWLINLLIAVVVNTFSDIRAETKRSAFGAGETFLGTEPHWAAEDEKTKNNRLLAFYQKTEIFWVILVVADLVAQGSKSSSSPESMLRLLDRLELAFTLAFDLEIIIRFLAYFPDWRTFFYRKRNCFDLFLAIACSIIQIPAISNSPIYPWLTVFQLIRWYRVILAFPRMKPLLITVFGSFSGLLNMVIFLFLMNFLGALMALQLFRGDLEAGETITFSQTYNSFLGMYQIFSSENWTDIVYDTMGAESQYKQNIIAAIFLCGWFLFSNFIVLQMFIAVINENFAIAEEQKRKQQIQAFIHRAEAPSAHASWIDRLNPYRLMTARHRAVRVKTLPPNLILPLKQNVGIDVSDVPSSLPMNDGKSTKGAVKRLLGRDGDEDQIPLKRFKRPPPRESTDDAEDEDDDRGLTDLLPPLNAAVSTDEHMDAFRERRNQQADFIAAHPSFDKSLWLFKQNNPIRKFCQACVPSAYGERIFGRSTNPTLALIVKTVVFLAVVASIVVAAIASPSYRREYYADHGISRRTWFDLTEVALGLIFVLEAAMKIVADGFIFAPNAYLLSLWNVLDFIILITLLINITTSLIFIGGLSRVTRALKSFRALRLITLFGRLRDTLHAVLFAGALKILDASIFMILYLIPFAVWGLNIFSGLLYYCNDDDSSGLTSCIGEFSTSSIDDSLTYLVPRVWVNPTVDESIWSFDSFRESILILFEIVSLEGWIDVMASVMNIVGRDQQPQNQASQWNAIYLVIFNLFGGVIILTLFVSIIIKNFSTRSGNALLTSEQRQWVDLSKFIKAQTPSQLPKGRPRLPFRAWCYDRAVNKNGFWAVGFTMIYYLHILLLMMEDFSENLLNEVQLDWIFLFLTVLYAVDLLVRFYGLGFKSFKSNGWNIFDLIVITGSFATTIPALQADSSGGTANQANVQLQKLFLVSISLKLVQRISSLNQLFKTSVASLPAIGNLFLLWATIFIFYAILYLEVFGLTKEGNNAGTRFQNYYTFGNALLMLAFMSTGEGWNGYMHDYTIQEPRCTENGNFLESDCGSAPGAYVLFISWNIISMYIFVNMFTGVVVESFAYVYQMPGKSSLNREEMRAFKQLWAEFDSQRIGYIKRKDLIRFFSRLTGVFEVRPFPVEFGVHNIIRHSRPDQVDNNASSQSYVITGVKHAVDVRRVAEQIAQIDYKQVRVRRQLFSRLYNEARISEEPGKGISFTAMLMMLAHYKLIDDESALQLDDLLLRRAKTERVTDLVNLDRVRGLLRTIYWRKRFLATRDARKLTLNAEAEGIPAIVLDPTPITPPDYNGQSRYDTPYSPQVQEKEESIPKRITPTEIIPPTSFSPSARTYPLPASDLSNSSDGNSLPSPSLYNSPTRLTSRPALLGRQPSNNSHLSSDDAHYRRDSRPDEDLHTKDYDDDMLDSMWGDMMREAVDQEGIKNEQG

[Multiple Choices]
A. 308..328; 344..364; 474..494; 530..549; 640..660; 670..690; 731..751; 771..791; 807..827; 851..871; 937..957; 1162..1182; 1209..1229; 1244..1264; 1306..1326; 1381..1401; 1422..1442; 1498..1518; 1532..1552; 1561..1581; 1633..1653; 1671..1691; 1722..1742
B. 39..59; 94..114; 117..137; 148..168; 177..197; 217..237; 365..385; 405..425; 433..453; 461..481; 488..508; 528..548
C. 308..328; 344..364; 474..494; 533..553; 640..660; 670..690; 731..751; 771..791; 807..827; 851..871; 937..957; 1162..1182; 1244..1264; 1306..1326; 1381..1401; 1422..1442; 1498..1518; 1532..1552; 1561..1581; 1633..1653; 1671..1691; 1722..1742
D. 308..328; 344..364; 474..494; 533..553; 640..660; 670..690; 731..751; 771..791; 807..827; 851..871; 937..957; 1162..1182; 1209..1229; 1244..1264; 1306..1326; 1381..1401; 1422..1442; 1498..1518; 1532..1552; 1561..1581; 1633..1653; 1671..1691; 1722..1742
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The matched-sequence UniProt record annotates the transmembrane intervals listed in D, including 533..553 and 1209..1229. These annotations are computationally supported (ECO:0000255), not evidence of experimental determination.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14), [H15](#evidence-h15), [H16](#evidence-h16), [H17](#evidence-h17), [H18](#evidence-h18), [H19](#evidence-h19), [H20](#evidence-h20), [H21](#evidence-h21), [H22](#evidence-h22), [H23](#evidence-h23), [H24](#evidence-h24), [H25](#evidence-h25).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the characteristic pattern of a multipass membrane channel, with repeated long hydrophobic stretches. In particular, the region around 1209..1229 is strongly hydrophobic, supporting its inclusion and distinguishing D (and A) from C. The hydrophobic segment corresponding to 533..553 also supports a membrane-spanning helix; its boundary is less sharply inferable from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about multipass channel proteins and hydrophobic membrane-spanning helices provides a meaningful basis for recognizing the listed regions and rejecting choices that omit an evident helix or list unrelated segments. Exact boundaries remain predictions rather than certain experimental facts.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> A differs from D at one interval, listing 530..549 instead of 533..553. Given the broad wording about identifying a segment that crosses a membrane, that shifted interval overlaps the same hydrophobic helix and could plausibly describe a membrane-spanning segment; the sequence alone does not sharply settle those boundary residues.


### Important caveats

- The reviewer-only annotation matches the supplied sequence, but the cited transmembrane features are computationally supported rather than experimentally established.
- Transmembrane boundaries can be approximate, so exact coordinate ranges may be less uniquely answerable than identifying the hydrophobic helices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the characteristic pattern of a multipass membrane channel, with repeated long hydrophobic stretches. In particular, the region around 1209..1229 is strongly hydrophobic, supporting its inclusion and distinguishing D (and A) from C. The hydrophobic segment corresponding to 533..553 also supports a membrane-spanning helix; its boundary is less sharply inferable from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about multipass channel proteins and hydrophobic membrane-spanning helices provides a meaningful basis for recognizing the listed regions and rejecting choices that omit an evident helix or list unrelated segments. Exact boundaries remain predictions rather than certain experimental facts."
  },
  "case_id": "transmembrane_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14",
      "H15",
      "H16",
      "H17",
      "H18",
      "H19",
      "H20",
      "H21",
      "H22",
      "H23",
      "H24",
      "H25"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record annotates the transmembrane intervals listed in D, including 533..553 and 1209..1229. These annotations are computationally supported (ECO:0000255), not evidence of experimental determination."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but the cited transmembrane features are computationally supported rather than experimentally established.",
    "Transmembrane boundaries can be approximate, so exact coordinate ranges may be less uniquely answerable than identifying the hydrophobic helices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "A differs from D at one interval, listing 530..549 instead of 533..553. Given the broad wording about identifying a segment that crosses a membrane, that shifted interval overlaps the same hydrophobic helix and could plausibly describe a membrane-spanning segment; the sequence alone does not sharply settle those boundary residues."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt record annotates the transmembrane intervals listed in D, including 533..553 and 1209..1229. These annotations are computationally supported (ECO:0000255), not evidence of experimental determination.",
    "evidence_ids": ["H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14", "H15", "H16", "H17", "H18", "H19", "H20", "H21", "H22", "H23", "H24", "H25"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the characteristic pattern of a multipass membrane channel, with repeated long hydrophobic stretches. In particular, the region around 1209..1229 is strongly hydrophobic, supporting its inclusion and distinguishing D (and A) from C. The hydrophobic segment corresponding to 533..553 also supports a membrane-spanning helix; its boundary is less sharply inferable from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about multipass channel proteins and hydrophobic membrane-spanning helices provides a meaningful basis for recognizing the listed regions and rejecting choices that omit an evident helix or list unrelated segments. Exact boundaries remain predictions rather than certain experimental facts."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "A differs from D at one interval, listing 530..549 instead of 533..553. Given the broad wording about identifying a segment that crosses a membrane, that shifted interval overlaps the same hydrophobic helix and could plausibly describe a membrane-spanning segment; the sequence alone does not sharply settle those boundary residues."
  },
  "important_caveats": [
    "The reviewer-only annotation matches the supplied sequence, but the cited transmembrane features are computationally supported rather than experimentally established.",
    "Transmembrane boundaries can be approximate, so exact coordinate ranges may be less uniquely answerable than identifying the hydrophobic helices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry J9VTB0 (CCH1_CRYN9, Calcium-channel protein CCH1 from Cryptococcus neoformans) annotates exactly 23 transmembrane helical regions with coordinates matching choice D precisely: 308..328, 344..364, 474..494, 533..553, 640..660, 670..690, 731..751, 771..791, 807..827, 851..871, 937..957, 1162..1182, 1209..1229, 1244..1264, 1306..1326, 1381..1401, 1422..1442, 1498..1518, 1532..1552, 1561..1581, 1633..1653, 1671..1691, 1722..1742. All annotations carry evidence code ECO:0000255 (by similarity), indicating computational/transferred annotation rather than direct experimental determination. The sequence matches (SHA256 identical, 2106 AA).

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [C16](#evidence-c16), [C17](#evidence-c17), [C18](#evidence-c18), [C19](#evidence-c19), [C20](#evidence-c20), [C21](#evidence-c21), [C22](#evidence-c22), [C23](#evidence-c23), [C24](#evidence-c24), [C25](#evidence-c25), [C26](#evidence-c26), [C27](#evidence-c27), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14), [H15](#evidence-h15), [H16](#evidence-h16), [H17](#evidence-h17), [H18](#evidence-h18), [H19](#evidence-h19), [H20](#evidence-h20), [H21](#evidence-h21), [H22](#evidence-h22), [H23](#evidence-h23), [H24](#evidence-h24), [H25](#evidence-h25).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is a 2106-residue multi-pass membrane protein (voltage-gated calcium channel family, 23 predicted TMs). (1) Choice B is clearly eliminable: it places all 12 TM regions within the first ~550 residues, which is incompatible with a large multi-pass ion channel whose sequence shows hydrophobic stretches distributed throughout. (2) Choice C omits the region 1209..1229; a hydrophobicity scan of the sequence at that position would reveal a ~21-residue hydrophobic stretch consistent with a TM helix, allowing elimination of C. (3) The distinction between A (530..549) and D (533..553) is a 3-residue boundary shift. A careful hydrophobicity analysis of the local sequence can provide some signal: if residues at 530-532 are less hydrophobic (e.g., contain polar/charged residues) while 550-553 remain hydrophobic, the 533..553 boundary is preferred. The overall topology of 23 TMs distributed across the full length is consistent with voltage-gated calcium channel architecture (6-pass repeats with auxiliary segments), supporting the full-length distribution in D over the truncated pattern in C. The family-level knowledge of calcium channel topology (multiple hydrophobic segments spread across the entire protein, not clustered in one region) meaningfully eliminates B and C, and the local hydrophobicity context provides at least a probabilistic basis for preferring D's boundary over A's.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question is largely answerable by: (a) recognizing the multi-pass membrane topology from the overall hydrophobic pattern, eliminating B; (b) performing hydrophobicity analysis to confirm the 1209..1229 region is a TM helix, eliminating C; (c) the 3-residue boundary shift (530..549 vs 533..553) is the weakest link but local hydrophobicity context provides some discriminative signal. The overall pattern of ~23 TMs distributed across a 2106 AA calcium channel is predictable from family knowledge. The 3-residue precision is at the limit of sequence-based prediction but the question does not require perfect boundary determination—only selection among the four offered options, where the cumulative evidence favors D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A"
]
```

> The 3-residue boundary difference between A (530..549) and D (533..553) is within the typical uncertainty of transmembrane helix boundary prediction. Different algorithms (TMHMM, Phobius, DeepTMHMM) routinely differ by 2-4 residues at TM boundaries. Without the specific annotation, both boundaries could be defended by a hydrophobicity analysis. However, A is less defensible because it also differs from the broader pattern: the UniProt annotation (by similarity) consistently uses 533..553, and the local sequence context likely disfavors the earlier boundary. The ambiguity is minor but real.


### Important caveats

- All 23 transmembrane annotations carry evidence code ECO:0000255 (by similarity), meaning they are computationally transferred rather than experimentally validated.
- The 3-residue boundary difference between choices A and D is within the typical uncertainty of TM prediction algorithms; the 'correct' boundary is somewhat arbitrary at this resolution.
- The protein is identified as CCH1 (calcium channel) from Cryptococcus neoformans, but this identification was not provided to the evaluated model—only the raw sequence.
- The sequence is 2106 AA with 23 TM regions, consistent with a large multi-pass membrane channel, which is the key family-level feature enabling prediction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is a 2106-residue multi-pass membrane protein (voltage-gated calcium channel family, 23 predicted TMs). (1) Choice B is clearly eliminable: it places all 12 TM regions within the first ~550 residues, which is incompatible with a large multi-pass ion channel whose sequence shows hydrophobic stretches distributed throughout. (2) Choice C omits the region 1209..1229; a hydrophobicity scan of the sequence at that position would reveal a ~21-residue hydrophobic stretch consistent with a TM helix, allowing elimination of C. (3) The distinction between A (530..549) and D (533..553) is a 3-residue boundary shift. A careful hydrophobicity analysis of the local sequence can provide some signal: if residues at 530-532 are less hydrophobic (e.g., contain polar/charged residues) while 550-553 remain hydrophobic, the 533..553 boundary is preferred. The overall topology of 23 TMs distributed across the full length is consistent with voltage-gated calcium channel architecture (6-pass repeats with auxiliary segments), supporting the full-length distribution in D over the truncated pattern in C. The family-level knowledge of calcium channel topology (multiple hydrophobic segments spread across the entire protein, not clustered in one region) meaningfully eliminates B and C, and the local hydrophobicity context provides at least a probabilistic basis for preferring D's boundary over A's.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question is largely answerable by: (a) recognizing the multi-pass membrane topology from the overall hydrophobic pattern, eliminating B; (b) performing hydrophobicity analysis to confirm the 1209..1229 region is a TM helix, eliminating C; (c) the 3-residue boundary shift (530..549 vs 533..553) is the weakest link but local hydrophobicity context provides some discriminative signal. The overall pattern of ~23 TMs distributed across a 2106 AA calcium channel is predictable from family knowledge. The 3-residue precision is at the limit of sequence-based prediction but the question does not require perfect boundary determination—only selection among the four offered options, where the cumulative evidence favors D."
  },
  "case_id": "transmembrane_0064",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14",
      "C15",
      "C16",
      "C17",
      "C18",
      "C19",
      "C20",
      "C21",
      "C22",
      "C23",
      "C24",
      "C25",
      "C26",
      "C27",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14",
      "H15",
      "H16",
      "H17",
      "H18",
      "H19",
      "H20",
      "H21",
      "H22",
      "H23",
      "H24",
      "H25"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry J9VTB0 (CCH1_CRYN9, Calcium-channel protein CCH1 from Cryptococcus neoformans) annotates exactly 23 transmembrane helical regions with coordinates matching choice D precisely: 308..328, 344..364, 474..494, 533..553, 640..660, 670..690, 731..751, 771..791, 807..827, 851..871, 937..957, 1162..1182, 1209..1229, 1244..1264, 1306..1326, 1381..1401, 1422..1442, 1498..1518, 1532..1552, 1561..1581, 1633..1653, 1671..1691, 1722..1742. All annotations carry evidence code ECO:0000255 (by similarity), indicating computational/transferred annotation rather than direct experimental determination. The sequence matches (SHA256 identical, 2106 AA)."
  },
  "important_caveats": [
    "All 23 transmembrane annotations carry evidence code ECO:0000255 (by similarity), meaning they are computationally transferred rather than experimentally validated.",
    "The 3-residue boundary difference between choices A and D is within the typical uncertainty of TM prediction algorithms; the 'correct' boundary is somewhat arbitrary at this resolution.",
    "The protein is identified as CCH1 (calcium channel) from Cryptococcus neoformans, but this identification was not provided to the evaluated model—only the raw sequence.",
    "The sequence is 2106 AA with 23 TM regions, consistent with a large multi-pass membrane channel, which is the key family-level feature enabling prediction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A"
    ],
    "reason": "The 3-residue boundary difference between A (530..549) and D (533..553) is within the typical uncertainty of transmembrane helix boundary prediction. Different algorithms (TMHMM, Phobius, DeepTMHMM) routinely differ by 2-4 residues at TM boundaries. Without the specific annotation, both boundaries could be defended by a hydrophobicity analysis. However, A is less defensible because it also differs from the broader pattern: the UniProt annotation (by similarity) consistently uses 533..553, and the local sequence context likely disfavors the earlier boundary. The ambiguity is minor but real."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0064",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry J9VTB0 (CCH1_CRYN9, Calcium-channel protein CCH1 from Cryptococcus neoformans) annotates exactly 23 transmembrane helical regions with coordinates matching choice D precisely: 308..328, 344..364, 474..494, 533..553, 640..660, 670..690, 731..751, 771..791, 807..827, 851..871, 937..957, 1162..1182, 1209..1229, 1244..1264, 1306..1326, 1381..1401, 1422..1442, 1498..1518, 1532..1552, 1561..1581, 1633..1653, 1671..1691, 1722..1742. All annotations carry evidence code ECO:0000255 (by similarity), indicating computational/transferred annotation rather than direct experimental determination. The sequence matches (SHA256 identical, 2106 AA).",
    "evidence_ids": ["C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","C16","C17","C18","C19","C20","C21","C22","C23","C24","C25","C26","C27","H3","H4","H5","H6","H7","H8","H9","H10","H11","H12","H13","H14","H15","H16","H17","H18","H19","H20","H21","H22","H23","H24","H25"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is a 2106-residue multi-pass membrane protein (voltage-gated calcium channel family, 23 predicted TMs). (1) Choice B is clearly eliminable: it places all 12 TM regions within the first ~550 residues, which is incompatible with a large multi-pass ion channel whose sequence shows hydrophobic stretches distributed throughout. (2) Choice C omits the region 1209..1229; a hydrophobicity scan of the sequence at that position would reveal a ~21-residue hydrophobic stretch consistent with a TM helix, allowing elimination of C. (3) The distinction between A (530..549) and D (533..553) is a 3-residue boundary shift. A careful hydrophobicity analysis of the local sequence can provide some signal: if residues at 530-532 are less hydrophobic (e.g., contain polar/charged residues) while 550-553 remain hydrophobic, the 533..553 boundary is preferred. The overall topology of 23 TMs distributed across the full length is consistent with voltage-gated calcium channel architecture (6-pass repeats with auxiliary segments), supporting the full-length distribution in D over the truncated pattern in C. The family-level knowledge of calcium channel topology (multiple hydrophobic segments spread across the entire protein, not clustered in one region) meaningfully eliminates B and C, and the local hydrophobicity context provides at least a probabilistic basis for preferring D's boundary over A's.",
    "missing_item_specific_fact": "",
    "reason": "The question is largely answerable by: (a) recognizing the multi-pass membrane topology from the overall hydrophobic pattern, eliminating B; (b) performing hydrophobicity analysis to confirm the 1209..1229 region is a TM helix, eliminating C; (c) the 3-residue boundary shift (530..549 vs 533..553) is the weakest link but local hydrophobicity context provides some discriminative signal. The overall pattern of ~23 TMs distributed across a 2106 AA calcium channel is predictable from family knowledge. The 3-residue precision is at the limit of sequence-based prediction but the question does not require perfect boundary determination—only selection among the four offered options, where the cumulative evidence favors D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A"],
    "reason": "The 3-residue boundary difference between A (530..549) and D (533..553) is within the typical uncertainty of transmembrane helix boundary prediction. Different algorithms (TMHMM, Phobius, DeepTMHMM) routinely differ by 2-4 residues at TM boundaries. Without the specific annotation, both boundaries could be defended by a hydrophobicity analysis. However, A is less defensible because it also differs from the broader pattern: the UniProt annotation (by similarity) consistently uses 533..553, and the local sequence context likely disfavors the earlier boundary. The ambiguity is minor but real."
  },
  "important_caveats": [
    "All 23 transmembrane annotations carry evidence code ECO:0000255 (by similarity), meaning they are computationally transferred rather than experimentally validated.",
    "The 3-residue boundary difference between choices A and D is within the typical uncertainty of TM prediction algorithms; the 'correct' boundary is somewhat arbitrary at this resolution.",
    "The protein is identified as CCH1 (calcium channel) from Cryptococcus neoformans, but this identification was not provided to the evaluated model—only the raw sequence.",
    "The sequence is 2106 AA with 23 TM regions, consistent with a large multi-pass membrane channel, which is the key family-level feature enabling prediction."
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
  "benchmark_sequence_length": 2106,
  "benchmark_sequence_sha256": "ee0d3c63e4b344d6689faf26c96c64144cc1f925b9abbedae13921c591beb9c2",
  "current_entry_audit": {
    "entryVersion": 63,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2013-11-13",
    "sequenceVersion": 2
  },
  "current_record_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 2106,
  "current_source_sequence_sha256": "ee0d3c63e4b344d6689faf26c96c64144cc1f925b9abbedae13921c591beb9c2",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 62,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9VTB0",
  "selected_historical_entry_version": 62,
  "selected_historical_record_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "selected_historical_source_sequence_length": 2106,
  "selected_historical_source_sequence_sha256": "ee0d3c63e4b344d6689faf26c96c64144cc1f925b9abbedae13921c591beb9c2",
  "selected_historical_version": {
    "accession": "J9VTB0",
    "database": "Swiss-Prot",
    "entryVersion": 62,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CCH1_CRYN9",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9VTB0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":63,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2013-11-13\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Calcium-channel protein CCH1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":328},\"start\":{\"modifier\":\"EXACT\",\"value\":308}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":364},\"start\":{\"modifier\":\"EXACT\",\"value\":344}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":494},\"start\":{\"modifier\":\"EXACT\",\"value\":474}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":553},\"start\":{\"modifier\":\"EXACT\",\"value\":533}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":660},\"start\":{\"modifier\":\"EXACT\",\"value\":640}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":690},\"start\":{\"modifier\":\"EXACT\",\"value\":670}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":751},\"start\":{\"modifier\":\"EXACT\",\"value\":731}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":791},\"start\":{\"modifier\":\"EXACT\",\"value\":771}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":827},\"start\":{\"modifier\":\"EXACT\",\"value\":807}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":871},\"start\":{\"modifier\":\"EXACT\",\"value\":851}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":957},\"start\":{\"modifier\":\"EXACT\",\"value\":937}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1182},\"start\":{\"modifier\":\"EXACT\",\"value\":1162}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1229},\"start\":{\"modifier\":\"EXACT\",\"value\":1209}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1264},\"start\":{\"modifier\":\"EXACT\",\"value\":1244}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1326},\"start\":{\"modifier\":\"EXACT\",\"value\":1306}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1401},\"start\":{\"modifier\":\"EXACT\",\"value\":1381}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C21",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1442},\"start\":{\"modifier\":\"EXACT\",\"value\":1422}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C22",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1518},\"start\":{\"modifier\":\"EXACT\",\"value\":1498}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/18",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C23",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1552},\"start\":{\"modifier\":\"EXACT\",\"value\":1532}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/19",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C24",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1581},\"start\":{\"modifier\":\"EXACT\",\"value\":1561}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/20",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C25",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1653},\"start\":{\"modifier\":\"EXACT\",\"value\":1633}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/21",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C26",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1691},\"start\":{\"modifier\":\"EXACT\",\"value\":1671}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/22",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence C27

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VTB0.json)

```json
{
  "evidence_id": "C27",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1742},\"start\":{\"modifier\":\"EXACT\",\"value\":1722}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/23",
  "retrieved_utc": "2026-11-02T04:28:58.195980+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8ba1e61c5b47a2b8b636f7e5e36264e0a2720117204f936c780752046f112685",
  "url": "https://rest.uniprot.org/uniprotkb/J9VTB0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H1",
  "excerpt": "ID   CCH1_CRYN9              Reviewed;        2106 AA.\nAC   J9VTB0;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-NOV-2013, sequence version 2.\nDT   28-JAN-2026, entry version 62.\nDE   RecName: Full=Calcium-channel protein CCH1 {ECO:0000305};\nGN   Name=CCH1 {ECO:0000303|PubMed:18503003};\nGN   ORFNames=CNAG_01208 {ECO:0000312|EMBL:AFR94935.2};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, INTERACTION WITH TEF3, AND SUBCELLULAR LOCATION.\nRX   PubMed=18503003; DOI=10.1128/ec.00116-08;\nRA   Liu M., Gelli A.;\nRT   \"Elongation factor 3, EF3, associates with the calcium channel Cch1 and\nRT   targets Cch1 to the plasma membrane in Cryptococcus neoformans.\";\nRL   Eukaryot. Cell 7:1118-1126(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        308..328\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 130-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        344..364\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 133-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        474..494\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        533..553\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 139-141",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        640..660\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 142-144",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        670..690\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 145-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        731..751\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-150",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        771..791\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 151-153",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        807..827\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 154-156",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        851..871\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 157-159",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        937..957\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-162",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        1162..1182\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 163-165",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H15",
  "excerpt": "FT   TRANSMEM        1209..1229\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 166-168",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H16",
  "excerpt": "FT   TRANSMEM        1244..1264\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 169-171",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H17",
  "excerpt": "FT   TRANSMEM        1306..1326\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 172-174",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H18",
  "excerpt": "FT   TRANSMEM        1381..1401\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 175-177",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H19",
  "excerpt": "FT   TRANSMEM        1422..1442\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 178-180",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H20",
  "excerpt": "FT   TRANSMEM        1498..1518\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 181-183",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H21",
  "excerpt": "FT   TRANSMEM        1532..1552\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 184-186",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H22",
  "excerpt": "FT   TRANSMEM        1561..1581\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 187-189",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H23",
  "excerpt": "FT   TRANSMEM        1633..1653\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 190-192",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H24",
  "excerpt": "FT   TRANSMEM        1671..1691\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 193-195",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

### Evidence H25

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62)

```json
{
  "entry_version": 62,
  "evidence_id": "H25",
  "excerpt": "FT   TRANSMEM        1722..1742\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:02.869375+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 196-198",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b9e3e6ce2b6282c110d47f90c799167c03b243b28896d1c1b2d9e2a073af201b",
  "url": "https://rest.uniprot.org/unisave/J9VTB0?format=txt&versions=62"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 64. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
