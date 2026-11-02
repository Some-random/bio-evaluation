# GO_cellular_component_0163

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — RQC complex

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSRRALRRLRGEQRGQEPLGPDALQFVLLDDDDAEEEGPKTGLGGRRPGGAGKEGVRVNNRFELINIEDLEDDLVVNGERSDCTLPDSASSGNKGRAKHGNPENKQDGDAAAKAGSSEQSNASGKLRKKKKKQKNKKSCTGESSENGLEDIDRILERIEDSSGFSHPGPPPLSSRKHVLYVEHRHLNPDTELKRYFGARAVLGEQRPRQRQRVYPKCTWLTTPKSTWPRYSKPGLSMRLLESKKGLSFFAFEHSEEYQQAQHKFLVAVESMEPNNIVALLQTSPYHVDSLLQLSDACRFQEDQEMARDLIGEPAYPHLLPMEKSWCRRPHWSFYLALYKQMSFLEKRGCPRTALEYCKLILSLEPDEDPLCMLLLIDHMALRARNYEYLIRLFQEWEAHRNLSQLPNFAFSVPLAYFLLSQQTDLPDHELSSARQQASLLIQQALTMFPGVLMPLLEYCSVRPDATVSNHRFFGPDAEISQPPALSQLVSLYLGRSHFLWKEPAIMSWLEENVHEVLEAVDSGDPAVEACENRRKVLYQRAPRNIHRHVILSEIKEAVAALPSDVTTQSVMGFDPLPPVDTIYSYVRPERLSPVSHGNTIALFFRSLLPNYTTEGERLEEGVAGGPNRNQGLNRLMLAVRDMMANFHFNDLEVPREDNPEGEGDWD

[Multiple Choices]
A. lipid droplet
B. RQC complex
C. ATP-binding cassette (ABC) transporter complex
D. other organism cell membrane
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The exact sequence matches rat TCF25, and its GO annotation includes RQC complex. That assignment is ISO:RGD (inferred from sequence orthology), not direct experimental evidence for this protein. The record separately reports mainly nuclear localization experimentally.

Citations as saved: [C1](#evidence-c1), [C8](#evidence-c8), [H6](#evidence-h6), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence lacks obvious transmembrane segments, which argues against an ABC transporter complex or a foreign cell membrane association. But that does not specifically establish membership in the RQC complex.


**Missing item-specific fact**

> The protein-specific identification as TCF25 and its RQC-complex assignment, which is annotated by sequence-orthology inference, are not supplied in the question.


**Reason**

> General sequence inspection can make some membrane-associated choices less plausible, but identifying the specific RQC complex association requires an item-specific annotation or equivalent protein-specific fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the sequence-matched record supports RQC complex; its mainly nuclear localization is not offered as an option.


### Important caveats

- The RQC-complex annotation is inferred from sequence orthology (ISO:RGD), not shown here as direct experimental evidence for this rat protein.
- The record reports mainly nuclear localization experimentally, so the keyed complex annotation should not be read as establishing that RQC is the protein's primary cellular location.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence lacks obvious transmembrane segments, which argues against an ABC transporter complex or a foreign cell membrane association. But that does not specifically establish membership in the RQC complex.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as TCF25 and its RQC-complex assignment, which is annotated by sequence-orthology inference, are not supplied in the question.",
    "reason": "General sequence inspection can make some membrane-associated choices less plausible, but identifying the specific RQC complex association requires an item-specific annotation or equivalent protein-specific fact."
  },
  "case_id": "GO_cellular_component_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C8",
      "H6",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches rat TCF25, and its GO annotation includes RQC complex. That assignment is ISO:RGD (inferred from sequence orthology), not direct experimental evidence for this protein. The record separately reports mainly nuclear localization experimentally."
  },
  "important_caveats": [
    "The RQC-complex annotation is inferred from sequence orthology (ISO:RGD), not shown here as direct experimental evidence for this rat protein.",
    "The record reports mainly nuclear localization experimentally, so the keyed complex annotation should not be read as establishing that RQC is the protein's primary cellular location."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sequence-matched record supports RQC complex; its mainly nuclear localization is not offered as an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches rat TCF25, and its GO annotation includes RQC complex. That assignment is ISO:RGD (inferred from sequence orthology), not direct experimental evidence for this protein. The record separately reports mainly nuclear localization experimentally.",
    "evidence_ids": ["C1", "C8", "H6", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence lacks obvious transmembrane segments, which argues against an ABC transporter complex or a foreign cell membrane association. But that does not specifically establish membership in the RQC complex.",
    "missing_item_specific_fact": "The protein-specific identification as TCF25 and its RQC-complex assignment, which is annotated by sequence-orthology inference, are not supplied in the question.",
    "reason": "General sequence inspection can make some membrane-associated choices less plausible, but identifying the specific RQC complex association requires an item-specific annotation or equivalent protein-specific fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sequence-matched record supports RQC complex; its mainly nuclear localization is not offered as an option."
  },
  "important_caveats": [
    "The RQC-complex annotation is inferred from sequence orthology (ISO:RGD), not shown here as direct experimental evidence for this rat protein.",
    "The record reports mainly nuclear localization experimentally, so the keyed complex annotation should not be read as establishing that RQC is the protein's primary cellular location."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A8I6ASZ5) explicitly annotates GO:1990112 (RQC complex) with evidence code ISO:RGD (C8, H6), and the recommended protein name is 'Ribosome quality control complex subunit TCF25' (C4, H1). The GO term definition (GO4) describes a multiprotein complex associated with ribosomes and stalled polypeptide degradation, consistent with TCF25's role. However, the RQC complex annotation is inferred from orthology (ISO:RGD), not direct experimental evidence for this specific rat protein; the experimental evidence (PubMed:32805187) primarily supports nuclear localization (C5, H3, H5). The answer is supported by database annotation.

Citations as saved: [C4](#evidence-c4), [C8](#evidence-c8), [H1](#evidence-h1), [H6](#evidence-h6), [GO4](#evidence-go4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General reasoning can partially eliminate options C and D: the sequence lacks the hydrophobic transmembrane domains and nucleotide-binding domains characteristic of ABC transporters (GO:0043190, GO2), and 'other organism cell membrane' (GO:0044218, GO3) is an implausible compartment for an endogenous rat protein. However, distinguishing option A (lipid droplet) from option B (RQC complex) requires knowing that TCF25/NULP1 specifically interacts with the 60S ribosomal subunit and is a defined subunit of the RQC complex. The sequence contains nuclear localization signals (e.g., 'KKKKKQKNKK' near position 100) and HEAT-like repeats, but no features uniquely diagnostic of RQC complex membership versus generic nuclear/cytoplasmic localization.


**Missing item-specific fact**

> The specific protein-protein interaction annotation identifying TCF25 as a subunit of the RQC complex (GO:1990112, ISO:RGD) is a protein-specific database fact not derivable from sequence features alone. Without knowing the protein's identity as TCF25/NULP1 and its documented role in ribosome-associated quality control, the sequence provides no specific signal pointing to 'RQC complex' over 'nucleus' or 'cytoplasm' or even 'lipid droplet'.


**Reason**

> While elimination of C and D is achievable through general structural reasoning (absence of TM domains, implausibility of foreign membrane for a rat protein), the positive identification of RQC complex membership depends on a protein-specific interaction annotation (ISO:RGD). The sequence's nuclear localization signals and lack of membrane features are consistent with many nuclear/cytoplasmic proteins, not uniquely with RQC complex subunits. Recognizing this as TCF25 and recalling its RQC complex association constitutes memorization of a database entry rather than sequence-based reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four options, C (ABC transporter) and D (other organism cell membrane) are clearly implausible given the sequence lacks transmembrane domains and the protein is not a pathogen-associated factor. A (lipid droplet) is unlikely as the sequence lacks typical amphipathic helix patterns of lipid droplet-associated proteins. B is the annotated answer. No genuine ambiguity among the provided choices, though the 'primary' location per experimental evidence is nucleus, which is not offered as an option.


### Important caveats

- The RQC complex GO annotation carries evidence code ISO:RGD (inferred from orthology), not direct experimental evidence for this rat protein. The only experimental subcellular evidence (PubMed:32805187) supports nuclear localization.
- The question asks for 'primary Cellular Component' but the experimentally determined primary location is 'Nucleus' (ECO:0000269, EXP), which is not among the options. The RQC complex is a protein complex annotation, not a spatial compartment in the traditional sense.
- The sequence match is confirmed (666 AA, sha256 match) to A0A8I6ASZ5 (TCF25_RAT), but this accession identification was reviewer-only and not available to the evaluated model.
- The GO annotation for RQC complex was added via orthology transfer from human TCF25 (Q9BQ70); direct biochemical demonstration of rat TCF25 in the RQC complex was not found in the supplied evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General reasoning can partially eliminate options C and D: the sequence lacks the hydrophobic transmembrane domains and nucleotide-binding domains characteristic of ABC transporters (GO:0043190, GO2), and 'other organism cell membrane' (GO:0044218, GO3) is an implausible compartment for an endogenous rat protein. However, distinguishing option A (lipid droplet) from option B (RQC complex) requires knowing that TCF25/NULP1 specifically interacts with the 60S ribosomal subunit and is a defined subunit of the RQC complex. The sequence contains nuclear localization signals (e.g., 'KKKKKQKNKK' near position 100) and HEAT-like repeats, but no features uniquely diagnostic of RQC complex membership versus generic nuclear/cytoplasmic localization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific protein-protein interaction annotation identifying TCF25 as a subunit of the RQC complex (GO:1990112, ISO:RGD) is a protein-specific database fact not derivable from sequence features alone. Without knowing the protein's identity as TCF25/NULP1 and its documented role in ribosome-associated quality control, the sequence provides no specific signal pointing to 'RQC complex' over 'nucleus' or 'cytoplasm' or even 'lipid droplet'.",
    "reason": "While elimination of C and D is achievable through general structural reasoning (absence of TM domains, implausibility of foreign membrane for a rat protein), the positive identification of RQC complex membership depends on a protein-specific interaction annotation (ISO:RGD). The sequence's nuclear localization signals and lack of membrane features are consistent with many nuclear/cytoplasmic proteins, not uniquely with RQC complex subunits. Recognizing this as TCF25 and recalling its RQC complex association constitutes memorization of a database entry rather than sequence-based reasoning."
  },
  "case_id": "GO_cellular_component_0163",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C8",
      "H1",
      "H6",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A8I6ASZ5) explicitly annotates GO:1990112 (RQC complex) with evidence code ISO:RGD (C8, H6), and the recommended protein name is 'Ribosome quality control complex subunit TCF25' (C4, H1). The GO term definition (GO4) describes a multiprotein complex associated with ribosomes and stalled polypeptide degradation, consistent with TCF25's role. However, the RQC complex annotation is inferred from orthology (ISO:RGD), not direct experimental evidence for this specific rat protein; the experimental evidence (PubMed:32805187) primarily supports nuclear localization (C5, H3, H5). The answer is supported by database annotation."
  },
  "important_caveats": [
    "The RQC complex GO annotation carries evidence code ISO:RGD (inferred from orthology), not direct experimental evidence for this rat protein. The only experimental subcellular evidence (PubMed:32805187) supports nuclear localization.",
    "The question asks for 'primary Cellular Component' but the experimentally determined primary location is 'Nucleus' (ECO:0000269, EXP), which is not among the options. The RQC complex is a protein complex annotation, not a spatial compartment in the traditional sense.",
    "The sequence match is confirmed (666 AA, sha256 match) to A0A8I6ASZ5 (TCF25_RAT), but this accession identification was reviewer-only and not available to the evaluated model.",
    "The GO annotation for RQC complex was added via orthology transfer from human TCF25 (Q9BQ70); direct biochemical demonstration of rat TCF25 in the RQC complex was not found in the supplied evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four options, C (ABC transporter) and D (other organism cell membrane) are clearly implausible given the sequence lacks transmembrane domains and the protein is not a pathogen-associated factor. A (lipid droplet) is unlikely as the sequence lacks typical amphipathic helix patterns of lipid droplet-associated proteins. B is the annotated answer. No genuine ambiguity among the provided choices, though the 'primary' location per experimental evidence is nucleus, which is not offered as an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0163",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A8I6ASZ5) explicitly annotates GO:1990112 (RQC complex) with evidence code ISO:RGD (C8, H6), and the recommended protein name is 'Ribosome quality control complex subunit TCF25' (C4, H1). The GO term definition (GO4) describes a multiprotein complex associated with ribosomes and stalled polypeptide degradation, consistent with TCF25's role. However, the RQC complex annotation is inferred from orthology (ISO:RGD), not direct experimental evidence for this specific rat protein; the experimental evidence (PubMed:32805187) primarily supports nuclear localization (C5, H3, H5). The answer is supported by database annotation.",
    "evidence_ids": ["C4", "C8", "H1", "H6", "GO4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General reasoning can partially eliminate options C and D: the sequence lacks the hydrophobic transmembrane domains and nucleotide-binding domains characteristic of ABC transporters (GO:0043190, GO2), and 'other organism cell membrane' (GO:0044218, GO3) is an implausible compartment for an endogenous rat protein. However, distinguishing option A (lipid droplet) from option B (RQC complex) requires knowing that TCF25/NULP1 specifically interacts with the 60S ribosomal subunit and is a defined subunit of the RQC complex. The sequence contains nuclear localization signals (e.g., 'KKKKKQKNKK' near position 100) and HEAT-like repeats, but no features uniquely diagnostic of RQC complex membership versus generic nuclear/cytoplasmic localization.",
    "missing_item_specific_fact": "The specific protein-protein interaction annotation identifying TCF25 as a subunit of the RQC complex (GO:1990112, ISO:RGD) is a protein-specific database fact not derivable from sequence features alone. Without knowing the protein's identity as TCF25/NULP1 and its documented role in ribosome-associated quality control, the sequence provides no specific signal pointing to 'RQC complex' over 'nucleus' or 'cytoplasm' or even 'lipid droplet'.",
    "reason": "While elimination of C and D is achievable through general structural reasoning (absence of TM domains, implausibility of foreign membrane for a rat protein), the positive identification of RQC complex membership depends on a protein-specific interaction annotation (ISO:RGD). The sequence's nuclear localization signals and lack of membrane features are consistent with many nuclear/cytoplasmic proteins, not uniquely with RQC complex subunits. Recognizing this as TCF25 and recalling its RQC complex association constitutes memorization of a database entry rather than sequence-based reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four options, C (ABC transporter) and D (other organism cell membrane) are clearly implausible given the sequence lacks transmembrane domains and the protein is not a pathogen-associated factor. A (lipid droplet) is unlikely as the sequence lacks typical amphipathic helix patterns of lipid droplet-associated proteins. B is the annotated answer. No genuine ambiguity among the provided choices, though the 'primary' location per experimental evidence is nucleus, which is not offered as an option."
  },
  "important_caveats": [
    "The RQC complex GO annotation carries evidence code ISO:RGD (inferred from orthology), not direct experimental evidence for this rat protein. The only experimental subcellular evidence (PubMed:32805187) supports nuclear localization.",
    "The question asks for 'primary Cellular Component' but the experimentally determined primary location is 'Nucleus' (ECO:0000269, EXP), which is not among the options. The RQC complex is a protein complex annotation, not a spatial compartment in the traditional sense.",
    "The sequence match is confirmed (666 AA, sha256 match) to A0A8I6ASZ5 (TCF25_RAT), but this accession identification was reviewer-only and not available to the evaluated model.",
    "The GO annotation for RQC complex was added via orthology transfer from human TCF25 (Q9BQ70); direct biochemical demonstration of rat TCF25 in the RQC complex was not found in the supplied evidence."
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

**Accession:** `A0A8I6ASZ5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.287559+00:00.  

```json
"A0A8I6ASZ5"
```

Source SHA-256: `db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.287559+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BQ70","source":"UniProtKB"}],"value":"Nuclear localized protein 1"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"1309054","source":"RGD"}],"value":"Transcription factor 25"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"TCF-25"}]}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Ribosome quality control complex subunit TCF25"}}}
```

Source SHA-256: `db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.287559+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"32805187","source":"PubMed"}],"value":"Mainly nuclear"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"32805187","source":"PubMed"}],"id":"SL-0191","value":"Nucleus"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9BQ70","source":"UniProtKB"}],"id":"SL-0091","value":"Cytoplasm, cytosol"}}]}
```

Source SHA-256: `db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6ASZ5.json)  
**Locator:** `/uniProtKBCrossReferences/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:51.287559+00:00.  

```json
{"database":"GO","id":"GO:1990112","properties":[{"key":"GoTerm","value":"C:RQC complex"},{"key":"GoEvidenceType","value":"ISO:RGD"}]}
```

Source SHA-256: `db13e28cf53212b88a3330247eb6b69fce14e32a3cdbaa15c6dfdc4fe02619c8`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:27:34.894954+00:00.  

```text
ID   TCF25_RAT               Reviewed;         666 AA.
AC   A0A8I6ASZ5;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   25-MAY-2022, sequence version 1.
DT   28-JAN-2026, entry version 19.
DE   RecName: Full=Ribosome quality control complex subunit TCF25 {ECO:0000305};
DE   AltName: Full=Nuclear localized protein 1 {ECO:0000250|UniProtKB:Q9BQ70};
DE   AltName: Full=Transcription factor 25 {ECO:0000312|RGD:1309054};
DE            Short=TCF-25 {ECO:0000305};
GN   Name=Tcf25 {ECO:0000312|RGD:1309054};
GN   Synonyms=Nulp1 {ECO:0000303|PubMed:32805187};
OS   Rattus norvegicus (Rat).
OC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;
OC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;
OC   Murinae; Rattus.
OX   NCBI_TaxID=10116 {ECO:0000312|Proteomes:UP000002494};
```

Source SHA-256: `02d5de5a62e40229c163c44c1ed60fb43f5d7fd00a2bdc4d42a93088921dc0ef`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19)  
**Locator:** `lines 91-93`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:27:34.894954+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:32805187}. Cytoplasm,
CC       cytosol {ECO:0000250|UniProtKB:Q9BQ70}. Note=Mainly nuclear.
CC       {ECO:0000269|PubMed:32805187}.
```

Source SHA-256: `02d5de5a62e40229c163c44c1ed60fb43f5d7fd00a2bdc4d42a93088921dc0ef`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19)  
**Locator:** `lines 111-111`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:27:34.894954+00:00.  

```text
DR   GO; GO:0005634; C:nucleus; ISO:RGD.
```

Source SHA-256: `02d5de5a62e40229c163c44c1ed60fb43f5d7fd00a2bdc4d42a93088921dc0ef`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6ASZ5?format=txt&versions=19)  
**Locator:** `lines 112-112`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:27:34.894954+00:00.  

```text
DR   GO; GO:1990112; C:RQC complex; ISO:RGD.
```

Source SHA-256: `02d5de5a62e40229c163c44c1ed60fb43f5d7fd00a2bdc4d42a93088921dc0ef`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 244782-244797`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0043190
name: ATP-binding cassette (ABC) transporter complex
namespace: cellular_component
alt_id: GO:0043191
alt_id: GO:0043192
def: "A complex for the transport of metabolites into and out of the cell, typically comprised of four domains; two membrane-associated domains and two ATP-binding domains at the intracellular face of the membrane, that form a central pore through the plasma membrane. Each of the four core domains may be encoded as a separate polypeptide or the domains can be fused in any one of a number of ways into multidomain polypeptides. In Bacteria and Archaebacteria, ABC transporters also include substrate binding proteins to bind substrate external to the cytoplasm and deliver it to the transporter." [GOC:jl, GOC:mtg_sensu, PMID:11421269, PMID:15111107]
subset: goslim_metagenomics
subset: goslim_pir
synonym: "ABC-type efflux permease complex" NARROW []
synonym: "ABC-type efflux porter complex" NARROW []
synonym: "ABC-type uptake permease complex" NARROW []
synonym: "mating pheromone exporter" NARROW []
is_a: GO:0098533 ! ATPase dependent transmembrane transport complex
is_a: GO:0098797 ! plasma membrane protein complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 255298-255307`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0044218
name: other organism cell membrane
namespace: cellular_component
alt_id: GO:0044279
def: "The cell membrane of a secondary organism with which the first organism is interacting." [GOC:jl]
synonym: "foreign membrane" RELATED []
synonym: "other organism membrane" BROAD []
is_a: GO:0044217 ! other organism part

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 549333-549341`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:1990112
name: RQC complex
namespace: cellular_component
def: "A multiprotein complex that forms a stable complex with large ribosomal subunits (60S in eukaryotes and 50S in prokaryotes) containing stalled polypeptides and triggers their degradation (ribosomal quality control). In budding yeast, this complex includes Cdc48p, Rkr1p, Tae2p, Rqc1p, Npl4p and Ufd1p proteins." [GOC:rb, PMID:23178123, PMID:23232563]
synonym: "ribosome quality control complex" EXACT [PMID:23178123, PMID:23232563]
synonym: "ribosome-bound quality control complex" EXACT []
is_a: GO:0032991 ! protein-containing complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 163. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
