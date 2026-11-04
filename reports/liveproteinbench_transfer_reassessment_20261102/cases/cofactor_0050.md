# cofactor_0050

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0050.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGLQLMTPASSPMGPFFGLPWQQEAIHDNIYTPRKYQVELLEAALDHNTIVCLNSGSGKTFIAVLLSKELSYQIRGDFSKNAKRTVFLVNSEKQVSQQVSAVRTHTDLKVGEYSDLQKTQCWAKEKWYQEFETRQVLVMTCHIFLNVLKSGNVSLSNINLLVFDECHLAIQDHPYREIMKICESCQPCPRILGLTASILNGKCDPRDLEEKIQKLEKILRSNAETATDLVVLDRYASQPCEIVLDCGPYVDRSGLFQRLLNELDEALNFLIDCNISTHSKERDSTIISKQILSDCRAVLLVLGPWCADKVAGMMVRELQKYIKHEQEELHRKFLLFTDTILRKIHALCEEHFSPASLDMKFVTPKVIKLLEILRKYKPYERQQFESVEWYNNRNQDNYVSWSDSEDDDDDEDEEIEEKEKTETSFPSPFTNILCGIIFVERRYTAVVLNRLIKEAGKQDPELAYISSNFITGHGIGKNQPRNKQMEVEFRKQEEVLRKFRAHETNLLIATSIVEEGVDIPKCNLVVRFDLPSEYRSYVQSKGRARAPISNYIMLADSDKIKTFEEDLKTYKAIEKILRNKCSKSIDCGNTESEPVVDDDEIFPPYVLRQDDGSPRVTINTAIGHINRYCARLPSDPFTHLAPKCKTREMSDGPYRSTLYLPINSPLRAPIVGPPMNCARLAERAVALICCKKLHEIGELDDHLMPVGKETVKYEEELDLHDEEETSVPGRPGSTKRRQCYPKAIPECLRNSYPKPGQPCYLYVIGMVLTTPLPDELNFRRRKLYPPEDTTRCFGILTAKPIPQIPHFPVYTRSGEVTISIELKKSGFTLNLEQLELITRLHQYIFSHILRLEKPALEFKPTVADCAYCVLPLNVVNDSGTLDIDFKFVEDIEKSEARTGIPNTQYSAESPFIFKLEDYQDAVIIPRYRNFDQPHRFYVADVYTDLTPLSKFPSPEYETFAEYYKTKYNLDLTNLNQPLLDVDHTSSRLNLLTPRHLNQKGKALPLSSAEKRKAKWESLQNKQILVPELCAIHPVPASLWRKAVCLPSILYRLHCLLTAEELRAQTAIDAGVGVKSLPEDFRYPNLDFGWKRSIDSKTFISSQSSSAVESEGDCRLNTTMVPDSATSSAANHVIYTQTNDQMSVNCTPLCQKSLSDLRGVCFSEDYKAINGVSCNGVTSDSEAESGVCFQKDERIACTQEIPEKSTSFHIQNLPKENQPILNECTLSKKFLDGNVSKPTSDECPSTCTSDMQYESGLSNGYSSKTLGPNPGLILQALTLSNASDGFNLERLEMLGDSFLKHAITTYLFCTYPDAHEGRLSYMRSKKVSNCNLYRLGKKKGSPSRMVVSIFDPPVNWLPPGYIVNQDKSSDKWESNETSGEGVMANGKIDEDFDDDDEEDEDLMWRNPKEETDFDDDFLEYDQEHIKFIDSMLMGSGAFVKKIPLSSFAPPDQNYEWRAPKKPLLESAQFPSEFDDFDYSSWDAMCYLDPSKAVEEDDFVVGFWNPSEENCGTDVGKQSISYDLHTEQCIADKSIADCVEALLGCYLTSCGERAAQLFLCSLGLKVLPQVRRSVTSTNSISASSSYQKTSTRDICTLNSELSSCKGVEYGYLKIPPRCMFEHPDAEKTLDHLISGFENFEKKINYPFKNKAYLLQAFTHASYHYNTITDCYQRLEFLGDAILDYLITKHLYEDPRQHSPGVLTDLRSALVNNTIFASLAVKYDYHKYFKAISPELFHVIDDFVQFQLEKNEMQGMDSELRRSEEDEEKEEDIEVPKAMGDIFESLAGAIYMDSGMSLETVWRVYYPMMHPLIEKFSANVPRSPVRELLEMEPETAKFSPAERTYDGKVRVTVEVVGKGKFKGVGRSYRIAKSAAARRALRSLKANQSQVPNS

[Multiple Choices]
A. FMN
B. Mg(2+)
C. NAD(+)
D. Zn(2+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence matches the annotated protein, whose UniProt cofactor annotation lists Mg(2+) and Mn(2+) and says it binds two magnesium or manganese ions per subunit. That annotation is transferred by similarity (ECO:0000250), rather than direct experimental evidence for this exact protein; Mg(2+) is nevertheless a supported choice among the offered options.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence is consistent with a Dicer-family RNase III nuclease, whose conserved catalytic domains use divalent metal ions to support phosphodiester-bond cleavage; Mg(2+) is a common catalytic ion for this nuclease family. This meaningfully favors Mg(2+) over FMN, NAD(+), or Zn(2+) among the options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable family-level inference provides a credible basis for selecting Mg(2+) without needing the exact protein's database record. This is a probabilistic inference, not proof of the cofactor usage of this particular protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source also lists Mn(2+), but it is not offered; among the four presented options, Mg(2+) is the defensible choice.


### Important caveats

- The supporting annotation is similarity-transferred, not direct experimental evidence for this exact protein.
- The source reports magnesium or manganese binding, so Mg(2+) is not necessarily the only biologically relevant metal.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence is consistent with a Dicer-family RNase III nuclease, whose conserved catalytic domains use divalent metal ions to support phosphodiester-bond cleavage; Mg(2+) is a common catalytic ion for this nuclease family. This meaningfully favors Mg(2+) over FMN, NAD(+), or Zn(2+) among the options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable family-level inference provides a credible basis for selecting Mg(2+) without needing the exact protein's database record. This is a probabilistic inference, not proof of the cofactor usage of this particular protein."
  },
  "case_id": "cofactor_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, whose UniProt cofactor annotation lists Mg(2+) and Mn(2+) and says it binds two magnesium or manganese ions per subunit. That annotation is transferred by similarity (ECO:0000250), rather than direct experimental evidence for this exact protein; Mg(2+) is nevertheless a supported choice among the offered options."
  },
  "important_caveats": [
    "The supporting annotation is similarity-transferred, not direct experimental evidence for this exact protein.",
    "The source reports magnesium or manganese binding, so Mg(2+) is not necessarily the only biologically relevant metal."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source also lists Mn(2+), but it is not offered; among the four presented options, Mg(2+) is the defensible choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, whose UniProt cofactor annotation lists Mg(2+) and Mn(2+) and says it binds two magnesium or manganese ions per subunit. That annotation is transferred by similarity (ECO:0000250), rather than direct experimental evidence for this exact protein; Mg(2+) is nevertheless a supported choice among the offered options.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence is consistent with a Dicer-family RNase III nuclease, whose conserved catalytic domains use divalent metal ions to support phosphodiester-bond cleavage; Mg(2+) is a common catalytic ion for this nuclease family. This meaningfully favors Mg(2+) over FMN, NAD(+), or Zn(2+) among the options.",
    "missing_item_specific_fact": "",
    "reason": "A transferable family-level inference provides a credible basis for selecting Mg(2+) without needing the exact protein's database record. This is a probabilistic inference, not proof of the cofactor usage of this particular protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source also lists Mn(2+), but it is not offered; among the four presented options, Mg(2+) is the defensible choice."
  },
  "important_caveats": [
    "The supporting annotation is similarity-transferred, not direct experimental evidence for this exact protein.",
    "The source reports magnesium or manganese binding, so Mg(2+) is not necessarily the only biologically relevant metal."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H3) explicitly lists Mg(2+) as a cofactor for this protein (Endoribonuclease Dicer-L, EC 3.1.26.3), noting it 'Binds 2 magnesium or manganese ions per subunit.' The evidence code ECO:0000250 indicates this is inferred by similarity from human Dicer (Q9UPY3), but the RNase III family requirement for divalent metal ions (Mg2+/Mn2+) is well-established. Among the four choices, Mg(2+) is the correct cofactor. Mn(2+) is also listed but is not among the options.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark DEDD catalytic tetrad of the RNase III superfamily (visible as 'DEDDDDDEDEE' in the sequence) and a large multi-domain architecture (~1891 AA) with PAZ, RNase III, and helicase domains characteristic of Dicer. RNase III enzymes universally require divalent metal ions, specifically Mg2+, to coordinate the scissile phosphate during phosphodiester bond hydrolysis. This is a deeply conserved family-level property observed across bacterial RNase III, human Dicer, and other homologs. Among the choices: FMN is for flavoprotein oxidoreductases, NAD+ for dehydrogenases, and Zn2+ for metalloproteases or some restriction endonucleases—none match the RNase III mechanism. The DEDD motif specifically coordinates Mg2+ (not Zn2+), making B the clear answer via family-level inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the DEDD catalytic motif and the overall Dicer/RNase III domain architecture allows transferable inference from well-studied RNase III family members (bacterial RNase III, human Dicer) that these enzymes require Mg2+ for catalysis. This family-level knowledge meaningfully distinguishes Mg(2+) from FMN, NAD+, and Zn(2+) among the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although Mn(2+) is also annotated as a cofactor, it is not among the offered choices. Among A-D, only Mg(2+) is consistent with the RNase III catalytic mechanism. Zn(2+) is used by some nucleases but not by RNase III enzymes with the DEDD motif.


### Important caveats

- The UniProt cofactor annotation is based on similarity transfer (ECO:0000250) from human Dicer (Q9UPY3), not direct experimental characterization of Xenopus Dicer-L.
- Mn(2+) is also listed as an alternative cofactor in the annotation but is not among the answer choices, so it does not create ambiguity among the given options.
- The sequence is 1891 AA, consistent with full-length Dicer, but the model must rely on domain-level features rather than exact sequence identity to a known protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark DEDD catalytic tetrad of the RNase III superfamily (visible as 'DEDDDDDEDEE' in the sequence) and a large multi-domain architecture (~1891 AA) with PAZ, RNase III, and helicase domains characteristic of Dicer. RNase III enzymes universally require divalent metal ions, specifically Mg2+, to coordinate the scissile phosphate during phosphodiester bond hydrolysis. This is a deeply conserved family-level property observed across bacterial RNase III, human Dicer, and other homologs. Among the choices: FMN is for flavoprotein oxidoreductases, NAD+ for dehydrogenases, and Zn2+ for metalloproteases or some restriction endonucleases—none match the RNase III mechanism. The DEDD motif specifically coordinates Mg2+ (not Zn2+), making B the clear answer via family-level inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the DEDD catalytic motif and the overall Dicer/RNase III domain architecture allows transferable inference from well-studied RNase III family members (bacterial RNase III, human Dicer) that these enzymes require Mg2+ for catalysis. This family-level knowledge meaningfully distinguishes Mg(2+) from FMN, NAD+, and Zn(2+) among the offered choices."
  },
  "case_id": "cofactor_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly lists Mg(2+) as a cofactor for this protein (Endoribonuclease Dicer-L, EC 3.1.26.3), noting it 'Binds 2 magnesium or manganese ions per subunit.' The evidence code ECO:0000250 indicates this is inferred by similarity from human Dicer (Q9UPY3), but the RNase III family requirement for divalent metal ions (Mg2+/Mn2+) is well-established. Among the four choices, Mg(2+) is the correct cofactor. Mn(2+) is also listed but is not among the options."
  },
  "important_caveats": [
    "The UniProt cofactor annotation is based on similarity transfer (ECO:0000250) from human Dicer (Q9UPY3), not direct experimental characterization of Xenopus Dicer-L.",
    "Mn(2+) is also listed as an alternative cofactor in the annotation but is not among the answer choices, so it does not create ambiguity among the given options.",
    "The sequence is 1891 AA, consistent with full-length Dicer, but the model must rely on domain-level features rather than exact sequence identity to a known protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although Mn(2+) is also annotated as a cofactor, it is not among the offered choices. Among A-D, only Mg(2+) is consistent with the RNase III catalytic mechanism. Zn(2+) is used by some nucleases but not by RNase III enzymes with the DEDD motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) explicitly lists Mg(2+) as a cofactor for this protein (Endoribonuclease Dicer-L, EC 3.1.26.3), noting it 'Binds 2 magnesium or manganese ions per subunit.' The evidence code ECO:0000250 indicates this is inferred by similarity from human Dicer (Q9UPY3), but the RNase III family requirement for divalent metal ions (Mg2+/Mn2+) is well-established. Among the four choices, Mg(2+) is the correct cofactor. Mn(2+) is also listed but is not among the options.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark DEDD catalytic tetrad of the RNase III superfamily (visible as 'DEDDDDDEDEE' in the sequence) and a large multi-domain architecture (~1891 AA) with PAZ, RNase III, and helicase domains characteristic of Dicer. RNase III enzymes universally require divalent metal ions, specifically Mg2+, to coordinate the scissile phosphate during phosphodiester bond hydrolysis. This is a deeply conserved family-level property observed across bacterial RNase III, human Dicer, and other homologs. Among the choices: FMN is for flavoprotein oxidoreductases, NAD+ for dehydrogenases, and Zn2+ for metalloproteases or some restriction endonucleases—none match the RNase III mechanism. The DEDD motif specifically coordinates Mg2+ (not Zn2+), making B the clear answer via family-level inference.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the DEDD catalytic motif and the overall Dicer/RNase III domain architecture allows transferable inference from well-studied RNase III family members (bacterial RNase III, human Dicer) that these enzymes require Mg2+ for catalysis. This family-level knowledge meaningfully distinguishes Mg(2+) from FMN, NAD+, and Zn(2+) among the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although Mn(2+) is also annotated as a cofactor, it is not among the offered choices. Among A-D, only Mg(2+) is consistent with the RNase III catalytic mechanism. Zn(2+) is used by some nucleases but not by RNase III enzymes with the DEDD motif."
  },
  "important_caveats": [
    "The UniProt cofactor annotation is based on similarity transfer (ECO:0000250) from human Dicer (Q9UPY3), not direct experimental characterization of Xenopus Dicer-L.",
    "Mn(2+) is also listed as an alternative cofactor in the annotation but is not among the answer choices, so it does not create ambiguity among the given options.",
    "The sequence is 1891 AA, consistent with full-length Dicer, but the model must rely on domain-level features rather than exact sequence identity to a known protein."
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
  "benchmark_sequence_length": 1891,
  "benchmark_sequence_sha256": "f0d38653f552392ea0c0e2a67360b0747665e7fa5312e459ceb4a963f9fffff9",
  "current_entry_audit": {
    "entryVersion": 17,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2023-02-22",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 1891,
  "current_source_sequence_sha256": "f0d38653f552392ea0c0e2a67360b0747665e7fa5312e459ceb4a963f9fffff9",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 15,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A974H8H3",
  "selected_historical_entry_version": 15,
  "selected_historical_record_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "selected_historical_source_sequence_length": 1891,
  "selected_historical_source_sequence_sha256": "f0d38653f552392ea0c0e2a67360b0747665e7fa5312e459ceb4a963f9fffff9",
  "selected_historical_version": {
    "accession": "A0A974H8H3",
    "database": "Swiss-Prot",
    "entryVersion": 15,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DICRL_XENLA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A974H8H3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":17,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2023-02-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"African clawed frog\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Amphibia\",\"Batrachia\",\"Anura\",\"Pipoidea\",\"Pipidae\",\"Xenopodinae\",\"Xenopus\",\"Xenopus\"],\"scientificName\":\"Xenopus laevis\",\"taxonId\":8355}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"value\":\"3.1.26.3\"}],\"fullName\":{\"value\":\"Endoribonuclease Dicer-L\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A974H8H3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9UPY3\",\"source\":\"UniProtKB\"}],\"name\":\"Mg(2+)\"},{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9UPY3\",\"source\":\"UniProtKB\"}],\"name\":\"Mn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9UPY3\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 2 magnesium or manganese ions per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:26:07.960553+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b4e859fc458998c778dc7d17ac18a1b291d83251adafa61508017f28421fce75",
  "url": "https://rest.uniprot.org/uniprotkb/A0A974H8H3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H1",
  "excerpt": "ID   DICRL_XENLA             Reviewed;        1891 AA.\nAC   A0A974H8H3; A0A1L8F9L1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-FEB-2023, sequence version 1.\nDT   28-JAN-2026, entry version 15.\nDE   RecName: Full=Endoribonuclease Dicer-L;\nDE            EC=3.1.26.3;\nGN   Name=dicer1.L; Synonyms=dicer1;\nOS   Xenopus laevis (African clawed frog).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Amphibia;\nOC   Batrachia; Anura; Pipoidea; Pipidae; Xenopodinae; Xenopus; Xenopus.\nOX   NCBI_TaxID=8355;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Endoribonuclease Dicer-L;\nDE            EC=3.1.26.3;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15)

```json
{
  "entry_version": 15,
  "evidence_id": "H3",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000250|UniProtKB:Q9UPY3};\nCC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;\nCC         Evidence={ECO:0000250|UniProtKB:Q9UPY3};\nCC       Note=Binds 2 magnesium or manganese ions per subunit.\nCC       {ECO:0000250|UniProtKB:Q9UPY3};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:10.677603+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-71",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "41772a767bfa5445739bab2f1bdd061396d2f2d9dfae9600af1001db9cb33496",
  "url": "https://rest.uniprot.org/unisave/A0A974H8H3?format=txt&versions=15"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 50. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
