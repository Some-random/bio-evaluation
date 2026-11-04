# active_site_0067

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0067.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 1236 (For beta-ketoacyl synthase activity)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

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

> The sequence-matched UniProt annotation identifies position 1236 as an active site for beta-ketoacyl synthase activity. This is computational annotation based on a PROSITE-ProRule, not direct experimental validation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, repeated enzyme sequence is consistent with a modular polyketide synthase. Transferable knowledge of PKS ketosynthase domains and their conserved catalytic-site signatures gives a meaningful way to assess the candidate positions against the supplied sequence; position 1236 is consistent with the beta-ketoacyl synthase role, unlike the out-of-range position 6593 or the differently described position 156. Position 358 shares the KS functional label, so its sequence/domain context must be compared rather than choosing by the label alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence supplies features that can support a family- and motif-based prediction; choosing D need not depend solely on recalling this protein’s database entry. The inference is not an experimental determination, and distinguishing D from the same-role alternative A may require careful motif/domain analysis.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although A and D both describe beta-ketoacyl synthase activity, the supplied sequence permits comparison of their positions against conserved domain and catalytic-site patterns; the reviewer evidence specifically supports D.


### Important caveats

- The supporting annotation is computational (PROSITE-ProRule), not experimental evidence.
- Other positions in this protein are also annotated for beta-ketoacyl synthase activity, but they are not among the offered choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, repeated enzyme sequence is consistent with a modular polyketide synthase. Transferable knowledge of PKS ketosynthase domains and their conserved catalytic-site signatures gives a meaningful way to assess the candidate positions against the supplied sequence; position 1236 is consistent with the beta-ketoacyl synthase role, unlike the out-of-range position 6593 or the differently described position 156. Position 358 shares the KS functional label, so its sequence/domain context must be compared rather than choosing by the label alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence supplies features that can support a family- and motif-based prediction; choosing D need not depend solely on recalling this protein’s database entry. The inference is not an experimental determination, and distinguishing D from the same-role alternative A may require careful motif/domain analysis."
  },
  "case_id": "active_site_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 1236 as an active site for beta-ketoacyl synthase activity. This is computational annotation based on a PROSITE-ProRule, not direct experimental validation."
  },
  "important_caveats": [
    "The supporting annotation is computational (PROSITE-ProRule), not experimental evidence.",
    "Other positions in this protein are also annotated for beta-ketoacyl synthase activity, but they are not among the offered choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although A and D both describe beta-ketoacyl synthase activity, the supplied sequence permits comparison of their positions against conserved domain and catalytic-site patterns; the reviewer evidence specifically supports D."
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
    "reason": "The sequence-matched UniProt annotation identifies position 1236 as an active site for beta-ketoacyl synthase activity. This is computational annotation based on a PROSITE-ProRule, not direct experimental validation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, repeated enzyme sequence is consistent with a modular polyketide synthase. Transferable knowledge of PKS ketosynthase domains and their conserved catalytic-site signatures gives a meaningful way to assess the candidate positions against the supplied sequence; position 1236 is consistent with the beta-ketoacyl synthase role, unlike the out-of-range position 6593 or the differently described position 156. Position 358 shares the KS functional label, so its sequence/domain context must be compared rather than choosing by the label alone.",
    "missing_item_specific_fact": "",
    "reason": "The sequence supplies features that can support a family- and motif-based prediction; choosing D need not depend solely on recalling this protein’s database entry. The inference is not an experimental determination, and distinguishing D from the same-role alternative A may require careful motif/domain analysis."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although A and D both describe beta-ketoacyl synthase activity, the supplied sequence permits comparison of their positions against conserved domain and catalytic-site patterns; the reviewer evidence specifically supports D."
  },
  "important_caveats": [
    "The supporting annotation is computational (PROSITE-ProRule), not experimental evidence.",
    "Other positions in this protein are also annotated for beta-ketoacyl synthase activity, but they are not among the offered choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B4ER97 (Spectinabilin PKS NorC, 2266 aa, sequence matched) annotates position 1236 as 'Active site' with description 'For beta-ketoacyl synthase activity' (evidence ECO:0000255, PROSITE-ProRule PRU01348). This is a computational/curated annotation based on PROSITE pattern matching to the conserved KS catalytic cysteine motif, not an experimental determination, but it directly supports the author's key. The sequence length is 2266, confirming position 1236 is valid.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General PKS knowledge can eliminate option B (position 6593 exceeds the 2266-aa protein length) and option C (acyl-thioester intermediate is an AT/ACP domain function, not a KS catalytic residue). However, distinguishing position 358 from position 1236 as the KS catalytic Cys in this 2266-aa non-colinear modular PKS requires precise domain-boundary identification or the specific PROSITE-ProRule annotation. The UniProt entry annotates THREE KS active sites (1236, 1371, 1411), all clustered in the second half of the protein, which is atypical for a standard linear modular PKS architecture. The non-colinear nature of this PKS (per the cited literature) means general linear-module architecture rules (e.g., 'first KS follows the loading AT') do not reliably predict which position in the raw sequence is the KS catalytic Cys. Counting to exact residue positions in a 2266-aa sequence is impractical, and the conserved KS motif context (catalytic Cys within PROSITE PRU01348) cannot be reliably located by eye without domain-prediction tools.


**Missing item-specific fact**

> The exact residue number of the KS catalytic cysteine in this particular non-colinear modular PKS (B4ER97/NorC). The PROSITE-ProRule computational assignment to position 1236, and the unusual clustering of three KS sites (1236, 1371, 1411) in the C-terminal half, cannot be predicted from general PKS architecture knowledge given the non-colinear arrangement.


**Reason**

> While general PKS biology eliminates options B and C, the critical A-vs-D distinction (position 358 vs. 1236 for KS activity) requires the specific PROSITE-ProRule annotation for this protein. The non-colinear PKS architecture makes general linear-module positional reasoning unreliable, and precise residue counting in a 2266-aa sequence is not feasible from the raw input alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A (position 358) and D (position 1236) describe 'beta-ketoacyl synthase activity.' Without the specific annotation, a model cannot definitively exclude position 358 as a potential KS catalytic site in a non-colinear PKS with unusual domain architecture. The evidence confirms 1236 is annotated as KS, but does not explicitly annotate 358 as something else (it is simply absent from the active-site features shown). A model relying solely on the sequence cannot rule out 358 with certainty.


### Important caveats

- The PROSITE-ProRule annotation (ECO:0000255) is computational pattern-matching, not experimental mutagenesis or structural determination.
- The protein is a non-colinear PKS (per cited literature), meaning standard linear modular PKS domain-ordering rules may not apply for position prediction.
- Three KS active sites are annotated (1236, 1371, 1411); the question selects only 1236 without explaining why the others are excluded.
- Option B (position 6593) is trivially eliminable as the protein is only 2266 residues.
- The reviewer-only evidence confirms sequence match but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General PKS knowledge can eliminate option B (position 6593 exceeds the 2266-aa protein length) and option C (acyl-thioester intermediate is an AT/ACP domain function, not a KS catalytic residue). However, distinguishing position 358 from position 1236 as the KS catalytic Cys in this 2266-aa non-colinear modular PKS requires precise domain-boundary identification or the specific PROSITE-ProRule annotation. The UniProt entry annotates THREE KS active sites (1236, 1371, 1411), all clustered in the second half of the protein, which is atypical for a standard linear modular PKS architecture. The non-colinear nature of this PKS (per the cited literature) means general linear-module architecture rules (e.g., 'first KS follows the loading AT') do not reliably predict which position in the raw sequence is the KS catalytic Cys. Counting to exact residue positions in a 2266-aa sequence is impractical, and the conserved KS motif context (catalytic Cys within PROSITE PRU01348) cannot be reliably located by eye without domain-prediction tools.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact residue number of the KS catalytic cysteine in this particular non-colinear modular PKS (B4ER97/NorC). The PROSITE-ProRule computational assignment to position 1236, and the unusual clustering of three KS sites (1236, 1371, 1411) in the C-terminal half, cannot be predicted from general PKS architecture knowledge given the non-colinear arrangement.",
    "reason": "While general PKS biology eliminates options B and C, the critical A-vs-D distinction (position 358 vs. 1236 for KS activity) requires the specific PROSITE-ProRule annotation for this protein. The non-colinear PKS architecture makes general linear-module positional reasoning unreliable, and precise residue counting in a 2266-aa sequence is not feasible from the raw input alone."
  },
  "case_id": "active_site_0067",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B4ER97 (Spectinabilin PKS NorC, 2266 aa, sequence matched) annotates position 1236 as 'Active site' with description 'For beta-ketoacyl synthase activity' (evidence ECO:0000255, PROSITE-ProRule PRU01348). This is a computational/curated annotation based on PROSITE pattern matching to the conserved KS catalytic cysteine motif, not an experimental determination, but it directly supports the author's key. The sequence length is 2266, confirming position 1236 is valid."
  },
  "important_caveats": [
    "The PROSITE-ProRule annotation (ECO:0000255) is computational pattern-matching, not experimental mutagenesis or structural determination.",
    "The protein is a non-colinear PKS (per cited literature), meaning standard linear modular PKS domain-ordering rules may not apply for position prediction.",
    "Three KS active sites are annotated (1236, 1371, 1411); the question selects only 1236 without explaining why the others are excluded.",
    "Option B (position 6593) is trivially eliminable as the protein is only 2266 residues.",
    "The reviewer-only evidence confirms sequence match but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A (position 358) and D (position 1236) describe 'beta-ketoacyl synthase activity.' Without the specific annotation, a model cannot definitively exclude position 358 as a potential KS catalytic site in a non-colinear PKS with unusual domain architecture. The evidence confirms 1236 is annotated as KS, but does not explicitly annotate 358 as something else (it is simply absent from the active-site features shown). A model relying solely on the sequence cannot rule out 358 with certainty."
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
    "reason": "UniProt entry B4ER97 (Spectinabilin PKS NorC, 2266 aa, sequence matched) annotates position 1236 as 'Active site' with description 'For beta-ketoacyl synthase activity' (evidence ECO:0000255, PROSITE-ProRule PRU01348). This is a computational/curated annotation based on PROSITE pattern matching to the conserved KS catalytic cysteine motif, not an experimental determination, but it directly supports the author's key. The sequence length is 2266, confirming position 1236 is valid.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General PKS knowledge can eliminate option B (position 6593 exceeds the 2266-aa protein length) and option C (acyl-thioester intermediate is an AT/ACP domain function, not a KS catalytic residue). However, distinguishing position 358 from position 1236 as the KS catalytic Cys in this 2266-aa non-colinear modular PKS requires precise domain-boundary identification or the specific PROSITE-ProRule annotation. The UniProt entry annotates THREE KS active sites (1236, 1371, 1411), all clustered in the second half of the protein, which is atypical for a standard linear modular PKS architecture. The non-colinear nature of this PKS (per the cited literature) means general linear-module architecture rules (e.g., 'first KS follows the loading AT') do not reliably predict which position in the raw sequence is the KS catalytic Cys. Counting to exact residue positions in a 2266-aa sequence is impractical, and the conserved KS motif context (catalytic Cys within PROSITE PRU01348) cannot be reliably located by eye without domain-prediction tools.",
    "missing_item_specific_fact": "The exact residue number of the KS catalytic cysteine in this particular non-colinear modular PKS (B4ER97/NorC). The PROSITE-ProRule computational assignment to position 1236, and the unusual clustering of three KS sites (1236, 1371, 1411) in the C-terminal half, cannot be predicted from general PKS architecture knowledge given the non-colinear arrangement.",
    "reason": "While general PKS biology eliminates options B and C, the critical A-vs-D distinction (position 358 vs. 1236 for KS activity) requires the specific PROSITE-ProRule annotation for this protein. The non-colinear PKS architecture makes general linear-module positional reasoning unreliable, and precise residue counting in a 2266-aa sequence is not feasible from the raw input alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A (position 358) and D (position 1236) describe 'beta-ketoacyl synthase activity.' Without the specific annotation, a model cannot definitively exclude position 358 as a potential KS catalytic site in a non-colinear PKS with unusual domain architecture. The evidence confirms 1236 is annotated as KS, but does not explicitly annotate 358 as something else (it is simply absent from the active-site features shown). A model relying solely on the sequence cannot rule out 358 with certainty."
  },
  "important_caveats": [
    "The PROSITE-ProRule annotation (ECO:0000255) is computational pattern-matching, not experimental mutagenesis or structural determination.",
    "The protein is a non-colinear PKS (per cited literature), meaning standard linear modular PKS domain-ordering rules may not apply for position prediction.",
    "Three KS active sites are annotated (1236, 1371, 1411); the question selects only 1236 without explaining why the others are excluded.",
    "Option B (position 6593) is trivially eliminable as the protein is only 2266 residues.",
    "The reviewer-only evidence confirms sequence match but was not available to the evaluated model."
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
  "benchmark_sequence_length": 2266,
  "benchmark_sequence_sha256": "dd3fabbdff587c4be38842084fbf29b98933cc68a78e913808797784fa6be7ca",
  "current_entry_audit": {
    "entryVersion": 82,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2008-09-23",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 2266,
  "current_source_sequence_sha256": "dd3fabbdff587c4be38842084fbf29b98933cc68a78e913808797784fa6be7ca",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 80,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B4ER97",
  "selected_historical_entry_version": 80,
  "selected_historical_record_sha256": "1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef",
  "selected_historical_source_sequence_length": 2266,
  "selected_historical_source_sequence_sha256": "dd3fabbdff587c4be38842084fbf29b98933cc68a78e913808797784fa6be7ca",
  "selected_historical_version": {
    "accession": "B4ER97",
    "database": "Swiss-Prot",
    "entryVersion": 80,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NORC_STRON",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B4ER97\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:19.126101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER97.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":82,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2008-09-23\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:19.126101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER97.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Streptoverticillium orinoci\",\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces orinoci\",\"taxonId\":67339}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:19.126101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER97.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAO85898.1\",\"source\":\"EMBL\"}],\"value\":\"Modular polyketide synthase NorC\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17763486\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.290\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Spectinabilin polyketide synthase system protein NorC\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Spectinabilin PKS system protein NorC\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:19.126101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER97.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1236},\"start\":{\"modifier\":\"EXACT\",\"value\":1236}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:27:19.126101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER97.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1371},\"start\":{\"modifier\":\"EXACT\",\"value\":1371}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:27:19.126101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER97.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"For beta-ketoacyl synthase activity\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01348\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1411},\"start\":{\"modifier\":\"EXACT\",\"value\":1411}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:27:19.126101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER97.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B4ER97.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Traitcheva N.\",\"Jenke-Kodama H.\",\"He J.\",\"Dittmann E.\",\"Hertweck C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"17763486\"},{\"database\":\"DOI\",\"id\":\"10.1002/cbic.200700309\"}],\"citationType\":\"journal article\",\"firstPage\":\"1841\",\"id\":\"17763486\",\"journal\":\"ChemBioChem\",\"lastPage\":\"1849\",\"publicationDate\":\"2007\",\"title\":\"Non-colinear polyketide biosynthesis in the aureothin and neoaureothin pathways: an evolutionary perspective.\",\"volume\":\"8\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"CAO85898.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"HKI-0260\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:27:19.126101+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4332fdfd8b2e693c9be27351fac30766009673b58e428df8d21cdaa87e97c93b",
  "url": "https://rest.uniprot.org/uniprotkb/B4ER97.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)

```json
{
  "entry_version": 80,
  "evidence_id": "H1",
  "excerpt": "ID   NORC_STRON              Reviewed;        2266 AA.\nAC   B4ER97;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   23-SEP-2008, sequence version 1.\nDT   28-JAN-2026, entry version 80.\nDE   RecName: Full=Spectinabilin polyketide synthase system protein NorC {ECO:0000305};\nDE            Short=Spectinabilin PKS system protein NorC {ECO:0000305};\nDE            EC=2.3.1.290 {ECO:0000305|PubMed:17763486};\nDE   AltName: Full=Modular polyketide synthase NorC {ECO:0000312|EMBL:CAO85898.1};\nGN   Name=norC {ECO:0000303|PubMed:17763486};\nOS   Streptomyces orinoci (Streptoverticillium orinoci).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=67339;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:21.445291+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef",
  "url": "https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)

```json
{
  "entry_version": 80,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAO85898.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND SUBUNIT.\nRC   STRAIN=HKI-0260;\nRX   PubMed=17763486; DOI=10.1002/cbic.200700309;\nRA   Traitcheva N., Jenke-Kodama H., He J., Dittmann E., Hertweck C.;\nRT   \"Non-colinear polyketide biosynthesis in the aureothin and neoaureothin\nRT   pathways: an evolutionary perspective.\";\nRL   ChemBioChem 8:1841-1849(2007).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:21.445291+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef",
  "url": "https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)

```json
{
  "entry_version": 80,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        1236\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:21.445291+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 161-163",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef",
  "url": "https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)

```json
{
  "entry_version": 80,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        1371\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:21.445291+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 164-166",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef",
  "url": "https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)

```json
{
  "entry_version": 80,
  "evidence_id": "H5",
  "excerpt": "FT   ACT_SITE        1411\nFT                   /note=\"For beta-ketoacyl synthase activity\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01348\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:21.445291+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 167-169",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef",
  "url": "https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 67. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
