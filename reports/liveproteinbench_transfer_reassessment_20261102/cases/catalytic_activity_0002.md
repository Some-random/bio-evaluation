# catalytic_activity_0002

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0002.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — 4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTSGRGVSQMVTDDKLRYFLKKVTADLHETRGRLRELEEAAGEPIAVVAMGCRFPGGVRSPEDLWHLVASGRDAITPFPADRGWETAGLYDPDPDRPGKSCAREGGFLDDVASFDAGLFGVSPREALALDPQQRLLLEVTWETFERAGLTPAALRGTRTGVFVGTSSQEYAMLVHNARENFEGYSTGYLASVISGRLAYNFGLQGPAVTVDTACSSSLVALHQAAQALRAGDCTLALAGGVAVLATPSMFVEFSRQRGLAPDGRCKAFAAAADGTGWGEGVGLLLLERLSEARREGHPVLAVVRGSAVNQDGASNGLTAPNGPAQQRVIRRALAACRAVGGPGGRGGGPWHRDPAGRSHRGPGAAGHLRPRASRPTSFVARVVEVQYRPHPGRRRRRRCDQDGDGPAPRRTAAHPAYRRPHSTGGLVGGHRAAAHRGEGVAGDRPTPPGRRVLLRHQRHQRPCGAGTSRAGRLPRPRRTAGTAPGGDTAAALGALRPHRARPAGTGRPAARPYPRPPAPLPADTAHSLLVSRTLFGHRAVVLGDDRDELLTGLDALAGGGNAPGVLTGVAGEPRKPVLVFPGQGAQWEGMAAELYRESAVFRDRLRQCAEALAPHTGFSLVDVVCGAEGAAALDRVDVVQPALWAMLVSLAALWRSHGVEPGAVVGHSQGEIAAACVAGALSLEDGARIVALRSRLIAERLSGRGGMAFLGLPAGRAREWLAAWETRLGVAAVNGPSSVVVSGDAEALDGMLAAAEEEGVRAIRVAVDYASHSAQVATLEDELLAALPGITPRTAEIPFFSTVNGALIDTSALDPAYWYRNLRQTVRFESTVRRLLEAGHRGFVEVSPHPVLAVSVQEILDATATEGVVLASLRRGEGGLRRFLTSVGEAHVHGIPADFALPPGRLVDLPTLAFERRRYWLDAQPAAPAHQAEGSAGESAGESAGESAEESEAALFRQRLAGLPESERERAVLHTVCEQAAVVLNLTSAADLDTGKAFTDLGFVSMTAMELRNRLATATGIRLTPTAAFDHPTPEKLAAHLLSRLTGTAEPIAQPVAAPPAAGEPIAIVAMGCRYPGEVASPEELWELLAAGRDATSSFPANRGWNTDELYDPNPGRPGRTYVRRGGFLHDADQFDPQLFGISPREALAMDPQQRLLLEVAWEVLERARLSPASVRGSRTGVFMGISGQDYLPVLTASPDGGAGHLMTGTSTSVASGRIAYTFGLRGPAVTVDTACSSSLVALHLAIQALRQGDCSAALVGGATVLSTPGAFVEFSQQRALAPDGRCKAFAAGADGTGWGEGAGMLLVEPLSEARRQGHPVLALIRGSATNQDGASNGLSAPNGQAQQQVIRQALANSGLTTRDVDAVEAHGTGTALGDPIEAEALLATYGQDRPAQRPLWLGSLKSNIGHTAAAAGVGGVIKMVLALRRGVLPPTLHAADPTPHVDWSAGAVELLTEAREWPETGRPRRAGVSAFGISGTNAHVVLEQAPDPDPAPGSGLPHPAATLPAVPWPLSGRTAAALRAQAGRLHRFVLAHPGLAPADIGRSLAAGRAGLEHRAVVLGRDRDQLLAELATLAEGEGDDAGAAVRGTVRARSRMACLFTAGPGARSGPGRELYARMPVYAAAVDEAGAAFQALPARPLGETMALDEAPADPVLAQVLHFAEQVALFRLLDHWGTAPSHLLGHGPGEAAAAHCAGVLSLSDAAALLPALRATEDDIRRTVKELTFHPPRIPLVSGRTGRPLTPGELRSPEHWIALARETGTPAEGLRWLLADGVHHCLLPVPVDTAGIPGDLAEDGLLLLPDPSRDGTGATALLRALARLYVRGVAVGWDRMLADCGARLVELPTYAFQRGRYWPELAALPAAGPRPAGRADGQGGREFQERLAGASEEEREALLAALVRTHAAAALRLPDADAIDERTPLPELGFDSLTAVDLRNRLGADTGLRLAPSLVFQHPTVTALARHLLAAWTAAGGADRAAEDTTGAGTTLGPLLARAGELGRSEEFQELMHRMAAFRPAFDTPRAEHRIPPVRLSRGPAAPGLVCFPTFAGSSGPQQYARLAAAARGERDLWVLPAPGFSWDQPLPASVDALARLQADGVQECAEGQPVVLLGYSAGGWIAHATAAALEARGAGPSGVVLLDTYWPDSAMLPRLHARIDQDRKSGSSEAHWTEEIRDDAGLTAMAHYSRLFQTWRPAPITAPTLLVRAAEPAVAEPPRDWRPHWRLPHTAVDAPGTHFTLIREHGPAALGSVHHWLNGLQKKEH

[Multiple Choices]
A. restrictinol + glycine + H(+) = restricticin + H2O
B. Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.
C. (S,S)-drim-8-en-11-yl diphosphate + D-mannitol = sporulositol A + diphosphate
D. 4-nitrobenzoyl-CoA + 6 (S)-methylmalonyl-CoA + malonyl-CoA + 6 NADPH + 12 H(+) = demethyldeoxyspectinabilin + 7 CO2 + 6 NADP(+) + 8 CoA + 5 H2O
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

> The exact sequence matches the UniProt entry whose catalytic-activity annotation gives the reaction in D, with a literature evidence citation. This supports the key, though the supplied excerpts do not independently establish that the reaction was directly measured for this protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The very long sequence contains repeated, domain-rich regions characteristic of a modular polyketide synthase. D is the option describing assembly of a polyketide from acyl-CoA building blocks with NADPH, which fits that enzyme class. The other choices describe a small-molecule peptide reaction, xylan hydrolysis, or terpene formation and do not fit this architecture as well.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable recognition of modular polyketide synthase architecture meaningfully distinguishes D among the offered reactions. It supports the reaction class rather than independently proving every substrate and stoichiometric detail.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence architecture and the distinct reaction classes offered favor D; no other option is comparably defensible.


### Important caveats

- The supporting database annotation cites literature, but the excerpts do not provide the underlying experimental details.
- The reviewer evidence confirms an exact sequence match; its target-specific annotation is not needed for the transferable inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The very long sequence contains repeated, domain-rich regions characteristic of a modular polyketide synthase. D is the option describing assembly of a polyketide from acyl-CoA building blocks with NADPH, which fits that enzyme class. The other choices describe a small-molecule peptide reaction, xylan hydrolysis, or terpene formation and do not fit this architecture as well.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of modular polyketide synthase architecture meaningfully distinguishes D among the offered reactions. It supports the reaction class rather than independently proving every substrate and stoichiometric detail."
  },
  "case_id": "catalytic_activity_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry whose catalytic-activity annotation gives the reaction in D, with a literature evidence citation. This supports the key, though the supplied excerpts do not independently establish that the reaction was directly measured for this protein."
  },
  "important_caveats": [
    "The supporting database annotation cites literature, but the excerpts do not provide the underlying experimental details.",
    "The reviewer evidence confirms an exact sequence match; its target-specific annotation is not needed for the transferable inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence architecture and the distinct reaction classes offered favor D; no other option is comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry whose catalytic-activity annotation gives the reaction in D, with a literature evidence citation. This supports the key, though the supplied excerpts do not independently establish that the reaction was directly measured for this protein.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The very long sequence contains repeated, domain-rich regions characteristic of a modular polyketide synthase. D is the option describing assembly of a polyketide from acyl-CoA building blocks with NADPH, which fits that enzyme class. The other choices describe a small-molecule peptide reaction, xylan hydrolysis, or terpene formation and do not fit this architecture as well.",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of modular polyketide synthase architecture meaningfully distinguishes D among the offered reactions. It supports the reaction class rather than independently proving every substrate and stoichiometric detail."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence architecture and the distinct reaction classes offered favor D; no other option is comparably defensible."
  },
  "important_caveats": [
    "The supporting database annotation cites literature, but the excerpts do not provide the underlying experimental details.",
    "The reviewer evidence confirms an exact sequence match; its target-specific annotation is not needed for the transferable inference."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProtKB entry B4ER97 (sequence sha256 matched, 2266 AA) annotates this protein as Spectinabilin polyketide synthase system protein NorC (EC 2.3.1.290) with the exact catalytic activity reaction listed in Choice D. The evidence code ECO:0000305 with PubMed:17763486 (Traitcheva et al. 2007, ChemBioChem) supports this annotation. Both the current entry (C5) and the archived Swiss-Prot record (H4) confirm the identical reaction string.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 2266-residue protein displays the hallmark domain architecture of a modular type I polyketide synthase: multiple KS domain signatures (the 'MGCRFPGGVRSPEDLWHL' and 'MGCRYPGEVASPEELWEL' motifs with the conserved Cys-His-His catalytic triad), AT domains (the 'GGFLDDVASFDAGLFGVSPREALALDPQQRLLLE' pattern), a KR domain (the 'GGMAFLGLPAGRAREWLAAWETRLG' region with the NADPH-binding Rossmann fold), ACP regions, and a C-terminal TE domain ('GHHWLNGLQKKEH'). This architecture is diagnostic of modular PKS enzymes and is clearly distinguishable from NRPS (which would show adenylation and condensation domain motifs), glycoside hydrolases (small, single-domain, with conserved GH catalytic residues), and terpene synthases/glycosyltransferases (short, with conserved DDxxD motifs). Among the four choices, only D is a polyketide synthase reaction (malonyl-CoA/methylmalonyl-CoA chain elongation with NADPH-dependent reductions). Choices A (NRPS amide-bond formation), B (xylanase endohydrolysis), and C (terpene diphosphate + sugar condensation) represent entirely different enzyme classes whose domain architectures are absent from this sequence. Recognizing the PKS family and selecting the only PKS reaction among the options is a transferable inference from general PKS biochemistry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model trained on protein family knowledge can identify the modular PKS domain architecture from sequence motifs and eliminate the three non-PKS options. The exact product name 'demethyldeoxyspectinabilin' and precise stoichiometry are not required for discrimination because D is the sole PKS reaction among the choices; the enzyme-class identification suffices to select it uniquely.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent four distinct enzyme classes (NRPS, glycoside hydrolase, terpene/glycosyltransferase, PKS). The sequence unambiguously shows modular PKS architecture, so only one option is consistent.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (inferred by curator) citing PubMed:17763486, meaning the reaction assignment is curator-inferred from pathway literature rather than from a single purified-enzyme kinetics experiment on this exact protein.
- The model does not need to know the exact product name 'demethyldeoxyspectinabilin'; it only needs to recognize the enzyme as a modular PKS and select the only PKS reaction among the alternatives.
- The reviewer-only UniProt accession and organism identity were not provided to the evaluated model; the reasoning above relies solely on sequence motifs and general PKS knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 2266-residue protein displays the hallmark domain architecture of a modular type I polyketide synthase: multiple KS domain signatures (the 'MGCRFPGGVRSPEDLWHL' and 'MGCRYPGEVASPEELWEL' motifs with the conserved Cys-His-His catalytic triad), AT domains (the 'GGFLDDVASFDAGLFGVSPREALALDPQQRLLLE' pattern), a KR domain (the 'GGMAFLGLPAGRAREWLAAWETRLG' region with the NADPH-binding Rossmann fold), ACP regions, and a C-terminal TE domain ('GHHWLNGLQKKEH'). This architecture is diagnostic of modular PKS enzymes and is clearly distinguishable from NRPS (which would show adenylation and condensation domain motifs), glycoside hydrolases (small, single-domain, with conserved GH catalytic residues), and terpene synthases/glycosyltransferases (short, with conserved DDxxD motifs). Among the four choices, only D is a polyketide synthase reaction (malonyl-CoA/methylmalonyl-CoA chain elongation with NADPH-dependent reductions). Choices A (NRPS amide-bond formation), B (xylanase endohydrolysis), and C (terpene diphosphate + sugar condensation) represent entirely different enzyme classes whose domain architectures are absent from this sequence. Recognizing the PKS family and selecting the only PKS reaction among the options is a transferable inference from general PKS biochemistry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model trained on protein family knowledge can identify the modular PKS domain architecture from sequence motifs and eliminate the three non-PKS options. The exact product name 'demethyldeoxyspectinabilin' and precise stoichiometry are not required for discrimination because D is the sole PKS reaction among the choices; the enzyme-class identification suffices to select it uniquely."
  },
  "case_id": "catalytic_activity_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProtKB entry B4ER97 (sequence sha256 matched, 2266 AA) annotates this protein as Spectinabilin polyketide synthase system protein NorC (EC 2.3.1.290) with the exact catalytic activity reaction listed in Choice D. The evidence code ECO:0000305 with PubMed:17763486 (Traitcheva et al. 2007, ChemBioChem) supports this annotation. Both the current entry (C5) and the archived Swiss-Prot record (H4) confirm the identical reaction string."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by curator) citing PubMed:17763486, meaning the reaction assignment is curator-inferred from pathway literature rather than from a single purified-enzyme kinetics experiment on this exact protein.",
    "The model does not need to know the exact product name 'demethyldeoxyspectinabilin'; it only needs to recognize the enzyme as a modular PKS and select the only PKS reaction among the alternatives.",
    "The reviewer-only UniProt accession and organism identity were not provided to the evaluated model; the reasoning above relies solely on sequence motifs and general PKS knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four distinct enzyme classes (NRPS, glycoside hydrolase, terpene/glycosyltransferase, PKS). The sequence unambiguously shows modular PKS architecture, so only one option is consistent."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProtKB entry B4ER97 (sequence sha256 matched, 2266 AA) annotates this protein as Spectinabilin polyketide synthase system protein NorC (EC 2.3.1.290) with the exact catalytic activity reaction listed in Choice D. The evidence code ECO:0000305 with PubMed:17763486 (Traitcheva et al. 2007, ChemBioChem) supports this annotation. Both the current entry (C5) and the archived Swiss-Prot record (H4) confirm the identical reaction string.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 2266-residue protein displays the hallmark domain architecture of a modular type I polyketide synthase: multiple KS domain signatures (the 'MGCRFPGGVRSPEDLWHL' and 'MGCRYPGEVASPEELWEL' motifs with the conserved Cys-His-His catalytic triad), AT domains (the 'GGFLDDVASFDAGLFGVSPREALALDPQQRLLLE' pattern), a KR domain (the 'GGMAFLGLPAGRAREWLAAWETRLG' region with the NADPH-binding Rossmann fold), ACP regions, and a C-terminal TE domain ('GHHWLNGLQKKEH'). This architecture is diagnostic of modular PKS enzymes and is clearly distinguishable from NRPS (which would show adenylation and condensation domain motifs), glycoside hydrolases (small, single-domain, with conserved GH catalytic residues), and terpene synthases/glycosyltransferases (short, with conserved DDxxD motifs). Among the four choices, only D is a polyketide synthase reaction (malonyl-CoA/methylmalonyl-CoA chain elongation with NADPH-dependent reductions). Choices A (NRPS amide-bond formation), B (xylanase endohydrolysis), and C (terpene diphosphate + sugar condensation) represent entirely different enzyme classes whose domain architectures are absent from this sequence. Recognizing the PKS family and selecting the only PKS reaction among the options is a transferable inference from general PKS biochemistry.",
    "missing_item_specific_fact": "",
    "reason": "A model trained on protein family knowledge can identify the modular PKS domain architecture from sequence motifs and eliminate the three non-PKS options. The exact product name 'demethyldeoxyspectinabilin' and precise stoichiometry are not required for discrimination because D is the sole PKS reaction among the choices; the enzyme-class identification suffices to select it uniquely."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four distinct enzyme classes (NRPS, glycoside hydrolase, terpene/glycosyltransferase, PKS). The sequence unambiguously shows modular PKS architecture, so only one option is consistent."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by curator) citing PubMed:17763486, meaning the reaction assignment is curator-inferred from pathway literature rather than from a single purified-enzyme kinetics experiment on this exact protein.",
    "The model does not need to know the exact product name 'demethyldeoxyspectinabilin'; it only needs to recognize the enzyme as a modular PKS and select the only PKS reaction among the alternatives.",
    "The reviewer-only UniProt accession and organism identity were not provided to the evaluated model; the reasoning above relies solely on sequence motifs and general PKS knowledge."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 2. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
