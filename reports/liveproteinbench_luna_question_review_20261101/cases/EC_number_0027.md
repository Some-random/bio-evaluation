# EC_number_0027

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 3.4.21.90

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MFPMQFTNSAYRQMEPMFAPGPRGQVQPYRPRTKRRQEPQVGNAAIAALANQMSALQLQVAGLAGQARVDRRGPRRVQKSKQKKKNPSNGEKPKEKKKKQKQQEKKGSGGVIKKPRNRPGKEVRISVKRARQSTFPVYHDGAISGYAVLIGSRVFKPAHVKGKIDHPELADIKFQVAEDMDLEAAAYPKSMRDQAAEPATMMDGVYNWEYGTIRVEDNVVIDASGRGKPGDSGRAITDNSGKVVGIVLGGGPDGRRTRLSVIGFDKKMKAREIAYSEAIPWTRAPALLLLPMVIACTYNSNTFDCSKPSCQDCCITAEPKKAMAMLKDNLNDPNYWDLLIAVTTCNSARKKRAVSTSPAAVYDTQILAAHAAASPYRAYCPDCDGTACISPIAIDEVVSSGSDHVLRIRVGSQSGVTAKGGAAGETSLRYLGRDGKVHAADNTRLVVRTTAKCDVLQATGHYILASCPEGQSITVAATLDGTRHQCTTVFEHQVTEKFTRERSKGHHLSDLTKKCTRFSTTPKKSAPYLVDVYDALPISVEISTVVTCNDNQCTVKVPPGTTVKFDKKCKSAAQATVTFTSDSQTFTCEEPVLTAASITQGKPHLRSSMLPSGGKEVKARIPFPFPPETATCRVSVAPLPSITYEESDVLLAGTAKYPVLLTTRNLGFHSNATSEWIQGKYLRRIPVTPQGIELTWGNNAPLHFWSSVRYASGDADAYPWELLVHHTKHHPEYAWAFVGVACGLLVIAVCMFACACNRVRYSLVANTFNPNPPPLTALTAALCCIPGARADQPYLDIIAYLWTNSKVAFGLQCAAPVACVLIVTYALRHCRLCCKSFLGVRGWSALLVILAYVQSCKSYEHTVVVPMDPRAPSYEAVINRNGYDPLKLTIAVNFTVISPTTALEYWTCASVPIVEPPHVGCCTSVSCPSDLSTLHAFTGKAVSDVHCDVHTNVYPLLWGAAHCFCSTENTQVSAVAATVSEFCAQDSERAEAFSVHSSSVTAEVLVTLGEVVTAVHVYVDGVTSARGTDLKIVAGPITTDYSPFDRKVVRIGEEVYNYDWPPYGAGRPGTFGDIQARSTNYVKPNDLYGDIGIEVLQPTNDHVHVAYTYTTSGLLRWLQDAPKPLSVTAPHGCKISANPLLALDCGVGAVPMSINIPDAKFTRKLKDPKPSALKCVVDSCEYGVDYGGAATITYEGHEAGKCGIHSLTPGVPLRTSVVEVVAGANTVKTTFSSPTPEVTLEVEICSAMVTCASECTPPKEHVVATRPRHGSDTGGYISGPAMRWAGGIVGTLAVLFLILAVTYCVVKKCRSKRIRIVKS

[Multiple Choices]
A. 3.4.21.62
B. 3.4.21.90
C. 1.1.1.336
D. 4.2.3.1
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact sequence matches the 1,319-aa Alphavirus salmon subtype 3 structural polyprotein. UniProt assigns EC 3.4.21.90 to its capsid protein and describes autocatalytic release of that protein from the polyprotein, supporting choice B. The annotation is transferred by similarity from UniProtKB:P03315, rather than evidence of a direct experimental measurement for this sequence.

Cited evidence: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence’s length, basic regions, and multiple hydrophobic segments are consistent with a viral structural polyprotein, but that general inference does not establish the capsid cleavage activity or distinguish EC 3.4.21.90 from the other protease choice.

**Missing item-specific fact**

> The needed fact is that this particular alphavirus structural polyprotein contains a capsid protein that autocatalytically cleaves itself from the polyprotein, an activity annotated as EC 3.4.21.90.

**Reason**

> Identifying the broad protein context from sequence is not enough to determine the exact EC number. Selecting B depends on protein-specific functional annotation or equivalent prior knowledge absent from the input.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The matched database annotation assigns the relevant capsid autocleavage activity to EC 3.4.21.90; the other choices are not supported by the supplied sequence context.

### Important caveats

- The EC annotation applies to the capsid component within the structural polyprotein, not necessarily to the polyprotein as a whole.
- The annotation’s evidence is transferred from another UniProt entry (ECO:0000250); it should not be represented as direct experimental confirmation for this exact sequence.
- The current and historical database records match the sequence, but the author’s exact source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "EC_number_0027",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the 1,319-aa Alphavirus salmon subtype 3 structural polyprotein. UniProt assigns EC 3.4.21.90 to its capsid protein and describes autocatalytic release of that protein from the polyprotein, supporting choice B. The annotation is transferred by similarity from UniProtKB:P03315, rather than evidence of a direct experimental measurement for this sequence.",
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H1",
      "H3"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence’s length, basic regions, and multiple hydrophobic segments are consistent with a viral structural polyprotein, but that general inference does not establish the capsid cleavage activity or distinguish EC 3.4.21.90 from the other protease choice.",
    "missing_item_specific_fact": "The needed fact is that this particular alphavirus structural polyprotein contains a capsid protein that autocatalytically cleaves itself from the polyprotein, an activity annotated as EC 3.4.21.90.",
    "reason": "Identifying the broad protein context from sequence is not enough to determine the exact EC number. Selecting B depends on protein-specific functional annotation or equivalent prior knowledge absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched database annotation assigns the relevant capsid autocleavage activity to EC 3.4.21.90; the other choices are not supported by the supplied sequence context."
  },
  "important_caveats": [
    "The EC annotation applies to the capsid component within the structural polyprotein, not necessarily to the polyprotein as a whole.",
    "The annotation’s evidence is transferred from another UniProt entry (ECO:0000250); it should not be represented as direct experimental confirmation for this exact sequence.",
    "The current and historical database records match the sequence, but the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q53AM4`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 100. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:59.296476+00:00.  

```json
"Q53AM4"
```

Source SHA-256: `ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:59.296476+00:00.  

```json
{"commonName":"SAV3","lineage":["Viruses","Riboviria","Orthornavirae","Kitrinoviricota","Alsuviricetes","Martellivirales","Togaviridae","Alphavirus"],"scientificName":"Alphavirus salmon subtype 3","synonyms":["Norwegian salmonid alphavirus"],"taxonId":344701}
```

Source SHA-256: `ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:59.296476+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"p130"}}],"contains":[{"alternativeNames":[{"fullName":{"value":"Coat protein"},"shortNames":[{"value":"C"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P03315","source":"UniProtKB"}],"value":"3.4.21.90"}],"fullName":{"value":"Capsid protein"}}},{"alternativeNames":[{"fullName":{"value":"p62"}},{"fullName":{"value":"pE2"}}],"recommendedName":{"fullName":{"value":"Precursor of protein E3/E2"}}},{"recommendedName":{"fullName":{"value":"Assembly protein E3"}}},{"alternativeNames":[{"fullName":{"value":"E2 envelope glycoprotein"}}],"recommendedName":{"fullName":{"value":"Spike glycoprotein E2"}}},{"recommendedName":{"fullName":{"value":"6K protein"}}},{"alternativeNames":[{"fullName":{"value":"E1 envelope glycoprotein"}}],"recommendedName":{"fullName":{"value":"Spike glycoprotein E1"}}}],"recommendedName":{"fullName":{"value":"Structural polyprotein"}}}
```

Source SHA-256: `ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q53AM4.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:59.296476+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.4.21.90","evidences":[{"evidenceCode":"ECO:0000250","id":"P03315","source":"UniProtKB"}],"name":"Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond."}}
```

Source SHA-256: `ad33112560822e121b7d354239830b125bea405eff79532dee89517b1094c2df`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)  
**Locator:** `lines 1-32`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 100 / 1.  
**Retrieved:** 2026-11-02T04:31:02.984412+00:00.  

```text
ID   POLS_SAV3               Reviewed;        1319 AA.
AC   Q53AM4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   24-MAY-2005, sequence version 1.
DT   28-JAN-2026, entry version 100.
DE   RecName: Full=Structural polyprotein;
DE   AltName: Full=p130;
DE   Contains:
DE     RecName: Full=Capsid protein;
DE              EC=3.4.21.90 {ECO:0000250|UniProtKB:P03315};
DE     AltName: Full=Coat protein;
DE              Short=C;
DE   Contains:
DE     RecName: Full=Precursor of protein E3/E2;
DE     AltName: Full=p62;
DE     AltName: Full=pE2;
DE   Contains:
DE     RecName: Full=Assembly protein E3;
DE   Contains:
DE     RecName: Full=Spike glycoprotein E2;
DE     AltName: Full=E2 envelope glycoprotein;
DE   Contains:
DE     RecName: Full=6K protein;
DE   Contains:
DE     RecName: Full=Spike glycoprotein E1;
DE     AltName: Full=E1 envelope glycoprotein;
OS   Alphavirus salmon subtype 3 (SAV3) (Norwegian salmonid alphavirus).
OC   Viruses; Riboviria; Orthornavirae; Kitrinoviricota; Alsuviricetes;
OC   Martellivirales; Togaviridae; Alphavirus.
OX   NCBI_TaxID=344701;
OH   NCBI_TaxID=8022; Oncorhynchus mykiss (Rainbow trout) (Salmo gairdneri).
OH   NCBI_TaxID=8030; Salmo salar (Atlantic salmon).
```

Source SHA-256: `7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q53AM4?format=txt&versions=100)  
**Locator:** `lines 119-122`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 100 / 1.  
**Retrieved:** 2026-11-02T04:31:02.984412+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Autocatalytic release of the core protein from the N-terminus
CC         of the togavirus structural polyprotein by hydrolysis of a -Trp-|-
CC         Ser- bond.; EC=3.4.21.90; Evidence={ECO:0000250|UniProtKB:P03315};
```

Source SHA-256: `7cbb74628c1b939e0285c5b363d558ced4a4e466fe72c755f1b8b743b62cbe84`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json) (zero-based source row 27). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
