# LiveProteinBench: evaluation deep dive

We reviewed the questions in our evaluation set to understand whether the benchmark can be scored reliably. We also compared model answers to identify skills that could guide protein training data.

## Are the questions reliable?

GPT-6 Luna and Qwen3.8 Flash-Next (NVFP4) reviewed the questions.

- Both reviewers flagged questions with **multiple defensible answers (4.95%)**, questions requiring **protein-specific lookup or recall (3.00%)**, and **answer keys contradicted by the evidence (0.69%)**. These categories overlap.

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
<summary>Example: interpreting an EC number</summary>

**Skill:** Connect an EC number to the specific enzyme activity it describes.

**Original task description:** The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence..

**Protein sequence:**

```text
MMESAVTAHTLRIAMAQFDFPVGAVTQNTDRIIEYIAAARDEFEADIVLFPELAISGYPPEDLLLRPGFLAHCEQALARIAAATRGIVAVVGWPQSAGSVVYNAASVLREGRIEATYRKRELPNYAVFDERRYFDVDPDGDNCVVTVKGVQVGVVICEDLWFAEPLAKTVQAGAELVLVPNASPYERGKHAQRDALLAERTRESGAAIAYLNVVGGQDALVFDGASVVADGDGTVHPAAAAFVDQWLVVDYAAGERSFTPVVWVDDGDESMDALAWRAVVRGLKDYCGKNGFRKVWLGLSGGIDSALVLAMAVDALGGENVTAVRLPSRYTAGLSNDLADEQCRALGVKLETIAIEPAFEGLLAALGPLFADTQPDITEENLQSRSRGVILMALSNKFGGLVLTTGNKSEYAVGYATIYGDMCGGYAPLKDLYKTEVFGLAKWRNTVGGAPVIPPAVISRPPSAELRDNQTDQDSLPPYDVLDGILYRYVDQEQSRDDIVAAGYAADTVEHVLRLVRLNEWKRHQAAPGPKVSRRAFGRERRYPITNGYSGQ
```

**Original choices:**

```text
A. 5.6.2.4
B. 2.3.1.193
C. 6.3.5.1
D. 1.14.19.80
```

**Author’s answer:** C, EC 6.3.5.1.

**What happened:** The teacher identified EC 6.3.5.1 as NAD synthase, which helps make NAD⁺ for cell metabolism. Our trained model called it DNA ligase, which joins DNA, rejected the choice, and selected D.

<details>
<summary>Full saved answers from both models</summary>

**Our trained model’s full saved answer:**

<pre>## Analysis of the Protein Sequence for EC Number Prediction

### Step 1: Analyze Protein Sequence Characteristics

**Length:** ~450 amino acids
**Key structural motifs identified:**
- **N-terminal Rossmann-like fold**: `GWPQSAGS` (GxGxxG-type nucleotide/cofactor binding motif) — characteristic of NAD(P)-dependent oxidoreductases
- **&quot;GDS&quot; motif** (~position 380): associated with catalytic sites in certain oxidoreductase families
- **&quot;GKNFG&quot;**: possible metal-binding or catalytic residue environment
- **Overall topology**: Two-domain architecture (N-terminal cofactor-binding + C-terminal catalytic domain)

### Step 2: Evaluate Each Option

| Option | EC Number | Enzyme Class | Compatibility? |
|--------|-----------|-------------|----------------|
| A | 5.6.2.4 | Transferase (hydroxyalkyl) | ❌ No transferase motifs (no conserved catalytic triad or reactive center typical of transferases) |
| B | 2.3.1.193 | Acyl transferase | ❌ No acyl-CoA/acyl-group processing motifs (no HxHC, no thioesterase active site) |
| C | 6.3.5.1 | DNA Ligase (ATP-dependent) | ❌ Lacks ADP/ATP-binding domain (e.g., VAIK motif), lacks KxDxG motif essential for adenylate linkage |
| D | 1.14.19.80 | Oxidoreductase (ascorbate:Fe²⁺ oxidoreductase) | ✅ Strong match |

### Step 3: Reasoning

The Rossmann-like fold at the N-terminus (`GWPQSAGS`) is the hallmark of NAD(P)-dependent oxidoreductases. Among the four options, **only EC 1.14.19.80** belongs to the oxidoreductase family (EC 1.x.x.x). 

- Options A (5.6.2.4) and B (2.3.1.193) are transferases — the sequence lacks any conserved transferase catalytic motifs (e.g., conserved acidic residues, thiol/tryptophan catalytic sites).
- Option C (6.3.5.1) is a DNA ligase — DNA ligases are characterized by distinct NTP-binding motifs (VAIK, KxDG), which are completely absent here.
- Option D (1.14.19.80) describes an oxido-reductase using ascorbate as electron acceptor — the Rossmann fold + C-terminal catalytic domain architecture is fully consistent with this assignment.

### Step 4: Final Answer

The protein&#x27;s domain architecture (Rossmann fold + catalytic domain) and absence of non-oxidoreductase features strongly support classification as an ascorbate:iron(II) oxidoreductase.

**answer: D**</pre>

**Teacher’s full saved answer:**

<pre>1. reasoning: The sequence is a soluble, roughly 500-residue enzyme with a likely multidomain architecture consistent with an ATP-dependent, glutamine-utilizing ligase. That fits EC 6.3.5.1, glutamine-dependent NAD⁺ synthetase. The sequence lacks the membrane-spanning hydrophobic regions expected for option D, and the other options describe different reaction classes.
2. answer: C</pre>

</details>

</details>

### Using the skills

We start with synthetic protein questions, answers, and reasoning generated by Qwen Flash-Next, and generate new questions targeted to the identified skills. We compare teacher and Qwen 4B answers and select questions where the teacher consistently chooses a supported answer and Qwen 4B is wrong. GPT-Luna reviews the selected questions and answers.

## Open question: How can we improve a student when both the student and teacher are wrong?

As AI-for-science problems move closer to the research frontier, the correct answer may not yet be known—even to experts—and verifying it may require expensive experiments or simulations. Comparing a wrong teacher answer with a wrong student answer can reveal differences, but it does not tell us which difference is useful to learn from.

