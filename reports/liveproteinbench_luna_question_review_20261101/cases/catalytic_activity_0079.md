# catalytic_activity_0079

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.

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
A. glycyl-tRNA(Gly) + acetyl-CoA = N-acetylglycyl-tRNA(Gly) + CoA + H(+)
B. Autocatalytic release of the core protein from the N-terminus of the togavirus structural polyprotein by hydrolysis of a -Trp-|-Ser- bond.
C. N-acetyl-D-glutamate = N-acetyl-L-glutamate
D. norajmaline + S-adenosyl-L-methionine = 4-methylnorajmaline + S-adenosyl-L-homocysteine + H(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence exactly matches a UniProt entry annotated as an alphavirus structural polyprotein with the catalytic activity in choice B. The annotation is supported by transfer from another UniProt entry (ECO:0000250), so it supports the key but does not establish direct experimental verification for this sequence.

Cited evidence: [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence and its hydrophobic regions are compatible with a viral structural polyprotein, making B more plausible than the listed reactions for small soluble enzymes. That architecture alone does not establish the specific autocatalytic cleavage or the Trp-Ser bond.

**Missing item-specific fact**

> That this particular sequence is an alphavirus structural polyprotein whose capsid protein is released by autocatalytic hydrolysis at a Trp-Ser bond.

**Reason**

> Choosing B's specific reaction requires a protein-specific functional annotation or equivalent external knowledge; generic sequence architecture does not determine that cleavage chemistry.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The listed reactions are distinct, and the sequence-matched annotation supports B; no other option is comparably supported by the supplied sequence.

### Important caveats

- The sequence match applies to the current and retrieved historical UniProt records, but the author's exact source snapshot is unknown.
- The catalytic-activity evidence is transferred from another UniProt entry rather than shown here as direct experimental evidence for this sequence.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "catalytic_activity_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches a UniProt entry annotated as an alphavirus structural polyprotein with the catalytic activity in choice B. The annotation is supported by transfer from another UniProt entry (ECO:0000250), so it supports the key but does not establish direct experimental verification for this sequence.",
    "evidence_ids": [
      "C3",
      "C4",
      "C5",
      "H3"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence and its hydrophobic regions are compatible with a viral structural polyprotein, making B more plausible than the listed reactions for small soluble enzymes. That architecture alone does not establish the specific autocatalytic cleavage or the Trp-Ser bond.",
    "missing_item_specific_fact": "That this particular sequence is an alphavirus structural polyprotein whose capsid protein is released by autocatalytic hydrolysis at a Trp-Ser bond.",
    "reason": "Choosing B's specific reaction requires a protein-specific functional annotation or equivalent external knowledge; generic sequence architecture does not determine that cleavage chemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The listed reactions are distinct, and the sequence-matched annotation supports B; no other option is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "The sequence match applies to the current and retrieved historical UniProt records, but the author's exact source snapshot is unknown.",
    "The catalytic-activity evidence is transferred from another UniProt entry rather than shown here as direct experimental evidence for this sequence."
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

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json) (zero-based source row 79). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
