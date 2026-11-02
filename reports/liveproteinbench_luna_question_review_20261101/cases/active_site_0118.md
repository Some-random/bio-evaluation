# active_site_0118

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 558 (For beta-ketoacyl synthase activity)

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

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

## Luna’s full visible review

### Expected-answer support: supported

> The sequence exactly matches the annotated 2,121-residue protein, and both current and pre-cutoff UniProt records annotate position 558 as an active site for beta-ketoacyl synthase activity. This is PROSITE-ProRule computational annotation, not evidence of direct experimental validation.

Cited evidence: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence and choices may suggest a multidomain polyketide synthase, but general knowledge does not establish that this particular residue at position 558 has the stated role.

**Missing item-specific fact**

> The protein-specific mapping of residue 558 to the beta-ketoacyl synthase active site, supplied here by a PROSITE-ProRule annotation.

**Reason**

> Selecting the exact numbered residue and its function requires a protein-specific annotation or equivalent external analysis; recognizing the protein or relying on general catalytic-residue heuristics is not enough.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The supplied matching annotation supports option C among the listed choices. Other active-site annotations exist at positions not offered, but they do not make another listed option defensible.

### Important caveats

- The matching historical record also annotates positions 693 and 735 for beta-ketoacyl synthase activity; option C is one supported residue, not an exhaustive active-site list.
- The author’s exact source snapshot is unknown, although the sequence matches the checked historical record.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "active_site_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the annotated 2,121-residue protein, and both current and pre-cutoff UniProt records annotate position 558 as an active site for beta-ketoacyl synthase activity. This is PROSITE-ProRule computational annotation, not evidence of direct experimental validation.",
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ]
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

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q2TXQ8`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 122. The exact author source snapshot remains unknown.

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

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json) (zero-based source row 118). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
