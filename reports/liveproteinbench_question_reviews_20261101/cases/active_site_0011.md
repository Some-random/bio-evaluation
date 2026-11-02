# active_site_0011

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 1686 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSKNIQRQRSISSISSRGVDRDRDPASGGLGLLSPYNSRSPLAGLHHSPGSLDATANQLSRPTFLLERKATEDIAKLDGVLFDDIPTLGSSNDHISSLGAGSPYPTINTSLAVTNPNYLSASSPGGPRRRANTASGPLSPAPPASPIDRLSKTTNRGSFVPSTARQPMNSQPPAPASSAPPPKQRTTSPSVASPPSQTRSQTVPYLSSNFGPTANMYGQRQPSGVDPSRPFHQVPLPPPPMSPPPAIGTINSIMTNIPPPPPRYPSAPAAAIHLPGPPGAPPPSGLPPPPGPPPNNTTNWQGTWIGAYGSYIPPPPPQQTHRPYNPQPYKTVNGQTIAIPPPPPPTESMQMSATYIPQGDSYGEGVGIPGLGMDDMAAWSATSQSSWLGGYNSIGSLAPTNASDTAASTPVDAYGSHNRDNSTTSNATSSGASGIPPELAAQWPLDRVLDWLQANNFSNDWRSTFRALDLHGNRFLEVGSANGGRGNFGMMHQLVYPRLAAECISSGTGWDQPREREEGKRMRRLIRHIVKGETPGTGMSSHTRKESISNTSLVPTSAGPDSGSPDTPIKAPGPGFSVGHPGGNHRKLLVGNFDDEGAHRRSPVASEPSEVGITFTERSSSNRGYSPAGSPAPTPGLFSSSTAPNLASSPGGRFGGHRNRNSTDSVSSNAAIYGSGVPPDASQVLRSQMNFGDMAKDTRRYGHDGGNRPSPLGDNASNGDRSAGASEPPGSAKEGKSFLSIFNHRKKKHHDDPDSPTSPMQHKSHSLGSRGNASETSLERPGSSVSTSHEHNTPASSMRSRRITTGRIFILATLDYWNYRMVDVSDVESASDLRQLICINLGLPDADGAQVYLTELGKFDHEDPLDDSQLVANKKVRADAAGSLKVFVRPGNMAGLAVNIGQSQNALSPAHLPAGAKMDEDTYARLNGQRRRSSSSPPASRQNTLTGGEHGKPTSTGADDDENKDPKSDDIAQQAEAHRIEMERKQQAYLAKRKHARENGNSPSENGTGSYTGIVGPKVIDFDEPRNSPFEDKKPFDSAFAPQRRAPAAPLDPSATLIKANSLSKRGSHQRNSQGSVDGFPSKRQGTGMTESPKHISEKRKPTNERQALGGIGAALAGMGRGLGGIAHPGGAGQRGTSPNRSSPGSAGESAGVASSTTDRGEDAKSRKPISSGNVSPTSSARTVSDEPPQLPKVVIKPRIFDGDSSSDEDSDDDSDDGLFAKPLAGRGGDDAAAKGKEPATKPVAKSPMSKHGTFWNDADSDGDEDPISESASNLNKRPSLTVNTKRGRKGLSVTFTSPDLPSSAGSKTAAGDEDDRSSRGSKRTPNTPHSEGWDSNNDKDVKLSRRKSFMEKDTSIWANRPPTDALINNLEDFFPNLDVDQPVLEEGELPGDLPPSPIAEAEEPHDQQQAKSMTTSRISNLYNDSDTLGSDESTLKALERPASIVSVARKNTRRSGGLGRMKSIREVAHKRYTQGAGAPPPVPAAPNNSNNSSSSGSKNSNLMRRKSTKMFNANIVQIRPERGSMILPQIPQDHLPSLPHNANNQIPKRQTTFRWFKGQLIGKGTYGRVYLGMNATTGEFLAVKEVEVNPKAAGGDKNKMKELVAALDQEIDTMQHLDHVNIVQYLGCERKETSISIFLEYIPGGSIGSCLRKHGKFEESVVSSLTRQTLSGLAYLHREGILHRDLKADNILLDVDGTAKISDFGISKKTDNIYGNDKTNSMQGSVFWMAPEVIRSQGEGYSAKVDIWSLGCVVLEMFAGRRPWSKDEAVGAIYKIANGETPPIPEEVSAAVTPVALSFMWDCFSVNPEERPTATKLLAEHPFCVFRDDYDFDQTELYAKIKGTWNTK

[Multiple Choices]
A. Position 1236 (For beta-ketoacyl synthase activity)
B. Position 180 (For beta-ketoacyl synthase activity)
C. Position 1686 (Proton acceptor)
D. Position 538 (Proton acceptor)
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence's UniProt annotation assigns position 1686 as a proton acceptor. This is a PROSITE-ProRule computational annotation, not direct experimental validation.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a protein-kinase catalytic HRDLK motif in its C-terminal kinase domain. The conserved Asp in this motif is a catalytic base, supporting the proton-acceptor choice at position 1686; the beta-ketoacyl-synthase choices do not fit the kinase sequence context.


**Missing item-specific fact**

> No additional item-specific fact is essential to distinguish the choices if the kinase motif and residue numbering are identified from the supplied sequence.


**Reason**

> A conserved catalytic kinase motif provides a concrete sequence-based rationale for the proton-acceptor option, rather than requiring recall of the protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The kinase motif supports the proton-acceptor choice at position 1686; the other listed positions and activity labels are not comparably supported by the sequence.


### Important caveats

- The supporting database annotation is computationally assigned by PROSITE-ProRule; the supplied evidence does not establish experimental confirmation of this residue's role.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a protein-kinase catalytic HRDLK motif in its C-terminal kinase domain. The conserved Asp in this motif is a catalytic base, supporting the proton-acceptor choice at position 1686; the beta-ketoacyl-synthase choices do not fit the kinase sequence context.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No additional item-specific fact is essential to distinguish the choices if the kinase motif and residue numbering are identified from the supplied sequence.",
    "reason": "A conserved catalytic kinase motif provides a concrete sequence-based rationale for the proton-acceptor option, rather than requiring recall of the protein's database entry."
  },
  "case_id": "active_site_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched sequence's UniProt annotation assigns position 1686 as a proton acceptor. This is a PROSITE-ProRule computational annotation, not direct experimental validation."
  },
  "important_caveats": [
    "The supporting database annotation is computationally assigned by PROSITE-ProRule; the supplied evidence does not establish experimental confirmation of this residue's role."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The kinase motif supports the proton-acceptor choice at position 1686; the other listed positions and activity labels are not comparably supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence's UniProt annotation assigns position 1686 as a proton acceptor. This is a PROSITE-ProRule computational annotation, not direct experimental validation.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a protein-kinase catalytic HRDLK motif in its C-terminal kinase domain. The conserved Asp in this motif is a catalytic base, supporting the proton-acceptor choice at position 1686; the beta-ketoacyl-synthase choices do not fit the kinase sequence context.",
    "missing_item_specific_fact": "No additional item-specific fact is essential to distinguish the choices if the kinase motif and residue numbering are identified from the supplied sequence.",
    "reason": "A conserved catalytic kinase motif provides a concrete sequence-based rationale for the proton-acceptor option, rather than requiring recall of the protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The kinase motif supports the proton-acceptor choice at position 1686; the other listed positions and activity labels are not comparably supported by the sequence."
  },
  "important_caveats": [
    "The supporting database annotation is computationally assigned by PROSITE-ProRule; the supplied evidence does not establish experimental confirmation of this residue's role."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A194W8T8 (MKH1_CYTMA, MAPKKK mkh1 from Cytospora mali, EC 2.7.11.24) annotates position 1686 as 'Proton acceptor' active site, with evidence code ECO:0000255 (PROSITE-ProRule PRU00159, i.e., transferred by protein-family similarity). The sequence matches exactly (1849 AA, SHA256 match). The HRD motif ('HRDLKADNILL') is visible in the C-terminal kinase domain, and the aspartate in HRD is the canonical catalytic base/proton acceptor in protein kinases. The annotation is computational (family-based) rather than direct experimental mutagenesis, but it is consistent with well-established kinase biochemistry.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [H1](#evidence-h1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable protein-kinase motifs (glycine-rich loop, VAIK-like lysine, HRD catalytic loop 'HRDLKADNILL', DFG motif) in the C-terminal ~350 residues, confirming this is a protein kinase. The catalytic aspartate in the HRD motif is the proton acceptor. Position 538 falls in the N-terminal low-complexity/disordered region (rich in Ser, Thr, Pro, Arg, Gly with no catalytic motifs), so it cannot be the kinase catalytic residue. Positions 1236 and 180 are similarly in the N-terminal regulatory region, and 'beta-ketoacyl synthase activity' is a fatty-acid-synthase function entirely unrelated to a MAPKKK. Thus, by recognizing kinase motifs and their domain location, one can eliminate A, B, and D, leaving C.


**Missing item-specific fact**

> Exact residue counting to 1686 in a 1849-aa sequence is impractical by hand, but the reasoning does not require exact counting—only that 1686/1849 ≈ 91% (within the kinase domain) while 538/1849 ≈ 29% (within the disordered N-terminus) is sufficient to distinguish C from D.


**Reason**

> A knowledgeable reader can identify kinase domain motifs, recognize that the catalytic HRD aspartate must lie within the kinase domain (C-terminal region), and eliminate position 538 (N-terminal disordered region) and the 'beta-ketoacyl synthase' distractors (wrong enzyme class). This constitutes a concrete biological reasoning chain from the supplied sequence and choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B invoke beta-ketoacyl synthase activity, which is irrelevant to a protein kinase. Option D places the proton acceptor at position 538, deep in the N-terminal disordered region far from any kinase catalytic motif. Only option C places the proton acceptor within the kinase domain at the HRD aspartate. No ambiguity exists.


### Important caveats

- The active-site annotation carries evidence code ECO:0000255 (inferred by similarity via PROSITE-ProRule), not direct experimental mutagenesis data for this specific protein.
- The UniProt entry was first publicly released in June 2025; the author's source snapshot is unknown, though the sequence has been unchanged since 2016.
- Precisely counting to residue 1686 in a 1849-residue sequence is extremely error-prone without computational assistance; the reasoning relies on approximate domain localization rather than exact arithmetic.
- The accession identity was inferred from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable protein-kinase motifs (glycine-rich loop, VAIK-like lysine, HRD catalytic loop 'HRDLKADNILL', DFG motif) in the C-terminal ~350 residues, confirming this is a protein kinase. The catalytic aspartate in the HRD motif is the proton acceptor. Position 538 falls in the N-terminal low-complexity/disordered region (rich in Ser, Thr, Pro, Arg, Gly with no catalytic motifs), so it cannot be the kinase catalytic residue. Positions 1236 and 180 are similarly in the N-terminal regulatory region, and 'beta-ketoacyl synthase activity' is a fatty-acid-synthase function entirely unrelated to a MAPKKK. Thus, by recognizing kinase motifs and their domain location, one can eliminate A, B, and D, leaving C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Exact residue counting to 1686 in a 1849-aa sequence is impractical by hand, but the reasoning does not require exact counting—only that 1686/1849 ≈ 91% (within the kinase domain) while 538/1849 ≈ 29% (within the disordered N-terminus) is sufficient to distinguish C from D.",
    "reason": "A knowledgeable reader can identify kinase domain motifs, recognize that the catalytic HRD aspartate must lie within the kinase domain (C-terminal region), and eliminate position 538 (N-terminal disordered region) and the 'beta-ketoacyl synthase' distractors (wrong enzyme class). This constitutes a concrete biological reasoning chain from the supplied sequence and choices."
  },
  "case_id": "active_site_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "H1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A194W8T8 (MKH1_CYTMA, MAPKKK mkh1 from Cytospora mali, EC 2.7.11.24) annotates position 1686 as 'Proton acceptor' active site, with evidence code ECO:0000255 (PROSITE-ProRule PRU00159, i.e., transferred by protein-family similarity). The sequence matches exactly (1849 AA, SHA256 match). The HRD motif ('HRDLKADNILL') is visible in the C-terminal kinase domain, and the aspartate in HRD is the canonical catalytic base/proton acceptor in protein kinases. The annotation is computational (family-based) rather than direct experimental mutagenesis, but it is consistent with well-established kinase biochemistry."
  },
  "important_caveats": [
    "The active-site annotation carries evidence code ECO:0000255 (inferred by similarity via PROSITE-ProRule), not direct experimental mutagenesis data for this specific protein.",
    "The UniProt entry was first publicly released in June 2025; the author's source snapshot is unknown, though the sequence has been unchanged since 2016.",
    "Precisely counting to residue 1686 in a 1849-residue sequence is extremely error-prone without computational assistance; the reasoning relies on approximate domain localization rather than exact arithmetic.",
    "The accession identity was inferred from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B invoke beta-ketoacyl synthase activity, which is irrelevant to a protein kinase. Option D places the proton acceptor at position 538, deep in the N-terminal disordered region far from any kinase catalytic motif. Only option C places the proton acceptor within the kinase domain at the HRD aspartate. No ambiguity exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A194W8T8 (MKH1_CYTMA, MAPKKK mkh1 from Cytospora mali, EC 2.7.11.24) annotates position 1686 as 'Proton acceptor' active site, with evidence code ECO:0000255 (PROSITE-ProRule PRU00159, i.e., transferred by protein-family similarity). The sequence matches exactly (1849 AA, SHA256 match). The HRD motif ('HRDLKADNILL') is visible in the C-terminal kinase domain, and the aspartate in HRD is the canonical catalytic base/proton acceptor in protein kinases. The annotation is computational (family-based) rather than direct experimental mutagenesis, but it is consistent with well-established kinase biochemistry.",
    "evidence_ids": ["C5", "H3", "C4", "H1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable protein-kinase motifs (glycine-rich loop, VAIK-like lysine, HRD catalytic loop 'HRDLKADNILL', DFG motif) in the C-terminal ~350 residues, confirming this is a protein kinase. The catalytic aspartate in the HRD motif is the proton acceptor. Position 538 falls in the N-terminal low-complexity/disordered region (rich in Ser, Thr, Pro, Arg, Gly with no catalytic motifs), so it cannot be the kinase catalytic residue. Positions 1236 and 180 are similarly in the N-terminal regulatory region, and 'beta-ketoacyl synthase activity' is a fatty-acid-synthase function entirely unrelated to a MAPKKK. Thus, by recognizing kinase motifs and their domain location, one can eliminate A, B, and D, leaving C.",
    "missing_item_specific_fact": "Exact residue counting to 1686 in a 1849-aa sequence is impractical by hand, but the reasoning does not require exact counting—only that 1686/1849 ≈ 91% (within the kinase domain) while 538/1849 ≈ 29% (within the disordered N-terminus) is sufficient to distinguish C from D.",
    "reason": "A knowledgeable reader can identify kinase domain motifs, recognize that the catalytic HRD aspartate must lie within the kinase domain (C-terminal region), and eliminate position 538 (N-terminal disordered region) and the 'beta-ketoacyl synthase' distractors (wrong enzyme class). This constitutes a concrete biological reasoning chain from the supplied sequence and choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B invoke beta-ketoacyl synthase activity, which is irrelevant to a protein kinase. Option D places the proton acceptor at position 538, deep in the N-terminal disordered region far from any kinase catalytic motif. Only option C places the proton acceptor within the kinase domain at the HRD aspartate. No ambiguity exists."
  },
  "important_caveats": [
    "The active-site annotation carries evidence code ECO:0000255 (inferred by similarity via PROSITE-ProRule), not direct experimental mutagenesis data for this specific protein.",
    "The UniProt entry was first publicly released in June 2025; the author's source snapshot is unknown, though the sequence has been unchanged since 2016.",
    "Precisely counting to residue 1686 in a 1849-residue sequence is extremely error-prone without computational assistance; the reasoning relies on approximate domain localization rather than exact arithmetic.",
    "The accession identity was inferred from dataset metadata and was not provided to the evaluated model."
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

**Accession:** `A0A194W8T8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.396358+00:00.  

```json
"A0A194W8T8"
```

Source SHA-256: `1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.396358+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39631571","source":"PubMed"}],"value":"2.7.11.24"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39631571","source":"PubMed"}],"value":"Mitogen-activated protein kinase kinase kinase mkh1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39631571","source":"PubMed"}],"value":"MAP kinase kinase kinase mkh1"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"39631571","source":"PubMed"}],"value":"MAPKKK mkh1"}]}}
```

Source SHA-256: `1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A194W8T8.json)  
**Locator:** `/features/39`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:41.396358+00:00.  

```json
{"description":"Proton acceptor","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU00159","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":1686},"start":{"modifier":"EXACT","value":1686}},"type":"Active site"}
```

Source SHA-256: `1d8fb7dfca0c30806738123fd65cb610f550595d8c15b16c52823f1772eb9f36`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:22.695404+00:00.  

```text
ID   MKH1_CYTMA              Reviewed;        1849 AA.
AC   A0A194W8T8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-OCT-2016, sequence version 1.
DT   28-JAN-2026, entry version 30.
DE   RecName: Full=Mitogen-activated protein kinase kinase kinase mkh1 {ECO:0000303|PubMed:39631571};
DE            Short=MAP kinase kinase kinase mkh1 {ECO:0000303|PubMed:39631571};
DE            Short=MAPKKK mkh1 {ECO:0000303|PubMed:39631571};
DE            EC=2.7.11.24 {ECO:0000305|PubMed:39631571};
GN   Name=mkh1 {ECO:0000303|PubMed:39631571}; ORFNames=VM1G_08015;
OS   Cytospora mali (Apple Valsa canker fungus) (Valsa mali).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;
OC   Sordariomycetidae; Diaporthales; Cytosporaceae; Cytospora.
OX   NCBI_TaxID=578113;
```

Source SHA-256: `d8496e59b0240fb2d9db3c0360daa33c12604e1a19d07fbf3a81c8ec7bbcdb1a`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A194W8T8?format=txt&versions=30)  
**Locator:** `lines 213-215`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:22.695404+00:00.  

```text
FT   ACT_SITE        1686
FT                   /note="Proton acceptor"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU00159"
```

Source SHA-256: `d8496e59b0240fb2d9db3c0360daa33c12604e1a19d07fbf3a81c8ec7bbcdb1a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 11. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
