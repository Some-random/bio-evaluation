# motif_position_0014

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/motif_position_0014.txt)

**Task:** `motif_position`  
**Expected answer:** **D** — 151..158

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | Unusable review | Unusable review |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVVSKDNNKRRRKETETPPPPPPVPPAGSSLAPPSAVAAIESSPEMPKRTKVQAQRKFAQGQSAPSSSSSIAYSAAAAAAGSGSGPSTSGADSNQPPIEILPNKCPKPQDFLTFLCFRGTRALPAHLDFLNQGKSKDSEASSTGANNNNNARKPNNSRASLAGNKKKRGRPAKGATKKVDVVAPIPDPTEKPSTAEKPASDKNNLIAAEAPKIPSRNPTPVLPGAVRKRAEVVTDGNRRGARGRGAGISHDKTTPAALSKDNKRRSNRASTKESKPVIDDDNSEDLDEQEADDDEDEFFSAHDATSRNGEEVKADSPVKAEPTKRGRPSAAKKAVEPAPEGQTVLKDKAPVKRVRQRESPIFIPSPESSGRMTRQRAFFEPVKVPPHKEEPGAHDPPKDEPKKQPETPPSKTEKEQEPTKQIKEAKEKTNSSIYAKEAKQQLENGDSLHGAVAKGKKSLNVFDFSSDDEQPLAKSIKLKKGAKGASPKKGGAAPIAPAARNRKAAAKKLDKEKEIEKEKQREKEEEIERDKAKEKKDKEKEKEKEKHPVPESKVEEPPSGGKRGKAGKKKAEDAPADEEDLAPPSSKKVATNARGSRKSAKSKASEDSAELEPQRSQRPSRKTKEAAAIYMGIIGHKLQLADDEEDDLSMSSFPDIPNVKEMEKMENEIKRNAAGKLNVPEASTVLSAGKSTRKPSPRPKDSPVTAPVEATRNESPSPPEAEEEKPPPPARRGRPPKQNKVNAGPAHKPRIEGMLVKKGSLAKMSEQQAKPKAKSEHSKVDSDEEEDFLINEELNETKRKLEKSFSDSDDEPLAIKVPAVAVKEKELLPPKMASPPPKLVPVPSPISVPTPAVSVAPSLAVPSILPTSTGTTQLTMLPLTAKATSSLGSMPMFPSIQASYSPLKTMEKKPPVPTSKILNVPATYALPGSASGAVSFQKTSSYLPQASPHYHSGYVRPPPTPTHQFGGGAPSGSKTPSQGSSPLKYQTPPTTYPPPIEAYQCPKINPNFLTPKYERSPLPRSSTSSFPSPSPVKFQPTSGTTATTVGTPSSATKSPLAPPPPSPPVSQVVIQTSSLNLSMSIAATVNAAPMPVASTSAAAAHQTTVATTVTATSTPPPAHSNSAATGGGAGANSDPLKDEIGSILAQATLMPSKEESGKIFGIASVSLAQSSGPDNTKCTLGKCGSIHKPVLGPVVPTEGYFGDQLSSKERRKAKVNMTHEQIQKWLIECSSNPDEIQDDLDDDFDDSLRPQQSTTPPPTRDDKELSASFSSSSKNTRGDLGKSESAWSAKGPSLKATPVLVTPPNRKELHEQADSKDCDALDYDKSSTPVNLTQKITSNESLAVEKKVNDRKGKESAKAAASKAATQPRSTAATPPTPISSTPTPASLTPSKSSPTPPPAVKQKAEKGKRNATAGGGATALASPPAAPTPANPKRTPVYNQKNAKAQQQQAETKPASNPPSGAGTKRESVYAFGKDDESGSKSGNRRRTDPSPVPAPALVPNALSERSPTKKRAAAAAAATAVQLTLSPTENCKIEGKPSKAPTGRGAKKQQQQAPAPPAPPVEASGDSDAEGATFYIPLQGAGVGGSGDGGIQGVAVKLGREGPDGPNQKVVMQATLVTKAQMDTNSKPLPESLNTNELVKTLLHAASNDAASTTTSLKSLPKASTSAAAGAAAAPGASSLVRVNSNSSLFSGSAKSRTAAQTSSTAAAVAKKYKDDTPIKMANNTAFPRHDDPTQMVEAPIFRPTEKEFADPIEFIERITPIAARFGICKIIPPASFKPECRISDEMRFTAYNQYVHKMLHRWGPSAKELSAIKKYLATQSIVMNHPPWIGGMEVDLPRLYHTVQELGGLKEVIEKKKWARVAEEMCIPKLAQDRVTKLDDIYCKYLLPYDTLSPAERQKLFDEVEADWAKREARARRNADRFVNTESVSNEEDDLSSDEDEESEEEIDGVSMECIVKGRSMPLSQFYRIARNTMALWFKSTDPTVNEVEAEFWRHVAVRDSHVCVHSGSIDSSGWGYGFPSPGPKGKGSNYARHPWNLKVLTNNSGSVLRSLGPVMGVTVPTLHVGMLFSACCWYRDPHGLSWIEYLHTGASKLWYGIPDDQSANFRAALTSLIPTHCQNKTIWLPCDTVMVPPHMLTDRGVSLCRIEQKPGEFIVVFPRAYTSSLATGYVVSESVYFATMSWLDLAKDDFRDIHESCEPAMFSLEQLLFALGYDQRVNSEALHQMLPMLNDVCEKESAAREQLRAAGVTSTEKVQAEKGQKAKKQQQPPYKSIESECDLCRANLYISMVRTEDGNIYCLQHALKNLNNGNIQAKQCKLIYAYNVDDIQQLIRQLQEKINHKAAVKKK

[Multiple Choices]
A. 92..94
B. 133..139
C. 301..304
D. 151..158
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Motif Position Prediction, which is to identify the specific positions of a conserved motif within a protein sequence. A motif is a short, recurring pattern in protein sequences that is often associated with a specific function or structure. Based on the provided protein sequence, you will need to determine the start and end positions of the motif.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry annotates 151..158 as a nuclear localization signal, supporting choice D. This is a PROSITE-ProRule computational annotation, not evidence of experimental validation.

Citations as saved: [C16](#evidence-c16), [H14](#evidence-h14).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The region at D begins with basic residues (ARK), followed after a spacer by a stronger basic cluster (KKKR...). Basic clusters separated by a spacer are characteristic of bipartite nuclear localization signals. This makes D a credible choice over the other offered intervals, though the options do not specify the motif identity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of NLS sequence patterns, applied to the sequence and candidate positions, gives a meaningful basis for choosing D without needing the exact database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The motif is not named in the prompt, but the basic pattern around D makes it the strongest offered candidate for an NLS-related motif.


### Important caveats

- Choice D covers only part of the apparent bipartite basic pattern; the supporting sequence feature extends beyond that interval.
- The supporting source annotation is computational, and the exact motif boundaries are not established experimentally by the supplied evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The region at D begins with basic residues (ARK), followed after a spacer by a stronger basic cluster (KKKR...). Basic clusters separated by a spacer are characteristic of bipartite nuclear localization signals. This makes D a credible choice over the other offered intervals, though the options do not specify the motif identity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of NLS sequence patterns, applied to the sequence and candidate positions, gives a meaningful basis for choosing D without needing the exact database record."
  },
  "case_id": "motif_position_0014",
  "expected_answer_check": {
    "evidence_ids": [
      "C16",
      "H14"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates 151..158 as a nuclear localization signal, supporting choice D. This is a PROSITE-ProRule computational annotation, not evidence of experimental validation."
  },
  "important_caveats": [
    "Choice D covers only part of the apparent bipartite basic pattern; the supporting sequence feature extends beyond that interval.",
    "The supporting source annotation is computational, and the exact motif boundaries are not established experimentally by the supplied evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The motif is not named in the prompt, but the basic pattern around D makes it the strongest offered candidate for an NLS-related motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "motif_position_0014",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates 151..158 as a nuclear localization signal, supporting choice D. This is a PROSITE-ProRule computational annotation, not evidence of experimental validation.",
    "evidence_ids": ["C16", "H14"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The region at D begins with basic residues (ARK), followed after a spacer by a stronger basic cluster (KKKR...). Basic clusters separated by a spacer are characteristic of bipartite nuclear localization signals. This makes D a credible choice over the other offered intervals, though the options do not specify the motif identity.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of NLS sequence patterns, applied to the sequence and candidate positions, gives a meaningful basis for choosing D without needing the exact database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The motif is not named in the prompt, but the basic pattern around D makes it the strongest offered candidate for an NLS-related motif."
  },
  "important_caveats": [
    "Choice D covers only part of the apparent bipartite basic pattern; the supporting sequence feature extends beyond that interval.",
    "The supporting source annotation is computational, and the exact motif boundaries are not established experimentally by the supplied evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

No visible final review text was saved. Internal model reasoning is not a substitute for a visible review and is not published. The final-content extraction failed because the saved final content was not text.

**Saved parsed visible review:** `null`.

**Saved visible final text:** empty string (`""`).

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 2351,
  "benchmark_sequence_sha256": "be658148c13eab3c3a1fc603695de8fcdf3c06d589b81be2a18610404321fae9",
  "current_entry_audit": {
    "entryVersion": 183,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-10-01",
    "sequenceVersion": 3
  },
  "current_record_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 2351,
  "current_source_sequence_sha256": "be658148c13eab3c3a1fc603695de8fcdf3c06d589b81be2a18610404321fae9",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 181,
      "exact_sequence_comparison": "matched",
      "sequence_version": 3
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VT00",
  "selected_historical_entry_version": 181,
  "selected_historical_record_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "selected_historical_source_sequence_length": 2351,
  "selected_historical_source_sequence_sha256": "be658148c13eab3c3a1fc603695de8fcdf3c06d589b81be2a18610404321fae9",
  "selected_historical_version": {
    "accession": "Q9VT00",
    "database": "Swiss-Prot",
    "entryVersion": 181,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "JARD2_DROME",
    "sequenceVersion": 3
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VT00\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":183,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-10-01\",\"sequenceVersion\":3}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17970746\",\"source\":\"PubMed\"}],\"value\":\"Protein jumonji\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"17970746\",\"source\":\"PubMed\"}],\"value\":\"dJmj\"}]}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0036004\",\"source\":\"FlyBase\"}],\"value\":\"Jumonji, AT rich interactive domain protein 2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"JmjN\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00537\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1782},\"start\":{\"modifier\":\"EXACT\",\"value\":1741}},\"type\":\"Domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"ARID\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00355\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1897},\"start\":{\"modifier\":\"EXACT\",\"value\":1805}},\"type\":\"Domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"JmjC\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00538\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":2198},\"start\":{\"modifier\":\"EXACT\",\"value\":2033}},\"type\":\"Domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":104},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":451},\"start\":{\"modifier\":\"EXACT\",\"value\":133}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":627},\"start\":{\"modifier\":\"EXACT\",\"value\":475}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":793},\"start\":{\"modifier\":\"EXACT\",\"value\":643}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1067},\"start\":{\"modifier\":\"EXACT\",\"value\":947}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1134},\"start\":{\"modifier\":\"EXACT\",\"value\":1110}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1570},\"start\":{\"modifier\":\"EXACT\",\"value\":1228}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Disordered\",\"evidences\":[{\"evidenceCode\":\"ECO:0000256\",\"id\":\"MobiDB-lite\",\"source\":\"SAM\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1951},\"start\":{\"modifier\":\"EXACT\",\"value\":1925}},\"type\":\"Region\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Nuclear localization signal\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00768\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":158},\"start\":{\"modifier\":\"EXACT\",\"value\":151}},\"type\":\"Motif\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VT00.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"citation\":{\"authors\":[\"Sasai N.\",\"Kato Y.\",\"Kimura G.\",\"Takeuchi T.\",\"Yamaguchi M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17970746\"},{\"database\":\"DOI\",\"id\":\"10.1111/j.1742-4658.2007.06135.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"6139\",\"id\":\"17970746\",\"journal\":\"FEBS J.\",\"lastPage\":\"6151\",\"publicationDate\":\"2007\",\"title\":\"The Drosophila jumonji gene encodes a JmjC-containing nuclear protein that is required for metamorphosis.\",\"volume\":\"274\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:33:46.888531+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c86e5e80115e7796b503e35b30646564a15b8efa38bb5243f064f111b4da1811",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VT00.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H1",
  "excerpt": "ID   JARD2_DROME             Reviewed;        2351 AA.\nAC   Q9VT00; Q6AWH4; Q8SXP6;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2002, sequence version 3.\nDT   28-JAN-2026, entry version 181.\nDE   RecName: Full=Jumonji, AT rich interactive domain protein 2 {ECO:0000312|FlyBase:FBgn0036004};\nDE   AltName: Full=Protein jumonji {ECO:0000303|PubMed:17970746};\nDE            Short=dJmj {ECO:0000303|PubMed:17970746};\nGN   Name=Jarid2 {ECO:0000312|FlyBase:FBgn0036004};\nGN   Synonyms=Jmj {ECO:0000303|PubMed:17970746};\nGN   ORFNames=CG3654 {ECO:0000312|FlyBase:FBgn0036004};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H2",
  "excerpt": "RN   [5] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=17970746; DOI=10.1111/j.1742-4658.2007.06135.x;\nRA   Sasai N., Kato Y., Kimura G., Takeuchi T., Yamaguchi M.;\nRT   \"The Drosophila jumonji gene encodes a JmjC-containing nuclear protein that\nRT   is required for metamorphosis.\";\nRL   FEBS J. 274:6139-6151(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H3",
  "excerpt": "FT   DOMAIN          1741..1782\nFT                   /note=\"JmjN\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00537\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 233-235",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H4",
  "excerpt": "FT   DOMAIN          1805..1897\nFT                   /note=\"ARID\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00355\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 236-238",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H5",
  "excerpt": "FT   DOMAIN          2033..2198\nFT                   /note=\"JmjC\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00538\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 239-241",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H6",
  "excerpt": "FT   REGION          1..104\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 242-244",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H7",
  "excerpt": "FT   REGION          133..451\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 245-247",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H8",
  "excerpt": "FT   REGION          475..627\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 248-250",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H9",
  "excerpt": "FT   REGION          643..793\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 251-253",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H10",
  "excerpt": "FT   REGION          947..1067\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 254-256",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H11",
  "excerpt": "FT   REGION          1110..1134\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 257-259",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H12",
  "excerpt": "FT   REGION          1228..1570\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 260-262",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H13",
  "excerpt": "FT   REGION          1925..1951\nFT                   /note=\"Disordered\"\nFT                   /evidence=\"ECO:0000256|SAM:MobiDB-lite\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 263-265",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181)

```json
{
  "entry_version": 181,
  "evidence_id": "H14",
  "excerpt": "FT   MOTIF           151..158\nFT                   /note=\"Nuclear localization signal\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU00768\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:51.212926+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 266-268",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c5087eab6edce35d6fcd43bbaa274b8a4b6eff0c95c51ede05e9f3ff14a504ae",
  "url": "https://rest.uniprot.org/unisave/Q9VT00?format=txt&versions=181"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/motif_position.json), zero-based source row 14. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
