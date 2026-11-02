# GO_cellular_component_0004

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — plasmodesma

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MDYDDSDFQNQNLHLAGEANNKFPPVLQPYALPKFDFDDTLNTHLRFDSLGESEAFLGIEGNEDNNWIEDFSRGSSGIVFSSGATESCAISRHNNVWSEATSSESVAMLLNSVGQDEVIVREDTIKKSDTSHELGCTMETVEPGQTSHERSLSKEETVNLQPNPSVDDTPGESSVVKTDDGQEQVLVKDDSPTAVEEASVEEKNSILTSNTATVEAIDTTDLGKIGTETTDNLLDQTEEKANVESRMEDDCSDGNVQTIITCSGELNNQSTLLPETSNDENVISDHIQSSYNRNDLTADARSILVEGHSDSHIDSASEVEKVEAENIGKTAKPDLKEIELSDVTVLERGDQAPSTLEVGGQDVSGTECQDLLVSTVHTSVAVEASLELAGELTTITNSVSIEKPELLSHQHMEVITSEHESTFQIETETYPQIHVFETSESVYISTMDSMVEAREGGVSKKSDNEGSARTSNLEQSMELPVNANDRDQDVKNSQILSESVVSGSVGYVSGGSTSELAESESQSDSIPTDKSETMIDSSLNLEELQPLSQDGAPAVSLTSSIDLHMVKTSSDDSDQGSYSETKKVYGEPENGQTVPPVDASCSGSQMDQEARKRAEGTKQSTYSVEGCPRSEGSKDAVDADGVGQVLQQQSEELIFEENVVTEAVKAPETLSVLDKDNKNEMPITSSLPILGSEAGKDGQEEDNTAASGGIMAAGTPVTHPKGDAIVLGDSRASTCSESSVKSYVTAIEDAATNLKTPLDSFPTVKTSELQFNNTETNSVKKPEDQNISGFMSAGSPVLNRNETSSSEMNLTPDQLKAGKISKAVIFSQATLVSPIVVGSPSTSSLDKTAAKSSKAKSERKPRRTSKSVGKETSRKGTSVKGATPIEQFQSGGKTNAVNQSLASHIQITQSTEKQRSLQSPALKAFGSLSTPTASLPDLNSSALSSILRRPFTDLQQVQLRAQIFVYGALIQGTAPDEAYMISAFGGADGGKGSWEKSWRTCVVRAQKSLVATPETPLQSRPGKTETPSAGHTNSKESSGTNPMIPLSSPLWSLSTSVDTLQSSSVQRGSAATHQPLLSASHAHQTPPTQNIVGHNTPWMSPLPFRNAWLASQQTSGFDVGSRFPVYPITDPVKLTPMKESSMTLSGAKHVQSGTSSNVSKVTPTLEPTSTVVAPAQHSTRVKSRKRKKMPVSVESGPNILNSLKQTELAASPLVPFTPTPANLGYNAGTLPSVVSMTAVPMDLVSTFPGKKIKSSFPSPIFGGNLVREVKQRSVLSEDTIEKLKEAKMHAEDASALATAAVSHSEYVWKQIEQQSHAGLQPETQDRLASAAVAIAAAAAVAKAAAAAANVAANAALQAKLMAEEASLPNASDQGLPKSYDSILPGQGTPASILKGEGAVVNSSSVLIAAREASKKRVEAATAATKRAENMDSIVKAAELASEAVSQAGILVSMGHPPLLNKLVEAGPSNYWRQAQESQEVQPCKTVVLEKETVSTSEGTFAGPKIVQTEFGGSVNTADGVSGPVPATGKLKGQEGDKYADLAKNNDVVFEPEVGSKFSIDAQQTIKATKNEDIKEGSNVEVFKEEPGLRTAWYSANVLSLEDDKAYVLFSDLSVEQGTDKLKEWVALKGEGDQAPKIRPARSVTALPYEGTRKRRRAALGDHIWKIGDRVDSWVHDSWLEGVITEKNKKDENTVTVHFPAEEETLTIKAWNLRPSLVWKDGKWIECSSSGETISSSHEGDTPKEKRPRLGTPALVAEVKDTSMKIVDDPDLGKPPQTGVLNLGVSENTFNIGKSTREENKPDPLRMKRTGLQKQGSKVIFGVPKPGKKRKFMDVSKHYVSEASTKTQERKEPVKPVRSIVPQNSGIGSWKMPSKTISIEKQTTISRPKTFKPAPKPKEKPGATARIIPRKDSRNTTASDMESDESAENRGPGSGVSFKGTVEEQTTSSSHDTGSKNSSSLSTNKGRVAPTAGRLAKIEEDKALAENSSKTSEGMEPRRSIRRIQPTSRLLEGLQTSMMTSKIPSVSHSKSHLSQSKK

[Multiple Choices]
A. neuron projection
B. integrator complex
C. cytoplasm
D. plasmodesma
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

## Luna’s full visible review

### Expected-answer support: supported

> The sequence-matched UniProt record annotates the protein to the plasmodesma (GO:0009506; HDA:TAIR), supporting D. However, it also reports experimentally supported nuclear localization, so the evidence does not establish that plasmodesma is the primary location.

Cited evidence: [C7](#evidence-c7), [H6](#evidence-h6), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices make plasmodesma a plausible plant-specific location, but the supplied sequence gives no clear, specific signal that distinguishes it from the other choices or establishes plasmodesmal localization.

**Missing item-specific fact**

> The protein-specific plasmodesma localization annotation or experimental localization evidence is absent from the question input.

**Reason**

> Identifying D depends on item-specific localization knowledge, not a concrete inference from the sequence and choices. The reviewer-only annotation supports the key but was not supplied to the evaluated model.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The evidence supports D, but the protein is also experimentally annotated to the nucleus, which is not an option. The supplied evidence does not establish cytoplasm as an alternative answer or resolve which location is primary.

### Important caveats

- The plasmodesma annotation is HDA:TAIR, whereas the nuclear localization annotation is IDA:UniProtKB; these evidence types should not be conflated.
- The exact source snapshot used by the question author is unknown, although the reviewer evidence matches the supplied sequence and a historical entry.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "GO_cellular_component_0004",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the protein to the plasmodesma (GO:0009506; HDA:TAIR), supporting D. However, it also reports experimentally supported nuclear localization, so the evidence does not establish that plasmodesma is the primary location.",
    "evidence_ids": [
      "C7",
      "H6",
      "C5",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices make plasmodesma a plausible plant-specific location, but the supplied sequence gives no clear, specific signal that distinguishes it from the other choices or establishes plasmodesmal localization.",
    "missing_item_specific_fact": "The protein-specific plasmodesma localization annotation or experimental localization evidence is absent from the question input.",
    "reason": "Identifying D depends on item-specific localization knowledge, not a concrete inference from the sequence and choices. The reviewer-only annotation supports the key but was not supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D, but the protein is also experimentally annotated to the nucleus, which is not an option. The supplied evidence does not establish cytoplasm as an alternative answer or resolve which location is primary."
  },
  "important_caveats": [
    "The plasmodesma annotation is HDA:TAIR, whereas the nuclear localization annotation is IDA:UniProtKB; these evidence types should not be conflated.",
    "The exact source snapshot used by the question author is unknown, although the reviewer evidence matches the supplied sequence and a historical entry."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `F4JP43`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 95. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F4JP43.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:12.242053+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"37676567","source":"PubMed"}],"id":"SL-0191","value":"Nucleus"}}]}
```

Source SHA-256: `b6b875ea63af54cc79d5ff9353463ef2348a7572fb1567dd6696307d7a15769f`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F4JP43.json)  
**Locator:** `/uniProtKBCrossReferences/31`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:12.242053+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0007005","id":"21533090","source":"PubMed"}],"id":"GO:0009506","properties":[{"key":"GoTerm","value":"C:plasmodesma"},{"key":"GoEvidenceType","value":"HDA:TAIR"}]}
```

Source SHA-256: `b6b875ea63af54cc79d5ff9353463ef2348a7572fb1567dd6696307d7a15769f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F4JP43?format=txt&versions=95)  
**Locator:** `lines 142-142`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:28:16.792374+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:37676567}.
```

Source SHA-256: `3e308dae603c090ea86146ef2f689ad6e69b9ff7f3df342e5090daa986ccaa7c`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F4JP43?format=txt&versions=95)  
**Locator:** `lines 194-194`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 95 / 1.  
**Retrieved:** 2026-11-02T04:28:16.792374+00:00.  

```text
DR   GO; GO:0009506; C:plasmodesma; HDA:TAIR.
```

Source SHA-256: `3e308dae603c090ea86146ef2f689ad6e69b9ff7f3df342e5090daa986ccaa7c`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json) (zero-based source row 4). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
