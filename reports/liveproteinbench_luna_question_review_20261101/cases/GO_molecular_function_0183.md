# GO_molecular_function_0183

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — 3-oxoacyl-&#91;acyl-carrier-protein&#93; synthase activity

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MVNIYIFGDQTVRVDDAVHKLLHVKNNPILKSFLDGSFAAIRKQIFLLPANERTSLPDAHTLPLLLEAVRRGRRHVALESALVCLCEIGQYIALLQTTDLCHPPTGSILVGFCTGSLAAAAVSCVRTSIDLLTLGIEAVVVAFRVGMHVARRANALGGDGGSQWKPWSLAVTDGSESETEKILEEFTRDEVSGVHVANRHDAYILAKGLPAIMKPYVSAAGSNTLTISGTPRVLEALKASPHLRGTKSLPVSIYAPYHAAHLYNEADVESIFACKPVESALFHRELRTPLISCATGTVLKEKTFGDLLRALVMEILTCQIRFDKVEESIVQHTPGATAQLIPIHTNIAPRMKTSLTQVGLQVECFKAIANQEPAAEALSESPSNDSSKIAIIGFSGRFPEADGLNEFWELLQQGLDVHKPIPADRFDLEAHYDATLREKNTSRIKHGCWIRSPGSFDARFFQMSPREACQTDPAQRLALLTAYEAMEMAGFVPDRTPSSQRDRVGVYYGMTSDDWREVNSSQDIDTYFIPGGIRAFVPGRINYFFKFSGPSITVDTACSSSLAAIHTACNALLNSDCDTALAGGTNILTNPDNFAGLDRGHFLSSTGNCKTFDDDADGYCRADGVGTVILKRLQDAIADNDPIFGVIVGARTSHSAEAVSITRPLADAQAHLFRKLLAESGIHPHEISYIEMHGTGTQAGDAVEMKSVLDSFARDDSRAPDRPLHLGSVKANVGHGESASGVTALIKVLLMMQKNRIPPHCGIKGRINRHFPTDMEYRNVHIPFMETDWTRPQEGKRRSFINNFSAAGGNTAVLVEDAPLLEQSRAISSPDPQRYHVITLSARSVRSLSKNMRALGEFIGSETSPGLLARIAYTTTARRMHHSYRVAFVGNDLQEVKRRFLDTDVTEAIKPCPTKSPGVGFLFTGQGAQQTAMARELYDRFTSFRADILEFEAVGRGHGFPSILPLITGAVDVEELSPMIVQLGTVVIQIAMARLWQTWGLTPEYALGHSLGEYAALQIAGVLSISDTIYLAGSRAALLEKRCTAGSHGMLAVKASVAHLEEALKGMQVEVSCINGFDDTVLSGTNDEIDRASKELSELKVTFKRLILPFAFHSSQVDPILEELEHIASQLSFQPPRIPIVSPTVGHIITDEGTIGAQYIRRHCREPVNFLGAIQAAQGSGICNSGALAVEIGAHPILTRMMKAAVGSSVTVCSTLSHREDMFKTLTESLSVLHLAGVRLNWDEYHRDFNNQVVMLPAYSWDYQDYWIQYQNNFCLTKGSPERSESVDAIQPMSTRLSPSVQKILEEEMTAAQASIIIESDITDPELLPVALDHKVNGVTLCPSSLYADIGHTLGTYLLGKKEDVTDYKIDVSNMAVEKALVVKGTGPQLFRASLDMDWNMLRGMMKVYSVNNMGTLTTHHAQCTIELQRPHQWQEGWNRQLYLIQRSIEQLKKGVEEGWTHKMRRGVAYRLFSSMMQYGPSYQAMEEVIFDSSGLEATAQVRLQSTTGRYSFNPVWSDSLGHITGFVTNCNDSIDLTENLFVNHGWGFMRCVEPFSPDTVYQTHVKMQPVDGNNGFYVGDVYVLNDHRIIAQYGAVTFQKVARRVLEMLLPATTSKGRSSNIRPRNVGTAQSAKIVQSKRRTQTPHVEDAWQQVLEMIARELGVDPGQLTEDVNFTDMGVDSLMSLTIIGNFREFLSLDVPWSLFEDCPSVQSLRIYLNMSSLSESDSIETSSYPTPDESTTTTITSPSGSDRNVGRNSGIDGVGTTVGLVLSILAEEIGVNVRDLSNADGLSELGLDSLLSITALGRVRDETDLDLPSDFFLEHSSVAAITAALHAIFGSTEQGPEQSLITSHPPAMSINLQGDEGCPQTLFLFPDGSGSSTSYSALPTISKDVRVYAMDCPYLKRPNELAKCQLQDLTPVYVAEIRRRQLRGPYSLGGWSAGGIAAYEAAQYLVDQGERVERLILIDSPNPMGLGKCPPHFYRFLEEAGVFGVHGGRKPPAWLLQHFQAFNDVLSQYTLEPFRPADATPNTTLIYAQDGVCKSPRDPRPERHPGDPEVFSWLLENRVDMSCNGWDQLLGEDNIHLGTVFDANHFTIVRTPAVVRLSEIVRMAMSRKFQ

[Multiple Choices]
A. 18S rRNA cytidine N-acetyltransferase activity
B. cellulose synthase (UDP-forming) activity
C. 3-oxoacyl-[acyl-carrier-protein] synthase activity
D. calmodulin binding
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The exact sequence matches a reviewed record naming the protein a non-reducing polyketide synthase. The record reports experimentally supported polyketide-chain synthesis and assigns 3-oxoacyl-[acyl-carrier-protein] synthase activity by IEA:InterPro. This supports C as the best choice, though the specific GO-term assignment is computational rather than direct evidence of an isolated domain assay.

Cited evidence: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 2121-aa sequence is consistent with a large, soluble multidomain polyketide synthase, including features compatible with ketosynthase and carrier-protein domains. Such an enzyme performs chain-condensation chemistry, which fits C; the other options describe unrelated activities. This is a sequence/domain-based inference, not recognition of a database entry.

**Missing item-specific fact**

> No item-specific lookup is necessary to distinguish the broad catalytic class, although confirming the exact protein identity or the precise GO annotation would require external information.

**Reason**

> The sequence and choices provide a meaningful biological basis for selecting the polyketide-chain condensation activity. The exact annotation is narrower than the broad inference and should not be treated as experimentally established solely from the sequence.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Among the listed choices, C is the only one consistent with a multidomain polyketide synthase.

### Important caveats

- The GO annotation for C is IEA:InterPro, a computational annotation.
- The cited experimental evidence supports the protein's non-reducing polyketide synthase role; it is not presented here as a direct assay of the precise GO activity.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_molecular_function_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a reviewed record naming the protein a non-reducing polyketide synthase. The record reports experimentally supported polyketide-chain synthesis and assigns 3-oxoacyl-[acyl-carrier-protein] synthase activity by IEA:InterPro. This supports C as the best choice, though the specific GO-term assignment is computational rather than direct evidence of an isolated domain assay.",
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 2121-aa sequence is consistent with a large, soluble multidomain polyketide synthase, including features compatible with ketosynthase and carrier-protein domains. Such an enzyme performs chain-condensation chemistry, which fits C; the other options describe unrelated activities. This is a sequence/domain-based inference, not recognition of a database entry.",
    "missing_item_specific_fact": "No item-specific lookup is necessary to distinguish the broad catalytic class, although confirming the exact protein identity or the precise GO annotation would require external information.",
    "reason": "The sequence and choices provide a meaningful biological basis for selecting the polyketide-chain condensation activity. The exact annotation is narrower than the broad inference and should not be treated as experimentally established solely from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, C is the only one consistent with a multidomain polyketide synthase."
  },
  "important_caveats": [
    "The GO annotation for C is IEA:InterPro, a computational annotation.",
    "The cited experimental evidence supports the protein's non-reducing polyketide synthase role; it is not presented here as a direct assay of the precise GO activity."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:41.744302+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22447538","source":"PubMed"}],"value":"Non-reducing polyketide synthase; part of the gene cluster that mediates the biosynthesis of a methylated derivative of known natural products orthosporin and diaporthin (PubMed:22447538). AoiG catalyzes the biosynthesis of the hexaketide isocoumarin scaffold, via condensation of one acetyl-CoA starter unit with 6 malonyl-CoA units (PubMed:22447538). An oxidoreductase that has still to be identified catalyzes the stereospecific reduction of the carbonyl moiety of the hexaketide isocoumarin scaffold to generate the S-configured secondary alcohol at C-11 of orthosporin. The methyltrasferase aoiF then catalyzes the biotransformation of not only orthosporin to diaporthin but also diaporthin to the final product, by performing a tandem methylation of the polyketide core (PubMed:22447538)"}]}
```

Source SHA-256: `b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ8.json)  
**Locator:** `/uniProtKBCrossReferences/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:41.744302+00:00.  

```json
{"database":"GO","id":"GO:0004315","properties":[{"key":"GoTerm","value":"F:3-oxoacyl-[acyl-carrier-protein] synthase activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `b4c4ebc4523172992ff4dfe61bdc82ee604fd15ae8b9e8ecdc17c3d54ba10d69`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)  
**Locator:** `lines 39-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:30:44.949915+00:00.  

```text
CC   -!- FUNCTION: Non-reducing polyketide synthase; part of the gene cluster
CC       that mediates the biosynthesis of a methylated derivative of known
CC       natural products orthosporin and diaporthin (PubMed:22447538). AoiG
CC       catalyzes the biosynthesis of the hexaketide isocoumarin scaffold, via
CC       condensation of one acetyl-CoA starter unit with 6 malonyl-CoA units
CC       (PubMed:22447538). An oxidoreductase that has still to be identified
CC       catalyzes the stereospecific reduction of the carbonyl moiety of the
CC       hexaketide isocoumarin scaffold to generate the S-configured secondary
CC       alcohol at C-11 of orthosporin. The methyltrasferase aoiF then
CC       catalyzes the biotransformation of not only orthosporin to diaporthin
CC       but also diaporthin to the final product, by performing a tandem
CC       methylation of the polyketide core (PubMed:22447538).
CC       {ECO:0000269|PubMed:22447538}.
```

Source SHA-256: `cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ8?format=txt&versions=122)  
**Locator:** `lines 81-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:30:44.949915+00:00.  

```text
DR   GO; GO:0004315; F:3-oxoacyl-[acyl-carrier-protein] synthase activity; IEA:InterPro.
```

Source SHA-256: `cd83ac8893085d09d81e762189c4a2dd94de9101c2c32f33675ed9162a05627b`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json) (zero-based source row 183). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
