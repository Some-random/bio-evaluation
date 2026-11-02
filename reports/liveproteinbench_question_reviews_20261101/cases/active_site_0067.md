# active_site_0067

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **D** — Position 1236 (For beta-ketoacyl synthase activity)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTSGRGVSQMVTDDKLRYFLKKVTADLHETRGRLRELEEAAGEPIAVVAMGCRFPGGVRSPEDLWHLVASGRDAITPFPADRGWETAGLYDPDPDRPGKSCAREGGFLDDVASFDAGLFGVSPREALALDPQQRLLLEVTWETFERAGLTPAALRGTRTGVFVGTSSQEYAMLVHNARENFEGYSTGYLASVISGRLAYNFGLQGPAVTVDTACSSSLVALHQAAQALRAGDCTLALAGGVAVLATPSMFVEFSRQRGLAPDGRCKAFAAAADGTGWGEGVGLLLLERLSEARREGHPVLAVVRGSAVNQDGASNGLTAPNGPAQQRVIRRALAACRAVGGPGGRGGGPWHRDPAGRSHRGPGAAGHLRPRASRPTSFVARVVEVQYRPHPGRRRRRRCDQDGDGPAPRRTAAHPAYRRPHSTGGLVGGHRAAAHRGEGVAGDRPTPPGRRVLLRHQRHQRPCGAGTSRAGRLPRPRRTAGTAPGGDTAAALGALRPHRARPAGTGRPAARPYPRPPAPLPADTAHSLLVSRTLFGHRAVVLGDDRDELLTGLDALAGGGNAPGVLTGVAGEPRKPVLVFPGQGAQWEGMAAELYRESAVFRDRLRQCAEALAPHTGFSLVDVVCGAEGAAALDRVDVVQPALWAMLVSLAALWRSHGVEPGAVVGHSQGEIAAACVAGALSLEDGARIVALRSRLIAERLSGRGGMAFLGLPAGRAREWLAAWETRLGVAAVNGPSSVVVSGDAEALDGMLAAAEEEGVRAIRVAVDYASHSAQVATLEDELLAALPGITPRTAEIPFFSTVNGALIDTSALDPAYWYRNLRQTVRFESTVRRLLEAGHRGFVEVSPHPVLAVSVQEILDATATEGVVLASLRRGEGGLRRFLTSVGEAHVHGIPADFALPPGRLVDLPTLAFERRRYWLDAQPAAPAHQAEGSAGESAGESAGESAEESEAALFRQRLAGLPESERERAVLHTVCEQAAVVLNLTSAADLDTGKAFTDLGFVSMTAMELRNRLATATGIRLTPTAAFDHPTPEKLAAHLLSRLTGTAEPIAQPVAAPPAAGEPIAIVAMGCRYPGEVASPEELWELLAAGRDATSSFPANRGWNTDELYDPNPGRPGRTYVRRGGFLHDADQFDPQLFGISPREALAMDPQQRLLLEVAWEVLERARLSPASVRGSRTGVFMGISGQDYLPVLTASPDGGAGHLMTGTSTSVASGRIAYTFGLRGPAVTVDTACSSSLVALHLAIQALRQGDCSAALVGGATVLSTPGAFVEFSQQRALAPDGRCKAFAAGADGTGWGEGAGMLLVEPLSEARRQGHPVLALIRGSATNQDGASNGLSAPNGQAQQQVIRQALANSGLTTRDVDAVEAHGTGTALGDPIEAEALLATYGQDRPAQRPLWLGSLKSNIGHTAAAAGVGGVIKMVLALRRGVLPPTLHAADPTPHVDWSAGAVELLTEAREWPETGRPRRAGVSAFGISGTNAHVVLEQAPDPDPAPGSGLPHPAATLPAVPWPLSGRTAAALRAQAGRLHRFVLAHPGLAPADIGRSLAAGRAGLEHRAVVLGRDRDQLLAELATLAEGEGDDAGAAVRGTVRARSRMACLFTAGPGARSGPGRELYARMPVYAAAVDEAGAAFQALPARPLGETMALDEAPADPVLAQVLHFAEQVALFRLLDHWGTAPSHLLGHGPGEAAAAHCAGVLSLSDAAALLPALRATEDDIRRTVKELTFHPPRIPLVSGRTGRPLTPGELRSPEHWIALARETGTPAEGLRWLLADGVHHCLLPVPVDTAGIPGDLAEDGLLLLPDPSRDGTGATALLRALARLYVRGVAVGWDRMLADCGARLVELPTYAFQRGRYWPELAALPAAGPRPAGRADGQGGREFQERLAGASEEEREALLAALVRTHAAAALRLPDADAIDERTPLPELGFDSLTAVDLRNRLGADTGLRLAPSLVFQHPTVTALARHLLAAWTAAGGADRAAEDTTGAGTTLGPLLARAGELGRSEEFQELMHRMAAFRPAFDTPRAEHRIPPVRLSRGPAAPGLVCFPTFAGSSGPQQYARLAAAARGERDLWVLPAPGFSWDQPLPASVDALARLQADGVQECAEGQPVVLLGYSAGGWIAHATAAALEARGAGPSGVVLLDTYWPDSAMLPRLHARIDQDRKSGSSEAHWTEEIRDDAGLTAMAHYSRLFQTWRPAPITAPTLLVRAAEPAVAEPPRDWRPHWRLPHTAVDAPGTHFTLIREHGPAALGSVHHWLNGLQKKEH

[Multiple Choices]
A. Position 358 (For beta-ketoacyl synthase activity)
B. Position 6593 (Proton acceptor; for dehydratase activity)
C. Position 156 (Acyl-thioester intermediate)
D. Position 1236 (For beta-ketoacyl synthase activity)
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

> The exact sequence matches the UniProt entry, which annotates position 1236 as an active site for beta-ketoacyl synthase activity. This is computational annotation based on a PROSITE-ProRule, not direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a very large, modular polyketide synthase; general knowledge may suggest catalytic motifs, but does not by itself establish that residue 1236 is an active site for this activity.


**Missing item-specific fact**

> The protein-specific assignment of position 1236 to beta-ketoacyl synthase activity, which is supplied by the database annotation but not by the question input.


**Reason**

> Selecting the exact numbered residue and its assigned role depends on an item-specific annotation or equivalent protein-specific analysis. The reviewer-only source supports the key but was not available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports D among the listed options. It also annotates positions 1371 and 1411 for the same activity, but neither is an offered choice.


### Important caveats

- The annotation is computational and sequence-matched; it is not evidence of direct experimental validation.
- The protein has multiple annotated beta-ketoacyl synthase active-site positions, while each choice gives only one residue.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a very large, modular polyketide synthase; general knowledge may suggest catalytic motifs, but does not by itself establish that residue 1236 is an active site for this activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific assignment of position 1236 to beta-ketoacyl synthase activity, which is supplied by the database annotation but not by the question input.",
    "reason": "Selecting the exact numbered residue and its assigned role depends on an item-specific annotation or equivalent protein-specific analysis. The reviewer-only source supports the key but was not available to the evaluated model."
  },
  "case_id": "active_site_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which annotates position 1236 as an active site for beta-ketoacyl synthase activity. This is computational annotation based on a PROSITE-ProRule, not direct experimental confirmation."
  },
  "important_caveats": [
    "The annotation is computational and sequence-matched; it is not evidence of direct experimental validation.",
    "The protein has multiple annotated beta-ketoacyl synthase active-site positions, while each choice gives only one residue."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports D among the listed options. It also annotates positions 1371 and 1411 for the same activity, but neither is an offered choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which annotates position 1236 as an active site for beta-ketoacyl synthase activity. This is computational annotation based on a PROSITE-ProRule, not direct experimental confirmation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a very large, modular polyketide synthase; general knowledge may suggest catalytic motifs, but does not by itself establish that residue 1236 is an active site for this activity.",
    "missing_item_specific_fact": "The protein-specific assignment of position 1236 to beta-ketoacyl synthase activity, which is supplied by the database annotation but not by the question input.",
    "reason": "Selecting the exact numbered residue and its assigned role depends on an item-specific annotation or equivalent protein-specific analysis. The reviewer-only source supports the key but was not available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports D among the listed options. It also annotates positions 1371 and 1411 for the same activity, but neither is an offered choice."
  },
  "important_caveats": [
    "The annotation is computational and sequence-matched; it is not evidence of direct experimental validation.",
    "The protein has multiple annotated beta-ketoacyl synthase active-site positions, while each choice gives only one residue."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B4ER97 (Spectinabilin PKS system protein NorC, 2266 AA) annotates position 1236 as an Active site 'For beta-ketoacyl synthase activity' (evidence ECO:0000255|PROSITE-ProRule:PRU01348). The sequence matches exactly (SHA256 confirmed). Option B (position 6593) is impossible as it exceeds the 2266-residue protein length. Option C (position 156, acyl-thioester intermediate) describes ACP-type function, not KS. Option A (position 358) is not annotated as a KS active site in UniProt. Position 1236 is the only option consistent with the database annotation. Note: the annotation is computational (PROSITE-ProRule similarity-based, ECO:0000255), not experimentally verified.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C1](#evidence-c1), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can eliminate B (position 6593 exceeds the 2266-AA protein length) and C (acyl-thioester intermediate describes ACP function, not KS) through general biological reasoning. However, distinguishing A (position 358) from D (position 1236)—both labeled 'For beta-ketoacyl synthase activity'—requires knowing which KS domain in this multi-module PKS contains the catalytic cysteine at which exact residue number. The sequence contains apparent duplicated domain architecture (e.g., 'GCRFPGG' near the N-terminus and 'GCRYPGE' near the middle), suggesting two KS-like regions, making it non-trivial to determine from sequence alone whether position 358 or 1236 is the true catalytic residue without precise domain-boundary mapping or database annotation.


**Missing item-specific fact**

> The exact domain architecture and catalytic residue positions of NorC (B4ER97), specifically which of the two KS-like regions in this modular PKS harbors the functional catalytic cysteine and at which residue number, as annotated in UniProt (positions 1236, 1371, 1411 annotated; position 358 not annotated).


**Reason**

> While general PKS biology allows elimination of obviously wrong options (B, C), the core discrimination between A and D depends on knowing the precise residue numbering of the catalytic cysteine in a 2266-AA multi-domain enzyme. Identifying the 'GHSQGE' KS motif in the sequence is possible, but mapping it to exactly position 1236 versus position 358 requires either impractical residue counting or database lookup of domain boundaries.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B is eliminated by protein length (2266 < 6593). Option C describes a different enzymatic function (ACP). Options A and D both claim KS activity, but UniProt annotates only 1236 (not 358) as a KS active site, making D the uniquely supported answer among the choices. The question's phrasing 'the enzyme's catalytic center' (singular) is slightly imprecise given the protein has three annotated KS active sites (1236, 1371, 1411), but since only 1236 appears among the options, this does not create genuine ambiguity.


### Important caveats

- The active site annotation at position 1236 is computational (ECO:0000255, PROSITE-ProRule:PRU01348), i.e., inferred by sequence/structure similarity, not experimentally validated.
- The UniProt entry also annotates positions 1371 and 1411 as KS active sites; the question implicitly selects 1236 by offering only that option among the choices.
- The protein sequence contains apparent internal duplication of domain architecture, which could confuse domain-boundary identification without reference annotation.
- The reviewer-only evidence was absent from the evaluated model input; the model would need to rely on its own knowledge or sequence analysis to arrive at position 1236.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can eliminate B (position 6593 exceeds the 2266-AA protein length) and C (acyl-thioester intermediate describes ACP function, not KS) through general biological reasoning. However, distinguishing A (position 358) from D (position 1236)—both labeled 'For beta-ketoacyl synthase activity'—requires knowing which KS domain in this multi-module PKS contains the catalytic cysteine at which exact residue number. The sequence contains apparent duplicated domain architecture (e.g., 'GCRFPGG' near the N-terminus and 'GCRYPGE' near the middle), suggesting two KS-like regions, making it non-trivial to determine from sequence alone whether position 358 or 1236 is the true catalytic residue without precise domain-boundary mapping or database annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact domain architecture and catalytic residue positions of NorC (B4ER97), specifically which of the two KS-like regions in this modular PKS harbors the functional catalytic cysteine and at which residue number, as annotated in UniProt (positions 1236, 1371, 1411 annotated; position 358 not annotated).",
    "reason": "While general PKS biology allows elimination of obviously wrong options (B, C), the core discrimination between A and D depends on knowing the precise residue numbering of the catalytic cysteine in a 2266-AA multi-domain enzyme. Identifying the 'GHSQGE' KS motif in the sequence is possible, but mapping it to exactly position 1236 versus position 358 requires either impractical residue counting or database lookup of domain boundaries."
  },
  "case_id": "active_site_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C1",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B4ER97 (Spectinabilin PKS system protein NorC, 2266 AA) annotates position 1236 as an Active site 'For beta-ketoacyl synthase activity' (evidence ECO:0000255|PROSITE-ProRule:PRU01348). The sequence matches exactly (SHA256 confirmed). Option B (position 6593) is impossible as it exceeds the 2266-residue protein length. Option C (position 156, acyl-thioester intermediate) describes ACP-type function, not KS. Option A (position 358) is not annotated as a KS active site in UniProt. Position 1236 is the only option consistent with the database annotation. Note: the annotation is computational (PROSITE-ProRule similarity-based, ECO:0000255), not experimentally verified."
  },
  "important_caveats": [
    "The active site annotation at position 1236 is computational (ECO:0000255, PROSITE-ProRule:PRU01348), i.e., inferred by sequence/structure similarity, not experimentally validated.",
    "The UniProt entry also annotates positions 1371 and 1411 as KS active sites; the question implicitly selects 1236 by offering only that option among the choices.",
    "The protein sequence contains apparent internal duplication of domain architecture, which could confuse domain-boundary identification without reference annotation.",
    "The reviewer-only evidence was absent from the evaluated model input; the model would need to rely on its own knowledge or sequence analysis to arrive at position 1236."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is eliminated by protein length (2266 < 6593). Option C describes a different enzymatic function (ACP). Options A and D both claim KS activity, but UniProt annotates only 1236 (not 358) as a KS active site, making D the uniquely supported answer among the choices. The question's phrasing 'the enzyme's catalytic center' (singular) is slightly imprecise given the protein has three annotated KS active sites (1236, 1371, 1411), but since only 1236 appears among the options, this does not create genuine ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0067",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B4ER97 (Spectinabilin PKS system protein NorC, 2266 AA) annotates position 1236 as an Active site 'For beta-ketoacyl synthase activity' (evidence ECO:0000255|PROSITE-ProRule:PRU01348). The sequence matches exactly (SHA256 confirmed). Option B (position 6593) is impossible as it exceeds the 2266-residue protein length. Option C (position 156, acyl-thioester intermediate) describes ACP-type function, not KS. Option A (position 358) is not annotated as a KS active site in UniProt. Position 1236 is the only option consistent with the database annotation. Note: the annotation is computational (PROSITE-ProRule similarity-based, ECO:0000255), not experimentally verified.",
    "evidence_ids": ["C5", "H3", "C1", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can eliminate B (position 6593 exceeds the 2266-AA protein length) and C (acyl-thioester intermediate describes ACP function, not KS) through general biological reasoning. However, distinguishing A (position 358) from D (position 1236)—both labeled 'For beta-ketoacyl synthase activity'—requires knowing which KS domain in this multi-module PKS contains the catalytic cysteine at which exact residue number. The sequence contains apparent duplicated domain architecture (e.g., 'GCRFPGG' near the N-terminus and 'GCRYPGE' near the middle), suggesting two KS-like regions, making it non-trivial to determine from sequence alone whether position 358 or 1236 is the true catalytic residue without precise domain-boundary mapping or database annotation.",
    "missing_item_specific_fact": "The exact domain architecture and catalytic residue positions of NorC (B4ER97), specifically which of the two KS-like regions in this modular PKS harbors the functional catalytic cysteine and at which residue number, as annotated in UniProt (positions 1236, 1371, 1411 annotated; position 358 not annotated).",
    "reason": "While general PKS biology allows elimination of obviously wrong options (B, C), the core discrimination between A and D depends on knowing the precise residue numbering of the catalytic cysteine in a 2266-AA multi-domain enzyme. Identifying the 'GHSQGE' KS motif in the sequence is possible, but mapping it to exactly position 1236 versus position 358 requires either impractical residue counting or database lookup of domain boundaries."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is eliminated by protein length (2266 < 6593). Option C describes a different enzymatic function (ACP). Options A and D both claim KS activity, but UniProt annotates only 1236 (not 358) as a KS active site, making D the uniquely supported answer among the choices. The question's phrasing 'the enzyme's catalytic center' (singular) is slightly imprecise given the protein has three annotated KS active sites (1236, 1371, 1411), but since only 1236 appears among the options, this does not create genuine ambiguity."
  },
  "important_caveats": [
    "The active site annotation at position 1236 is computational (ECO:0000255, PROSITE-ProRule:PRU01348), i.e., inferred by sequence/structure similarity, not experimentally validated.",
    "The UniProt entry also annotates positions 1371 and 1411 as KS active sites; the question implicitly selects 1236 by offering only that option among the choices.",
    "The protein sequence contains apparent internal duplication of domain architecture, which could confuse domain-boundary identification without reference annotation.",
    "The reviewer-only evidence was absent from the evaluated model input; the model would need to rely on its own knowledge or sequence analysis to arrive at position 1236."
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

**Accession:** `B4ER97` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 80. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:19.126101+00:00.  

```json
"B4ER97"
```

Source SHA-256: `4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:19.126101+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"CAO85898.1","source":"EMBL"}],"value":"Modular polyketide synthase NorC"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"17763486","source":"PubMed"}],"value":"2.3.1.290"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Spectinabilin polyketide synthase system protein NorC"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Spectinabilin PKS system protein NorC"}]}}
```

Source SHA-256: `4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)  
**Locator:** `/features/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:19.126101+00:00.  

```json
{"description":"For beta-ketoacyl synthase activity","evidences":[{"evidenceCode":"ECO:0000255","id":"PRU01348","source":"PROSITE-ProRule"}],"location":{"end":{"modifier":"EXACT","value":1236},"start":{"modifier":"EXACT","value":1236}},"type":"Active site"}
```

Source SHA-256: `4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)  
**Locator:** `lines 161-163`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-02T04:27:21.445291+00:00.  

```text
FT   ACT_SITE        1236
FT                   /note="For beta-ketoacyl synthase activity"
FT                   /evidence="ECO:0000255|PROSITE-ProRule:PRU01348"
```

Source SHA-256: `1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 67. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
