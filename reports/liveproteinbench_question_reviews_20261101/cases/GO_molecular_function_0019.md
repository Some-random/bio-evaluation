# GO_molecular_function_0019

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — DNA-binding transcription factor activity, RNA polymerase II-specific

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSGRAVSNSQHAQQSFGSGPQLYRDVAELHAVPSPSHGALMDPSHFDDFAFAYQGLPDQPSLVSLADHAHAHASQSPTAFPQHQAMSGLAHNGLPFGALPAGNRSQSMDGSDAPPDRTSPASNALEDSTTDEFGLASRSRADATDLGGKPKEDKADATPAWSELKTKAGKERKRLPLACIACRRKKIRCSGEKPACKHCLRSRIPCVYKVTTRKAAPRTDYMAMLDKRLKRMEERIIKVIPKSDQEVASSVTRAVVKPAIPGTVPSNKPTKKRGAEEAFGPDLEAWAKAPSKPKIDGDDRPSSLQVQEAEENKLQHEGTEALPSKEIQEHLAEVFFDNIYGQSYHLLHKPSYMRKLKNGTLPPVLVLTVCAVAARFTSSPLVNSSGPEFLRGEEWASHARDICTRRYEWPNLTILTCLLILGLHEFGTCQGGRSWALGGQAIRMAFALQLHKDLEYDPSGRTGPKKQLSFIDREIRRRIMWACFLMDRFNSSGTDRPMFIREDTIQIPLPVKEKYFQFDMPAPTEMLDGQVPHPASPNDGQLADARENMGVAAFLIRAIALWGRIITYLSQGGKDLDPNPMWEDESQYVKHLNDVVNLEASLPSSLKYSAENLDVHKTENTASQFLFMHICLQHNILFVSRAAMSARKQQGVHDDFFSEASKRTFSAANQISELLREAEQSRCFVSAPFAGYCAFSSTTVHILGVISGNPNMKPTAEANLTTNVKYLHKMKKYWGMFHWMVENVRTQYRNALDAMRAGANLQDRAAQSSFLQYGDWFNRYPHGLSDAEFMDPATHKRKDSGADGVLEAKPELQSVEEYFSTLPTPQSVEHKDTIRAVGTKRKQSAKKQAGLPTQSGQHLESMQGTDADSVSGAQERRFSGGLGLPSNSYNPLAVSNAQNPAFSTAMSPMSPANMTAFSHHAHTPTFFPPELLAMNFGQGANGNIDPLDRQLVFGGYSLDASTGLGGGQDIMSGLDWDAVASGAHPDGGLQGRRSTAKAGMNGQAAGMADGAGLSGPEASSAWFMPFNMEPPEMGQDPGFNMGGIDPFTGVFGGGGSGLATPNALGGLQQQGP

[Multiple Choices]
A. protein homodimerization activity
B. cellulose synthase (UDP-forming) activity
C. DNA-binding transcription factor activity, RNA polymerase II-specific
D. dynein complex binding
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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates this protein as a Zn(2)-C6 fungal transcription factor and assigns DNA-binding transcription factor activity, RNA polymerase II-specific. Its functional annotation cites experimental evidence, while the GO assignment itself is marked IEA:InterPro.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a characteristic cysteine-rich Zn(2)-C6 fungal DNA-binding motif, consistent with a fungal transcription factor. That supports choice C over cellulose synthase, which would be expected to have a membrane-enzyme architecture, and over the less specifically indicated binding activities in A and D.


**Missing item-specific fact**

> The exact protein identity and its specific biological roles are not provided, but are not necessary to distinguish C as the best-supported option from these choices.


**Reason**

> A recognizable DNA-binding domain and the contrast with the enzyme distractor provide a meaningful sequence-based argument. The sequence does not independently prove every detail of the GO term, including RNA polymerase II specificity, but the choices make C the defensible best answer.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence’s fungal Zn(2)-C6 motif supports transcription-factor function; none of the other options is comparably indicated.


### Important caveats

- The GO annotation is computationally assigned (IEA:InterPro), whereas the database’s broader functional description cites experimental evidence; these evidence types should not be conflated.
- The reviewer-only sequence match supports the key but does not establish what information was available to the original question author.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a characteristic cysteine-rich Zn(2)-C6 fungal DNA-binding motif, consistent with a fungal transcription factor. That supports choice C over cellulose synthase, which would be expected to have a membrane-enzyme architecture, and over the less specifically indicated binding activities in A and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact protein identity and its specific biological roles are not provided, but are not necessary to distinguish C as the best-supported option from these choices.",
    "reason": "A recognizable DNA-binding domain and the contrast with the enzyme distractor provide a meaningful sequence-based argument. The sequence does not independently prove every detail of the GO term, including RNA polymerase II specificity, but the choices make C the defensible best answer."
  },
  "case_id": "GO_molecular_function_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein as a Zn(2)-C6 fungal transcription factor and assigns DNA-binding transcription factor activity, RNA polymerase II-specific. Its functional annotation cites experimental evidence, while the GO assignment itself is marked IEA:InterPro."
  },
  "important_caveats": [
    "The GO annotation is computationally assigned (IEA:InterPro), whereas the database’s broader functional description cites experimental evidence; these evidence types should not be conflated.",
    "The reviewer-only sequence match supports the key but does not establish what information was available to the original question author."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence’s fungal Zn(2)-C6 motif supports transcription-factor function; none of the other options is comparably indicated."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein as a Zn(2)-C6 fungal transcription factor and assigns DNA-binding transcription factor activity, RNA polymerase II-specific. Its functional annotation cites experimental evidence, while the GO assignment itself is marked IEA:InterPro.",
    "evidence_ids": ["C1", "C5", "C7", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a characteristic cysteine-rich Zn(2)-C6 fungal DNA-binding motif, consistent with a fungal transcription factor. That supports choice C over cellulose synthase, which would be expected to have a membrane-enzyme architecture, and over the less specifically indicated binding activities in A and D.",
    "missing_item_specific_fact": "The exact protein identity and its specific biological roles are not provided, but are not necessary to distinguish C as the best-supported option from these choices.",
    "reason": "A recognizable DNA-binding domain and the contrast with the enzyme distractor provide a meaningful sequence-based argument. The sequence does not independently prove every detail of the GO term, including RNA polymerase II specificity, but the choices make C the defensible best answer."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence’s fungal Zn(2)-C6 motif supports transcription-factor function; none of the other options is comparably indicated."
  },
  "important_caveats": [
    "The GO annotation is computationally assigned (IEA:InterPro), whereas the database’s broader functional description cites experimental evidence; these evidence types should not be conflated.",
    "The reviewer-only sequence match supports the key but does not establish what information was available to the original question author."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (A0A0J9WP80) is experimentally characterized as a Zn(2)-C6 fungal-type transcription factor FTF2 (PubMed:26817616, PubMed:36986302, ECO:0000269). It is explicitly named 'Zn(2)-C6 fungal-type transcription factor' and shown to regulate gene expression (SIX effectors, hydrophobins). GO:0000981 'DNA-binding transcription factor activity, RNA polymerase II-specific' is annotated via IEA:InterPro (C7, H6), consistent with the Zn2C6 domain being a well-established fungal DNA-binding domain that operates with RNA Pol II. The experimental evidence confirms transcription factor activity; the specific GO term assignment is computational but scientifically sound for a fungal Zn2C6 TF.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a cysteine-rich cluster 'CIACRRKKIRCSGEKPACKHCLRSRIPCVYKVTTRKAAPRT' with six cysteines in a spacing pattern consistent with the Zn(2)-C6 (zinc cluster) DNA-binding domain, a hallmark of fungal transcription factors. Recognizing this motif supports DNA-binding transcription factor activity. Fungi transcribe mRNA via RNA polymerase II, making the 'RNA polymerase II-specific' qualifier appropriate. Distractor B (cellulose synthase) requires glycosyltransferase/transmembrane motifs absent here; D (dynein complex binding) requires dynein-interacting motifs absent here; A (homodimerization) is not the primary molecular function of a Zn2C6 DNA-binding domain.


**Missing item-specific fact**

> None critical. The Zn2C6 domain recognition requires familiarity with fungal zinc-cluster motifs, but this is well-established molecular biology knowledge. The somewhat non-canonical cysteine spacing in this particular instance (X6 rather than X13-15 between some cysteines) adds minor difficulty but the overall six-cysteine cluster pattern remains recognizable.


**Reason**

> A model with knowledge of fungal transcription factor domains can identify the Zn2C6 cysteine cluster from the sequence, link it to DNA binding, and apply general knowledge that fungal TFs operate with RNA Pol II. The three distractors lack any supporting sequence features (no glycosyltransferase motifs, no dynein-binding motifs, and the Zn2C6 domain is primarily a DNA-binding rather than dimerization domain).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Zn2C6 domain unambiguously points to DNA-binding transcription factor activity. Cellulose synthase (B) and dynein binding (D) have no sequence support. Homodimerization (A) is not the primary molecular function of a Zn2C6 domain; while some Zn2C6 TFs can dimerize, their defining activity is sequence-specific DNA binding. The question asks for 'primary molecular function,' clearly favoring C.


### Important caveats

- The GO:0000981 annotation is IEA:InterPro (computational inference from domain match), not direct experimental GO annotation. However, the experimental evidence (ECO:0000269) independently confirms transcription factor function.
- The Zn2C6 cysteine spacing in this protein is somewhat degenerate relative to the canonical C-X2-C-X(13-15)-C-X2-C-X(2-3)-C-X(2-3)-C pattern, which may make motif recognition harder for some models.
- The protein is from Fusarium oxysporum (a fungus), and the 'RNA polymerase II-specific' qualifier is appropriate because fungi use RNA Pol II for protein-coding gene transcription, unlike the RNA Pol I/III usage in some other contexts.
- The UniProt entry was first public in June 2025 and reviewed in January 2026; the benchmark construction date is unknown, so the annotation may not have been available at benchmark creation time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a cysteine-rich cluster 'CIACRRKKIRCSGEKPACKHCLRSRIPCVYKVTTRKAAPRT' with six cysteines in a spacing pattern consistent with the Zn(2)-C6 (zinc cluster) DNA-binding domain, a hallmark of fungal transcription factors. Recognizing this motif supports DNA-binding transcription factor activity. Fungi transcribe mRNA via RNA polymerase II, making the 'RNA polymerase II-specific' qualifier appropriate. Distractor B (cellulose synthase) requires glycosyltransferase/transmembrane motifs absent here; D (dynein complex binding) requires dynein-interacting motifs absent here; A (homodimerization) is not the primary molecular function of a Zn2C6 DNA-binding domain.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The Zn2C6 domain recognition requires familiarity with fungal zinc-cluster motifs, but this is well-established molecular biology knowledge. The somewhat non-canonical cysteine spacing in this particular instance (X6 rather than X13-15 between some cysteines) adds minor difficulty but the overall six-cysteine cluster pattern remains recognizable.",
    "reason": "A model with knowledge of fungal transcription factor domains can identify the Zn2C6 cysteine cluster from the sequence, link it to DNA binding, and apply general knowledge that fungal TFs operate with RNA Pol II. The three distractors lack any supporting sequence features (no glycosyltransferase motifs, no dynein-binding motifs, and the Zn2C6 domain is primarily a DNA-binding rather than dimerization domain)."
  },
  "case_id": "GO_molecular_function_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H1",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The protein (A0A0J9WP80) is experimentally characterized as a Zn(2)-C6 fungal-type transcription factor FTF2 (PubMed:26817616, PubMed:36986302, ECO:0000269). It is explicitly named 'Zn(2)-C6 fungal-type transcription factor' and shown to regulate gene expression (SIX effectors, hydrophobins). GO:0000981 'DNA-binding transcription factor activity, RNA polymerase II-specific' is annotated via IEA:InterPro (C7, H6), consistent with the Zn2C6 domain being a well-established fungal DNA-binding domain that operates with RNA Pol II. The experimental evidence confirms transcription factor activity; the specific GO term assignment is computational but scientifically sound for a fungal Zn2C6 TF."
  },
  "important_caveats": [
    "The GO:0000981 annotation is IEA:InterPro (computational inference from domain match), not direct experimental GO annotation. However, the experimental evidence (ECO:0000269) independently confirms transcription factor function.",
    "The Zn2C6 cysteine spacing in this protein is somewhat degenerate relative to the canonical C-X2-C-X(13-15)-C-X2-C-X(2-3)-C-X(2-3)-C pattern, which may make motif recognition harder for some models.",
    "The protein is from Fusarium oxysporum (a fungus), and the 'RNA polymerase II-specific' qualifier is appropriate because fungi use RNA Pol II for protein-coding gene transcription, unlike the RNA Pol I/III usage in some other contexts.",
    "The UniProt entry was first public in June 2025 and reviewed in January 2026; the benchmark construction date is unknown, so the annotation may not have been available at benchmark creation time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Zn2C6 domain unambiguously points to DNA-binding transcription factor activity. Cellulose synthase (B) and dynein binding (D) have no sequence support. Homodimerization (A) is not the primary molecular function of a Zn2C6 domain; while some Zn2C6 TFs can dimerize, their defining activity is sequence-specific DNA binding. The question asks for 'primary molecular function,' clearly favoring C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (A0A0J9WP80) is experimentally characterized as a Zn(2)-C6 fungal-type transcription factor FTF2 (PubMed:26817616, PubMed:36986302, ECO:0000269). It is explicitly named 'Zn(2)-C6 fungal-type transcription factor' and shown to regulate gene expression (SIX effectors, hydrophobins). GO:0000981 'DNA-binding transcription factor activity, RNA polymerase II-specific' is annotated via IEA:InterPro (C7, H6), consistent with the Zn2C6 domain being a well-established fungal DNA-binding domain that operates with RNA Pol II. The experimental evidence confirms transcription factor activity; the specific GO term assignment is computational but scientifically sound for a fungal Zn2C6 TF.",
    "evidence_ids": ["C4", "C5", "C7", "H1", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a cysteine-rich cluster 'CIACRRKKIRCSGEKPACKHCLRSRIPCVYKVTTRKAAPRT' with six cysteines in a spacing pattern consistent with the Zn(2)-C6 (zinc cluster) DNA-binding domain, a hallmark of fungal transcription factors. Recognizing this motif supports DNA-binding transcription factor activity. Fungi transcribe mRNA via RNA polymerase II, making the 'RNA polymerase II-specific' qualifier appropriate. Distractor B (cellulose synthase) requires glycosyltransferase/transmembrane motifs absent here; D (dynein complex binding) requires dynein-interacting motifs absent here; A (homodimerization) is not the primary molecular function of a Zn2C6 DNA-binding domain.",
    "missing_item_specific_fact": "None critical. The Zn2C6 domain recognition requires familiarity with fungal zinc-cluster motifs, but this is well-established molecular biology knowledge. The somewhat non-canonical cysteine spacing in this particular instance (X6 rather than X13-15 between some cysteines) adds minor difficulty but the overall six-cysteine cluster pattern remains recognizable.",
    "reason": "A model with knowledge of fungal transcription factor domains can identify the Zn2C6 cysteine cluster from the sequence, link it to DNA binding, and apply general knowledge that fungal TFs operate with RNA Pol II. The three distractors lack any supporting sequence features (no glycosyltransferase motifs, no dynein-binding motifs, and the Zn2C6 domain is primarily a DNA-binding rather than dimerization domain)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Zn2C6 domain unambiguously points to DNA-binding transcription factor activity. Cellulose synthase (B) and dynein binding (D) have no sequence support. Homodimerization (A) is not the primary molecular function of a Zn2C6 domain; while some Zn2C6 TFs can dimerize, their defining activity is sequence-specific DNA binding. The question asks for 'primary molecular function,' clearly favoring C."
  },
  "important_caveats": [
    "The GO:0000981 annotation is IEA:InterPro (computational inference from domain match), not direct experimental GO annotation. However, the experimental evidence (ECO:0000269) independently confirms transcription factor function.",
    "The Zn2C6 cysteine spacing in this protein is somewhat degenerate relative to the canonical C-X2-C-X(13-15)-C-X2-C-X(2-3)-C-X(2-3)-C pattern, which may make motif recognition harder for some models.",
    "The protein is from Fusarium oxysporum (a fungus), and the 'RNA polymerase II-specific' qualifier is appropriate because fungi use RNA Pol II for protein-coding gene transcription, unlike the RNA Pol I/III usage in some other contexts.",
    "The UniProt entry was first public in June 2025 and reviewed in January 2026; the benchmark construction date is unknown, so the annotation may not have been available at benchmark creation time."
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

**Accession:** `A0A0J9WP80` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 51. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0J9WP80.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:11.971052+00:00.  

```json
"A0A0J9WP80"
```

Source SHA-256: `233db24394251b04ce4ad2614aee099b64f729bde2f714650a660b7e09b32594`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0J9WP80.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:11.971052+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26817616","source":"PubMed"}],"value":"Fusarium transcription factor 2"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26817616","source":"PubMed"}],"value":"Zn(2)-C6 fungal-type transcription factor FTF2"}}}
```

Source SHA-256: `233db24394251b04ce4ad2614aee099b64f729bde2f714650a660b7e09b32594`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0J9WP80.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:11.971052+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26817616","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36986302","source":"PubMed"}],"value":"Zn(2)-C6 fungal-type transcription factor that has a role in conidia production and also in plant colonization (PubMed:26817616, PubMed:36986302). Acts as a negative regulator of the production of macroconidia and is required for full virulence and the positive regulation of SIX effectors (PubMed:36986302). In addition, FTF2 is also involved in the regulation of class II hydrophobins FOXG_02746 and FOXG_02748 likely required for plant colonization (PubMed:26817616, PubMed:36986302)"}]}
```

Source SHA-256: `233db24394251b04ce4ad2614aee099b64f729bde2f714650a660b7e09b32594`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0J9WP80.json)  
**Locator:** `/uniProtKBCrossReferences/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:11.971052+00:00.  

```json
{"database":"GO","id":"GO:0003677","properties":[{"key":"GoTerm","value":"F:DNA binding"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `233db24394251b04ce4ad2614aee099b64f729bde2f714650a660b7e09b32594`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0J9WP80.json)  
**Locator:** `/uniProtKBCrossReferences/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:11.971052+00:00.  

```json
{"database":"GO","id":"GO:0000981","properties":[{"key":"GoTerm","value":"F:DNA-binding transcription factor activity, RNA polymerase II-specific"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `233db24394251b04ce4ad2614aee099b64f729bde2f714650a660b7e09b32594`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0J9WP80?format=txt&versions=51)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:24:14.442802+00:00.  

```text
ID   FTF2_FUSO4              Reviewed;        1072 AA.
AC   A0A0J9WP80;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   14-OCT-2015, sequence version 1.
DT   28-JAN-2026, entry version 51.
DE   RecName: Full=Zn(2)-C6 fungal-type transcription factor FTF2 {ECO:0000303|PubMed:26817616};
DE   AltName: Full=Fusarium transcription factor 2 {ECO:0000303|PubMed:26817616};
GN   Name=FTF2 {ECO:0000303|PubMed:26817616}; ORFNames=FOXG_09390;
OS   Fusarium oxysporum f. sp. lycopersici (strain 4287 / CBS 123668 / FGSC 9935
OS   / NRRL 34936) (Fusarium vascular wilt of tomato).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Hypocreomycetidae; Hypocreales; Nectriaceae; Fusarium;
OC   Fusarium oxysporum species complex.
OX   NCBI_TaxID=426428;
```

Source SHA-256: `751d4f758c2e157df555c30fe021afb88cd7b5e0f8b42dc881a888cb83ea304e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0J9WP80?format=txt&versions=51)  
**Locator:** `lines 49-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:24:14.442802+00:00.  

```text
CC   -!- FUNCTION: Zn(2)-C6 fungal-type transcription factor that has a role in
CC       conidia production and also in plant colonization (PubMed:26817616,
CC       PubMed:36986302). Acts as a negative regulator of the production of
CC       macroconidia and is required for full virulence and the positive
CC       regulation of SIX effectors (PubMed:36986302). In addition, FTF2 is
CC       also involved in the regulation of class II hydrophobins FOXG_02746 and
CC       FOXG_02748 likely required for plant colonization (PubMed:26817616,
CC       PubMed:36986302). {ECO:0000269|PubMed:26817616,
CC       ECO:0000269|PubMed:36986302}.
```

Source SHA-256: `751d4f758c2e157df555c30fe021afb88cd7b5e0f8b42dc881a888cb83ea304e`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0J9WP80?format=txt&versions=51)  
**Locator:** `lines 79-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 51 / 1.  
**Retrieved:** 2026-11-02T04:24:14.442802+00:00.  

```text
DR   GO; GO:0000981; F:DNA-binding transcription factor activity, RNA polymerase II-specific; IEA:InterPro.
```

Source SHA-256: `751d4f758c2e157df555c30fe021afb88cd7b5e0f8b42dc881a888cb83ea304e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 19. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
