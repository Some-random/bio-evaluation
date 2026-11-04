# pathway_0118

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0118.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Membrane lipid metabolism. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | Unusable review | Unusable review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKTEDMALVFSKLILNPITKRQILNLFKKDDNGNLIIENYIDAYMKGEDINSLGYKTLKSVLDNGLKTFAGEIYKENFKDFLKDPLFKKGLISVVRGLGYFGVKRPFVSGAPFLVVWDVTYACNLRCKHCYANAGKPLEDELNTEEALKTIDILANSGVVAIAFSGGEPLMRKDLFELIDRAKDYNMQVSIASNGTMLNKTNAKKLKEHKVDFVQISLDGTKETHEKFRGIKGIYDKTIEGIKNVVDEDIFCAIATTATKLNYRDVPKVMDLAEELNVNYFMLYNYIPVGVGDYDIDLSPEEREELLNLLWEKLNNDTGKKYRTAFLSTAPYYSRTALEHNKYYLASHFANVDLGENERLKSLANFIGGCGCGRFYLSLRANGDIQPCVFFPLKLGNIKSFKDENDFLEFWRNNKILNDLRDRDKLKICGSCMYKYVCGGCRARAYSYYDDYLREDPGCILTKNLK

[Multiple Choices]
A. Steroid biosynthesis
B. iron-sulfur cluster biosynthesis. .
C. IMP biosynthesis via de novo pathway
D. Membrane lipid metabolism. .
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

**Saved status:** `invalid_review`.

**This response is not a usable structured review.** Its saved text is preserved below; any labels in that text are excluded from the summary counts.

**Validation errors:** `invalid_json:Expecting property name enclosed in double quotes: line 13 column 3 (char 1260)`.

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt record, which annotates its pathway as membrane lipid metabolism. This is a database pathway annotation linked to a publication, not by itself independent experimental validation of the pathway assignment.",
    "evidence_ids": ["C5", "H3", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a CxxxCxxC cysteine motif and additional cysteine-rich regions consistent with a radical-SAM enzyme using iron-sulfur cofactors. Transferable family-level recognition of archaeal radical-SAM lipid-modifying enzymes can favor a role in membrane lipid metabolism. The iron-sulfur cofactors do not imply that the protein functions in iron-sulfur cluster biosynthesis; that pathway concerns cluster assembly machinery.",
    "missing_item_specific_fact": "",
    "reason": "The motifs alone do not establish a pathway, but family-level similarity to specialized archaeal lipid enzymes provides a meaningful basis for choosing D over the unrelated alternatives. This is a probabilistic inference, not proof from sequence motifs alone.",
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the sequence and pathway choices; in particular, iron-sulfur cofactor binding is not equivalent to a role in iron-sulfur cluster biosynthesis."
  },
  "important_caveats": [
    "The pathway annotation supports the key, but the cited annotation evidence is not itself a direct assay of pathway function.",
    "A radical-SAM motif indicates enzyme/cofactor features, not a unique pathway; the lipid-pathway inference relies on family-level transfer as well."
  ]
}
```

</details>

**Saved parsed visible review:** `null`.

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (F8AME3) explicitly annotates the pathway as 'Membrane lipid metabolism' (C5, H3) with evidence code ECO:0000305 (inferred by curator) based on PubMed:38898040 (Nat. Commun. 2024). The protein is GMGT synthase (Gms), a radical SAM enzyme that catalyzes biosynthesis of glycerol monoalkyl glycerol tetraether (GMGT) lipids, which are membrane lipids in anaerobic archaea. The reference (C6, H2) documents experimental characterization including FUNCTION, CATALYTIC ACTIVITY, COFACTOR, and mutagenesis of the radical SAM cysteine cluster. The pathway assignment is consistent with the enzyme's demonstrated role in synthesizing membrane-spanning lipid molecules.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal sequence 'CGSCMYKYVCGGCRARAYSYYDDYLREDPGCILTKNLK' contains the canonical CX3CX2C radical SAM motif, identifying this as a radical SAM enzyme. The amino acid composition and context suggest an archaeal protein. Transferable knowledge about archaeal biology strongly constrains the answer: (1) Option A (Steroid biosynthesis) is eliminated because archaea do not synthesize steroids—steroid biosynthesis is a eukaryotic pathway. (2) Option C (IMP biosynthesis via de novo pathway) is eliminated because the sequence lacks any purine biosynthesis enzyme motifs (no GAR transformylase, AICAR synthetase, or related domains). (3) Option B (Iron-sulfur cluster biosynthesis) is a common confusion but distinguishable: the ISC/SUF pathway refers to enzymes that ASSEMBLE Fe-S clusters (IscS, Isu, NifU, SufB, etc.), whereas a radical SAM enzyme USES a &#91;4Fe-4S&#93; cluster as a cofactor to generate 5'-deoxyadenosyl radicals for substrate modification. Pathway nomenclature clearly separates cofactor usage from cluster assembly. (4) Option D (Membrane lipid metabolism) remains viable: archaeal radical SAM enzymes are known from other systems to participate in lipid biosynthesis (e.g., GDGT-related pathways), and the elimination of the other three options leaves D as the only pathway consistent with an archaeal radical SAM enzyme. This elimination-based reasoning, combined with the well-established pattern of archaeal radical SAM enzymes in lipid biosynthesis, meaningfully distinguishes D from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The radical SAM motif is directly readable from the sequence. The elimination of options A, B, and C relies on transferable knowledge: steroid biosynthesis is eukaryotic; IMP biosynthesis requires purine-enzyme domains absent here; Fe-S cluster biosynthesis refers to assembly machinery, not cofactor-using enzymes. The remaining option D is supported by the known pattern of archaeal radical SAM enzymes participating in membrane lipid (tetraether) biosynthesis. While the specific GMGT synthase characterization is recent (2024), the pathway-level answer is reachable by elimination plus family-level inference without memorizing this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C are clearly incompatible with an archaeal radical SAM enzyme. Option B is distinguishable from D by the well-known distinction between Fe-S cluster assembly pathways and enzymes that use Fe-S clusters as catalytic cofactors. No ambiguity among the four choices is identified.


### Important caveats

- The GMGT synthase function was experimentally characterized only in 2024 (PubMed:38898040). Before that, this protein's pathway assignment might not have been available in databases. However, the elimination-based reasoning described above does not depend on this specific 2024 paper.
- The pathway annotation uses ECO:0000305 (inferred by curator from the characterized function), not a direct experimental pathway-tracing measurement. This is standard for UniProt pathway assignments.
- The radical SAM motif is clearly present in the C-terminal region, but identifying the specific substrate (GMGT lipid precursor) from sequence alone would require the 2024 characterization. The pathway-level answer is reachable without substrate-level identification via elimination.
- The trailing periods in options B and D ('. .') appear to be formatting artifacts and do not affect the biological content.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal sequence 'CGSCMYKYVCGGCRARAYSYYDDYLREDPGCILTKNLK' contains the canonical CX3CX2C radical SAM motif, identifying this as a radical SAM enzyme. The amino acid composition and context suggest an archaeal protein. Transferable knowledge about archaeal biology strongly constrains the answer: (1) Option A (Steroid biosynthesis) is eliminated because archaea do not synthesize steroids—steroid biosynthesis is a eukaryotic pathway. (2) Option C (IMP biosynthesis via de novo pathway) is eliminated because the sequence lacks any purine biosynthesis enzyme motifs (no GAR transformylase, AICAR synthetase, or related domains). (3) Option B (Iron-sulfur cluster biosynthesis) is a common confusion but distinguishable: the ISC/SUF pathway refers to enzymes that ASSEMBLE Fe-S clusters (IscS, Isu, NifU, SufB, etc.), whereas a radical SAM enzyme USES a [4Fe-4S] cluster as a cofactor to generate 5'-deoxyadenosyl radicals for substrate modification. Pathway nomenclature clearly separates cofactor usage from cluster assembly. (4) Option D (Membrane lipid metabolism) remains viable: archaeal radical SAM enzymes are known from other systems to participate in lipid biosynthesis (e.g., GDGT-related pathways), and the elimination of the other three options leaves D as the only pathway consistent with an archaeal radical SAM enzyme. This elimination-based reasoning, combined with the well-established pattern of archaeal radical SAM enzymes in lipid biosynthesis, meaningfully distinguishes D from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The radical SAM motif is directly readable from the sequence. The elimination of options A, B, and C relies on transferable knowledge: steroid biosynthesis is eukaryotic; IMP biosynthesis requires purine-enzyme domains absent here; Fe-S cluster biosynthesis refers to assembly machinery, not cofactor-using enzymes. The remaining option D is supported by the known pattern of archaeal radical SAM enzymes participating in membrane lipid (tetraether) biosynthesis. While the specific GMGT synthase characterization is recent (2024), the pathway-level answer is reachable by elimination plus family-level inference without memorizing this exact protein's annotation."
  },
  "case_id": "pathway_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (F8AME3) explicitly annotates the pathway as 'Membrane lipid metabolism' (C5, H3) with evidence code ECO:0000305 (inferred by curator) based on PubMed:38898040 (Nat. Commun. 2024). The protein is GMGT synthase (Gms), a radical SAM enzyme that catalyzes biosynthesis of glycerol monoalkyl glycerol tetraether (GMGT) lipids, which are membrane lipids in anaerobic archaea. The reference (C6, H2) documents experimental characterization including FUNCTION, CATALYTIC ACTIVITY, COFACTOR, and mutagenesis of the radical SAM cysteine cluster. The pathway assignment is consistent with the enzyme's demonstrated role in synthesizing membrane-spanning lipid molecules."
  },
  "important_caveats": [
    "The GMGT synthase function was experimentally characterized only in 2024 (PubMed:38898040). Before that, this protein's pathway assignment might not have been available in databases. However, the elimination-based reasoning described above does not depend on this specific 2024 paper.",
    "The pathway annotation uses ECO:0000305 (inferred by curator from the characterized function), not a direct experimental pathway-tracing measurement. This is standard for UniProt pathway assignments.",
    "The radical SAM motif is clearly present in the C-terminal region, but identifying the specific substrate (GMGT lipid precursor) from sequence alone would require the 2024 characterization. The pathway-level answer is reachable without substrate-level identification via elimination.",
    "The trailing periods in options B and D ('. .') appear to be formatting artifacts and do not affect the biological content."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are clearly incompatible with an archaeal radical SAM enzyme. Option B is distinguishable from D by the well-known distinction between Fe-S cluster assembly pathways and enzymes that use Fe-S clusters as catalytic cofactors. No ambiguity among the four choices is identified."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (F8AME3) explicitly annotates the pathway as 'Membrane lipid metabolism' (C5, H3) with evidence code ECO:0000305 (inferred by curator) based on PubMed:38898040 (Nat. Commun. 2024). The protein is GMGT synthase (Gms), a radical SAM enzyme that catalyzes biosynthesis of glycerol monoalkyl glycerol tetraether (GMGT) lipids, which are membrane lipids in anaerobic archaea. The reference (C6, H2) documents experimental characterization including FUNCTION, CATALYTIC ACTIVITY, COFACTOR, and mutagenesis of the radical SAM cysteine cluster. The pathway assignment is consistent with the enzyme's demonstrated role in synthesizing membrane-spanning lipid molecules.",
    "evidence_ids": ["C5", "C6", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal sequence 'CGSCMYKYVCGGCRARAYSYYDDYLREDPGCILTKNLK' contains the canonical CX3CX2C radical SAM motif, identifying this as a radical SAM enzyme. The amino acid composition and context suggest an archaeal protein. Transferable knowledge about archaeal biology strongly constrains the answer: (1) Option A (Steroid biosynthesis) is eliminated because archaea do not synthesize steroids—steroid biosynthesis is a eukaryotic pathway. (2) Option C (IMP biosynthesis via de novo pathway) is eliminated because the sequence lacks any purine biosynthesis enzyme motifs (no GAR transformylase, AICAR synthetase, or related domains). (3) Option B (Iron-sulfur cluster biosynthesis) is a common confusion but distinguishable: the ISC/SUF pathway refers to enzymes that ASSEMBLE Fe-S clusters (IscS, Isu, NifU, SufB, etc.), whereas a radical SAM enzyme USES a [4Fe-4S] cluster as a cofactor to generate 5'-deoxyadenosyl radicals for substrate modification. Pathway nomenclature clearly separates cofactor usage from cluster assembly. (4) Option D (Membrane lipid metabolism) remains viable: archaeal radical SAM enzymes are known from other systems to participate in lipid biosynthesis (e.g., GDGT-related pathways), and the elimination of the other three options leaves D as the only pathway consistent with an archaeal radical SAM enzyme. This elimination-based reasoning, combined with the well-established pattern of archaeal radical SAM enzymes in lipid biosynthesis, meaningfully distinguishes D from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The radical SAM motif is directly readable from the sequence. The elimination of options A, B, and C relies on transferable knowledge: steroid biosynthesis is eukaryotic; IMP biosynthesis requires purine-enzyme domains absent here; Fe-S cluster biosynthesis refers to assembly machinery, not cofactor-using enzymes. The remaining option D is supported by the known pattern of archaeal radical SAM enzymes participating in membrane lipid (tetraether) biosynthesis. While the specific GMGT synthase characterization is recent (2024), the pathway-level answer is reachable by elimination plus family-level inference without memorizing this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C are clearly incompatible with an archaeal radical SAM enzyme. Option B is distinguishable from D by the well-known distinction between Fe-S cluster assembly pathways and enzymes that use Fe-S clusters as catalytic cofactors. No ambiguity among the four choices is identified."
  },
  "important_caveats": [
    "The GMGT synthase function was experimentally characterized only in 2024 (PubMed:38898040). Before that, this protein's pathway assignment might not have been available in databases. However, the elimination-based reasoning described above does not depend on this specific 2024 paper.",
    "The pathway annotation uses ECO:0000305 (inferred by curator from the characterized function), not a direct experimental pathway-tracing measurement. This is standard for UniProt pathway assignments.",
    "The radical SAM motif is clearly present in the C-terminal region, but identifying the specific substrate (GMGT lipid precursor) from sequence alone would require the 2024 characterization. The pathway-level answer is reachable without substrate-level identification via elimination.",
    "The trailing periods in options B and D ('. .') appear to be formatting artifacts and do not affect the biological content."
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
  "benchmark_sequence_length": 466,
  "benchmark_sequence_sha256": "d42b4cf572896d3288a042ca015e5e514cb1ffc87385172c2a6bf7d9f7389ae0",
  "current_entry_audit": {
    "entryVersion": 64,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-09-21",
    "sequenceVersion": 1
  },
  "current_record_sha256": "17353e74adf1b04760d092e7ccb20ff7b58fbb5dbf81cd35514ef3e267e3957b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 466,
  "current_source_sequence_sha256": "d42b4cf572896d3288a042ca015e5e514cb1ffc87385172c2a6bf7d9f7389ae0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 63,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "F8AME3",
  "selected_historical_entry_version": 63,
  "selected_historical_record_sha256": "ffeab1834d6d371a9d99d7ce477b3be2e5158fffdce4bcd9a0d81d96a004a88e",
  "selected_historical_source_sequence_length": 466,
  "selected_historical_source_sequence_sha256": "d42b4cf572896d3288a042ca015e5e514cb1ffc87385172c2a6bf7d9f7389ae0",
  "selected_historical_version": {
    "accession": "F8AME3",
    "database": "Swiss-Prot",
    "entryVersion": 63,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "GMS_METOI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8AME3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"F8AME3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:17.852248+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "17353e74adf1b04760d092e7ccb20ff7b58fbb5dbf81cd35514ef3e267e3957b",
  "url": "https://rest.uniprot.org/uniprotkb/F8AME3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8AME3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":64,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-09-21\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:17.852248+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "17353e74adf1b04760d092e7ccb20ff7b58fbb5dbf81cd35514ef3e267e3957b",
  "url": "https://rest.uniprot.org/uniprotkb/F8AME3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8AME3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Methanomada group\",\"Methanococci\",\"Methanococcales\",\"Methanococcaceae\",\"Methanothermococcus\"],\"scientificName\":\"Methanothermococcus okinawensis (strain DSM 14208 / JCM 11175 / IH1)\",\"taxonId\":647113}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:17.852248+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "17353e74adf1b04760d092e7ccb20ff7b58fbb5dbf81cd35514ef3e267e3957b",
  "url": "https://rest.uniprot.org/uniprotkb/F8AME3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8AME3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38898040\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38898040\",\"source\":\"PubMed\"}],\"value\":\"GMGT synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38898040\",\"source\":\"PubMed\"}],\"value\":\"Gms\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:17.852248+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "17353e74adf1b04760d092e7ccb20ff7b58fbb5dbf81cd35514ef3e267e3957b",
  "url": "https://rest.uniprot.org/uniprotkb/F8AME3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8AME3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"38898040\",\"source\":\"PubMed\"}],\"value\":\"Membrane lipid metabolism\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:28:17.852248+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "17353e74adf1b04760d092e7ccb20ff7b58fbb5dbf81cd35514ef3e267e3957b",
  "url": "https://rest.uniprot.org/uniprotkb/F8AME3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F8AME3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Li Y.\",\"Yu T.\",\"Feng X.\",\"Zhao B.\",\"Chen H.\",\"Yang H.\",\"Chen X.\",\"Zhang X.H.\",\"Anderson H.R.\",\"Burns N.Z.\",\"Zeng F.\",\"Tao L.\",\"Zeng Z.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38898040\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-49650-x\"}],\"citationType\":\"journal article\",\"firstPage\":\"5256\",\"id\":\"38898040\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"5256\",\"publicationDate\":\"2024\",\"title\":\"Biosynthesis of GMGT lipids by a radical SAM enzyme associated with anaerobic archaea and oxygen-deficient environments.\",\"volume\":\"15\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"DOMAIN\",\"MUTAGENESIS OF CYS-123; CYS-127; CYS-370; CYS-372 AND CYS-438\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:28:17.852248+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "17353e74adf1b04760d092e7ccb20ff7b58fbb5dbf81cd35514ef3e267e3957b",
  "url": "https://rest.uniprot.org/uniprotkb/F8AME3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F8AME3?format=txt&versions=63)

```json
{
  "entry_version": 63,
  "evidence_id": "H1",
  "excerpt": "ID   GMS_METOI               Reviewed;         466 AA.\nAC   F8AME3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   21-SEP-2011, sequence version 1.\nDT   28-JAN-2026, entry version 63.\nDE   RecName: Full=GMGT synthase {ECO:0000303|PubMed:38898040};\nDE            Short=Gms {ECO:0000303|PubMed:38898040};\nDE            EC=1.-.-.- {ECO:0000305|PubMed:38898040};\nGN   Name=gms {ECO:0000303|PubMed:38898040};\nGN   OrderedLocusNames=Metok_0864 {ECO:0000312|EMBL:AEH06837.1};\nGN   ORFNames=METOK_RS04425 {ECO:0000303|PubMed:38898040};\nOS   Methanothermococcus okinawensis (strain DSM 14208 / JCM 11175 / IH1).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Methanomada group;\nOC   Methanococci; Methanococcales; Methanococcaceae; Methanothermococcus.\nOX   NCBI_TaxID=647113;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:22.053218+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ffeab1834d6d371a9d99d7ce477b3be2e5158fffdce4bcd9a0d81d96a004a88e",
  "url": "https://rest.uniprot.org/unisave/F8AME3?format=txt&versions=63"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F8AME3?format=txt&versions=63)

```json
{
  "entry_version": 63,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, DOMAIN, AND MUTAGENESIS OF CYS-123;\nRP   CYS-127; CYS-370; CYS-372 AND CYS-438.\nRX   PubMed=38898040; DOI=10.1038/s41467-024-49650-x;\nRA   Li Y., Yu T., Feng X., Zhao B., Chen H., Yang H., Chen X., Zhang X.H.,\nRA   Anderson H.R., Burns N.Z., Zeng F., Tao L., Zeng Z.;\nRT   \"Biosynthesis of GMGT lipids by a radical SAM enzyme associated with\nRT   anaerobic archaea and oxygen-deficient environments.\";\nRL   Nat. Commun. 15:5256-5256(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:22.053218+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ffeab1834d6d371a9d99d7ce477b3be2e5158fffdce4bcd9a0d81d96a004a88e",
  "url": "https://rest.uniprot.org/unisave/F8AME3?format=txt&versions=63"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F8AME3?format=txt&versions=63)

```json
{
  "entry_version": 63,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Membrane lipid metabolism. {ECO:0000305|PubMed:38898040}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:22.053218+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ffeab1834d6d371a9d99d7ce477b3be2e5158fffdce4bcd9a0d81d96a004a88e",
  "url": "https://rest.uniprot.org/unisave/F8AME3?format=txt&versions=63"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 118. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
