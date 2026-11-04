# EC_number_0151

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0151.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 2.3.1.290

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTSGRGVSQMVTDDKLRYFLKKVTADLHETRGRLRELEEAAGEPIAVVAMGCRFPGGVRSPEDLWHLVASGRDAITPFPADRGWETAGLYDPDPDRPGKSCAREGGFLDDVASFDAGLFGVSPREALALDPQQRLLLEVTWETFERAGLTPAALRGTRTGVFVGTSSQEYAMLVHNARENFEGYSTGYLASVISGRLAYNFGLQGPAVTVDTACSSSLVALHQAAQALRAGDCTLALAGGVAVLATPSMFVEFSRQRGLAPDGRCKAFAAAADGTGWGEGVGLLLLERLSEARREGHPVLAVVRGSAVNQDGASNGLTAPNGPAQQRVIRRALAACRAVGGPGGRGGGPWHRDPAGRSHRGPGAAGHLRPRASRPTSFVARVVEVQYRPHPGRRRRRRCDQDGDGPAPRRTAAHPAYRRPHSTGGLVGGHRAAAHRGEGVAGDRPTPPGRRVLLRHQRHQRPCGAGTSRAGRLPRPRRTAGTAPGGDTAAALGALRPHRARPAGTGRPAARPYPRPPAPLPADTAHSLLVSRTLFGHRAVVLGDDRDELLTGLDALAGGGNAPGVLTGVAGEPRKPVLVFPGQGAQWEGMAAELYRESAVFRDRLRQCAEALAPHTGFSLVDVVCGAEGAAALDRVDVVQPALWAMLVSLAALWRSHGVEPGAVVGHSQGEIAAACVAGALSLEDGARIVALRSRLIAERLSGRGGMAFLGLPAGRAREWLAAWETRLGVAAVNGPSSVVVSGDAEALDGMLAAAEEEGVRAIRVAVDYASHSAQVATLEDELLAALPGITPRTAEIPFFSTVNGALIDTSALDPAYWYRNLRQTVRFESTVRRLLEAGHRGFVEVSPHPVLAVSVQEILDATATEGVVLASLRRGEGGLRRFLTSVGEAHVHGIPADFALPPGRLVDLPTLAFERRRYWLDAQPAAPAHQAEGSAGESAGESAGESAEESEAALFRQRLAGLPESERERAVLHTVCEQAAVVLNLTSAADLDTGKAFTDLGFVSMTAMELRNRLATATGIRLTPTAAFDHPTPEKLAAHLLSRLTGTAEPIAQPVAAPPAAGEPIAIVAMGCRYPGEVASPEELWELLAAGRDATSSFPANRGWNTDELYDPNPGRPGRTYVRRGGFLHDADQFDPQLFGISPREALAMDPQQRLLLEVAWEVLERARLSPASVRGSRTGVFMGISGQDYLPVLTASPDGGAGHLMTGTSTSVASGRIAYTFGLRGPAVTVDTACSSSLVALHLAIQALRQGDCSAALVGGATVLSTPGAFVEFSQQRALAPDGRCKAFAAGADGTGWGEGAGMLLVEPLSEARRQGHPVLALIRGSATNQDGASNGLSAPNGQAQQQVIRQALANSGLTTRDVDAVEAHGTGTALGDPIEAEALLATYGQDRPAQRPLWLGSLKSNIGHTAAAAGVGGVIKMVLALRRGVLPPTLHAADPTPHVDWSAGAVELLTEAREWPETGRPRRAGVSAFGISGTNAHVVLEQAPDPDPAPGSGLPHPAATLPAVPWPLSGRTAAALRAQAGRLHRFVLAHPGLAPADIGRSLAAGRAGLEHRAVVLGRDRDQLLAELATLAEGEGDDAGAAVRGTVRARSRMACLFTAGPGARSGPGRELYARMPVYAAAVDEAGAAFQALPARPLGETMALDEAPADPVLAQVLHFAEQVALFRLLDHWGTAPSHLLGHGPGEAAAAHCAGVLSLSDAAALLPALRATEDDIRRTVKELTFHPPRIPLVSGRTGRPLTPGELRSPEHWIALARETGTPAEGLRWLLADGVHHCLLPVPVDTAGIPGDLAEDGLLLLPDPSRDGTGATALLRALARLYVRGVAVGWDRMLADCGARLVELPTYAFQRGRYWPELAALPAAGPRPAGRADGQGGREFQERLAGASEEEREALLAALVRTHAAAALRLPDADAIDERTPLPELGFDSLTAVDLRNRLGADTGLRLAPSLVFQHPTVTALARHLLAAWTAAGGADRAAEDTTGAGTTLGPLLARAGELGRSEEFQELMHRMAAFRPAFDTPRAEHRIPPVRLSRGPAAPGLVCFPTFAGSSGPQQYARLAAAARGERDLWVLPAPGFSWDQPLPASVDALARLQADGVQECAEGQPVVLLGYSAGGWIAHATAAALEARGAGPSGVVLLDTYWPDSAMLPRLHARIDQDRKSGSSEAHWTEEIRDDAGLTAMAHYSRLFQTWRPAPITAPTLLVRAAEPAVAEPPRDWRPHWRLPHTAVDAPGTHFTLIREHGPAALGSVHHWLNGLQKKEH

[Multiple Choices]
A. 2.3.1.319
B. 2.5.1.56
C. 2.7.1.39
D. 2.3.1.290
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The sequence-matched historical UniProt record assigns EC 2.3.1.290 and annotates the associated catalytic reaction with that EC number. This supports D as a curated annotation; the excerpts cite a publication but do not independently establish the extent of experimental validation.

Citations as saved: [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's modular polyketide-synthase architecture can meaningfully favor the 2.3.1 options over the kinase and prenyltransferase options. But A and D share that broad EC class, and generic modular-PKS features do not establish the particular product or reaction that distinguishes their complete EC numbers.


**Missing item-specific fact**

> A product- or pathway-specific functional assignment, or an established connection to a sufficiently close characterized homolog, is needed to distinguish the specialized EC alternatives.


**Reason**

> Transferable knowledge identifies a broad enzyme type, but the offered choices include two alternatives within that type. The sequence alone supplies no clear product-specific or pathway-context feature to resolve their different EC numbers.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports one specific EC assignment, and no competing option is independently supported as the correct assignment. The limitation is that the original input does not meaningfully resolve the close alternatives, not that multiple answers are established.


### Important caveats

- The reviewer-only sequence-matched historical annotation supports the key but was not part of the original model input.
- The cited evidence is a curated database annotation; these excerpts alone do not demonstrate direct experimental verification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's modular polyketide-synthase architecture can meaningfully favor the 2.3.1 options over the kinase and prenyltransferase options. But A and D share that broad EC class, and generic modular-PKS features do not establish the particular product or reaction that distinguishes their complete EC numbers.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A product- or pathway-specific functional assignment, or an established connection to a sufficiently close characterized homolog, is needed to distinguish the specialized EC alternatives.",
    "reason": "Transferable knowledge identifies a broad enzyme type, but the offered choices include two alternatives within that type. The sequence alone supplies no clear product-specific or pathway-context feature to resolve their different EC numbers."
  },
  "case_id": "EC_number_0151",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record assigns EC 2.3.1.290 and annotates the associated catalytic reaction with that EC number. This supports D as a curated annotation; the excerpts cite a publication but do not independently establish the extent of experimental validation."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched historical annotation supports the key but was not part of the original model input.",
    "The cited evidence is a curated database annotation; these excerpts alone do not demonstrate direct experimental verification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one specific EC assignment, and no competing option is independently supported as the correct assignment. The limitation is that the original input does not meaningfully resolve the close alternatives, not that multiple answers are established."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0151",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record assigns EC 2.3.1.290 and annotates the associated catalytic reaction with that EC number. This supports D as a curated annotation; the excerpts cite a publication but do not independently establish the extent of experimental validation.",
    "evidence_ids": ["H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's modular polyketide-synthase architecture can meaningfully favor the 2.3.1 options over the kinase and prenyltransferase options. But A and D share that broad EC class, and generic modular-PKS features do not establish the particular product or reaction that distinguishes their complete EC numbers.",
    "missing_item_specific_fact": "A product- or pathway-specific functional assignment, or an established connection to a sufficiently close characterized homolog, is needed to distinguish the specialized EC alternatives.",
    "reason": "Transferable knowledge identifies a broad enzyme type, but the offered choices include two alternatives within that type. The sequence alone supplies no clear product-specific or pathway-context feature to resolve their different EC numbers."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one specific EC assignment, and no competing option is independently supported as the correct assignment. The limitation is that the original input does not meaningfully resolve the close alternatives, not that multiple answers are established."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched historical annotation supports the key but was not part of the original model input.",
    "The cited evidence is a curated database annotation; these excerpts alone do not demonstrate direct experimental verification."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry B4ER97 (sequence matched, 2266 AA) is annotated with EC 2.3.1.290 (Spectinabilin polyketide synthase system protein NorC). The annotation carries evidence code ECO:0000305 linked to PubMed:17763486 (Traitcheva et al., ChemBioChem 2007), a publication describing the aureothin/neoaureothin PKS pathways. The catalytic reaction (4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H+ → demethyldeoxyspectinabilin + …) is recorded with Rhea cross-references. The evidence code indicates curator inference from the cited publication rather than direct in vitro kinetics on this exact protein, but the annotation is consistently present in both current and historical (entry version 80) records.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The 2266-aa sequence contains multiple recognizable modular PKS domain signatures: an N-terminal KS-like region, several GHSxGE acyltransferase (AT) motifs, and ketoacyl-reductase (KR) domains, all hallmarks of a type-I modular polyketide synthase. This family-level knowledge confidently places the enzyme in EC class 2.3.1 (acyltransferases, specifically PKS-type), which eliminates B (2.5.1.56, a prenyltransferase) and C (2.7.1.39, a kinase) because neither class is consistent with the multi-domain PKS architecture or the very long sequence length. However, the 4th digit of a modular PKS EC number is defined by the specific chemical reaction and product identity (e.g., spectinabilin for 2.3.1.290 vs. whatever product 2.3.1.319 describes). Distinguishing 2.3.1.290 from 2.3.1.319 requires knowing which specific biosynthetic pathway and starter/extender unit combination this particular PKS assembles—information that is a database annotation fact about this exact protein, not derivable from general PKS domain architecture or transferable family-level patterns.


**Missing item-specific fact**

> The specific 4th-digit EC assignment (290 vs 319) depends on knowing the exact substrate/product identity of this particular PKS (spectinabilin demethyldeoxyspectinabilin for 2.3.1.290), which is a pathway-level annotation recorded in databases and is not encoded in a sequence motif that general PKS knowledge can resolve.


**Reason**

> Sequence features (KS, multiple AT with GHSxGE motifs, KR domains, extreme length) are transferable and identify the enzyme as a modular PKS in EC 2.3.1.x, eliminating choices B and C. But the distinction between the two remaining 2.3.1.x options (A: 2.3.1.319 vs D: 2.3.1.290) hinges on the specific 4th digit, which encodes the exact chemical reaction/product of this particular PKS. No general PKS family knowledge or sequence-motif analysis reliably predicts which specific natural-product pathway a given modular PKS belongs to; that is a per-protein database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both A (2.3.1.319) and D (2.3.1.290) fall in the 2.3.1.x acyltransferase/PKS range. From sequence alone a model can identify the protein as a modular PKS but cannot confidently assign the 4th digit without the specific pathway annotation. If 2.3.1.319 is also a modular PKS with similar domain architecture, both options could appear defensible to a model relying only on sequence-derived family recognition.


### Important caveats

- The UniProt annotation uses ECO:0000305 (curator inference from a publication), not direct enzyme assay evidence on this exact protein, though the cited paper describes the pathway biochemically.
- The identity of EC 2.3.1.319 was not independently verified; if it is a non-PKS acyltransferase or an obsolete/withdrawn entry, the A-vs-D ambiguity would be reduced.
- The reviewer-only evidence was not available to the evaluated model; the model had only the raw sequence and four EC-number choices.
- The sequence is 2266 aa, consistent with a multi-module PKS, but the exact module count and domain order were not independently parsed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 2266-aa sequence contains multiple recognizable modular PKS domain signatures: an N-terminal KS-like region, several GHSxGE acyltransferase (AT) motifs, and ketoacyl-reductase (KR) domains, all hallmarks of a type-I modular polyketide synthase. This family-level knowledge confidently places the enzyme in EC class 2.3.1 (acyltransferases, specifically PKS-type), which eliminates B (2.5.1.56, a prenyltransferase) and C (2.7.1.39, a kinase) because neither class is consistent with the multi-domain PKS architecture or the very long sequence length. However, the 4th digit of a modular PKS EC number is defined by the specific chemical reaction and product identity (e.g., spectinabilin for 2.3.1.290 vs. whatever product 2.3.1.319 describes). Distinguishing 2.3.1.290 from 2.3.1.319 requires knowing which specific biosynthetic pathway and starter/extender unit combination this particular PKS assembles—information that is a database annotation fact about this exact protein, not derivable from general PKS domain architecture or transferable family-level patterns.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific 4th-digit EC assignment (290 vs 319) depends on knowing the exact substrate/product identity of this particular PKS (spectinabilin demethyldeoxyspectinabilin for 2.3.1.290), which is a pathway-level annotation recorded in databases and is not encoded in a sequence motif that general PKS knowledge can resolve.",
    "reason": "Sequence features (KS, multiple AT with GHSxGE motifs, KR domains, extreme length) are transferable and identify the enzyme as a modular PKS in EC 2.3.1.x, eliminating choices B and C. But the distinction between the two remaining 2.3.1.x options (A: 2.3.1.319 vs D: 2.3.1.290) hinges on the specific 4th digit, which encodes the exact chemical reaction/product of this particular PKS. No general PKS family knowledge or sequence-motif analysis reliably predicts which specific natural-product pathway a given modular PKS belongs to; that is a per-protein database annotation."
  },
  "case_id": "EC_number_0151",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry B4ER97 (sequence matched, 2266 AA) is annotated with EC 2.3.1.290 (Spectinabilin polyketide synthase system protein NorC). The annotation carries evidence code ECO:0000305 linked to PubMed:17763486 (Traitcheva et al., ChemBioChem 2007), a publication describing the aureothin/neoaureothin PKS pathways. The catalytic reaction (4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H+ → demethyldeoxyspectinabilin + …) is recorded with Rhea cross-references. The evidence code indicates curator inference from the cited publication rather than direct in vitro kinetics on this exact protein, but the annotation is consistently present in both current and historical (entry version 80) records."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000305 (curator inference from a publication), not direct enzyme assay evidence on this exact protein, though the cited paper describes the pathway biochemically.",
    "The identity of EC 2.3.1.319 was not independently verified; if it is a non-PKS acyltransferase or an obsolete/withdrawn entry, the A-vs-D ambiguity would be reduced.",
    "The reviewer-only evidence was not available to the evaluated model; the model had only the raw sequence and four EC-number choices.",
    "The sequence is 2266 aa, consistent with a multi-module PKS, but the exact module count and domain order were not independently parsed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both A (2.3.1.319) and D (2.3.1.290) fall in the 2.3.1.x acyltransferase/PKS range. From sequence alone a model can identify the protein as a modular PKS but cannot confidently assign the 4th digit without the specific pathway annotation. If 2.3.1.319 is also a modular PKS with similar domain architecture, both options could appear defensible to a model relying only on sequence-derived family recognition."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0151",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry B4ER97 (sequence matched, 2266 AA) is annotated with EC 2.3.1.290 (Spectinabilin polyketide synthase system protein NorC). The annotation carries evidence code ECO:0000305 linked to PubMed:17763486 (Traitcheva et al., ChemBioChem 2007), a publication describing the aureothin/neoaureothin PKS pathways. The catalytic reaction (4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H+ → demethyldeoxyspectinabilin + …) is recorded with Rhea cross-references. The evidence code indicates curator inference from the cited publication rather than direct in vitro kinetics on this exact protein, but the annotation is consistently present in both current and historical (entry version 80) records.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The 2266-aa sequence contains multiple recognizable modular PKS domain signatures: an N-terminal KS-like region, several GHSxGE acyltransferase (AT) motifs, and ketoacyl-reductase (KR) domains, all hallmarks of a type-I modular polyketide synthase. This family-level knowledge confidently places the enzyme in EC class 2.3.1 (acyltransferases, specifically PKS-type), which eliminates B (2.5.1.56, a prenyltransferase) and C (2.7.1.39, a kinase) because neither class is consistent with the multi-domain PKS architecture or the very long sequence length. However, the 4th digit of a modular PKS EC number is defined by the specific chemical reaction and product identity (e.g., spectinabilin for 2.3.1.290 vs. whatever product 2.3.1.319 describes). Distinguishing 2.3.1.290 from 2.3.1.319 requires knowing which specific biosynthetic pathway and starter/extender unit combination this particular PKS assembles—information that is a database annotation fact about this exact protein, not derivable from general PKS domain architecture or transferable family-level patterns.",
    "missing_item_specific_fact": "The specific 4th-digit EC assignment (290 vs 319) depends on knowing the exact substrate/product identity of this particular PKS (spectinabilin demethyldeoxyspectinabilin for 2.3.1.290), which is a pathway-level annotation recorded in databases and is not encoded in a sequence motif that general PKS knowledge can resolve.",
    "reason": "Sequence features (KS, multiple AT with GHSxGE motifs, KR domains, extreme length) are transferable and identify the enzyme as a modular PKS in EC 2.3.1.x, eliminating choices B and C. But the distinction between the two remaining 2.3.1.x options (A: 2.3.1.319 vs D: 2.3.1.290) hinges on the specific 4th digit, which encodes the exact chemical reaction/product of this particular PKS. No general PKS family knowledge or sequence-motif analysis reliably predicts which specific natural-product pathway a given modular PKS belongs to; that is a per-protein database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both A (2.3.1.319) and D (2.3.1.290) fall in the 2.3.1.x acyltransferase/PKS range. From sequence alone a model can identify the protein as a modular PKS but cannot confidently assign the 4th digit without the specific pathway annotation. If 2.3.1.319 is also a modular PKS with similar domain architecture, both options could appear defensible to a model relying only on sequence-derived family recognition."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000305 (curator inference from a publication), not direct enzyme assay evidence on this exact protein, though the cited paper describes the pathway biochemically.",
    "The identity of EC 2.3.1.319 was not independently verified; if it is a non-PKS acyltransferase or an obsolete/withdrawn entry, the A-vs-D ambiguity would be reduced.",
    "The reviewer-only evidence was not available to the evaluated model; the model had only the raw sequence and four EC-number choices.",
    "The sequence is 2266 aa, consistent with a multi-module PKS, but the exact module count and domain order were not independently parsed here."
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17763486\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:58945\"}}],\"reaction\":{\"ecNumber\":\"2.3.1.290\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"17763486\",\"source\":\"PubMed\"}],\"name\":\"4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:58944\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57327\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57384\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142871\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142872\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
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
  "excerpt": "DE   RecName: Full=Spectinabilin polyketide synthase system protein NorC {ECO:0000305};\nDE            Short=Spectinabilin PKS system protein NorC {ECO:0000305};\nDE            EC=2.3.1.290 {ECO:0000305|PubMed:17763486};\nDE   AltName: Full=Modular polyketide synthase NorC {ECO:0000312|EMBL:CAO85898.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:21.445291+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80)

```json
{
  "entry_version": 80,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6\nCC         NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8\nCC         CoA + 5 H2O; Xref=Rhea:RHEA:58944, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:57287,\nCC         ChEBI:CHEBI:57327, ChEBI:CHEBI:57384, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:142871, ChEBI:CHEBI:142872;\nCC         EC=2.3.1.290; Evidence={ECO:0000305|PubMed:17763486};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:58945;\nCC         Evidence={ECO:0000305|PubMed:17763486};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:21.445291+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1e533da9fc504b0cc63c0368cc8cf6400afe7a53bd4a209da3d822458140ecef",
  "url": "https://rest.uniprot.org/unisave/B4ER97?format=txt&versions=80"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 151. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
