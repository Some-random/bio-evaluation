# active_site_0118

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 558 (For beta-ketoacyl synthase activity)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

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

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q2TXQ8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 122. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:41.744302+00:00.  

```json
"Q2TXQ8"
```

Source SHA-256: `b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:41.744302+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22447538","source":"PubMed"}],"value":"2.3.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22447538","source":"PubMed"}],"value":"Non-reducing polyketide synthase aoiG"}}}
```

Source SHA-256: `b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:41.744302+00:00.  

```json
{"description":"For beta-ketoacyl synthase activity","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01348","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":558},"start":{"modifier":"EXACT","value":558}},"type":"Active site"}
```

Source SHA-256: `b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:41.744302+00:00.  

```json
{"citation":{"authors":["Nakazawa T.","Ishiuchi K.","Praseuth A.","Noguchi H.","Hotta K.","Watanabe K."],"citationCrossReferences":[{"database":"PubMed","id":"22447538"},{"database":"DOI","id":"10.1002/cbic.201200107"}],"citationType":"journal article","firstPage":"855","id":"22447538","journal":"ChemBioChem","lastPage":"861","publicationDate":"2012","title":"Overexpressing transcriptional regulator in Aspergillus oryzae activates a silent biosynthetic pathway to produce a novel polyketide.","volume":"13"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","PATHWAY","DOMAIN","INDUCTION"]}
```

Source SHA-256: `b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)  
**Locator:** `lines 186-188`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:30:44.949915+00:00.  

```text
FT   ACT_SITE        558
FT                   /note="For beta-ketoacyl synthase activity"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01348"
```

Source SHA-256: `cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 118. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
