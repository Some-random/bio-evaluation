# catalytic_activity_0199

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0199.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — L-lysyl-&#91;protein&#93; + 2-oxoglutarate + O2 = (3S)-3-hydroxy-L-lysyl-&#91;protein&#93; + succinate + CO2

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSEVERALDVLLQEAEELCIGSSVVELDRIPTALEFCREFYSKNQPVVIRKALNWPAIGKWTPKYLIEALGDRSVDVAITPNGYADGLATQNGQEYFVLPLETKMKLSEVVRRLDDPTGAVHYIQKQNSNLSVDLPELAADLRVSDLDFAQQSFNKPPDAVNFWLGDERAVTSMHKDPYENVYCVISGHKDFVLIPPHQLSCVPRGIYPTGVYKTSDSGQFYIEPLRDEEGSDQFTEWVSVDPLSPDLAKYPEYARAKPLKVRVHAGDILYLPNYWFHHVSQSHKCIAVNFWYDLDYDSRYCYYRMLEQMTSARSG

[Multiple Choices]
A. L-lysyl-[protein] + 2-oxoglutarate + O2 = (3S)-3-hydroxy-L-lysyl-[protein] + succinate + CO2
B. D-glutamine + acetyl-CoA = N-acetyl-D-glutamine + CoA + H(+)
C. 4-nitrobenzoate + 2 NADH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NAD(+) + H2O
D. S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.
```

<details>
<summary>Complete original system instructions</summary>

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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt records list this exact lysyl-hydroxylation reaction as catalytic activity and attribute it to experimental evidence (ECO:0000269, PubMed 35410347). The historical record also contains the reaction. The cited study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a JmjC-like 2-oxoglutarate oxygenase domain, including a plausible HxD metal-binding motif. Transferable knowledge of this enzyme family supports Fe(II)/2-oxoglutarate-dependent oxidation, matching the hydroxylation and 2-oxoglutarate decarboxylation in A. The other choices describe acetyl transfer, NADH-dependent nitro reduction, or ubiquitin transfer, which do not fit that chemistry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and family-level chemistry meaningfully distinguish A among the offered choices. They provide less independent certainty about the precise lysyl substrate specificity, but no competing option matches the inferred oxygenase reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A matches the sequence-supported 2-oxoglutarate-dependent hydroxylation chemistry among the choices.


### Important caveats

- The sequence supports the oxygenase family inference more directly than the exact protein-bound lysine substrate specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a JmjC-like 2-oxoglutarate oxygenase domain, including a plausible HxD metal-binding motif. Transferable knowledge of this enzyme family supports Fe(II)/2-oxoglutarate-dependent oxidation, matching the hydroxylation and 2-oxoglutarate decarboxylation in A. The other choices describe acetyl transfer, NADH-dependent nitro reduction, or ubiquitin transfer, which do not fit that chemistry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level chemistry meaningfully distinguish A among the offered choices. They provide less independent certainty about the precise lysyl substrate specificity, but no competing option matches the inferred oxygenase reaction."
  },
  "case_id": "catalytic_activity_0199",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records list this exact lysyl-hydroxylation reaction as catalytic activity and attribute it to experimental evidence (ECO:0000269, PubMed 35410347). The historical record also contains the reaction. The cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence supports the oxygenase family inference more directly than the exact protein-bound lysine substrate specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A matches the sequence-supported 2-oxoglutarate-dependent hydroxylation chemistry among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0199",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records list this exact lysyl-hydroxylation reaction as catalytic activity and attribute it to experimental evidence (ECO:0000269, PubMed 35410347). The historical record also contains the reaction. The cited study was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a JmjC-like 2-oxoglutarate oxygenase domain, including a plausible HxD metal-binding motif. Transferable knowledge of this enzyme family supports Fe(II)/2-oxoglutarate-dependent oxidation, matching the hydroxylation and 2-oxoglutarate decarboxylation in A. The other choices describe acetyl transfer, NADH-dependent nitro reduction, or ubiquitin transfer, which do not fit that chemistry.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level chemistry meaningfully distinguish A among the offered choices. They provide less independent certainty about the precise lysyl substrate specificity, but no competing option matches the inferred oxygenase reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A matches the sequence-supported 2-oxoglutarate-dependent hydroxylation chemistry among the choices."
  },
  "important_caveats": [
    "The sequence supports the oxygenase family inference more directly than the exact protein-bound lysine substrate specificity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VU77 (JMJD7_DROME) annotates the catalytic activity as L-lysyl-&#91;protein&#93; + 2-oxoglutarate + O2 = (3S)-3-hydroxy-L-lysyl-&#91;protein&#93; + succinate + CO2 (EC 1.14.11.63), supported by experimental evidence (ECO:0000269, PubMed:35410347) including X-ray crystallography in complex with 2-oxoglutarate, Mn(2+), and succinate (PDB 7YXG-7YXL). The sequence SHA256 matches exactly. The evidence is direct experimental support, not merely computational inference.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence contains features consistent with a JmjC/2-oxoglutarate-dependent oxygenase domain: multiple histidine residues positioned for Fe(II) coordination (e.g., 'GHKDF' and 'HAGD...WFHHV' motifs), conserved aromatic residues (FWY, FWLG, VNFW appearing twice), and an overall ~150-200 residue domain architecture typical of the JmjC superfamily. This is transferable knowledge from well-characterized JmjC proteins (histone demethylases, PHD-type oxygenases, prolyl hydroxylases). Among the four choices, only A represents a 2-OG-dependent dioxygenase reaction. Choice B (acetyltransferase) requires GNAT-like fold motifs absent here; Choice C (nitroreductase) requires FMN-binding motifs absent here; Choice D (ubiquitin ligase) requires RING/U-box/HECT domains absent here. A model recognizing JmjC-type His-rich metal-coordination patterns and the absence of motifs for the other three enzyme classes can meaningfully select A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of JmjC domain features (His residues for Fe coordination, aromatic residues, domain size) is standard transferable knowledge from the well-studied JmjC/2-OG oxygenase superfamily. The other three options represent structurally distinct enzyme classes (acetyltransferase, nitroreductase, ubiquitin ligase) whose characteristic motifs are clearly absent from the sequence. This provides a concrete, credible inference path to A without requiring the specific JMJD7 database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent four structurally and mechanistically distinct enzyme classes. The JmjC/2-OG oxygenase features in the sequence and the absence of motifs for the other three classes make A the uniquely defensible answer. No ambiguity identified.


### Important caveats

- The JmjC fold in JMJD7 is described as 'unusual' and 'dimeric' in the literature, which may make canonical JmjC motif recognition slightly less straightforward than in classical histone demethylases, but the general His-rich Fe-coordination pattern and 2-OG oxygenase architecture remain identifiable.
- The UniProt annotation also lists EC 3.4.-.- (peptidase activity, transferred by similarity to P0C870), but no peptidase reaction is offered among the choices, so this does not create ambiguity.
- The reviewer-only evidence confirms the sequence matches Q9VU77 exactly (SHA256 match), validating the annotation's applicability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence contains features consistent with a JmjC/2-oxoglutarate-dependent oxygenase domain: multiple histidine residues positioned for Fe(II) coordination (e.g., 'GHKDF' and 'HAGD...WFHHV' motifs), conserved aromatic residues (FWY, FWLG, VNFW appearing twice), and an overall ~150-200 residue domain architecture typical of the JmjC superfamily. This is transferable knowledge from well-characterized JmjC proteins (histone demethylases, PHD-type oxygenases, prolyl hydroxylases). Among the four choices, only A represents a 2-OG-dependent dioxygenase reaction. Choice B (acetyltransferase) requires GNAT-like fold motifs absent here; Choice C (nitroreductase) requires FMN-binding motifs absent here; Choice D (ubiquitin ligase) requires RING/U-box/HECT domains absent here. A model recognizing JmjC-type His-rich metal-coordination patterns and the absence of motifs for the other three enzyme classes can meaningfully select A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of JmjC domain features (His residues for Fe coordination, aromatic residues, domain size) is standard transferable knowledge from the well-studied JmjC/2-OG oxygenase superfamily. The other three options represent structurally distinct enzyme classes (acetyltransferase, nitroreductase, ubiquitin ligase) whose characteristic motifs are clearly absent from the sequence. This provides a concrete, credible inference path to A without requiring the specific JMJD7 database annotation."
  },
  "case_id": "catalytic_activity_0199",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VU77 (JMJD7_DROME) annotates the catalytic activity as L-lysyl-[protein] + 2-oxoglutarate + O2 = (3S)-3-hydroxy-L-lysyl-[protein] + succinate + CO2 (EC 1.14.11.63), supported by experimental evidence (ECO:0000269, PubMed:35410347) including X-ray crystallography in complex with 2-oxoglutarate, Mn(2+), and succinate (PDB 7YXG-7YXL). The sequence SHA256 matches exactly. The evidence is direct experimental support, not merely computational inference."
  },
  "important_caveats": [
    "The JmjC fold in JMJD7 is described as 'unusual' and 'dimeric' in the literature, which may make canonical JmjC motif recognition slightly less straightforward than in classical histone demethylases, but the general His-rich Fe-coordination pattern and 2-OG oxygenase architecture remain identifiable.",
    "The UniProt annotation also lists EC 3.4.-.- (peptidase activity, transferred by similarity to P0C870), but no peptidase reaction is offered among the choices, so this does not create ambiguity.",
    "The reviewer-only evidence confirms the sequence matches Q9VU77 exactly (SHA256 match), validating the annotation's applicability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four structurally and mechanistically distinct enzyme classes. The JmjC/2-OG oxygenase features in the sequence and the absence of motifs for the other three classes make A the uniquely defensible answer. No ambiguity identified."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0199",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VU77 (JMJD7_DROME) annotates the catalytic activity as L-lysyl-[protein] + 2-oxoglutarate + O2 = (3S)-3-hydroxy-L-lysyl-[protein] + succinate + CO2 (EC 1.14.11.63), supported by experimental evidence (ECO:0000269, PubMed:35410347) including X-ray crystallography in complex with 2-oxoglutarate, Mn(2+), and succinate (PDB 7YXG-7YXL). The sequence SHA256 matches exactly. The evidence is direct experimental support, not merely computational inference.",
    "evidence_ids": ["C5", "C6", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence contains features consistent with a JmjC/2-oxoglutarate-dependent oxygenase domain: multiple histidine residues positioned for Fe(II) coordination (e.g., 'GHKDF' and 'HAGD...WFHHV' motifs), conserved aromatic residues (FWY, FWLG, VNFW appearing twice), and an overall ~150-200 residue domain architecture typical of the JmjC superfamily. This is transferable knowledge from well-characterized JmjC proteins (histone demethylases, PHD-type oxygenases, prolyl hydroxylases). Among the four choices, only A represents a 2-OG-dependent dioxygenase reaction. Choice B (acetyltransferase) requires GNAT-like fold motifs absent here; Choice C (nitroreductase) requires FMN-binding motifs absent here; Choice D (ubiquitin ligase) requires RING/U-box/HECT domains absent here. A model recognizing JmjC-type His-rich metal-coordination patterns and the absence of motifs for the other three enzyme classes can meaningfully select A.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of JmjC domain features (His residues for Fe coordination, aromatic residues, domain size) is standard transferable knowledge from the well-studied JmjC/2-OG oxygenase superfamily. The other three options represent structurally distinct enzyme classes (acetyltransferase, nitroreductase, ubiquitin ligase) whose characteristic motifs are clearly absent from the sequence. This provides a concrete, credible inference path to A without requiring the specific JMJD7 database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent four structurally and mechanistically distinct enzyme classes. The JmjC/2-OG oxygenase features in the sequence and the absence of motifs for the other three classes make A the uniquely defensible answer. No ambiguity identified."
  },
  "important_caveats": [
    "The JmjC fold in JMJD7 is described as 'unusual' and 'dimeric' in the literature, which may make canonical JmjC motif recognition slightly less straightforward than in classical histone demethylases, but the general His-rich Fe-coordination pattern and 2-OG oxygenase architecture remain identifiable.",
    "The UniProt annotation also lists EC 3.4.-.- (peptidase activity, transferred by similarity to P0C870), but no peptidase reaction is offered among the choices, so this does not create ambiguity.",
    "The reviewer-only evidence confirms the sequence matches Q9VU77 exactly (SHA256 match), validating the annotation's applicability."
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
  "benchmark_sequence_length": 316,
  "benchmark_sequence_sha256": "733e4d48eefaab9b6305e750c192e23a03fad9599f5119a6f7f33245bd687968",
  "current_entry_audit": {
    "entryVersion": 178,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 316,
  "current_source_sequence_sha256": "733e4d48eefaab9b6305e750c192e23a03fad9599f5119a6f7f33245bd687968",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 176,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VU77",
  "selected_historical_entry_version": 176,
  "selected_historical_record_sha256": "a1c372e1e6cdfb62ebfb0d23f4b2ede050f6bcae06c776e1265b4e0ab02f3ff5",
  "selected_historical_source_sequence_length": 316,
  "selected_historical_source_sequence_sha256": "733e4d48eefaab9b6305e750c192e23a03fad9599f5119a6f7f33245bd687968",
  "selected_historical_version": {
    "accession": "Q9VU77",
    "database": "Swiss-Prot",
    "entryVersion": 176,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "JMJD7_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU77.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VU77\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:39.402140+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VU77.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU77.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":178,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:39.402140+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VU77.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU77.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:39.402140+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VU77.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU77.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0036366\",\"source\":\"FlyBase\"}],\"value\":\"Jumonji domain containing protein 7\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35410347\",\"source\":\"PubMed\"}],\"value\":\"1.14.11.63\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C870\",\"source\":\"UniProtKB\"}],\"value\":\"3.4.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0C870\",\"source\":\"UniProtKB\"}],\"value\":\"Bifunctional peptidase and (3S)-lysyl hydroxylase JMJD7\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:39.402140+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VU77.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU77.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35410347\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:57153\"}}],\"reaction\":{\"ecNumber\":\"1.14.11.63\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35410347\",\"source\":\"PubMed\"}],\"name\":\"L-lysyl-[protein] + 2-oxoglutarate + O2 = (3S)-3-hydroxy-L-lysyl-[protein] + succinate + CO2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:57152\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:9752\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15133\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16810\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29969\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30031\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:141492\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:39.402140+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VU77.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VU77.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Chowdhury R.\",\"Abboud M.I.\",\"Wiley J.\",\"Tumber A.\",\"Markolovic S.\",\"Schofield C.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35410347\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41598-022-10028-y\"}],\"citationType\":\"journal article\",\"firstPage\":\"6065\",\"id\":\"35410347\",\"journal\":\"Sci. Rep.\",\"lastPage\":\"6065\",\"publicationDate\":\"2022\",\"title\":\"Conservation of the unusual dimeric JmjC fold of JMJD7 from Drosophila melanogaster to humans.\",\"volume\":\"12\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YXG\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YXH\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YXI\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YXJ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YXK\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YXL\",\"source\":\"PDB\"}],\"referenceNumber\":7,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEX WITH 2-OXOGLUTARATE; MN(2+); SUCCINATE; N-OXALYLGLYCINE; N-OXALYL-D-ALANINE; N-OXALYL-D-PHENYLALANINE AND LUTIDINIC ACID\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBUNIT\",\"DISULFIDE BOND\",\"OXIDATION AT CYS-19\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/6",
  "retrieved_utc": "2026-11-02T04:33:39.402140+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3f44f9cf8070a93f81c5ebea15797eae9345f5530025b2d6a02c1b0f107c3c0f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VU77.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VU77?format=txt&versions=176)

```json
{
  "entry_version": 176,
  "evidence_id": "H1",
  "excerpt": "ID   JMJD7_DROME             Reviewed;         316 AA.\nAC   Q9VU77;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 176.\nDE   RecName: Full=Bifunctional peptidase and (3S)-lysyl hydroxylase JMJD7 {ECO:0000250|UniProtKB:P0C870};\nDE            EC=1.14.11.63 {ECO:0000269|PubMed:35410347};\nDE            EC=3.4.-.- {ECO:0000250|UniProtKB:P0C870};\nDE   AltName: Full=Jumonji domain containing protein 7 {ECO:0000312|FlyBase:FBgn0036366};\nGN   Name=JMJD7 {ECO:0000312|FlyBase:FBgn0036366};\nGN   ORFNames=CG10133 {ECO:0000312|FlyBase:FBgn0036366};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:41.782034+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a1c372e1e6cdfb62ebfb0d23f4b2ede050f6bcae06c776e1265b4e0ab02f3ff5",
  "url": "https://rest.uniprot.org/unisave/Q9VU77?format=txt&versions=176"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VU77?format=txt&versions=176)

```json
{
  "entry_version": 176,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Bifunctional peptidase and (3S)-lysyl hydroxylase JMJD7 {ECO:0000250|UniProtKB:P0C870};\nDE            EC=1.14.11.63 {ECO:0000269|PubMed:35410347};\nDE            EC=3.4.-.- {ECO:0000250|UniProtKB:P0C870};\nDE   AltName: Full=Jumonji domain containing protein 7 {ECO:0000312|FlyBase:FBgn0036366};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:41.782034+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a1c372e1e6cdfb62ebfb0d23f4b2ede050f6bcae06c776e1265b4e0ab02f3ff5",
  "url": "https://rest.uniprot.org/unisave/Q9VU77?format=txt&versions=176"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VU77?format=txt&versions=176)

```json
{
  "entry_version": 176,
  "evidence_id": "H3",
  "excerpt": "RN   [7] {ECO:0007744|PDB:7YXG, ECO:0007744|PDB:7YXH, ECO:0007744|PDB:7YXI, ECO:0007744|PDB:7YXJ, ECO:0007744|PDB:7YXK, ECO:0007744|PDB:7YXL}\nRP   X-RAY CRYSTALLOGRAPHY (1.64 ANGSTROMS) IN COMPLEX WITH 2-OXOGLUTARATE;\nRP   MN(2+); SUCCINATE; N-OXALYLGLYCINE; N-OXALYL-D-ALANINE;\nRP   N-OXALYL-D-PHENYLALANINE AND LUTIDINIC ACID, FUNCTION, CATALYTIC ACTIVITY,\nRP   COFACTOR, SUBUNIT, DISULFIDE BOND, AND OXIDATION AT CYS-19.\nRX   PubMed=35410347; DOI=10.1038/s41598-022-10028-y;\nRA   Chowdhury R., Abboud M.I., Wiley J., Tumber A., Markolovic S.,\nRA   Schofield C.J.;\nRT   \"Conservation of the unusual dimeric JmjC fold of JMJD7 from Drosophila\nRT   melanogaster to humans.\";\nRL   Sci. Rep. 12:6065-6065(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:41.782034+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a1c372e1e6cdfb62ebfb0d23f4b2ede050f6bcae06c776e1265b4e0ab02f3ff5",
  "url": "https://rest.uniprot.org/unisave/Q9VU77?format=txt&versions=176"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VU77?format=txt&versions=176)

```json
{
  "entry_version": 176,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-lysyl-[protein] + 2-oxoglutarate + O2 = (3S)-3-hydroxy-L-\nCC         lysyl-[protein] + succinate + CO2; Xref=Rhea:RHEA:57152, Rhea:RHEA-\nCC         COMP:9752, Rhea:RHEA-COMP:15133, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:16526, ChEBI:CHEBI:16810, ChEBI:CHEBI:29969,\nCC         ChEBI:CHEBI:30031, ChEBI:CHEBI:141492; EC=1.14.11.63;\nCC         Evidence={ECO:0000269|PubMed:35410347};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:57153;\nCC         Evidence={ECO:0000269|PubMed:35410347};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:41.782034+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 124-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a1c372e1e6cdfb62ebfb0d23f4b2ede050f6bcae06c776e1265b4e0ab02f3ff5",
  "url": "https://rest.uniprot.org/unisave/Q9VU77?format=txt&versions=176"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 199. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
