# GO_biological_process_0093

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — transmembrane transport

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGKEQKEKKDGNLSIKEEVEKELNKKSTAELFRKIKNEKISFFLPFKCLPAQHRKLLFISFVCAVLSGGTLPFFISVFGVILKNMNLGDDINPIILSLVSIGLVQFILSMISSYCMDVITSKILKTLKLEYLRSVFYQDGQFHDNNPGSKLRSDLDFYLEQVSSGIGTKFITIFTYASSFLGLYIWSLIKNARLTLCITCVFPLIYVCGVICNKKVKLNKKTSLLYNNNTMSIIEEALMGIRTVASYCGEKTILNKFNLSETFYSKYILKANFVEALHIGLINGLILVSYAFGFWYGTRIIINSATNQYPNNDFNGASVISILLGVLISMFMLTIILPNITEYMKALEATNSLYEIINRKPLVENNDDGETLPNIKKIEFKNVRFHYDTRKDVEIYKDLSFTLKEGKTYAFVGESGCGKSTILKLIERLYDPTEGDIIVNDSHNLKDINLKWWRSKIGVVSQDPLLFSNSIKNNIKYSLYSLKDLEAMENYYEENTNDTYENKNFSLISNSMTSNELLEMKKEYQTIKDSDVVDVSKKVLIHDFVSSLPDKYDTLVGSNASKLSGGQKQRISIARAIMRNPKILILDEATSSLDNKSEYLVQKTINNLKGNENRITIIIAHRLSTIRYANTIFVLSNRERSDNNNNNNNDDNNNNNNNNNNKINNEGSYIIEQGTHDSLMKNKNGIYHLMINNQKISSNKSSNNGNDNGSDNKSSAYKDSDTGNDADNMNSLSIHENENISNNRNCKNTAENEKEEKVPFFKRMFRRKKKAPNNLRIIYKEIFSYKKDVTIIFFSILVAGGLYPVFALLYARYVSTLFDFANLEYNSNKYSIYILLIAIAMFISETLKNYYNNKIGEKVEKTMKRRLFENILYQEMSFFDQDKNTPGVLSAHINRDVHLLKTGLVNNIVIFSHFIMLFLVSMVMSFYFCPIVAAVLTFIYFINMRVFAVRARLTKSKEIEKKENMSSGVFAFSSDDEMFKDPSFLIQEAFYNMHTVINYGLEDYFCNLIEKAIDYKNKGQKRRIIVNAALWGFSQSAQLFINSFAYWFGSFLIKRGTILVDDFMKSLFTFIFTGSYAGKLMSLKGDSENAKLSFEKYYPLMIRKSNIDVRDDGGIRINKNLIKGKVDIKDVNFRYISRPNVPIYKNLSFTCDSKKTTAIVGETGSGKSTFMNLLLRFYDLKNDHIILKNDMTNFQDYQNNNNNSLVLKNVNEFSNQSGSAEDYTVFNNNGEILLDDINICDYNLRDLRNLFSIVSQEPMLFNMSIYENIKFGREDATLEDVKRVSKFAAIDEFIESLPNKYDTNVGPYGKSLSGGQKQRIAIARALLREPKILLLDEATSSLDSNSEKLIEKTIVDIKDKADKTIITIAHRIASIKRSDKIVVFNNPDRNGTFVQSHGTHDELLSAQDGIYKKYVKLAK

[Multiple Choices]
A. L-fucose catabolic process
B. cell wall organization
C. sorbitol catabolic process
D. transmembrane transport
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The sequence exactly matches the historical UniProt record for PfMDR1, which is annotated with GO:0055085, transmembrane transport. The record also describes an energy-dependent drug efflux pump and cites experimental evidence for its transport function. The GO annotation is IBA (computationally inferred), while the function statement cites experimental evidence.

Citations as saved: [H6](#evidence-h6), [H7](#evidence-h7), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence contains many strongly hydrophobic segments consistent with multiple membrane-spanning helices and two nucleotide-binding regions with ABC-transporter-like Walker A motifs. This architecture supports an ATP-driven membrane transporter, making transmembrane transport a meaningful fit among the choices.


**Missing item-specific fact**

> No protein-specific annotation or substrate identity is needed to distinguish the broad transport process from the offered sugar-catabolism and cell-wall-organization choices.


**Reason**

> The sequence itself provides recognizable transporter architecture, and the distractors describe processes not suggested by that architecture. Identifying the precise PfMDR1 identity would require external recognition, but the broad answer is also supported by sequence-based biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Of the listed choices, transmembrane transport is the only one matching the sequence's apparent multipass ABC-transporter architecture.


### Important caveats

- The sequence match establishes that reviewer evidence concerns the supplied protein; it does not establish which database snapshot the author used.
- The GO annotation is computationally inferred by IBA, whereas the UniProt function statement cites experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence contains many strongly hydrophobic segments consistent with multiple membrane-spanning helices and two nucleotide-binding regions with ABC-transporter-like Walker A motifs. This architecture supports an ATP-driven membrane transporter, making transmembrane transport a meaningful fit among the choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation or substrate identity is needed to distinguish the broad transport process from the offered sugar-catabolism and cell-wall-organization choices.",
    "reason": "The sequence itself provides recognizable transporter architecture, and the distractors describe processes not suggested by that architecture. Identifying the precise PfMDR1 identity would require external recognition, but the broad answer is also supported by sequence-based biological reasoning."
  },
  "case_id": "GO_biological_process_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "H6",
      "H7",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt record for PfMDR1, which is annotated with GO:0055085, transmembrane transport. The record also describes an energy-dependent drug efflux pump and cites experimental evidence for its transport function. The GO annotation is IBA (computationally inferred), while the function statement cites experimental evidence."
  },
  "important_caveats": [
    "The sequence match establishes that reviewer evidence concerns the supplied protein; it does not establish which database snapshot the author used.",
    "The GO annotation is computationally inferred by IBA, whereas the UniProt function statement cites experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Of the listed choices, transmembrane transport is the only one matching the sequence's apparent multipass ABC-transporter architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt record for PfMDR1, which is annotated with GO:0055085, transmembrane transport. The record also describes an energy-dependent drug efflux pump and cites experimental evidence for its transport function. The GO annotation is IBA (computationally inferred), while the function statement cites experimental evidence.",
    "evidence_ids": ["H6", "H7", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence contains many strongly hydrophobic segments consistent with multiple membrane-spanning helices and two nucleotide-binding regions with ABC-transporter-like Walker A motifs. This architecture supports an ATP-driven membrane transporter, making transmembrane transport a meaningful fit among the choices.",
    "missing_item_specific_fact": "No protein-specific annotation or substrate identity is needed to distinguish the broad transport process from the offered sugar-catabolism and cell-wall-organization choices.",
    "reason": "The sequence itself provides recognizable transporter architecture, and the distractors describe processes not suggested by that architecture. Identifying the precise PfMDR1 identity would require external recognition, but the broad answer is also supported by sequence-based biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Of the listed choices, transmembrane transport is the only one matching the sequence's apparent multipass ABC-transporter architecture."
  },
  "important_caveats": [
    "The sequence match establishes that reviewer evidence concerns the supplied protein; it does not establish which database snapshot the author used.",
    "The GO annotation is computationally inferred by IBA, whereas the UniProt function statement cites experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q7K6A5 (PfMDR1, Multidrug resistance protein 1 / P-glycoprotein homolog) is annotated with GO:0055085 (transmembrane transport) via IBA:GO_Central (H7). The protein's experimentally supported function (ECO:0000269, PubMed:35507548, PubMed:37527341) is as an 'energy-dependent efflux pump' that 'transports lumefantrine, mefloquine, chloroquine, quinine, quinidine, amodiaquine, piperaquine, dihydroartemisinin and quinacrine' across membranes (C5, H6). EC 7.6.2.2 is an ABC transporter class. The GO term definition (GO2) — 'the process in which a solute is transported across a lipid bilayer' — matches the protein's demonstrated function. The GO annotation evidence code is IBA (inferred by biological aspect from GO_Central), a computational inference from ontology structure, but the underlying experimental evidence for the protein's transmembrane transport function is strong (cryo-EM structures in complex with ATP/Mg²⁺/mefloquine, functional transport assays).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H6](#evidence-h6), [H7](#evidence-h7), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains two canonical ABC transporter nucleotide-binding domains identifiable by Walker A motifs (GESGCGKST at ~residue 590 and GETGSGKST at ~residue 1130) and two ABC signature motifs (SGGQKQR at ~residue 680 and ~residue 1220), flanked by multiple hydrophobic transmembrane helices. This is the textbook full-transporter ABC architecture (two TMDs + two NBDs). ABC transporters are, by definition, membrane-spanning solute translocators whose primary biological process is transmembrane transport. The distractors are eliminable by general knowledge: Plasmodium falciparum lacks a cell wall (eliminates B); no sugar-catabolism enzyme motifs (e.g., fucose mutarotase, sorbitol dehydrogenase) are present (eliminates A and C).


**Missing item-specific fact**

> None critical. The GO term 'transmembrane transport' is the broad parent term; a model might also consider narrower terms like 'drug transport' or 'ATP hydrolysis coupled transmembrane transport,' but those are not offered as options, so the ABC architecture uniquely selects D among the four choices.


**Reason**

> A biologist familiar with ABC transporter sequence signatures (Walker A, ABC signature, transmembrane helices) can identify the protein family from the sequence and infer its biological process as transmembrane transport without needing to look up the specific UniProt entry. The distractors are biologically implausible for this organism and sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The ABC transporter architecture unambiguously points to transmembrane transport. Option B (cell wall organization) is inapplicable to Plasmodium (no cell wall). Options A and C (sugar catabolism) lack any supporting enzymatic motifs. No two options are defensible.


### Important caveats

- The GO annotation evidence code for GO:0055085 is IBA:GO_Central (computational inference from ontology structure), not a direct experimental GO assignment. However, the protein's transmembrane transport function is experimentally validated (ECO:0000269, cryo-EM structures, functional assays).
- The UniProt entry was first publicly released 2025-02-05; the benchmark author's source snapshot date is unknown. Sequence match is confirmed across historical and current versions.
- The GO term 'transmembrane transport' (GO:0055085) is a broad parent; more specific terms like 'drug transport' or 'xenobiotic transport' could also apply, but they are not among the answer choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains two canonical ABC transporter nucleotide-binding domains identifiable by Walker A motifs (GESGCGKST at ~residue 590 and GETGSGKST at ~residue 1130) and two ABC signature motifs (SGGQKQR at ~residue 680 and ~residue 1220), flanked by multiple hydrophobic transmembrane helices. This is the textbook full-transporter ABC architecture (two TMDs + two NBDs). ABC transporters are, by definition, membrane-spanning solute translocators whose primary biological process is transmembrane transport. The distractors are eliminable by general knowledge: Plasmodium falciparum lacks a cell wall (eliminates B); no sugar-catabolism enzyme motifs (e.g., fucose mutarotase, sorbitol dehydrogenase) are present (eliminates A and C).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The GO term 'transmembrane transport' is the broad parent term; a model might also consider narrower terms like 'drug transport' or 'ATP hydrolysis coupled transmembrane transport,' but those are not offered as options, so the ABC architecture uniquely selects D among the four choices.",
    "reason": "A biologist familiar with ABC transporter sequence signatures (Walker A, ABC signature, transmembrane helices) can identify the protein family from the sequence and infer its biological process as transmembrane transport without needing to look up the specific UniProt entry. The distractors are biologically implausible for this organism and sequence."
  },
  "case_id": "GO_biological_process_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H6",
      "H7",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q7K6A5 (PfMDR1, Multidrug resistance protein 1 / P-glycoprotein homolog) is annotated with GO:0055085 (transmembrane transport) via IBA:GO_Central (H7). The protein's experimentally supported function (ECO:0000269, PubMed:35507548, PubMed:37527341) is as an 'energy-dependent efflux pump' that 'transports lumefantrine, mefloquine, chloroquine, quinine, quinidine, amodiaquine, piperaquine, dihydroartemisinin and quinacrine' across membranes (C5, H6). EC 7.6.2.2 is an ABC transporter class. The GO term definition (GO2) — 'the process in which a solute is transported across a lipid bilayer' — matches the protein's demonstrated function. The GO annotation evidence code is IBA (inferred by biological aspect from GO_Central), a computational inference from ontology structure, but the underlying experimental evidence for the protein's transmembrane transport function is strong (cryo-EM structures in complex with ATP/Mg²⁺/mefloquine, functional transport assays)."
  },
  "important_caveats": [
    "The GO annotation evidence code for GO:0055085 is IBA:GO_Central (computational inference from ontology structure), not a direct experimental GO assignment. However, the protein's transmembrane transport function is experimentally validated (ECO:0000269, cryo-EM structures, functional assays).",
    "The UniProt entry was first publicly released 2025-02-05; the benchmark author's source snapshot date is unknown. Sequence match is confirmed across historical and current versions.",
    "The GO term 'transmembrane transport' (GO:0055085) is a broad parent; more specific terms like 'drug transport' or 'xenobiotic transport' could also apply, but they are not among the answer choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The ABC transporter architecture unambiguously points to transmembrane transport. Option B (cell wall organization) is inapplicable to Plasmodium (no cell wall). Options A and C (sugar catabolism) lack any supporting enzymatic motifs. No two options are defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q7K6A5 (PfMDR1, Multidrug resistance protein 1 / P-glycoprotein homolog) is annotated with GO:0055085 (transmembrane transport) via IBA:GO_Central (H7). The protein's experimentally supported function (ECO:0000269, PubMed:35507548, PubMed:37527341) is as an 'energy-dependent efflux pump' that 'transports lumefantrine, mefloquine, chloroquine, quinine, quinidine, amodiaquine, piperaquine, dihydroartemisinin and quinacrine' across membranes (C5, H6). EC 7.6.2.2 is an ABC transporter class. The GO term definition (GO2) — 'the process in which a solute is transported across a lipid bilayer' — matches the protein's demonstrated function. The GO annotation evidence code is IBA (inferred by biological aspect from GO_Central), a computational inference from ontology structure, but the underlying experimental evidence for the protein's transmembrane transport function is strong (cryo-EM structures in complex with ATP/Mg²⁺/mefloquine, functional transport assays).",
    "evidence_ids": ["C1", "C4", "C5", "H6", "H7", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains two canonical ABC transporter nucleotide-binding domains identifiable by Walker A motifs (GESGCGKST at ~residue 590 and GETGSGKST at ~residue 1130) and two ABC signature motifs (SGGQKQR at ~residue 680 and ~residue 1220), flanked by multiple hydrophobic transmembrane helices. This is the textbook full-transporter ABC architecture (two TMDs + two NBDs). ABC transporters are, by definition, membrane-spanning solute translocators whose primary biological process is transmembrane transport. The distractors are eliminable by general knowledge: Plasmodium falciparum lacks a cell wall (eliminates B); no sugar-catabolism enzyme motifs (e.g., fucose mutarotase, sorbitol dehydrogenase) are present (eliminates A and C).",
    "missing_item_specific_fact": "None critical. The GO term 'transmembrane transport' is the broad parent term; a model might also consider narrower terms like 'drug transport' or 'ATP hydrolysis coupled transmembrane transport,' but those are not offered as options, so the ABC architecture uniquely selects D among the four choices.",
    "reason": "A biologist familiar with ABC transporter sequence signatures (Walker A, ABC signature, transmembrane helices) can identify the protein family from the sequence and infer its biological process as transmembrane transport without needing to look up the specific UniProt entry. The distractors are biologically implausible for this organism and sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The ABC transporter architecture unambiguously points to transmembrane transport. Option B (cell wall organization) is inapplicable to Plasmodium (no cell wall). Options A and C (sugar catabolism) lack any supporting enzymatic motifs. No two options are defensible."
  },
  "important_caveats": [
    "The GO annotation evidence code for GO:0055085 is IBA:GO_Central (computational inference from ontology structure), not a direct experimental GO assignment. However, the protein's transmembrane transport function is experimentally validated (ECO:0000269, cryo-EM structures, functional assays).",
    "The UniProt entry was first publicly released 2025-02-05; the benchmark author's source snapshot date is unknown. Sequence match is confirmed across historical and current versions.",
    "The GO term 'transmembrane transport' (GO:0055085) is a broad parent; more specific terms like 'drug transport' or 'xenobiotic transport' could also apply, but they are not among the answer choices."
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

**Accession:** `Q7K6A5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 159. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
"Q7K6A5"
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"1674943","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"8097560","source":"PubMed"}],"value":"P-glycoprotein homolog"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"1674943","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"8097560","source":"PubMed"}],"value":"PGH1"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"37527341","source":"PubMed"}],"value":"7.6.2.2"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"1674943","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"37527341","source":"PubMed"}],"value":"Multidrug resistance protein 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"1674943","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"37527341","source":"PubMed"}],"value":"PfMDR1"}]}}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7K6A5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:50.920847+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35507548","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"37527341","source":"PubMed"}],"value":"Energy-dependent efflux pump responsible for decreased drug accumulation in multidrug-resistant cells (PubMed:35507548, PubMed:37527341). Transports lumefantrine, mefloquine, chloroquine, quinine, quinidine, amodiaquine, piperaquine, dihydroartemisinin and quinacrine (PubMed:35507548)"}]}
```

Source SHA-256: `c1220f0801aea149e54fb44381ba7d041b9bfe565917395ce8a5169c3eefa409`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 83-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
CC   -!- FUNCTION: Energy-dependent efflux pump responsible for decreased drug
CC       accumulation in multidrug-resistant cells (PubMed:35507548,
CC       PubMed:37527341). Transports lumefantrine, mefloquine, chloroquine,
CC       quinine, quinidine, amodiaquine, piperaquine, dihydroartemisinin and
CC       quinacrine (PubMed:35507548). {ECO:0000269|PubMed:35507548,
CC       ECO:0000269|PubMed:37527341}.
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7K6A5?format=txt&versions=159)  
**Locator:** `lines 187-187`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 159 / 1.  
**Retrieved:** 2026-11-02T04:31:59.503134+00:00.  

```text
DR   GO; GO:0055085; P:transmembrane transport; IBA:GO_Central.
```

Source SHA-256: `340d0339c1b8029c60947228c9d25479f2a99420125e3d12307b6cf7f7e5b84d`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 343246-343266`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0055085
name: transmembrane transport
namespace: biological_process
alt_id: GO:0090662
def: "The process in which a solute is transported across a lipid bilayer, from one side of a membrane to the other." [GOC:dph, GOC:jid]
comment: Transmembrane transport is the transport of a solute across a lipid bilayer. Note that transport through the nuclear pore complex is not transmembrane because the nuclear membrane is a double membrane and is not traversed. For transport through the nuclear pore, consider instead the term 'nucleocytoplasmic transport ; GO:0006913' and its children. Note also that this term is not intended for use in annotating lateral movement within membranes.
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_pombe
subset: goslim_yeast
synonym: "ATP hydrolysis coupled transmembrane transport" NARROW []
synonym: "membrane transport" EXACT []
xref: Reactome:R-HSA-382556 "ABC-family proteins mediated transport"
xref: Reactome:R-HSA-425407 "SLC-mediated transmembrane transport"
xref: Reactome:R-HSA-5223345 "Miscellaneous transport and binding events"
is_a: GO:0006810 ! transport
is_a: GO:0009987 ! cellular process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 93. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
