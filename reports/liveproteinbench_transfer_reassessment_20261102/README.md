# LiveProteinBench: evaluation deep dive

We reviewed the questions in our evaluation set to understand whether the benchmark can be scored reliably. We also compared model answers to identify skills that could guide protein training data.

## Are the questions reliable?

GPT-6 Luna and Qwen3.8 Flash-Next (NVFP4) reviewed the questions.

- **Multiple defensible answers — 4.95%.** Both reviewers listed at least two defensible choices.

<details>
<summary>Example: a protein that can both cut and transfer</summary>

**Task:** Choose the protein’s molecular function.

**Original task description:** The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function..

**Protein sequence:**

```text
MRSSTISASAVVLLSGLASAQTFTDCNPTEKTCPSDPAIGGLQVTDFTAGKSSYWEVEDGTTMSYDGTLGAQFVISTATDAPTIKNIGYIMFGRIETWVRASAGTGIVSSFILESDDLDEIDWEWLGANNAEAENNFFGKGNTTTYDRAQYPAVATPIDTFHNYTIDWTAKSTIWYIDGVAVRTLLYDDKQTVGGKNYPQTPMLVKMGSWIGCASKAAETDSATAGTCSWAGGAVDLTQGPFTMYVKNVTIQDYGCATEYTYGDLTGDYTSIKATGGCSADGSAASPSASSSSAASGSSSSTKSSSGSSTLSTVTGTTSAIAVGTATGTATLSAGEKATAAAISGSTTSSSTIAKVTTTSDANSLKKPKHEYGMIDLGVMVLGLGLGYLVM
```

**Choices, explained in simpler language:**

- A. Break down GTP, an energy-carrying molecule *(GTPase activity)*.
- B. Transfer sugar units from one molecule to another *(glycosyltransferase activity)*.
- C. Store nutrients *(nutrient reservoir activity)*.
- D. Cut chemical bonds involving sugars *(hydrolase activity, acting on glycosyl bonds)*.

The explanations before the parentheses are paraphrases; the original choices are in parentheses.

**Author’s answer:** B.

**Why it was flagged:** Both reviewers pointed to an annotation describing a protein that can both **cut chitin**, a sugar-containing material, and **transfer chitin to another molecule**. Both listed B and D as defensible.

</details>

- **Protein-specific lookup or recall — 3.00%.** Both reviewers said answering requires a fact about the particular protein beyond general biological knowledge.

<details>
<summary>Example: distinguishing nearby temperatures</summary>

**Task:** Choose the protein’s optimal temperature.

**Original task description:** The current task is about Protein Thermal Adaptation Prediction, which is to predict the thermal adaptation category of a protein. This relates to the optimal temperature range in which the protein is stable and functional (e.g., cold-adapted, moderate temperature-adapted, or heat-adapted). This property is encoded by subtle patterns in the amino acid sequence that affect the protein's structural stability, such as amino acid composition and the potential for internal bonds. Based on the provided sequence, you must classify the protein into its most likely thermal category..

**Protein sequence:**

```text
MDLLQILLAIAGLLAILLLQKQWRTKTSPGAKAGRKLPPEPAGAWPVIGHLHKLGGPNPIYRNLAEWSDKYGPVMTLKLGMQNAVVVSDREAIKECFTTNDKALADRPPSSIGLHLGFNYAAIGAAPYGPYWRDMRKLVLLEVLSSRRLEMLRNVRISEIGTSIKELYSNIIRSSGGSGPAKVVISHWIEQLTLNYILRTIAGRRFSDDSSKDAQYVKGVINDFMYFAGQFVVSDVIPIPLLRWLDPQGHLKGMKRVAKEVDTMCEAWIQEHVQRRMREKPGPGQEQDFIDVLLNNRDVMRKAQEEIDNHVGKERWVDETDLKHLVYLQAIVKEGLRLYPPGPLGAPHRAIEDCQVGGYFIPKGTQLLVNVWKLHRDPRVWSEPEKFMPERFLTRQAEVDVFGHHFELLPFGSGRRACPGITFAVQVMHLTVARLLQGFDMTTPSNLPVDMTEGPGVTMPKAHPVEVLMMPRLPSALYEP
```

**Choices:**

- A. 24–29°C
- B. 30°C
- C. 56°C
- D. 34°C

**Author’s answer:** B, 30°C.

**Why it was flagged:** The reviewers said sequence and family knowledge might suggest a moderate temperature, but did not distinguish 30°C from 34°C or the nearby range.

</details>

- **Answer key contradicted by evidence — 0.69%.** Both reviewers judged the author’s answer contradicted by the evidence.

<details>
<summary>Example: the answer says steroid breakdown, but the evidence points to sugar breakdown</summary>

**Task description:** Predict the primary biological process in which the protein participates, based on its amino acid sequence.

**Original task description:** The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes..

**Protein sequence:**

```text
MAAVGRYSGKVVVVTGGSRGIGAAIVRAFVDSGAQVVFCDKDEAGGRAVEQELLGTVFIPGDVTQEGDLQTLISETVSRFGHLDCVVNNAGYHPPAQLPEETSAQGFRQLLEENLLGAYTLIKLALPHLRKSKGNIINISSLVGAIGQSQALTYVATKGAVTAMTKALALDESRYGVRVNCISPGNIWTPLWQELAAATSDPRATILEGTLAQPLGRMGQPAEVGAAAVFLASEATFCTGLELFMTGGAELGYGRKASSSTLVEVPILPP
```

**Choices:**

- A. Nuclear pore complex assembly
- B. Response to corticosterone
- C. Negative regulation of axon extension involved in axon guidance
- D. Steroid catabolic process

**Author’s answer:** D, steroid breakdown.

**What the reviewers found:** Both reviewers pointed to evidence that this protein participates in breaking down **L-fucose, a sugar**, rather than evidence supporting steroid breakdown as its primary process. Sugar breakdown is not one of the offered choices.

**Why this matters:** L-fucose is a sugar; steroids are a different class of molecules that includes many hormones. Breaking down a sugar and breaking down a steroid are different biological processes. The evidence identifies this protein with an initial step in L-fucose breakdown, while the benchmark’s answer says steroid breakdown.

</details>

These categories overlap.

## What problems does our trained model run into?

To investigate errors in our trained Qwen 4B model, we compared its answers with a teacher’s answers on questions where the teacher matched the benchmark answer and the student did not. The student answers are from epoch 5 of the original Flash-Next low-reasoning training run. GPT-6.1 Terra compared the saved answers and extracted **1,289 skill descriptions** across protein-problem categories. This comparison was inspired by [DeltaPrompts](https://arxiv.org/html/2605.15532v3).

<details>
<summary>Example: reading what is actually in the protein sequence</summary>

**Skill:** Check that a proposed sequence fragment is actually present before using it to identify the protein.

**Original task description:** The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence..

**Protein sequence:**

```text
MRTCGTSSEGQDECCLYGLSAMQGWRISMEDAHAAVLDLQAKSTGGSEKPTDPDKRLAFFGVYDGHGGDKVALFAGENVHKIVAKQEAFAKGDIEQALKDGFLATDRAILEDPKYEEEVSGCTAAVSVISKNKIWVANAGDSRSVLGVKGRAKPLSFDHKPQNEGEKARISAAGGFVDFGRVNGNLALSRAIGDFEFKKSPELSPEQQIVTAYPDVTVHEVTDDDEFLVIACDGIWDCQSSQSVVEFVRRGIAAKQELYRICENMMDNCLASNSETGGVGCDNMTMIIIGLLNGKTKEEWYNQISERVANGDGPCAPPEYGKSEFRGPGIRNQFEETPDNYDLENDRSRGFSVRSGRIILLGDGTELIPEQNDEELFDQREENRDVTNHLQHDKAEETSTAANLSESPSSANKNSSGSGTEATEKSASS
```

**Original choices:**

```text
A. 3.1.1.4
B. 1.1.1.336
C. 3.1.3.16
D. 2.7.7.43
```

**Author’s answer:** C, EC 3.1.3.16.

**What happened:** Our trained model said the sequence contained `GADAHHAAVL` and used that claim in its protein-family identification. That fragment is not present in the supplied sequence. The teacher cited `DGHGG`, which is present. The trained model chose D; the teacher chose C.

<details>
<summary>Full saved answers from both models</summary>

**Our trained model’s full saved answer:**

<pre>## Analysis of the Protein Sequence

### Step 1: Identifying Key Structural Motifs

Upon examining the ~420 amino acid protein sequence, I identified several distinctive features:

1. **GAddH domain(s)**: The N-terminal region contains &quot;GADAHHAAVL&quot; and the C-terminal region contains &quot;IILLGDGTE&quot; — hallmarks of GAddH (Glycine-aspartic acid-Ash-LeuHis) domain proteins.

2. **Zinc-binding/Cysteine-rich motif**: &quot;CDGIWDCQSSQSVVEF&quot; — the conserved cysteine residues suggest a zinc-binding domain.

3. **Additional GAddH-like region**: &quot;GGVGCDNMTMIIIGLLNGK&quot; near residues 250-280, indicating a second GAddH fold.

### Step 2: Biological Context

The multi-domain architecture (N-terminal GAddH + central CDGIWDC motif + C-terminal GAddH-like) is characteristic of the **GAddH domain superfamily**, which includes:
- Primases
- Nuclease X (Bacillus subtilis, ~500 aa)
- Mismatch repair proteins

Proteins in this superfamily commonly exhibit **transferase/phosphatase** activity on acid anhydride bonds (particularly phosphodiester bonds).

### Step 3: Evaluating Options

| Option | EC | Assessment |
|--------|-----|------------|
| A. 3.1.1.4 | β-lactamase (esterase) | No Ser-His-Arg triad; wrong domain architecture |
| B. 1.1.1.336 | Methyltransferase | No Rossmann-fold or catalytic methyltransferase motifs present |
| C. 3.1.3.16 | DNA mutase | Typically &gt;1000 aa; wrong enzyme class entirely |
| D. 2.7.7.43 | Transferase acting on acid anhydrides | Consistent with GAddH-domain nuclease/phosphatase activity |

### Step 4: Reasoning for Final Answer

The protein&#x27;s domain composition (two GAddH folds flanking a zinc/Cys-rich module), intermediate size (~420 aa), and characteristic loop patterns are highly consistent with a **transferase acting on acid anhydrides** — a GAddH-domain protein that catalyzes reactions involving phosphodiester or analogous anhydride bonds. None of the other options match the structural or functional profile of this protein.

## Final Answer

**D**</pre>

**Teacher’s full saved answer:**

<pre>1. reasoning: The sequence contains a conserved metal-dependent phosphatase-like catalytic region, including the prominent **DGHGG** motif and additional conserved Asp/Gly-rich segments. Its C-terminal low-complexity region is also consistent with a regulatory phosphatase protein. This supports a protein phosphatase function (EC 3.1.3.16), rather than a lipase, oxidoreductase, or nucleotidyltransferase.
2. answer: C</pre>

</details>

</details>

<details>
<summary>Example: distinguishing water-repelling stretches from membrane-spanning regions</summary>

**Skill:** Evaluate whether a protein sequence supports a membrane-spanning region instead of assuming that every water-repelling stretch crosses a membrane.

**Original task description:** The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides..

**Protein sequence:**

```text
MKPLVIFDLDGTLVDTPSGIVSAFITALRDLSMPFEDRRAIRATIGLPLEKAFGQILALPVEDERVTAAVRQYQAVFREQVLPQAPGLVFPGVVEGLALLKGQGYTLAVATSKVFASAKALLEAAGLWSYFDLVLGADMVAHPKPHPEMGLLAMSRLGADAATTAMVGDTTHDLLMAKQAGMAAIGVTWGIHTTDQLKAAEPQVIVDTFSEVVGAAHALLKLSSSPVSYC
```

**Original choices:**

```text
A. cytosol
B. microneme
C. presynaptic active zone
D. virion membrane
```

**Author’s answer:** A, cytosol.

**What happened:** Our trained model interpreted several short water-repelling stretches as membrane-spanning regions and chose B, microneme—a compartment found in certain parasites. The teacher reported no obvious membrane-spanning region and chose A, the cytosol, the fluid inside the cell.

**Why this skill matters:** Short water-repelling stretches can also occur in soluble proteins. Their presence alone does not establish that a protein crosses a membrane or identify a specific cellular compartment.

<details>
<summary>Full saved answers from both models</summary>

**Our trained model’s full saved answer:**

<pre>## Analysis

### Step 1: Sequence Characterization

I examined the ~240 amino acid protein sequence for key features:

- **Hydrophobicity**: The sequence contains multiple hydrophobic stretches (e.g., &quot;IVSAFITALR&quot;, &quot;FGQILALPV&quot;, &quot;GLVFPGVVEGLALL&quot;, &quot;AIGVTWGIHTTD&quot;) indicating **transmembrane domains**.
- **No soluble-cytosolic signature**: There are no dominant water-soluble regions without hydrophobic segments, ruling out a cytosolic location.
- **Targeting signals**: No clear nuclear localization signal (NLS), no mitochondrial targeting presequence, no clear SNARE motif (SxxSxxT consensus), no virus-specific fusion/glycosylation signatures.

### Step 2: Biological Context Assessment

| Option | Expected Features | Match? |
|--------|------------------|--------|
| A. Cytosol | Hydrophilic, no TMs | ❌ Clearly ruled out by multiple TMs |
| B. Microneme | Multi-pass membrane protein; traverses parasitophorous compartment during biogenesis | ✅ Consistent |
| C. Presynaptic active zone | SNARE motifs, syntrophin-like domains | ❌ No SNARE-like motifs detected |
| D. Virion membrane | Viral envelope protein motifs (fusion peptides, glycosylation sites) | ❌ No characteristic viral envelope motifs |

### Step 3: Final Reasoning

The protein displays a **multi-pass α-helical transmembrane architecture** with approximately 3–4 membrane-spanning segments, separated by amphipathic loops. This topology is highly consistent with proteins that traverse multiple internal membranes during trafficking through the apical complex (a hallmark of microneme biogenesis in apicomplexan parasites). There is no evidence supporting any of the other three locations.

### Step 4: Answer Selection

The multi-pass transmembrane topology, combined with the absence of neuronal or viral-specific motifs, points to a **microneme-localized** membrane protein.

2. answer: B</pre>

**Teacher’s full saved answer:**

<pre>1. reasoning: The sequence is a compact, enzyme-like protein with no obvious N-terminal signal peptide, transmembrane segment, or other targeting feature suggesting secretion or membrane insertion. It therefore fits a soluble intracellular protein. Among the choices, the cytosol is the most likely location; the specialized compartments listed would generally require targeting or membrane-associated features not apparent here.
2. answer: A</pre>

</details>

</details>

### Using the skills

We start with synthetic protein questions, answers, and reasoning generated by Qwen Flash-Next, and generate new questions targeted to the identified skills. We compare teacher and Qwen 4B answers and select questions where the teacher consistently chooses a supported answer and Qwen 4B is wrong. GPT-Luna reviews the selected questions and answers.

## Open question: How can we improve a student when both the student and teacher are wrong?

As AI-for-science problems move closer to the research frontier, the correct answer may not yet be known—even to experts—and verifying it may require expensive experiments or simulations. Comparing a wrong teacher answer with a wrong student answer can reveal differences, but it does not tell us which difference is useful to learn from.

