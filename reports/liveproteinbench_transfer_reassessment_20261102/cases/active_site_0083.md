# active_site_0083

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0083.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 154 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAAVTRYSGKVVVVTGGSRGIGAAIVRAFVDSGAQVVFCDKDEAGGRALEQELSGTVFIPGDVTQERDLQTLVSETLSRFGHLDCVVNNAGYHPPAQLPEETSAQGFRQLLEVNLLGTYTLIKLALPHLRKSRGNIINISSLVGAIGQSQALTYVATKGAVTAMTKALALDESRHGVRVNCISPGNIWTPLWEELAASTSDPRATILEGTLAQPLGRMGQPAEVAAAAVFLASEATFCTGLELLVTGGAELGYGRKASKSSLGEVPTLPPNVH

[Multiple Choices]
A. Position 241 (Lowers pKa of active site Tyr)
B. Position 242 (Charge relay system)
C. Position 210 (Proton donor)
D. Position 154 (Proton acceptor)
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

> The sequence-matched UniProt annotation assigns position 154 the role “Proton acceptor.” This is computationally supported by a PROSITE-ProRule annotation, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal glycine-rich cofactor-binding motif characteristic of SDR enzymes and a YxxxK motif: position 154 is Tyr and position 158 is Lys. In SDR-family enzymes, the conserved Tyr commonly serves as the catalytic acid/base, while the nearby Lys helps tune its chemistry. Thus the transferable family pattern supports D; the other listed positions are not the conserved catalytic Tyr.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence motifs meaningfully distinguish the catalytic Tyr at position 154 and its proton-acceptor role from the alternatives, without needing the exact protein’s database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered options, position 154 is the Tyr in the characteristic SDR catalytic motif; the choices do not present another comparably supported catalytic residue and role.


### Important caveats

- The source annotation is rule-based computational evidence rather than direct experimental validation.
- The biological inference supports the offered choice but does not independently establish every detail of the enzyme’s catalytic mechanism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich cofactor-binding motif characteristic of SDR enzymes and a YxxxK motif: position 154 is Tyr and position 158 is Lys. In SDR-family enzymes, the conserved Tyr commonly serves as the catalytic acid/base, while the nearby Lys helps tune its chemistry. Thus the transferable family pattern supports D; the other listed positions are not the conserved catalytic Tyr.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence motifs meaningfully distinguish the catalytic Tyr at position 154 and its proton-acceptor role from the alternatives, without needing the exact protein’s database annotation."
  },
  "case_id": "active_site_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns position 154 the role “Proton acceptor.” This is computationally supported by a PROSITE-ProRule annotation, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The source annotation is rule-based computational evidence rather than direct experimental validation.",
    "The biological inference supports the offered choice but does not independently establish every detail of the enzyme’s catalytic mechanism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered options, position 154 is the Tyr in the characteristic SDR catalytic motif; the choices do not present another comparably supported catalytic residue and role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns position 154 the role “Proton acceptor.” This is computationally supported by a PROSITE-ProRule annotation, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich cofactor-binding motif characteristic of SDR enzymes and a YxxxK motif: position 154 is Tyr and position 158 is Lys. In SDR-family enzymes, the conserved Tyr commonly serves as the catalytic acid/base, while the nearby Lys helps tune its chemistry. Thus the transferable family pattern supports D; the other listed positions are not the conserved catalytic Tyr.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence motifs meaningfully distinguish the catalytic Tyr at position 154 and its proton-acceptor role from the alternatives, without needing the exact protein’s database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered options, position 154 is the Tyr in the characteristic SDR catalytic motif; the choices do not present another comparably supported catalytic residue and role."
  },
  "important_caveats": [
    "The source annotation is rule-based computational evidence rather than direct experimental validation.",
    "The biological inference supports the offered choice but does not independently establish every detail of the enzyme’s catalytic mechanism."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H2) explicitly records ACT_SITE 154 as 'Proton acceptor' via PROSITE-ProRule:PRU10001 (ECO:0000255, computational/similarity-based). Position 154 in the supplied sequence is Tyrosine (Y), embedded in the canonical SDR YxxxK motif (Y154-V-A-T-K158). The SDR catalytic mechanism, in which the Tyr serves as the catalytic acid/base (proton acceptor/donor), is extensively validated by crystal structures and mutagenesis across the family. The annotation is computational rather than directly experimental for this specific protein, but it is grounded in a deeply characterized family mechanism.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark SDR (Short-chain Dehydrogenase/Reductase) family signatures: (1) a Rossmann-fold NAD-binding motif 'VVVVTGGSRGIGAAIVRAF' near the N-terminus (TGxxxGGxG at ~positions 16-22); (2) the catalytic tetrad Ser-Tyr-Lys-Asn, specifically the SxxxT motif (S149-Q-A-L-T153) immediately preceding Y154, and the YxxxK motif (Y154-V-A-T-K158). In SDRs, the conserved Tyr in the YxxxK motif is universally the catalytic proton acceptor/donor, while the Lys lowers its pKa. This is among the most well-characterized catalytic motifs in enzymology. Among the choices: A (L241, 'Lowers pKa of Tyr') is wrong because it is the Lys158, not a Leucine, that performs this role; B (E242, 'Charge relay system') invokes serine-protease chemistry, irrelevant to SDRs; C (T210, 'Proton donor') is a Threonine far from the catalytic center and not part of the YxxxK tetrad. Only D (Y154, 'Proton acceptor') matches the SDR catalytic Tyr. A model familiar with SDR family architecture can identify the YxxxK motif from the sequence and select D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the SDR family (NAD-binding Rossmann fold + SxxxT...YxxxK catalytic tetrad) is transferable family-level knowledge learned from hundreds of characterized SDRs. The YxxxK motif is one of the most textbook catalytic arrangements. The sequence visibly contains this motif at Y154-x-x-x-K158, and the other three choices are eliminated by basic SDR mechanistic knowledge (Leucine cannot lower Tyr pKa; charge relay is not SDR chemistry; Thr210 is not in the catalytic tetrad). No target-specific database lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices are well-separated by SDR family knowledge. Only the Tyr in the YxxxK motif is the catalytic proton acceptor in SDRs. The distractors invoke chemically or mechanistically incompatible roles (Leucine lowering pKa, charge relay, a distant Thr as proton donor) that do not match any known SDR mechanism.


### Important caveats

- The active-site annotation is computational (PROSITE-ProRule pattern match, ECO:0000255), not direct experimental evidence on this specific mouse protein. However, the SDR catalytic mechanism is one of the most experimentally validated in enzymology.
- The Tyr in SDRs functions as both proton acceptor and donor depending on reaction direction; the annotation labels it 'Proton acceptor,' which is one valid role and distinguishes it from choice C ('Proton donor' at a different residue).
- The reviewer-only evidence confirms the sequence matches UniProt E9Q3D4 (DHB14_MOUSE, L-fucose dehydrogenase / HSD17B14), but this identity was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark SDR (Short-chain Dehydrogenase/Reductase) family signatures: (1) a Rossmann-fold NAD-binding motif 'VVVVTGGSRGIGAAIVRAF' near the N-terminus (TGxxxGGxG at ~positions 16-22); (2) the catalytic tetrad Ser-Tyr-Lys-Asn, specifically the SxxxT motif (S149-Q-A-L-T153) immediately preceding Y154, and the YxxxK motif (Y154-V-A-T-K158). In SDRs, the conserved Tyr in the YxxxK motif is universally the catalytic proton acceptor/donor, while the Lys lowers its pKa. This is among the most well-characterized catalytic motifs in enzymology. Among the choices: A (L241, 'Lowers pKa of Tyr') is wrong because it is the Lys158, not a Leucine, that performs this role; B (E242, 'Charge relay system') invokes serine-protease chemistry, irrelevant to SDRs; C (T210, 'Proton donor') is a Threonine far from the catalytic center and not part of the YxxxK tetrad. Only D (Y154, 'Proton acceptor') matches the SDR catalytic Tyr. A model familiar with SDR family architecture can identify the YxxxK motif from the sequence and select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the SDR family (NAD-binding Rossmann fold + SxxxT...YxxxK catalytic tetrad) is transferable family-level knowledge learned from hundreds of characterized SDRs. The YxxxK motif is one of the most textbook catalytic arrangements. The sequence visibly contains this motif at Y154-x-x-x-K158, and the other three choices are eliminated by basic SDR mechanistic knowledge (Leucine cannot lower Tyr pKa; charge relay is not SDR chemistry; Thr210 is not in the catalytic tetrad). No target-specific database lookup is required."
  },
  "case_id": "active_site_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H2) explicitly records ACT_SITE 154 as 'Proton acceptor' via PROSITE-ProRule:PRU10001 (ECO:0000255, computational/similarity-based). Position 154 in the supplied sequence is Tyrosine (Y), embedded in the canonical SDR YxxxK motif (Y154-V-A-T-K158). The SDR catalytic mechanism, in which the Tyr serves as the catalytic acid/base (proton acceptor/donor), is extensively validated by crystal structures and mutagenesis across the family. The annotation is computational rather than directly experimental for this specific protein, but it is grounded in a deeply characterized family mechanism."
  },
  "important_caveats": [
    "The active-site annotation is computational (PROSITE-ProRule pattern match, ECO:0000255), not direct experimental evidence on this specific mouse protein. However, the SDR catalytic mechanism is one of the most experimentally validated in enzymology.",
    "The Tyr in SDRs functions as both proton acceptor and donor depending on reaction direction; the annotation labels it 'Proton acceptor,' which is one valid role and distinguishes it from choice C ('Proton donor' at a different residue).",
    "The reviewer-only evidence confirms the sequence matches UniProt E9Q3D4 (DHB14_MOUSE, L-fucose dehydrogenase / HSD17B14), but this identity was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are well-separated by SDR family knowledge. Only the Tyr in the YxxxK motif is the catalytic proton acceptor in SDRs. The distractors invoke chemically or mechanistically incompatible roles (Leucine lowering pKa, charge relay, a distant Thr as proton donor) that do not match any known SDR mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H2) explicitly records ACT_SITE 154 as 'Proton acceptor' via PROSITE-ProRule:PRU10001 (ECO:0000255, computational/similarity-based). Position 154 in the supplied sequence is Tyrosine (Y), embedded in the canonical SDR YxxxK motif (Y154-V-A-T-K158). The SDR catalytic mechanism, in which the Tyr serves as the catalytic acid/base (proton acceptor/donor), is extensively validated by crystal structures and mutagenesis across the family. The annotation is computational rather than directly experimental for this specific protein, but it is grounded in a deeply characterized family mechanism.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark SDR (Short-chain Dehydrogenase/Reductase) family signatures: (1) a Rossmann-fold NAD-binding motif 'VVVVTGGSRGIGAAIVRAF' near the N-terminus (TGxxxGGxG at ~positions 16-22); (2) the catalytic tetrad Ser-Tyr-Lys-Asn, specifically the SxxxT motif (S149-Q-A-L-T153) immediately preceding Y154, and the YxxxK motif (Y154-V-A-T-K158). In SDRs, the conserved Tyr in the YxxxK motif is universally the catalytic proton acceptor/donor, while the Lys lowers its pKa. This is among the most well-characterized catalytic motifs in enzymology. Among the choices: A (L241, 'Lowers pKa of Tyr') is wrong because it is the Lys158, not a Leucine, that performs this role; B (E242, 'Charge relay system') invokes serine-protease chemistry, irrelevant to SDRs; C (T210, 'Proton donor') is a Threonine far from the catalytic center and not part of the YxxxK tetrad. Only D (Y154, 'Proton acceptor') matches the SDR catalytic Tyr. A model familiar with SDR family architecture can identify the YxxxK motif from the sequence and select D.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the SDR family (NAD-binding Rossmann fold + SxxxT...YxxxK catalytic tetrad) is transferable family-level knowledge learned from hundreds of characterized SDRs. The YxxxK motif is one of the most textbook catalytic arrangements. The sequence visibly contains this motif at Y154-x-x-x-K158, and the other three choices are eliminated by basic SDR mechanistic knowledge (Leucine cannot lower Tyr pKa; charge relay is not SDR chemistry; Thr210 is not in the catalytic tetrad). No target-specific database lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices are well-separated by SDR family knowledge. Only the Tyr in the YxxxK motif is the catalytic proton acceptor in SDRs. The distractors invoke chemically or mechanistically incompatible roles (Leucine lowering pKa, charge relay, a distant Thr as proton donor) that do not match any known SDR mechanism."
  },
  "important_caveats": [
    "The active-site annotation is computational (PROSITE-ProRule pattern match, ECO:0000255), not direct experimental evidence on this specific mouse protein. However, the SDR catalytic mechanism is one of the most experimentally validated in enzymology.",
    "The Tyr in SDRs functions as both proton acceptor and donor depending on reaction direction; the annotation labels it 'Proton acceptor,' which is one valid role and distinguishes it from choice C ('Proton donor' at a different residue).",
    "The reviewer-only evidence confirms the sequence matches UniProt E9Q3D4 (DHB14_MOUSE, L-fucose dehydrogenase / HSD17B14), but this identity was not provided to the evaluated model."
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
  "benchmark_sequence_length": 273,
  "benchmark_sequence_sha256": "656e530c86ac38dd860b870f49c25d1c6de9ec15bf60eef81798043517661097",
  "current_entry_audit": {
    "entryVersion": 97,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-04-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 273,
  "current_source_sequence_sha256": "656e530c86ac38dd860b870f49c25d1c6de9ec15bf60eef81798043517661097",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 95,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E9Q3D4",
  "selected_historical_entry_version": 95,
  "selected_historical_record_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "selected_historical_source_sequence_length": 273,
  "selected_historical_source_sequence_sha256": "656e530c86ac38dd860b870f49c25d1c6de9ec15bf60eef81798043517661097",
  "selected_historical_version": {
    "accession": "E9Q3D4",
    "database": "Swiss-Prot",
    "entryVersion": 95,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHB14_MOUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E9Q3D4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":97,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-04-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Mouse\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Mus\",\"Mus\"],\"scientificName\":\"Mus musculus\",\"taxonId\":10090}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Hydroxysteroid 17-beta dehydrogenase 14\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"value\":\"1.1.1.122\"}],\"fullName\":{\"value\":\"L-fucose dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU10001\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":154},\"start\":{\"modifier\":\"EXACT\",\"value\":154}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":19},\"start\":{\"modifier\":\"EXACT\",\"value\":19}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":21},\"start\":{\"modifier\":\"EXACT\",\"value\":21}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":40},\"start\":{\"modifier\":\"EXACT\",\"value\":40}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":41},\"start\":{\"modifier\":\"EXACT\",\"value\":41}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":62},\"start\":{\"modifier\":\"EXACT\",\"value\":62}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":63},\"start\":{\"modifier\":\"EXACT\",\"value\":63}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":89},\"start\":{\"modifier\":\"EXACT\",\"value\":89}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":154},\"start\":{\"modifier\":\"EXACT\",\"value\":154}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":158},\"start\":{\"modifier\":\"EXACT\",\"value\":158}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":187},\"start\":{\"modifier\":\"EXACT\",\"value\":187}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":189},\"start\":{\"modifier\":\"EXACT\",\"value\":189}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E9Q3D4.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BPX1\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57540\",\"name\":\"NAD(+)\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":191},\"start\":{\"modifier\":\"EXACT\",\"value\":191}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:28:08.225634+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bd47482a576a5aceb231929788ca2f5078c56926357a52cc62412f8c497bcd3f",
  "url": "https://rest.uniprot.org/uniprotkb/E9Q3D4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H1",
  "excerpt": "ID   DHB14_MOUSE             Reviewed;         273 AA.\nAC   E9Q3D4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-APR-2011, sequence version 1.\nDT   28-JAN-2026, entry version 95.\nDE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000250|UniProtKB:Q9BPX1};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\nGN   Name=Hsd17b14 {ECO:0000312|MGI:MGI:1913315}; Synonyms=Dhrs10, retSDR3;\nOS   Mus musculus (Mouse).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Mus; Mus.\nOX   NCBI_TaxID=10090;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H2",
  "excerpt": "FT   ACT_SITE        154\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU10001\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 124-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H3",
  "excerpt": "FT   BINDING         19\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BPX1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         21\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BPX1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 131-134",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         40\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BPX1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 135-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         41\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BPX1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 139-142",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         62\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BPX1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 143-146",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         63\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BPX1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 147-150",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         89\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BPX1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 151-154",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         154\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BPX1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 155-158",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         158\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BPX1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 159-162",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         187\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BPX1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 163-166",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         189\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BPX1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 167-170",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95)

```json
{
  "entry_version": 95,
  "evidence_id": "H14",
  "excerpt": "FT   BINDING         191\nFT                   /ligand=\"NAD(+)\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57540\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BPX1\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:17.926007+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 171-174",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e2e2499fa9a4008684b0b5a4af04f9fe0ed35d0a8b57fcdbdd5131ae007b3673",
  "url": "https://rest.uniprot.org/unisave/E9Q3D4?format=txt&versions=95"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 83. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
