# DeepFRI / ProtST: biological process — complete evaluated input

Verbatim saved user message, including the complete protein sequence and 1,943 fixed GO descriptions. Reference targets and model answer are excluded.

```text
Predict Gene Ontology biological-process annotation for the protein from its complete amino acid sequence.
Return exactly one compact JSON object: {"scores":[p0,p1,...]} containing exactly 1943 numeric confidences in the fixed zero-based class order below. Supply every position, including classes assigned confidence zero. Each number must be between 0 and 1 inclusive, with at most three decimal places. Do not return class IDs as keys, omit any positions, include explanatory prose, or use Markdown. Return the final confidence vector directly.

Complete amino acid sequence:
GSMSSLCLQRLQEERKKWRKDHPFGFYAKPVKKADGSMDLQKWEAGIPGKEGTNWAGGVYPITVEYPNEYPSKPPKVKFPAGFYHPNVYPSGTICLSILNEDQDWRPAITLKQIVLGVQDLLDSPNPNSPAQEPAWRSFSRNKAEYDKKVLLQAKQYSK

Fixed global class order (zero-based position, class ID, description):
0	GO:0006228	UTP biosynthetic process
1	GO:0009135	purine nucleoside diphosphate metabolic process
2	GO:0002699	positive regulation of immune effector process
3	GO:0000463	maturation of LSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA)
4	GO:0009179	purine ribonucleoside diphosphate metabolic process
5	GO:0030183	B cell differentiation
6	GO:0032496	response to lipopolysaccharide
7	GO:0045935	positive regulation of nucleobase-containing compound metabolic process
8	GO:0006304	DNA modification
9	GO:0072528	pyrimidine-containing compound biosynthetic process
10	GO:2000116	regulation of cysteine-type endopeptidase activity
11	GO:0000413	protein peptidyl-prolyl isomerization
12	GO:0009966	regulation of signal transduction
13	GO:0031099	regeneration
14	GO:2000027	regulation of animal organ morphogenesis
15	GO:0006575	cellular modified amino acid metabolic process
16	GO:0043491	protein kinase B signaling
17	GO:0051726	regulation of cell cycle
18	GO:1901615	organic hydroxy compound metabolic process
19	GO:0030593	neutrophil chemotaxis
20	GO:0043242	negative regulation of protein-containing complex disassembly
21	GO:0048513	animal organ development
22	GO:0022898	regulation of transmembrane transporter activity
23	GO:0006979	response to oxidative stress
24	GO:0002833	positive regulation of response to biotic stimulus
25	GO:0017148	negative regulation of translation
26	GO:1902105	regulation of leukocyte differentiation
27	GO:0030336	negative regulation of cell migration
28	GO:0051236	establishment of RNA localization
29	GO:0048017	inositol lipid-mediated signaling
30	GO:0051674	localization of cell
31	GO:0006816	calcium ion transport
32	GO:0000162	tryptophan biosynthetic process
33	GO:0071702	organic substance transport
34	GO:0051173	positive regulation of nitrogen compound metabolic process
35	GO:0046907	intracellular transport
36	GO:0070585	protein localization to mitochondrion
37	GO:0050778	positive regulation of immune response
38	GO:0006163	purine nucleotide metabolic process
39	GO:0006450	regulation of translational fidelity
40	GO:0051321	meiotic cell cycle
41	GO:0001819	positive regulation of cytokine production
42	GO:0009235	cobalamin metabolic process
43	GO:0006650	glycerophospholipid metabolic process
44	GO:0048522	positive regulation of cellular process
45	GO:0030001	metal ion transport
46	GO:0008033	tRNA processing
47	GO:0006355	regulation of transcription, DNA-templated
48	GO:0046940	nucleoside monophosphate phosphorylation
49	GO:0002694	regulation of leukocyte activation
50	GO:0031326	regulation of cellular biosynthetic process
51	GO:0009142	nucleoside triphosphate biosynthetic process
52	GO:0050829	defense response to Gram-negative bacterium
53	GO:0009211	pyrimidine deoxyribonucleoside triphosphate metabolic process
54	GO:0043112	receptor metabolic process
55	GO:0009893	positive regulation of metabolic process
56	GO:0010951	negative regulation of endopeptidase activity
57	GO:0006508	proteolysis
58	GO:0043299	leukocyte degranulation
59	GO:0044282	small molecule catabolic process
60	GO:0008360	regulation of cell shape
61	GO:0043933	protein-containing complex subunit organization
62	GO:0007229	integrin-mediated signaling pathway
63	GO:0051271	negative regulation of cellular component movement
64	GO:0042119	neutrophil activation
65	GO:0046718	viral entry into host cell
66	GO:0009162	deoxyribonucleoside monophosphate metabolic process
67	GO:0006520	cellular amino acid metabolic process
68	GO:0022411	cellular component disassembly
69	GO:0044703	multi-organism reproductive process
70	GO:0006956	complement activation
71	GO:0032386	regulation of intracellular transport
72	GO:0009435	NAD biosynthetic process
73	GO:0051704	multi-organism process
74	GO:0000045	autophagosome assembly
75	GO:0048514	blood vessel morphogenesis
76	GO:0009914	hormone transport
77	GO:0000469	cleavage involved in rRNA processing
78	GO:0030042	actin filament depolymerization
79	GO:0000075	cell cycle checkpoint
80	GO:0051054	positive regulation of DNA metabolic process
81	GO:0043462	regulation of ATPase activity
82	GO:0019318	hexose metabolic process
83	GO:0002685	regulation of leukocyte migration
84	GO:0030435	sporulation resulting in formation of a cellular spore
85	GO:2000147	positive regulation of cell motility
86	GO:0000305	response to oxygen radical
87	GO:0120035	regulation of plasma membrane bounded cell projection organization
88	GO:0031497	chromatin assembly
89	GO:0002683	negative regulation of immune system process
90	GO:0009200	deoxyribonucleoside triphosphate metabolic process
91	GO:0006406	mRNA export from nucleus
92	GO:0009653	anatomical structure morphogenesis
93	GO:0016241	regulation of macroautophagy
94	GO:0032412	regulation of ion transmembrane transporter activity
95	GO:0010608	posttranscriptional regulation of gene expression
96	GO:0018298	protein-chromophore linkage
97	GO:0071709	membrane assembly
98	GO:0031669	cellular response to nutrient levels
99	GO:0006206	pyrimidine nucleobase metabolic process
100	GO:0010639	negative regulation of organelle organization
101	GO:0097435	supramolecular fiber organization
102	GO:0019748	secondary metabolic process
103	GO:0000165	MAPK cascade
104	GO:0048589	developmental growth
105	GO:0006401	RNA catabolic process
106	GO:0038094	Fc-gamma receptor signaling pathway
107	GO:0090501	RNA phosphodiester bond hydrolysis
108	GO:0031323	regulation of cellular metabolic process
109	GO:0006970	response to osmotic stress
110	GO:0030198	extracellular matrix organization
111	GO:0006260	DNA replication
112	GO:0045834	positive regulation of lipid metabolic process
113	GO:0009719	response to endogenous stimulus
114	GO:0002793	positive regulation of peptide secretion
115	GO:0010647	positive regulation of cell communication
116	GO:0051252	regulation of RNA metabolic process
117	GO:0009617	response to bacterium
118	GO:0034250	positive regulation of cellular amide metabolic process
119	GO:0015947	methane metabolic process
120	GO:0042981	regulation of apoptotic process
121	GO:0050731	positive regulation of peptidyl-tyrosine phosphorylation
122	GO:0098813	nuclear chromosome segregation
123	GO:0006801	superoxide metabolic process
124	GO:0052200	response to host defenses
125	GO:0002703	regulation of leukocyte mediated immunity
126	GO:0032465	regulation of cytokinesis
127	GO:0051603	proteolysis involved in cellular protein catabolic process
128	GO:0007601	visual perception
129	GO:0045892	negative regulation of transcription, DNA-templated
130	GO:0008213	protein alkylation
131	GO:0034471	ncRNA 5'-end processing
132	GO:0009267	cellular response to starvation
133	GO:0009314	response to radiation
134	GO:0002521	leukocyte differentiation
135	GO:1901571	fatty acid derivative transport
136	GO:0006399	tRNA metabolic process
137	GO:1901654	response to ketone
138	GO:0071396	cellular response to lipid
139	GO:0009116	nucleoside metabolic process
140	GO:0022008	neurogenesis
141	GO:1902806	regulation of cell cycle G1/S phase transition
142	GO:0033993	response to lipid
143	GO:0034284	response to monosaccharide
144	GO:0034340	response to type I interferon
145	GO:0060070	canonical Wnt signaling pathway
146	GO:0000904	cell morphogenesis involved in differentiation
147	GO:0009185	ribonucleoside diphosphate metabolic process
148	GO:0014074	response to purine-containing compound
149	GO:0007584	response to nutrient
150	GO:0006099	tricarboxylic acid cycle
151	GO:0034329	cell junction assembly
152	GO:0098754	detoxification
153	GO:0016925	protein sumoylation
154	GO:0018393	internal peptidyl-lysine acetylation
155	GO:0046394	carboxylic acid biosynthetic process
156	GO:0042493	response to drug
157	GO:0009100	glycoprotein metabolic process
158	GO:0006522	alanine metabolic process
159	GO:0009968	negative regulation of signal transduction
160	GO:0042455	ribonucleoside biosynthetic process
161	GO:0010817	regulation of hormone levels
162	GO:0002573	myeloid leukocyte differentiation
163	GO:0018904	ether metabolic process
164	GO:0031163	metallo-sulfur cluster assembly
165	GO:0048869	cellular developmental process
166	GO:0140053	mitochondrial gene expression
167	GO:0006553	lysine metabolic process
168	GO:0035335	peptidyl-tyrosine dephosphorylation
169	GO:0072594	establishment of protein localization to organelle
170	GO:0030155	regulation of cell adhesion
171	GO:0034220	ion transmembrane transport
172	GO:0019363	pyridine nucleotide biosynthetic process
173	GO:1901879	regulation of protein depolymerization
174	GO:0050804	modulation of chemical synaptic transmission
175	GO:0006165	nucleoside diphosphate phosphorylation
176	GO:0046395	carboxylic acid catabolic process
177	GO:0006091	generation of precursor metabolites and energy
178	GO:0031175	neuron projection development
179	GO:0098609	cell-cell adhesion
180	GO:0030100	regulation of endocytosis
181	GO:0006081	cellular aldehyde metabolic process
182	GO:0045493	xylan catabolic process
183	GO:0000462	maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA)
184	GO:0072527	pyrimidine-containing compound metabolic process
185	GO:0007249	I-kappaB kinase/NF-kappaB signaling
186	GO:0120036	plasma membrane bounded cell projection organization
187	GO:0009157	deoxyribonucleoside monophosphate biosynthetic process
188	GO:0006935	chemotaxis
189	GO:0001816	cytokine production
190	GO:1901700	response to oxygen-containing compound
191	GO:0070661	leukocyte proliferation
192	GO:0034660	ncRNA metabolic process
193	GO:0097659	nucleic acid-templated transcription
194	GO:0075136	response to host
195	GO:0099003	vesicle-mediated transport in synapse
196	GO:0016064	immunoglobulin mediated immune response
197	GO:0009231	riboflavin biosynthetic process
198	GO:0006576	cellular biogenic amine metabolic process
199	GO:0002831	regulation of response to biotic stimulus
200	GO:0061640	cytoskeleton-dependent cytokinesis
201	GO:1901214	regulation of neuron death
202	GO:0002764	immune response-regulating signaling pathway
203	GO:0018209	peptidyl-serine modification
204	GO:0009141	nucleoside triphosphate metabolic process
205	GO:1901070	guanosine-containing compound biosynthetic process
206	GO:0099537	trans-synaptic signaling
207	GO:0031109	microtubule polymerization or depolymerization
208	GO:0043408	regulation of MAPK cascade
209	GO:0040013	negative regulation of locomotion
210	GO:0010035	response to inorganic substance
211	GO:0034401	chromatin organization involved in regulation of transcription
212	GO:1901698	response to nitrogen compound
213	GO:0007569	cell aging
214	GO:0032984	protein-containing complex disassembly
215	GO:0001932	regulation of protein phosphorylation
216	GO:0007423	sensory organ development
217	GO:0051304	chromosome separation
218	GO:0032270	positive regulation of cellular protein metabolic process
219	GO:0042727	flavin-containing compound biosynthetic process
220	GO:0043467	regulation of generation of precursor metabolites and energy
221	GO:0043605	cellular amide catabolic process
222	GO:0016192	vesicle-mediated transport
223	GO:0006612	protein targeting to membrane
224	GO:1903530	regulation of secretion by cell
225	GO:0046451	diaminopimelate metabolic process
226	GO:0030900	forebrain development
227	GO:0030243	cellulose metabolic process
228	GO:0035999	tetrahydrofolate interconversion
229	GO:0090502	RNA phosphodiester bond hydrolysis, endonucleolytic
230	GO:0042724	thiamine-containing compound biosynthetic process
231	GO:0009063	cellular amino acid catabolic process
232	GO:0009725	response to hormone
233	GO:0072001	renal system development
234	GO:1901137	carbohydrate derivative biosynthetic process
235	GO:0007015	actin filament organization
236	GO:0048878	chemical homeostasis
237	GO:0009072	aromatic amino acid family metabolic process
238	GO:0001510	RNA methylation
239	GO:0007051	spindle organization
240	GO:0006753	nucleoside phosphate metabolic process
241	GO:0006464	cellular protein modification process
242	GO:0015698	inorganic anion transport
243	GO:0071705	nitrogen compound transport
244	GO:1905330	regulation of morphogenesis of an epithelium
245	GO:0034605	cellular response to heat
246	GO:0006415	translational termination
247	GO:0043085	positive regulation of catalytic activity
248	GO:0030833	regulation of actin filament polymerization
249	GO:0018193	peptidyl-amino acid modification
250	GO:1903046	meiotic cell cycle process
251	GO:0016071	mRNA metabolic process
252	GO:0050657	nucleic acid transport
253	GO:0045927	positive regulation of growth
254	GO:0071806	protein transmembrane transport
255	GO:0007266	Rho protein signal transduction
256	GO:0051291	protein heterooligomerization
257	GO:0030203	glycosaminoglycan metabolic process
258	GO:0032259	methylation
259	GO:0000270	peptidoglycan metabolic process
260	GO:0071322	cellular response to carbohydrate stimulus
261	GO:0051640	organelle localization
262	GO:0050953	sensory perception of light stimulus
263	GO:0006749	glutathione metabolic process
264	GO:0009173	pyrimidine ribonucleoside monophosphate metabolic process
265	GO:0009891	positive regulation of biosynthetic process
266	GO:0010498	proteasomal protein catabolic process
267	GO:0051249	regulation of lymphocyte activation
268	GO:0006812	cation transport
269	GO:0051208	sequestering of calcium ion
270	GO:0015979	photosynthesis
271	GO:0072331	signal transduction by p53 class mediator
272	GO:0006974	cellular response to DNA damage stimulus
273	GO:0002097	tRNA wobble base modification
274	GO:0002449	lymphocyte mediated immunity
275	GO:0006547	histidine metabolic process
276	GO:0051928	positive regulation of calcium ion transport
277	GO:0090529	cell septum assembly
278	GO:0006164	purine nucleotide biosynthetic process
279	GO:1901019	regulation of calcium ion transmembrane transporter activity
280	GO:0044042	glucan metabolic process
281	GO:0000398	mRNA splicing, via spliceosome
282	GO:0033002	muscle cell proliferation
283	GO:0043549	regulation of kinase activity
284	GO:0051100	negative regulation of binding
285	GO:0032886	regulation of microtubule-based process
286	GO:0007219	Notch signaling pathway
287	GO:0006094	gluconeogenesis
288	GO:0048518	positive regulation of biological process
289	GO:0043312	neutrophil degranulation
290	GO:0030168	platelet activation
291	GO:0042435	indole-containing compound biosynthetic process
292	GO:0044728	DNA methylation or demethylation
293	GO:0045786	negative regulation of cell cycle
294	GO:0051262	protein tetramerization
295	GO:0009062	fatty acid catabolic process
296	GO:0090132	epithelium migration
297	GO:0044264	cellular polysaccharide metabolic process
298	GO:0051092	positive regulation of NF-kappaB transcription factor activity
299	GO:0007586	digestion
300	GO:0048870	cell motility
301	GO:0046434	organophosphate catabolic process
302	GO:0017144	drug metabolic process
303	GO:0007611	learning or memory
304	GO:0031330	negative regulation of cellular catabolic process
305	GO:0070887	cellular response to chemical stimulus
306	GO:0046165	alcohol biosynthetic process
307	GO:1903409	reactive oxygen species biosynthetic process
308	GO:1901068	guanosine-containing compound metabolic process
309	GO:0055086	nucleobase-containing small molecule metabolic process
310	GO:0006354	DNA-templated transcription, elongation
311	GO:0016137	glycoside metabolic process
312	GO:0044068	modulation by symbiont of host cellular process
313	GO:0043648	dicarboxylic acid metabolic process
314	GO:0042537	benzene-containing compound metabolic process
315	GO:0070372	regulation of ERK1 and ERK2 cascade
316	GO:0050769	positive regulation of neurogenesis
317	GO:0032271	regulation of protein polymerization
318	GO:0009888	tissue development
319	GO:0010558	negative regulation of macromolecule biosynthetic process
320	GO:0046034	ATP metabolic process
321	GO:0022604	regulation of cell morphogenesis
322	GO:0016070	RNA metabolic process
323	GO:0006473	protein acetylation
324	GO:0044242	cellular lipid catabolic process
325	GO:0016042	lipid catabolic process
326	GO:0022406	membrane docking
327	GO:1903578	regulation of ATP metabolic process
328	GO:0006730	one-carbon metabolic process
329	GO:0009130	pyrimidine nucleoside monophosphate biosynthetic process
330	GO:0043101	purine-containing compound salvage
331	GO:0008610	lipid biosynthetic process
332	GO:0001934	positive regulation of protein phosphorylation
333	GO:0035194	post-transcriptional gene silencing by RNA
334	GO:0016998	cell wall macromolecule catabolic process
335	GO:1990845	adaptive thermogenesis
336	GO:0006760	folic acid-containing compound metabolic process
337	GO:0071310	cellular response to organic substance
338	GO:0006754	ATP biosynthetic process
339	GO:0051648	vesicle localization
340	GO:0032261	purine nucleotide salvage
341	GO:0042026	protein refolding
342	GO:0030072	peptide hormone secretion
343	GO:0008154	actin polymerization or depolymerization
344	GO:0009582	detection of abiotic stimulus
345	GO:0006793	phosphorus metabolic process
346	GO:0019222	regulation of metabolic process
347	GO:0031400	negative regulation of protein modification process
348	GO:0006183	GTP biosynthetic process
349	GO:0009225	nucleotide-sugar metabolic process
350	GO:0006635	fatty acid beta-oxidation
351	GO:0051223	regulation of protein transport
352	GO:0018022	peptidyl-lysine methylation
353	GO:0007420	brain development
354	GO:0006779	porphyrin-containing compound biosynthetic process
355	GO:1902533	positive regulation of intracellular signal transduction
356	GO:0090150	establishment of protein localization to membrane
357	GO:1901652	response to peptide
358	GO:0006470	protein dephosphorylation
359	GO:0035821	modulation of process of other organism
360	GO:0034440	lipid oxidation
361	GO:0030041	actin filament polymerization
362	GO:0019835	cytolysis
363	GO:0006412	translation
364	GO:0071347	cellular response to interleukin-1
365	GO:1901653	cellular response to peptide
366	GO:0007596	blood coagulation
367	GO:0046677	response to antibiotic
368	GO:0071621	granulocyte chemotaxis
369	GO:0002366	leukocyte activation involved in immune response
370	GO:0046417	chorismate metabolic process
371	GO:0070588	calcium ion transmembrane transport
372	GO:0048812	neuron projection morphogenesis
373	GO:0009607	response to biotic stimulus
374	GO:0061008	hepaticobiliary system development
375	GO:2001057	reactive nitrogen species metabolic process
376	GO:0080134	regulation of response to stress
377	GO:0050790	regulation of catalytic activity
378	GO:0071692	protein localization to extracellular region
379	GO:0097190	apoptotic signaling pathway
380	GO:0048584	positive regulation of response to stimulus
381	GO:0016072	rRNA metabolic process
382	GO:0006826	iron ion transport
383	GO:0099177	regulation of trans-synaptic signaling
384	GO:0006790	sulfur compound metabolic process
385	GO:0071267	L-methionine salvage
386	GO:0016052	carbohydrate catabolic process
387	GO:0016477	cell migration
388	GO:0007610	behavior
389	GO:0030036	actin cytoskeleton organization
390	GO:0009117	nucleotide metabolic process
391	GO:0009199	ribonucleoside triphosphate metabolic process
392	GO:0070374	positive regulation of ERK1 and ERK2 cascade
393	GO:0034968	histone lysine methylation
394	GO:0010921	regulation of phosphatase activity
395	GO:0006310	DNA recombination
396	GO:0051047	positive regulation of secretion
397	GO:0006084	acetyl-CoA metabolic process
398	GO:0060047	heart contraction
399	GO:0031929	TOR signaling
400	GO:0072657	protein localization to membrane
401	GO:0051282	regulation of sequestering of calcium ion
402	GO:0009765	photosynthesis, light harvesting
403	GO:0034614	cellular response to reactive oxygen species
404	GO:0009408	response to heat
405	GO:0045936	negative regulation of phosphate metabolic process
406	GO:0048666	neuron development
407	GO:0006383	transcription by RNA polymerase III
408	GO:0035239	tube morphogenesis
409	GO:0072521	purine-containing compound metabolic process
410	GO:0042180	cellular ketone metabolic process
411	GO:0031638	zymogen activation
412	GO:0048729	tissue morphogenesis
413	GO:0007283	spermatogenesis
414	GO:0015986	ATP synthesis coupled proton transport
415	GO:0032101	regulation of response to external stimulus
416	GO:0042451	purine nucleoside biosynthetic process
417	GO:0042445	hormone metabolic process
418	GO:0007155	cell adhesion
419	GO:0030162	regulation of proteolysis
420	GO:1903320	regulation of protein modification by small protein conjugation or removal
421	GO:0034976	response to endoplasmic reticulum stress
422	GO:0048638	regulation of developmental growth
423	GO:0009228	thiamine biosynthetic process
424	GO:0006767	water-soluble vitamin metabolic process
425	GO:1904892	regulation of receptor signaling pathway via STAT
426	GO:0009201	ribonucleoside triphosphate biosynthetic process
427	GO:0009061	anaerobic respiration
428	GO:0006614	SRP-dependent cotranslational protein targeting to membrane
429	GO:0035384	thioester biosynthetic process
430	GO:2001234	negative regulation of apoptotic signaling pathway
431	GO:0098869	cellular oxidant detoxification
432	GO:0007010	cytoskeleton organization
433	GO:0045944	positive regulation of transcription by RNA polymerase II
434	GO:0006323	DNA packaging
435	GO:0002237	response to molecule of bacterial origin
436	GO:0040029	regulation of gene expression, epigenetic
437	GO:0051156	glucose 6-phosphate metabolic process
438	GO:0045666	positive regulation of neuron differentiation
439	GO:0010564	regulation of cell cycle process
440	GO:0003015	heart process
441	GO:0032414	positive regulation of ion transmembrane transporter activity
442	GO:0000086	G2/M transition of mitotic cell cycle
443	GO:0002790	peptide secretion
444	GO:0008277	regulation of G protein-coupled receptor signaling pathway
445	GO:0009166	nucleotide catabolic process
446	GO:0032309	icosanoid secretion
447	GO:0009156	ribonucleoside monophosphate biosynthetic process
448	GO:0055065	metal ion homeostasis
449	GO:0009605	response to external stimulus
450	GO:0043279	response to alkaloid
451	GO:0006665	sphingolipid metabolic process
452	GO:0006909	phagocytosis
453	GO:0006166	purine ribonucleoside salvage
454	GO:0043254	regulation of protein-containing complex assembly
455	GO:0043102	amino acid salvage
456	GO:0062012	regulation of small molecule metabolic process
457	GO:0003018	vascular process in circulatory system
458	GO:0010563	negative regulation of phosphorus metabolic process
459	GO:0007165	signal transduction
460	GO:0006885	regulation of pH
461	GO:0042357	thiamine diphosphate metabolic process
462	GO:0009311	oligosaccharide metabolic process
463	GO:0008299	isoprenoid biosynthetic process
464	GO:0008037	cell recognition
465	GO:0008217	regulation of blood pressure
466	GO:0021700	developmental maturation
467	GO:1903532	positive regulation of secretion by cell
468	GO:0023014	signal transduction by protein phosphorylation
469	GO:1901663	quinone biosynthetic process
470	GO:0051046	regulation of secretion
471	GO:0097529	myeloid leukocyte migration
472	GO:0042254	ribosome biogenesis
473	GO:0006873	cellular ion homeostasis
474	GO:0033559	unsaturated fatty acid metabolic process
475	GO:0000288	nuclear-transcribed mRNA catabolic process, deadenylation-dependent decay
476	GO:0000281	mitotic cytokinesis
477	GO:0050801	ion homeostasis
478	GO:2000145	regulation of cell motility
479	GO:1905114	cell surface receptor signaling pathway involved in cell-cell signaling
480	GO:0009792	embryo development ending in birth or egg hatching
481	GO:0071331	cellular response to hexose stimulus
482	GO:0008202	steroid metabolic process
483	GO:0001889	liver development
484	GO:0033865	nucleoside bisphosphate metabolic process
485	GO:0007626	locomotory behavior
486	GO:0034308	primary alcohol metabolic process
487	GO:0007507	heart development
488	GO:1901293	nucleoside phosphate biosynthetic process
489	GO:0060548	negative regulation of cell death
490	GO:0051129	negative regulation of cellular component organization
491	GO:1903037	regulation of leukocyte cell-cell adhesion
492	GO:0071450	cellular response to oxygen radical
493	GO:0044273	sulfur compound catabolic process
494	GO:0050777	negative regulation of immune response
495	GO:0002700	regulation of production of molecular mediator of immune response
496	GO:0071495	cellular response to endogenous stimulus
497	GO:0016571	histone methylation
498	GO:0017038	protein import
499	GO:0046683	response to organophosphorus
500	GO:0010721	negative regulation of cell development
501	GO:0016126	sterol biosynthetic process
502	GO:0065009	regulation of molecular function
503	GO:0010466	negative regulation of peptidase activity
504	GO:0014070	response to organic cyclic compound
505	GO:0042127	regulation of cell population proliferation
506	GO:2000113	negative regulation of cellular macromolecule biosynthetic process
507	GO:0019362	pyridine nucleotide metabolic process
508	GO:0006090	pyruvate metabolic process
509	GO:0072359	circulatory system development
510	GO:0046486	glycerolipid metabolic process
511	GO:0043650	dicarboxylic acid biosynthetic process
512	GO:0001523	retinoid metabolic process
513	GO:0000466	maturation of 5.8S rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA)
514	GO:0051961	negative regulation of nervous system development
515	GO:0042440	pigment metabolic process
516	GO:0009086	methionine biosynthetic process
517	GO:0071482	cellular response to light stimulus
518	GO:0045087	innate immune response
519	GO:0002682	regulation of immune system process
520	GO:0043434	response to peptide hormone
521	GO:0050768	negative regulation of neurogenesis
522	GO:0031668	cellular response to extracellular stimulus
523	GO:0036293	response to decreased oxygen levels
524	GO:0009890	negative regulation of biosynthetic process
525	GO:0042221	response to chemical
526	GO:0009790	embryo development
527	GO:0045931	positive regulation of mitotic cell cycle
528	GO:1901701	cellular response to oxygen-containing compound
529	GO:0030595	leukocyte chemotaxis
530	GO:0030154	cell differentiation
531	GO:0006413	translational initiation
532	GO:0051222	positive regulation of protein transport
533	GO:0009581	detection of external stimulus
534	GO:0051179	localization
535	GO:0015671	oxygen transport
536	GO:0019395	fatty acid oxidation
537	GO:1901264	carbohydrate derivative transport
538	GO:0042255	ribosome assembly
539	GO:0071407	cellular response to organic cyclic compound
540	GO:0006869	lipid transport
541	GO:0030073	insulin secretion
542	GO:0065008	regulation of biological quality
543	GO:0060255	regulation of macromolecule metabolic process
544	GO:0051283	negative regulation of sequestering of calcium ion
545	GO:0046051	UTP metabolic process
546	GO:0019438	aromatic compound biosynthetic process
547	GO:0097549	chromatin organization involved in negative regulation of transcription
548	GO:0035304	regulation of protein dephosphorylation
549	GO:0046939	nucleotide phosphorylation
550	GO:0070126	mitochondrial translational termination
551	GO:0034248	regulation of cellular amide metabolic process
552	GO:0032502	developmental process
553	GO:0007160	cell-matrix adhesion
554	GO:0097306	cellular response to alcohol
555	GO:0002478	antigen processing and presentation of exogenous peptide antigen
556	GO:0006772	thiamine metabolic process
557	GO:0010876	lipid localization
558	GO:0031401	positive regulation of protein modification process
559	GO:0061025	membrane fusion
560	GO:0006283	transcription-coupled nucleotide-excision repair
561	GO:0006397	mRNA processing
562	GO:0072329	monocarboxylic acid catabolic process
563	GO:0006486	protein glycosylation
564	GO:0035023	regulation of Rho protein signal transduction
565	GO:0034219	carbohydrate transmembrane transport
566	GO:0000375	RNA splicing, via transesterification reactions
567	GO:0006261	DNA-dependent DNA replication
568	GO:0051301	cell division
569	GO:0046700	heterocycle catabolic process
570	GO:0046349	amino sugar biosynthetic process
571	GO:0015031	protein transport
572	GO:0042402	cellular biogenic amine catabolic process
573	GO:0043069	negative regulation of programmed cell death
574	GO:0000209	protein polyubiquitination
575	GO:0006558	L-phenylalanine metabolic process
576	GO:0048858	cell projection morphogenesis
577	GO:0051099	positive regulation of binding
578	GO:0120161	regulation of cold-induced thermogenesis
579	GO:0010629	negative regulation of gene expression
580	GO:0009064	glutamine family amino acid metabolic process
581	GO:0034285	response to disaccharide
582	GO:0019684	photosynthesis, light reaction
583	GO:0006595	polyamine metabolic process
584	GO:0071840	cellular component organization or biogenesis
585	GO:0032147	activation of protein kinase activity
586	GO:0071248	cellular response to metal ion
587	GO:0006605	protein targeting
588	GO:0008544	epidermis development
589	GO:0009749	response to glucose
590	GO:0010212	response to ionizing radiation
591	GO:0035383	thioester metabolic process
592	GO:0009253	peptidoglycan catabolic process
593	GO:0046031	ADP metabolic process
594	GO:0008654	phospholipid biosynthetic process
595	GO:0060322	head development
596	GO:0071805	potassium ion transmembrane transport
597	GO:0071428	rRNA-containing ribonucleoprotein complex export from nucleus
598	GO:0061061	muscle structure development
599	GO:0071466	cellular response to xenobiotic stimulus
600	GO:0051480	regulation of cytosolic calcium ion concentration
601	GO:0006914	autophagy
602	GO:0051272	positive regulation of cellular component movement
603	GO:0036260	RNA capping
604	GO:0023052	signaling
605	GO:0019884	antigen processing and presentation of exogenous antigen
606	GO:0009396	folic acid-containing compound biosynthetic process
607	GO:0007005	mitochondrion organization
608	GO:0051347	positive regulation of transferase activity
609	GO:0006370	7-methylguanosine mRNA capping
610	GO:0046578	regulation of Ras protein signal transduction
611	GO:0043086	negative regulation of catalytic activity
612	GO:0006720	isoprenoid metabolic process
613	GO:0071356	cellular response to tumor necrosis factor
614	GO:0034767	positive regulation of ion transmembrane transport
615	GO:0006071	glycerol metabolic process
616	GO:0051146	striated muscle cell differentiation
617	GO:0032102	negative regulation of response to external stimulus
618	GO:0009263	deoxyribonucleotide biosynthetic process
619	GO:0009167	purine ribonucleoside monophosphate metabolic process
620	GO:0044036	cell wall macromolecule metabolic process
621	GO:0017157	regulation of exocytosis
622	GO:0006633	fatty acid biosynthetic process
623	GO:0043412	macromolecule modification
624	GO:0006886	intracellular protein transport
625	GO:0045010	actin nucleation
626	GO:1901606	alpha-amino acid catabolic process
627	GO:0044839	cell cycle G2/M phase transition
628	GO:0031331	positive regulation of cellular catabolic process
629	GO:0016358	dendrite development
630	GO:0090066	regulation of anatomical structure size
631	GO:0045637	regulation of myeloid cell differentiation
632	GO:0010638	positive regulation of organelle organization
633	GO:0019877	diaminopimelate biosynthetic process
634	GO:0019682	glyceraldehyde-3-phosphate metabolic process
635	GO:0051384	response to glucocorticoid
636	GO:0042274	ribosomal small subunit biogenesis
637	GO:0006396	RNA processing
638	GO:0042129	regulation of T cell proliferation
639	GO:0032409	regulation of transporter activity
640	GO:0006144	purine nucleobase metabolic process
641	GO:0071333	cellular response to glucose stimulus
642	GO:0042063	gliogenesis
643	GO:0043010	camera-type eye development
644	GO:0019216	regulation of lipid metabolic process
645	GO:0046390	ribose phosphate biosynthetic process
646	GO:0140352	export from cell
647	GO:0032269	negative regulation of cellular protein metabolic process
648	GO:0050727	regulation of inflammatory response
649	GO:0050658	RNA transport
650	GO:1902275	regulation of chromatin organization
651	GO:0009251	glucan catabolic process
652	GO:0097305	response to alcohol
653	GO:0051270	regulation of cellular component movement
654	GO:0006783	heme biosynthetic process
655	GO:0032989	cellular component morphogenesis
656	GO:1901678	iron coordination entity transport
657	GO:0032940	secretion by cell
658	GO:0009611	response to wounding
659	GO:0009791	post-embryonic development
660	GO:0006568	tryptophan metabolic process
661	GO:2000112	regulation of cellular macromolecule biosynthetic process
662	GO:0051101	regulation of DNA binding
663	GO:0030307	positive regulation of cell growth
664	GO:0001655	urogenital system development
665	GO:0016050	vesicle organization
666	GO:2000146	negative regulation of cell motility
667	GO:0007267	cell-cell signaling
668	GO:0000003	reproduction
669	GO:0030004	cellular monovalent inorganic cation homeostasis
670	GO:0070589	cellular component macromolecule biosynthetic process
671	GO:2001020	regulation of response to DNA damage stimulus
672	GO:0016114	terpenoid biosynthetic process
673	GO:0014706	striated muscle tissue development
674	GO:0006259	DNA metabolic process
675	GO:0044766	multi-organism transport
676	GO:0031348	negative regulation of defense response
677	GO:0099504	synaptic vesicle cycle
678	GO:0001525	angiogenesis
679	GO:0048667	cell morphogenesis involved in neuron differentiation
680	GO:0070482	response to oxygen levels
681	GO:0002262	myeloid cell homeostasis
682	GO:0016197	endosomal transport
683	GO:0040017	positive regulation of locomotion
684	GO:0035303	regulation of dephosphorylation
685	GO:0044659	viral release from host cell by cytolysis
686	GO:0042726	flavin-containing compound metabolic process
687	GO:0016579	protein deubiquitination
688	GO:0006405	RNA export from nucleus
689	GO:0006875	cellular metal ion homeostasis
690	GO:0071363	cellular response to growth factor stimulus
691	GO:0009103	lipopolysaccharide biosynthetic process
692	GO:0050792	regulation of viral process
693	GO:0012501	programmed cell death
694	GO:0009124	nucleoside monophosphate biosynthetic process
695	GO:0097588	archaeal or bacterial-type flagellum-dependent cell motility
696	GO:0009247	glycolipid biosynthetic process
697	GO:0051275	beta-glucan catabolic process
698	GO:0072525	pyridine-containing compound biosynthetic process
699	GO:0030097	hemopoiesis
700	GO:0009892	negative regulation of metabolic process
701	GO:0050729	positive regulation of inflammatory response
702	GO:0008283	cell population proliferation
703	GO:0006418	tRNA aminoacylation for protein translation
704	GO:0007186	G protein-coupled receptor signaling pathway
705	GO:0022618	ribonucleoprotein complex assembly
706	GO:0070727	cellular macromolecule localization
707	GO:0001944	vasculature development
708	GO:0009310	amine catabolic process
709	GO:0039694	viral RNA genome replication
710	GO:0055080	cation homeostasis
711	GO:0009221	pyrimidine deoxyribonucleotide biosynthetic process
712	GO:0035195	gene silencing by miRNA
713	GO:1902680	positive regulation of RNA biosynthetic process
714	GO:0001959	regulation of cytokine-mediated signaling pathway
715	GO:0006353	DNA-templated transcription, termination
716	GO:0032200	telomere organization
717	GO:0006611	protein export from nucleus
718	GO:0046500	S-adenosylmethionine metabolic process
719	GO:0052548	regulation of endopeptidase activity
720	GO:1903522	regulation of blood circulation
721	GO:0042822	pyridoxal phosphate metabolic process
722	GO:0006662	glycerol ether metabolic process
723	GO:0019400	alditol metabolic process
724	GO:0009097	isoleucine biosynthetic process
725	GO:0044038	cell wall macromolecule biosynthetic process
726	GO:0046653	tetrahydrofolate metabolic process
727	GO:0051239	regulation of multicellular organismal process
728	GO:0030490	maturation of SSU-rRNA
729	GO:1903047	mitotic cell cycle process
730	GO:0023061	signal release
731	GO:0044106	cellular amine metabolic process
732	GO:0051091	positive regulation of DNA-binding transcription factor activity
733	GO:0015772	oligosaccharide transport
734	GO:0006119	oxidative phosphorylation
735	GO:0045597	positive regulation of cell differentiation
736	GO:0051048	negative regulation of secretion
737	GO:2000241	regulation of reproductive process
738	GO:1902905	positive regulation of supramolecular fiber organization
739	GO:0010410	hemicellulose metabolic process
740	GO:0060828	regulation of canonical Wnt signaling pathway
741	GO:0006367	transcription initiation from RNA polymerase II promoter
742	GO:0015937	coenzyme A biosynthetic process
743	GO:0002697	regulation of immune effector process
744	GO:0032787	monocarboxylic acid metabolic process
745	GO:0044403	symbiotic process
746	GO:0043066	negative regulation of apoptotic process
747	GO:0032355	response to estradiol
748	GO:0043270	positive regulation of ion transport
749	GO:0042326	negative regulation of phosphorylation
750	GO:0044272	sulfur compound biosynthetic process
751	GO:0016441	posttranscriptional gene silencing
752	GO:0042775	mitochondrial ATP synthesis coupled electron transport
753	GO:0050690	regulation of defense response to virus by virus
754	GO:0006596	polyamine biosynthetic process
755	GO:0051189	prosthetic group metabolic process
756	GO:0044764	multi-organism cellular process
757	GO:0001907	killing by symbiont of host cells
758	GO:0051336	regulation of hydrolase activity
759	GO:0033037	polysaccharide localization
760	GO:0009612	response to mechanical stimulus
761	GO:0031346	positive regulation of cell projection organization
762	GO:0043094	cellular metabolic compound salvage
763	GO:0009423	chorismate biosynthetic process
764	GO:0035296	regulation of tube diameter
765	GO:0071554	cell wall organization or biogenesis
766	GO:0046385	deoxyribose phosphate biosynthetic process
767	GO:0034654	nucleobase-containing compound biosynthetic process
768	GO:0031399	regulation of protein modification process
769	GO:1901880	negative regulation of protein depolymerization
770	GO:0040011	locomotion
771	GO:0046039	GTP metabolic process
772	GO:0071426	ribonucleoprotein complex export from nucleus
773	GO:0006563	L-serine metabolic process
774	GO:0006811	ion transport
775	GO:0010243	response to organonitrogen compound
776	GO:0030522	intracellular receptor signaling pathway
777	GO:0006887	exocytosis
778	GO:0050730	regulation of peptidyl-tyrosine phosphorylation
779	GO:0009628	response to abiotic stimulus
780	GO:0043207	response to external biotic stimulus
781	GO:0034470	ncRNA processing
782	GO:0016101	diterpenoid metabolic process
783	GO:0045937	positive regulation of phosphate metabolic process
784	GO:0032508	DNA duplex unwinding
785	GO:0042327	positive regulation of phosphorylation
786	GO:0044248	cellular catabolic process
787	GO:0030163	protein catabolic process
788	GO:0009401	phosphoenolpyruvate-dependent sugar phosphotransferase system
789	GO:0031329	regulation of cellular catabolic process
790	GO:0031345	negative regulation of cell projection organization
791	GO:0006534	cysteine metabolic process
792	GO:1901617	organic hydroxy compound biosynthetic process
793	GO:0034504	protein localization to nucleus
794	GO:1901987	regulation of cell cycle phase transition
795	GO:0001906	cell killing
796	GO:0030334	regulation of cell migration
797	GO:0009119	ribonucleoside metabolic process
798	GO:0071166	ribonucleoprotein complex localization
799	GO:0042325	regulation of phosphorylation
800	GO:1902749	regulation of cell cycle G2/M phase transition
801	GO:0043523	regulation of neuron apoptotic process
802	GO:0016458	gene silencing
803	GO:0051651	maintenance of location in cell
804	GO:0042401	cellular biogenic amine biosynthetic process
805	GO:0006664	glycolipid metabolic process
806	GO:0032501	multicellular organismal process
807	GO:0048699	generation of neurons
808	GO:0044085	cellular component biogenesis
809	GO:1903506	regulation of nucleic acid-templated transcription
810	GO:2001257	regulation of cation channel activity
811	GO:0042430	indole-containing compound metabolic process
812	GO:1901269	lipooligosaccharide metabolic process
813	GO:0032388	positive regulation of intracellular transport
814	GO:0002791	regulation of peptide secretion
815	GO:0009177	pyrimidine deoxyribonucleoside monophosphate biosynthetic process
816	GO:0009132	nucleoside diphosphate metabolic process
817	GO:2001141	regulation of RNA biosynthetic process
818	GO:0060401	cytosolic calcium ion transport
819	GO:0009144	purine nucleoside triphosphate metabolic process
820	GO:0006188	IMP biosynthetic process
821	GO:0034622	cellular protein-containing complex assembly
822	GO:0006771	riboflavin metabolic process
823	GO:2001233	regulation of apoptotic signaling pathway
824	GO:0032272	negative regulation of protein polymerization
825	GO:0046112	nucleobase biosynthetic process
826	GO:0050870	positive regulation of T cell activation
827	GO:0046184	aldehyde biosynthetic process
828	GO:0098655	cation transmembrane transport
829	GO:0106106	cold-induced thermogenesis
830	GO:0038095	Fc-epsilon receptor signaling pathway
831	GO:0070125	mitochondrial translational elongation
832	GO:0046490	isopentenyl diphosphate metabolic process
833	GO:0016075	rRNA catabolic process
834	GO:0051254	positive regulation of RNA metabolic process
835	GO:0022414	reproductive process
836	GO:0002696	positive regulation of leukocyte activation
837	GO:0015980	energy derivation by oxidation of organic compounds
838	GO:0019941	modification-dependent protein catabolic process
839	GO:0006813	potassium ion transport
840	GO:0015672	monovalent inorganic cation transport
841	GO:0051224	negative regulation of protein transport
842	GO:1903311	regulation of mRNA metabolic process
843	GO:0007623	circadian rhythm
844	GO:0000184	nuclear-transcribed mRNA catabolic process, nonsense-mediated decay
845	GO:0016125	sterol metabolic process
846	GO:1902221	erythrose 4-phosphate/phosphoenolpyruvate family amino acid metabolic process
847	GO:0007033	vacuole organization
848	GO:1901661	quinone metabolic process
849	GO:0009127	purine nucleoside monophosphate biosynthetic process
850	GO:0032543	mitochondrial translation
851	GO:0033365	protein localization to organelle
852	GO:0009967	positive regulation of signal transduction
853	GO:0017001	antibiotic catabolic process
854	GO:0070302	regulation of stress-activated protein kinase signaling cascade
855	GO:0071214	cellular response to abiotic stimulus
856	GO:0030653	beta-lactam antibiotic metabolic process
857	GO:0031334	positive regulation of protein-containing complex assembly
858	GO:1903008	organelle disassembly
859	GO:0007049	cell cycle
860	GO:0046777	protein autophosphorylation
861	GO:0061013	regulation of mRNA catabolic process
862	GO:0032504	multicellular organism reproduction
863	GO:0050852	T cell receptor signaling pathway
864	GO:0051234	establishment of localization
865	GO:0001817	regulation of cytokine production
866	GO:0002768	immune response-regulating cell surface receptor signaling pathway
867	GO:0019076	viral release from host cell
868	GO:0002283	neutrophil activation involved in immune response
869	GO:0061024	membrane organization
870	GO:1901342	regulation of vasculature development
871	GO:0045321	leukocyte activation
872	GO:0007276	gamete generation
873	GO:0043393	regulation of protein binding
874	GO:0019320	hexose catabolic process
875	GO:0035150	regulation of tube size
876	GO:0007600	sensory perception
877	GO:0048468	cell development
878	GO:0010975	regulation of neuron projection development
879	GO:0090276	regulation of peptide hormone secretion
880	GO:0007162	negative regulation of cell adhesion
881	GO:0007268	chemical synaptic transmission
882	GO:0006915	apoptotic process
883	GO:0006952	defense response
884	GO:0048002	antigen processing and presentation of peptide antigen
885	GO:0045471	response to ethanol
886	GO:0007548	sex differentiation
887	GO:0007034	vacuolar transport
888	GO:0006040	amino sugar metabolic process
889	GO:0052547	regulation of peptidase activity
890	GO:0046794	transport of virus
891	GO:0050920	regulation of chemotaxis
892	GO:0048646	anatomical structure formation involved in morphogenesis
893	GO:0002684	positive regulation of immune system process
894	GO:0009236	cobalamin biosynthetic process
895	GO:0015850	organic hydroxy compound transport
896	GO:0042178	xenobiotic catabolic process
897	GO:0006950	response to stress
898	GO:0031098	stress-activated protein kinase signaling cascade
899	GO:0048232	male gamete generation
900	GO:0050673	epithelial cell proliferation
901	GO:0002443	leukocyte mediated immunity
902	GO:0033157	regulation of intracellular protein transport
903	GO:0006541	glutamine metabolic process
904	GO:0050867	positive regulation of cell activation
905	GO:0006265	DNA topological change
906	GO:0044770	cell cycle phase transition
907	GO:0140014	mitotic nuclear division
908	GO:0010557	positive regulation of macromolecule biosynthetic process
909	GO:1903829	positive regulation of cellular protein localization
910	GO:0007346	regulation of mitotic cell cycle
911	GO:0009615	response to virus
912	GO:0019722	calcium-mediated signaling
913	GO:0033674	positive regulation of kinase activity
914	GO:0046854	phosphatidylinositol phosphorylation
915	GO:0050866	negative regulation of cell activation
916	GO:0031589	cell-substrate adhesion
917	GO:0046474	glycerophospholipid biosynthetic process
918	GO:0006566	threonine metabolic process
919	GO:0006555	methionine metabolic process
920	GO:0019430	removal of superoxide radicals
921	GO:0072529	pyrimidine-containing compound catabolic process
922	GO:0045926	negative regulation of growth
923	GO:1901215	negative regulation of neuron death
924	GO:0045184	establishment of protein localization
925	GO:0009070	serine family amino acid biosynthetic process
926	GO:0006096	glycolytic process
927	GO:0044003	modulation by symbiont of host process
928	GO:0052803	imidazole-containing compound metabolic process
929	GO:0010605	negative regulation of macromolecule metabolic process
930	GO:0031145	anaphase-promoting complex-dependent catabolic process
931	GO:0071715	icosanoid transport
932	GO:0051094	positive regulation of developmental process
933	GO:0009073	aromatic amino acid family biosynthetic process
934	GO:0044283	small molecule biosynthetic process
935	GO:0006820	anion transport
936	GO:0010038	response to metal ion
937	GO:0009085	lysine biosynthetic process
938	GO:0034341	response to interferon-gamma
939	GO:0009308	amine metabolic process
940	GO:0070206	protein trimerization
941	GO:0006366	transcription by RNA polymerase II
942	GO:0046365	monosaccharide catabolic process
943	GO:0045055	regulated exocytosis
944	GO:0002444	myeloid leukocyte mediated immunity
945	GO:0060627	regulation of vesicle-mediated transport
946	GO:0043122	regulation of I-kappaB kinase/NF-kappaB signaling
947	GO:0072659	protein localization to plasma membrane
948	GO:0006207	'de novo' pyrimidine nucleobase biosynthetic process
949	GO:0035890	exit from host
950	GO:0032784	regulation of DNA-templated transcription, elongation
951	GO:0008380	RNA splicing
952	GO:0007178	transmembrane receptor protein serine/threonine kinase signaling pathway
953	GO:1903508	positive regulation of nucleic acid-templated transcription
954	GO:0042593	glucose homeostasis
955	GO:0006221	pyrimidine nucleotide biosynthetic process
956	GO:0006796	phosphate-containing compound metabolic process
957	GO:0000122	negative regulation of transcription by RNA polymerase II
958	GO:0016567	protein ubiquitination
959	GO:0003012	muscle system process
960	GO:0044262	cellular carbohydrate metabolic process
961	GO:0070507	regulation of microtubule cytoskeleton organization
962	GO:0046942	carboxylic acid transport
963	GO:0140013	meiotic nuclear division
964	GO:0002822	regulation of adaptive immune response based on somatic recombination of immune receptors built from immunoglobulin superfamily domains
965	GO:0034599	cellular response to oxidative stress
966	GO:0000097	sulfur amino acid biosynthetic process
967	GO:0009306	protein secretion
968	GO:0007059	chromosome segregation
969	GO:0015774	polysaccharide transport
970	GO:0051924	regulation of calcium ion transport
971	GO:0043624	cellular protein complex disassembly
972	GO:0051983	regulation of chromosome segregation
973	GO:0097485	neuron projection guidance
974	GO:0050878	regulation of body fluid levels
975	GO:0050877	nervous system process
976	GO:0050848	regulation of calcium-mediated signaling
977	GO:0042278	purine nucleoside metabolic process
978	GO:0032392	DNA geometric change
979	GO:0048534	hematopoietic or lymphoid organ development
980	GO:0006637	acyl-CoA metabolic process
981	GO:0061136	regulation of proteasomal protein catabolic process
982	GO:0016485	protein processing
983	GO:0002009	morphogenesis of an epithelium
984	GO:0050793	regulation of developmental process
985	GO:0031960	response to corticosteroid
986	GO:0022407	regulation of cell-cell adhesion
987	GO:0006805	xenobiotic metabolic process
988	GO:0051128	regulation of cellular component organization
989	GO:0043666	regulation of phosphoprotein phosphatase activity
990	GO:0006911	phagocytosis, engulfment
991	GO:0010941	regulation of cell death
992	GO:0050796	regulation of insulin secretion
993	GO:0006606	protein import into nucleus
994	GO:0009712	catechol-containing compound metabolic process
995	GO:0030335	positive regulation of cell migration
996	GO:0044344	cellular response to fibroblast growth factor stimulus
997	GO:0006814	sodium ion transport
998	GO:0007156	homophilic cell adhesion via plasma membrane adhesion molecules
999	GO:0006954	inflammatory response
1000	GO:0098742	cell-cell adhesion via plasma-membrane adhesion molecules
1001	GO:1903050	regulation of proteolysis involved in cellular protein catabolic process
1002	GO:0015849	organic acid transport
1003	GO:0009730	detection of carbohydrate stimulus
1004	GO:0090068	positive regulation of cell cycle process
1005	GO:0001539	cilium or flagellum-dependent cell motility
1006	GO:1902600	proton transmembrane transport
1007	GO:0007018	microtubule-based movement
1008	GO:0009081	branched-chain amino acid metabolic process
1009	GO:0046835	carbohydrate phosphorylation
1010	GO:0006739	NADP metabolic process
1011	GO:0006066	alcohol metabolic process
1012	GO:0048880	sensory system development
1013	GO:0051962	positive regulation of nervous system development
1014	GO:0043410	positive regulation of MAPK cascade
1015	GO:0009309	amine biosynthetic process
1016	GO:0043067	regulation of programmed cell death
1017	GO:0019062	virion attachment to host cell
1018	GO:0005977	glycogen metabolic process
1019	GO:0034765	regulation of ion transmembrane transport
1020	GO:0007163	establishment or maintenance of cell polarity
1021	GO:0001667	ameboidal-type cell migration
1022	GO:0006281	DNA repair
1023	GO:0006360	transcription by RNA polymerase I
1024	GO:0034404	nucleobase-containing small molecule biosynthetic process
1025	GO:0046903	secretion
1026	GO:0032970	regulation of actin filament-based process
1027	GO:0044257	cellular protein catabolic process
1028	GO:0060537	muscle tissue development
1029	GO:0002455	humoral immune response mediated by circulating immunoglobulin
1030	GO:0009074	aromatic amino acid family catabolic process
1031	GO:0060284	regulation of cell development
1032	GO:0150063	visual system development
1033	GO:1902679	negative regulation of RNA biosynthetic process
1034	GO:0045861	negative regulation of proteolysis
1035	GO:0065003	protein-containing complex assembly
1036	GO:0098656	anion transmembrane transport
1037	GO:0006757	ATP generation from ADP
1038	GO:0050714	positive regulation of protein secretion
1039	GO:0019751	polyol metabolic process
1040	GO:0044265	cellular macromolecule catabolic process
1041	GO:0019054	modulation by virus of host cellular process
1042	GO:0010631	epithelial cell migration
1043	GO:0007399	nervous system development
1044	GO:0016032	viral process
1045	GO:0019220	regulation of phosphate metabolic process
1046	GO:0005996	monosaccharide metabolic process
1047	GO:0071453	cellular response to oxygen levels
1048	GO:0090305	nucleic acid phosphodiester bond hydrolysis
1049	GO:0072503	cellular divalent inorganic cation homeostasis
1050	GO:0034763	negative regulation of transmembrane transport
1051	GO:0002920	regulation of humoral immune response
1052	GO:0006525	arginine metabolic process
1053	GO:0071346	cellular response to interferon-gamma
1054	GO:0001822	kidney development
1055	GO:0009129	pyrimidine nucleoside monophosphate metabolic process
1056	GO:0065002	intracellular protein transmembrane transport
1057	GO:0042398	cellular modified amino acid biosynthetic process
1058	GO:0043174	nucleoside salvage
1059	GO:0001894	tissue homeostasis
1060	GO:0003006	developmental process involved in reproduction
1061	GO:0071326	cellular response to monosaccharide stimulus
1062	GO:0019856	pyrimidine nucleobase biosynthetic process
1063	GO:0048511	rhythmic process
1064	GO:0060402	calcium ion transport into cytosol
1065	GO:0001678	cellular glucose homeostasis
1066	GO:0071345	cellular response to cytokine stimulus
1067	GO:0002440	production of molecular mediator of immune response
1068	GO:0071897	DNA biosynthetic process
1069	GO:0046822	regulation of nucleocytoplasmic transport
1070	GO:0010033	response to organic substance
1071	GO:0071478	cellular response to radiation
1072	GO:0042744	hydrogen peroxide catabolic process
1073	GO:0002376	immune system process
1074	GO:0006839	mitochondrial transport
1075	GO:1901605	alpha-amino acid metabolic process
1076	GO:0009084	glutamine family amino acid biosynthetic process
1077	GO:0052126	movement in host environment
1078	GO:0032535	regulation of cellular component size
1079	GO:2001235	positive regulation of apoptotic signaling pathway
1080	GO:0006469	negative regulation of protein kinase activity
1081	GO:0045814	negative regulation of gene expression, epigenetic
1082	GO:0044406	adhesion of symbiont to host
1083	GO:0045893	positive regulation of transcription, DNA-templated
1084	GO:0045732	positive regulation of protein catabolic process
1085	GO:0018394	peptidyl-lysine acetylation
1086	GO:0031570	DNA integrity checkpoint
1087	GO:0009410	response to xenobiotic stimulus
1088	GO:0007166	cell surface receptor signaling pathway
1089	GO:0042823	pyridoxal phosphate biosynthetic process
1090	GO:0060968	regulation of gene silencing
1091	GO:1990748	cellular detoxification
1092	GO:0019083	viral transcription
1093	GO:0000819	sister chromatid segregation
1094	GO:0071973	bacterial-type flagellum-dependent cell motility
1095	GO:0043604	amide biosynthetic process
1096	GO:0016570	histone modification
1097	GO:0016236	macroautophagy
1098	GO:0006690	icosanoid metabolic process
1099	GO:1901607	alpha-amino acid biosynthetic process
1100	GO:0072524	pyridine-containing compound metabolic process
1101	GO:0046164	alcohol catabolic process
1102	GO:0097530	granulocyte migration
1103	GO:0019080	viral gene expression
1104	GO:0060341	regulation of cellular localization
1105	GO:0006959	humoral immune response
1106	GO:0010976	positive regulation of neuron projection development
1107	GO:0050865	regulation of cell activation
1108	GO:0045664	regulation of neuron differentiation
1109	GO:1901292	nucleoside phosphate catabolic process
1110	GO:0006518	peptide metabolic process
1111	GO:0019724	B cell mediated immunity
1112	GO:0006222	UMP biosynthetic process
1113	GO:0046348	amino sugar catabolic process
1114	GO:0007088	regulation of mitotic nuclear division
1115	GO:0000096	sulfur amino acid metabolic process
1116	GO:0055082	cellular chemical homeostasis
1117	GO:0015768	maltose transport
1118	GO:0006468	protein phosphorylation
1119	GO:0009583	detection of light stimulus
1120	GO:0033692	cellular polysaccharide biosynthetic process
1121	GO:0045491	xylan metabolic process
1122	GO:0000956	nuclear-transcribed mRNA catabolic process
1123	GO:0006936	muscle contraction
1124	GO:0010821	regulation of mitochondrion organization
1125	GO:0070997	neuron death
1126	GO:0009452	7-methylguanosine RNA capping
1127	GO:0006549	isoleucine metabolic process
1128	GO:0071456	cellular response to hypoxia
1129	GO:0050832	defense response to fungus
1130	GO:0051276	chromosome organization
1131	GO:0051588	regulation of neurotransmitter transport
1132	GO:1902653	secondary alcohol biosynthetic process
1133	GO:0006357	regulation of transcription by RNA polymerase II
1134	GO:0034656	nucleobase-containing small molecule catabolic process
1135	GO:0002431	Fc receptor mediated stimulatory signaling pathway
1136	GO:0039633	killing by virus of host cell
1137	GO:0044347	cell wall polysaccharide catabolic process
1138	GO:0006024	glycosaminoglycan biosynthetic process
1139	GO:0006898	receptor-mediated endocytosis
1140	GO:0007259	receptor signaling pathway via JAK-STAT
1141	GO:0006220	pyrimidine nucleotide metabolic process
1142	GO:0097746	regulation of blood vessel diameter
1143	GO:0043903	regulation of symbiotic process
1144	GO:0009416	response to light stimulus
1145	GO:0043632	modification-dependent macromolecule catabolic process
1146	GO:0051302	regulation of cell division
1147	GO:0001654	eye development
1148	GO:0090503	RNA phosphodiester bond hydrolysis, exonucleolytic
1149	GO:0048608	reproductive structure development
1150	GO:0009394	2'-deoxyribonucleotide metabolic process
1151	GO:0006778	porphyrin-containing compound metabolic process
1152	GO:0032411	positive regulation of transporter activity
1153	GO:0050767	regulation of neurogenesis
1154	GO:0006026	aminoglycan catabolic process
1155	GO:0060759	regulation of response to cytokine stimulus
1156	GO:0031667	response to nutrient levels
1157	GO:0006140	regulation of nucleotide metabolic process
1158	GO:0009896	positive regulation of catabolic process
1159	GO:0055067	monovalent inorganic cation homeostasis
1160	GO:0001505	regulation of neurotransmitter levels
1161	GO:0071496	cellular response to external stimulus
1162	GO:0009065	glutamine family amino acid catabolic process
1163	GO:0046686	response to cadmium ion
1164	GO:0043200	response to amino acid
1165	GO:0007265	Ras protein signal transduction
1166	GO:0032273	positive regulation of protein polymerization
1167	GO:0043244	regulation of protein-containing complex disassembly
1168	GO:0001558	regulation of cell growth
1169	GO:0031640	killing of cells of other organism
1170	GO:0051402	neuron apoptotic process
1171	GO:0022412	cellular process involved in reproduction in multicellular organism
1172	GO:0048015	phosphatidylinositol-mediated signaling
1173	GO:0071451	cellular response to superoxide
1174	GO:0042592	homeostatic process
1175	GO:0080135	regulation of cellular response to stress
1176	GO:0042559	pteridine-containing compound biosynthetic process
1177	GO:0006457	protein folding
1178	GO:0006536	glutamate metabolic process
1179	GO:0099536	synaptic signaling
1180	GO:0006325	chromatin organization
1181	GO:0010257	NADH dehydrogenase complex assembly
1182	GO:0010389	regulation of G2/M transition of mitotic cell cycle
1183	GO:0045859	regulation of protein kinase activity
1184	GO:0070555	response to interleukin-1
1185	GO:0007017	microtubule-based process
1186	GO:0002274	myeloid leukocyte activation
1187	GO:0048193	Golgi vesicle transport
1188	GO:0030488	tRNA methylation
1189	GO:0051259	protein complex oligomerization
1190	GO:0043542	endothelial cell migration
1191	GO:0032870	cellular response to hormone stimulus
1192	GO:0007517	muscle organ development
1193	GO:0042542	response to hydrogen peroxide
1194	GO:0051253	negative regulation of RNA metabolic process
1195	GO:0072358	cardiovascular system development
1196	GO:0042743	hydrogen peroxide metabolic process
1197	GO:0098771	inorganic ion homeostasis
1198	GO:0022607	cellular component assembly
1199	GO:0044057	regulation of system process
1200	GO:1901575	organic substance catabolic process
1201	GO:0045595	regulation of cell differentiation
1202	GO:0044270	cellular nitrogen compound catabolic process
1203	GO:0018958	phenol-containing compound metabolic process
1204	GO:0009057	macromolecule catabolic process
1205	GO:0034754	cellular hormone metabolic process
1206	GO:0030099	myeloid cell differentiation
1207	GO:0071774	response to fibroblast growth factor
1208	GO:0080090	regulation of primary metabolic process
1209	GO:0036230	granulocyte activation
1210	GO:0044803	multi-organism membrane organization
1211	GO:0046364	monosaccharide biosynthetic process
1212	GO:0098916	anterograde trans-synaptic signaling
1213	GO:0046916	cellular transition metal ion homeostasis
1214	GO:0051273	beta-glucan metabolic process
1215	GO:0002429	immune response-activating cell surface receptor signaling pathway
1216	GO:0017000	antibiotic biosynthetic process
1217	GO:2000142	regulation of DNA-templated transcription, initiation
1218	GO:0040007	growth
1219	GO:0018108	peptidyl-tyrosine phosphorylation
1220	GO:0009168	purine ribonucleoside monophosphate biosynthetic process
1221	GO:0006400	tRNA modification
1222	GO:0043065	positive regulation of apoptotic process
1223	GO:0031503	protein-containing complex localization
1224	GO:0006644	phospholipid metabolic process
1225	GO:0030098	lymphocyte differentiation
1226	GO:0009174	pyrimidine ribonucleoside monophosphate biosynthetic process
1227	GO:0019344	cysteine biosynthetic process
1228	GO:0044091	membrane biogenesis
1229	GO:0045930	negative regulation of mitotic cell cycle
1230	GO:0019730	antimicrobial humoral response
1231	GO:0051260	protein homooligomerization
1232	GO:1900542	regulation of purine nucleotide metabolic process
1233	GO:0031047	gene silencing by RNA
1234	GO:0006996	organelle organization
1235	GO:0019064	fusion of virus membrane with host plasma membrane
1236	GO:0006189	'de novo' IMP biosynthetic process
1237	GO:0051641	cellular localization
1238	GO:0038096	Fc-gamma receptor signaling pathway involved in phagocytosis
1239	GO:0015074	DNA integration
1240	GO:0008652	cellular amino acid biosynthetic process
1241	GO:0032981	mitochondrial respiratory chain complex I assembly
1242	GO:0043271	negative regulation of ion transport
1243	GO:0198738	cell-cell signaling by wnt
1244	GO:0009889	regulation of biosynthetic process
1245	GO:1901071	glucosamine-containing compound metabolic process
1246	GO:0070663	regulation of leukocyte proliferation
1247	GO:0090407	organophosphate biosynthetic process
1248	GO:0042168	heme metabolic process
1249	GO:0045229	external encapsulating structure organization
1250	GO:0044419	interspecies interaction between organisms
1251	GO:0050871	positive regulation of B cell activation
1252	GO:0000105	histidine biosynthetic process
1253	GO:0043487	regulation of RNA stability
1254	GO:0015985	energy coupled proton transport, down electrochemical gradient
1255	GO:0051346	negative regulation of hydrolase activity
1256	GO:0043628	ncRNA 3'-end processing
1257	GO:0000070	mitotic sister chromatid segregation
1258	GO:0051701	interaction with host
1259	GO:0000245	spliceosomal complex assembly
1260	GO:0033500	carbohydrate homeostasis
1261	GO:0050921	positive regulation of chemotaxis
1262	GO:0045727	positive regulation of translation
1263	GO:0006910	phagocytosis, recognition
1264	GO:0048771	tissue remodeling
1265	GO:0016049	cell growth
1266	GO:0019953	sexual reproduction
1267	GO:0009991	response to extracellular stimulus
1268	GO:0071427	mRNA-containing ribonucleoprotein complex export from nucleus
1269	GO:0060048	cardiac muscle contraction
1270	GO:0008219	cell death
1271	GO:0033044	regulation of chromosome organization
1272	GO:0097237	cellular response to toxic substance
1273	GO:0043009	chordate embryonic development
1274	GO:0007409	axonogenesis
1275	GO:0000902	cell morphogenesis
1276	GO:0050864	regulation of B cell activation
1277	GO:0033209	tumor necrosis factor-mediated signaling pathway
1278	GO:0006836	neurotransmitter transport
1279	GO:0006586	indolalkylamine metabolic process
1280	GO:0030682	mitigation of host defenses by symbiont
1281	GO:0051348	negative regulation of transferase activity
1282	GO:0010675	regulation of cellular carbohydrate metabolic process
1283	GO:0043039	tRNA aminoacylation
1284	GO:0009260	ribonucleotide biosynthetic process
1285	GO:0009205	purine ribonucleoside triphosphate metabolic process
1286	GO:0000027	ribosomal large subunit assembly
1287	GO:0002446	neutrophil mediated immunity
1288	GO:1903708	positive regulation of hemopoiesis
1289	GO:0042391	regulation of membrane potential
1290	GO:0048524	positive regulation of viral process
1291	GO:0050863	regulation of T cell activation
1292	GO:1901616	organic hydroxy compound catabolic process
1293	GO:0006338	chromatin remodeling
1294	GO:0006810	transport
1295	GO:1901570	fatty acid derivative biosynthetic process
1296	GO:0055076	transition metal ion homeostasis
1297	GO:0036211	protein modification process
1298	GO:0051241	negative regulation of multicellular organismal process
1299	GO:0051251	positive regulation of lymphocyte activation
1300	GO:0051050	positive regulation of transport
1301	GO:0009265	2'-deoxyribonucleotide biosynthetic process
1302	GO:0015669	gas transport
1303	GO:1901657	glycosyl compound metabolic process
1304	GO:0009894	regulation of catabolic process
1305	GO:0000041	transition metal ion transport
1306	GO:0030030	cell projection organization
1307	GO:1990778	protein localization to cell periphery
1308	GO:0009208	pyrimidine ribonucleoside triphosphate metabolic process
1309	GO:0044179	hemolysis in other organism
1310	GO:0010648	negative regulation of cell communication
1311	GO:0046425	regulation of receptor signaling pathway via JAK-STAT
1312	GO:0008643	carbohydrate transport
1313	GO:0006368	transcription elongation from RNA polymerase II promoter
1314	GO:0061572	actin filament bundle organization
1315	GO:0006270	DNA replication initiation
1316	GO:1902652	secondary alcohol metabolic process
1317	GO:0006937	regulation of muscle contraction
1318	GO:0006544	glycine metabolic process
1319	GO:0019752	carboxylic acid metabolic process
1320	GO:0046174	polyol catabolic process
1321	GO:0001666	response to hypoxia
1322	GO:0051495	positive regulation of cytoskeleton organization
1323	GO:1901361	organic cyclic compound catabolic process
1324	GO:0002218	activation of innate immune response
1325	GO:1904064	positive regulation of cation transmembrane transport
1326	GO:0043043	peptide biosynthetic process
1327	GO:0006694	steroid biosynthetic process
1328	GO:0048585	negative regulation of response to stimulus
1329	GO:0019058	viral life cycle
1330	GO:0000272	polysaccharide catabolic process
1331	GO:0043570	maintenance of DNA repeat elements
1332	GO:0030111	regulation of Wnt signaling pathway
1333	GO:0071222	cellular response to lipopolysaccharide
1334	GO:0046219	indolalkylamine biosynthetic process
1335	GO:0099024	plasma membrane invagination
1336	GO:0051209	release of sequestered calcium ion into cytosol
1337	GO:0051172	negative regulation of nitrogen compound metabolic process
1338	GO:0046128	purine ribonucleoside metabolic process
1339	GO:0050670	regulation of lymphocyte proliferation
1340	GO:0051649	establishment of localization in cell
1341	GO:0016999	antibiotic metabolic process
1342	GO:0050890	cognition
1343	GO:0051169	nuclear transport
1344	GO:0030838	positive regulation of actin filament polymerization
1345	GO:0031328	positive regulation of cellular biosynthetic process
1346	GO:0019932	second-messenger-mediated signaling
1347	GO:0010720	positive regulation of cell development
1348	GO:0046148	pigment biosynthetic process
1349	GO:0051017	actin filament bundle assembly
1350	GO:1901565	organonitrogen compound catabolic process
1351	GO:0050851	antigen receptor-mediated signaling pathway
1352	GO:0034032	purine nucleoside bisphosphate metabolic process
1353	GO:0031333	negative regulation of protein-containing complex assembly
1354	GO:0046651	lymphocyte proliferation
1355	GO:0006073	cellular glucan metabolic process
1356	GO:0006414	translational elongation
1357	GO:0043068	positive regulation of programmed cell death
1358	GO:0006766	vitamin metabolic process
1359	GO:0090316	positive regulation of intracellular protein transport
1360	GO:1903362	regulation of cellular protein catabolic process
1361	GO:0000725	recombinational repair
1362	GO:0010952	positive regulation of peptidase activity
1363	GO:0050776	regulation of immune response
1364	GO:0019319	hexose biosynthetic process
1365	GO:0002263	cell activation involved in immune response
1366	GO:0045765	regulation of angiogenesis
1367	GO:0006351	transcription, DNA-templated
1368	GO:0051716	cellular response to stimulus
1369	GO:0044843	cell cycle G1/S phase transition
1370	GO:0001676	long-chain fatty acid metabolic process
1371	GO:0009266	response to temperature stimulus
1372	GO:1905475	regulation of protein localization to membrane
1373	GO:0006913	nucleocytoplasmic transport
1374	GO:0098657	import into cell
1375	GO:0000303	response to superoxide
1376	GO:0015748	organophosphate ester transport
1377	GO:0002520	immune system development
1378	GO:0048609	multicellular organismal reproductive process
1379	GO:0048872	homeostasis of number of cells
1380	GO:0045787	positive regulation of cell cycle
1381	GO:0070201	regulation of establishment of protein localization
1382	GO:0006631	fatty acid metabolic process
1383	GO:0010562	positive regulation of phosphorus metabolic process
1384	GO:0044275	cellular carbohydrate catabolic process
1385	GO:0015766	disaccharide transport
1386	GO:0009229	thiamine diphosphate biosynthetic process
1387	GO:0000377	RNA splicing, via transesterification reactions with bulged adenosine as nucleophile
1388	GO:0051883	killing of cells in other organism involved in symbiotic interaction
1389	GO:0071216	cellular response to biotic stimulus
1390	GO:0002474	antigen processing and presentation of peptide antigen via MHC class I
1391	GO:0051248	negative regulation of protein metabolic process
1392	GO:1903827	regulation of cellular protein localization
1393	GO:0044255	cellular lipid metabolic process
1394	GO:0019882	antigen processing and presentation
1395	GO:0015711	organic anion transport
1396	GO:0002250	adaptive immune response
1397	GO:0060429	epithelium development
1398	GO:0019068	virion assembly
1399	GO:0006446	regulation of translational initiation
1400	GO:0010646	regulation of cell communication
1401	GO:0051604	protein maturation
1402	GO:0009101	glycoprotein biosynthetic process
1403	GO:0008015	blood circulation
1404	GO:0015931	nucleobase-containing compound transport
1405	GO:0016573	histone acetylation
1406	GO:0006958	complement activation, classical pathway
1407	GO:0009593	detection of chemical stimulus
1408	GO:0050805	negative regulation of synaptic transmission
1409	GO:0006098	pentose-phosphate shunt
1410	GO:1901991	negative regulation of mitotic cell cycle phase transition
1411	GO:0007204	positive regulation of cytosolic calcium ion concentration
1412	GO:0002433	immune response-regulating cell surface receptor signaling pathway involved in phagocytosis
1413	GO:0008284	positive regulation of cell population proliferation
1414	GO:0006006	glucose metabolic process
1415	GO:0008218	bioluminescence
1416	GO:0050954	sensory perception of mechanical stimulus
1417	GO:0009451	RNA modification
1418	GO:0019184	nonribosomal peptide biosynthetic process
1419	GO:0009620	response to fungus
1420	GO:0050900	leukocyte migration
1421	GO:0042692	muscle cell differentiation
1422	GO:0031396	regulation of protein ubiquitination
1423	GO:0043281	regulation of cysteine-type endopeptidase activity involved in apoptotic process
1424	GO:0006333	chromatin assembly or disassembly
1425	GO:0031324	negative regulation of cellular metabolic process
1426	GO:0051338	regulation of transferase activity
1427	GO:0048583	regulation of response to stimulus
1428	GO:0045785	positive regulation of cell adhesion
1429	GO:0000271	polysaccharide biosynthetic process
1430	GO:2000377	regulation of reactive oxygen species metabolic process
1431	GO:0051817	modulation of process of other organism involved in symbiotic interaction
1432	GO:0000724	double-strand break repair via homologous recombination
1433	GO:0042364	water-soluble vitamin biosynthetic process
1434	GO:0007275	multicellular organism development
1435	GO:0034637	cellular carbohydrate biosynthetic process
1436	GO:0009746	response to hexose
1437	GO:0007568	aging
1438	GO:0030178	negative regulation of Wnt signaling pathway
1439	GO:0042181	ketone biosynthetic process
1440	GO:0048856	anatomical structure development
1441	GO:0042330	taxis
1442	GO:0010556	regulation of macromolecule biosynthetic process
1443	GO:1901658	glycosyl compound catabolic process
1444	GO:0000302	response to reactive oxygen species
1445	GO:0043062	extracellular structure organization
1446	GO:0046049	UMP metabolic process
1447	GO:0022613	ribonucleoprotein complex biogenesis
1448	GO:0044409	entry into host
1449	GO:0051205	protein insertion into membrane
1450	GO:0071941	nitrogen cycle metabolic process
1451	GO:0043488	regulation of mRNA stability
1452	GO:0043934	sporulation
1453	GO:0031167	rRNA methylation
1454	GO:0038093	Fc receptor signaling pathway
1455	GO:0031647	regulation of protein stability
1456	GO:0002252	immune effector process
1457	GO:0071695	anatomical structure maturation
1458	GO:0009259	ribonucleotide metabolic process
1459	GO:0043545	molybdopterin cofactor metabolic process
1460	GO:0009755	hormone-mediated signaling pathway
1461	GO:0008285	negative regulation of cell population proliferation
1462	GO:0032990	cell part morphogenesis
1463	GO:0006955	immune response
1464	GO:0007599	hemostasis
1465	GO:0035592	establishment of protein localization to extracellular region
1466	GO:0051960	regulation of nervous system development
1467	GO:0046209	nitric oxide metabolic process
1468	GO:0035556	intracellular signal transduction
1469	GO:0050821	protein stabilization
1470	GO:0002706	regulation of lymphocyte mediated immunity
1471	GO:0033866	nucleoside bisphosphate biosynthetic process
1472	GO:0000460	maturation of 5.8S rRNA
1473	GO:0051707	response to other organism
1474	GO:0032879	regulation of localization
1475	GO:0009262	deoxyribonucleotide metabolic process
1476	GO:0006928	movement of cell or subcellular component
1477	GO:0009089	lysine biosynthetic process via diaminopimelate
1478	GO:0015936	coenzyme A metabolic process
1479	GO:0034764	positive regulation of transmembrane transport
1480	GO:0010604	positive regulation of macromolecule metabolic process
1481	GO:0009148	pyrimidine nucleoside triphosphate biosynthetic process
1482	GO:0002377	immunoglobulin production
1483	GO:0002757	immune response-activating signal transduction
1484	GO:0071824	protein-DNA complex subunit organization
1485	GO:0032774	RNA biosynthetic process
1486	GO:0009112	nucleobase metabolic process
1487	GO:0071616	acyl-CoA biosynthetic process
1488	GO:0061458	reproductive system development
1489	GO:0019359	nicotinamide nucleotide biosynthetic process
1490	GO:0038061	NIK/NF-kappaB signaling
1491	GO:0051783	regulation of nuclear division
1492	GO:0045017	glycerolipid biosynthetic process
1493	GO:0046879	hormone secretion
1494	GO:0032869	cellular response to insulin stimulus
1495	GO:0030258	lipid modification
1496	GO:0070838	divalent metal ion transport
1497	GO:0009126	purine nucleoside monophosphate metabolic process
1498	GO:1903507	negative regulation of nucleic acid-templated transcription
1499	GO:0030217	T cell differentiation
1500	GO:0072523	purine-containing compound catabolic process
1501	GO:0007605	sensory perception of sound
1502	GO:0009887	animal organ morphogenesis
1503	GO:0002224	toll-like receptor signaling pathway
1504	GO:0031347	regulation of defense response
1505	GO:0022904	respiratory electron transport chain
1506	GO:0019637	organophosphate metabolic process
1507	GO:1990266	neutrophil migration
1508	GO:0006403	RNA localization
1509	GO:0044706	multi-multicellular organism process
1510	GO:0009250	glucan biosynthetic process
1511	GO:0002275	myeloid cell activation involved in immune response
1512	GO:0120031	plasma membrane bounded cell projection assembly
1513	GO:1901568	fatty acid derivative metabolic process
1514	GO:0005975	carbohydrate metabolic process
1515	GO:0009240	isopentenyl diphosphate biosynthetic process
1516	GO:0010468	regulation of gene expression
1517	GO:0006629	lipid metabolic process
1518	GO:0008361	regulation of cell size
1519	GO:0007411	axon guidance
1520	GO:0042819	vitamin B6 biosynthetic process
1521	GO:0034249	negative regulation of cellular amide metabolic process
1522	GO:0009067	aspartate family amino acid biosynthetic process
1523	GO:0019439	aromatic compound catabolic process
1524	GO:0045934	negative regulation of nucleobase-containing compound metabolic process
1525	GO:0001503	ossification
1526	GO:1903039	positive regulation of leukocyte cell-cell adhesion
1527	GO:0002688	regulation of leukocyte chemotaxis
1528	GO:0009147	pyrimidine nucleoside triphosphate metabolic process
1529	GO:0009165	nucleotide biosynthetic process
1530	GO:0044092	negative regulation of molecular function
1531	GO:0034762	regulation of transmembrane transport
1532	GO:0051090	regulation of DNA-binding transcription factor activity
1533	GO:0016569	covalent chromatin modification
1534	GO:0033875	ribonucleoside bisphosphate metabolic process
1535	GO:0000226	microtubule cytoskeleton organization
1536	GO:0051170	import into nucleus
1537	GO:1902903	regulation of supramolecular fiber organization
1538	GO:0055074	calcium ion homeostasis
1539	GO:1901988	negative regulation of cell cycle phase transition
1540	GO:0033014	tetrapyrrole biosynthetic process
1541	GO:0009056	catabolic process
1542	GO:0051493	regulation of cytoskeleton organization
1543	GO:0031327	negative regulation of cellular biosynthetic process
1544	GO:0098542	defense response to other organism
1545	GO:0006941	striated muscle contraction
1546	GO:0044247	cellular polysaccharide catabolic process
1547	GO:0071555	cell wall organization
1548	GO:0035891	exit from host cell
1549	GO:0023056	positive regulation of signaling
1550	GO:0048285	organelle fission
1551	GO:0006526	arginine biosynthetic process
1552	GO:0009743	response to carbohydrate
1553	GO:0043446	cellular alkane metabolic process
1554	GO:0060326	cell chemotaxis
1555	GO:0071383	cellular response to steroid hormone stimulus
1556	GO:0034033	purine nucleoside bisphosphate biosynthetic process
1557	GO:0006109	regulation of carbohydrate metabolic process
1558	GO:0071265	L-methionine biosynthetic process
1559	GO:0007264	small GTPase mediated signal transduction
1560	GO:0008104	protein localization
1561	GO:0051051	negative regulation of transport
1562	GO:0048284	organelle fusion
1563	GO:0045333	cellular respiration
1564	GO:0031325	positive regulation of cellular metabolic process
1565	GO:0042723	thiamine-containing compound metabolic process
1566	GO:0030003	cellular cation homeostasis
1567	GO:0006275	regulation of DNA replication
1568	GO:0050707	regulation of cytokine secretion
1569	GO:0099643	signal release from synapse
1570	GO:0006241	CTP biosynthetic process
1571	GO:0010256	endomembrane system organization
1572	GO:0046129	purine ribonucleoside biosynthetic process
1573	GO:0010324	membrane invagination
1574	GO:0043173	nucleotide salvage
1575	GO:0042113	B cell activation
1576	GO:0007269	neurotransmitter secretion
1577	GO:0070897	transcription preinitiation complex assembly
1578	GO:0007417	central nervous system development
1579	GO:0032103	positive regulation of response to external stimulus
1580	GO:0048731	system development
1581	GO:0015977	carbon fixation
1582	GO:0051240	positive regulation of multicellular organismal process
1583	GO:0010001	glial cell differentiation
1584	GO:0044093	positive regulation of molecular function
1585	GO:0006417	regulation of translation
1586	GO:0046488	phosphatidylinositol metabolic process
1587	GO:0030031	cell projection assembly
1588	GO:0072507	divalent inorganic cation homeostasis
1589	GO:0034661	ncRNA catabolic process
1590	GO:0006643	membrane lipid metabolic process
1591	GO:0098660	inorganic ion transmembrane transport
1592	GO:1901990	regulation of mitotic cell cycle phase transition
1593	GO:0006591	ornithine metabolic process
1594	GO:0050808	synapse organization
1595	GO:0001775	cell activation
1596	GO:0043603	cellular amide metabolic process
1597	GO:0006545	glycine biosynthetic process
1598	GO:1904950	negative regulation of establishment of protein localization
1599	GO:0001701	in utero embryonic development
1600	GO:0006364	rRNA processing
1601	GO:0097191	extrinsic apoptotic signaling pathway
1602	GO:0009163	nucleoside biosynthetic process
1603	GO:0009202	deoxyribonucleoside triphosphate biosynthetic process
1604	GO:0071417	cellular response to organonitrogen compound
1605	GO:0006284	base-excision repair
1606	GO:0044550	secondary metabolite biosynthetic process
1607	GO:0009220	pyrimidine ribonucleotide biosynthetic process
1608	GO:0009078	pyruvate family amino acid metabolic process
1609	GO:0050678	regulation of epithelial cell proliferation
1610	GO:0051345	positive regulation of hydrolase activity
1611	GO:0045862	positive regulation of proteolysis
1612	GO:0018105	peptidyl-serine phosphorylation
1613	GO:0043547	positive regulation of GTPase activity
1614	GO:0009219	pyrimidine deoxyribonucleotide metabolic process
1615	GO:0061564	axon development
1616	GO:0032944	regulation of mononuclear cell proliferation
1617	GO:0006475	internal protein amino acid acetylation
1618	GO:0065004	protein-DNA complex assembly
1619	GO:0045088	regulation of innate immune response
1620	GO:0032268	regulation of cellular protein metabolic process
1621	GO:0001101	response to acid chemical
1622	GO:0031344	regulation of cell projection organization
1623	GO:0046496	nicotinamide nucleotide metabolic process
1624	GO:0050708	regulation of protein secretion
1625	GO:0046040	IMP metabolic process
1626	GO:0006022	aminoglycan metabolic process
1627	GO:0023051	regulation of signaling
1628	GO:0034613	cellular protein localization
1629	GO:0008203	cholesterol metabolic process
1630	GO:0051098	regulation of binding
1631	GO:0048871	multicellular organismal homeostasis
1632	GO:0060249	anatomical structure homeostasis
1633	GO:2001251	negative regulation of chromosome organization
1634	GO:0062197	cellular response to chemical stress
1635	GO:0033043	regulation of organelle organization
1636	GO:0048863	stem cell differentiation
1637	GO:0033036	macromolecule localization
1638	GO:1903706	regulation of hemopoiesis
1639	GO:0042176	regulation of protein catabolic process
1640	GO:0045292	mRNA cis splicing, via spliceosome
1641	GO:0043543	protein acylation
1642	GO:0010906	regulation of glucose metabolic process
1643	GO:0022610	biological adhesion
1644	GO:0045047	protein targeting to ER
1645	GO:0051028	mRNA transport
1646	GO:0031124	mRNA 3'-end processing
1647	GO:1901659	glycosyl compound biosynthetic process
1648	GO:0051289	protein homotetramerization
1649	GO:0051247	positive regulation of protein metabolic process
1650	GO:2000045	regulation of G1/S transition of mitotic cell cycle
1651	GO:0019725	cellular homeostasis
1652	GO:0070848	response to growth factor
1653	GO:0001933	negative regulation of protein phosphorylation
1654	GO:0052173	response to defenses of other organism
1655	GO:0016311	dephosphorylation
1656	GO:0072655	establishment of protein localization to mitochondrion
1657	GO:0051650	establishment of vesicle localization
1658	GO:0023057	negative regulation of signaling
1659	GO:0002687	positive regulation of leukocyte migration
1660	GO:0045860	positive regulation of protein kinase activity
1661	GO:0022409	positive regulation of cell-cell adhesion
1662	GO:0042060	wound healing
1663	GO:0006302	double-strand break repair
1664	GO:0061077	chaperone-mediated protein folding
1665	GO:0034286	response to maltose
1666	GO:0016051	carbohydrate biosynthetic process
1667	GO:0015833	peptide transport
1668	GO:0016043	cellular component organization
1669	GO:0051261	protein depolymerization
1670	GO:0009110	vitamin biosynthetic process
1671	GO:1901136	carbohydrate derivative catabolic process
1672	GO:0016055	Wnt signaling pathway
1673	GO:0015909	long-chain fatty acid transport
1674	GO:2000026	regulation of multicellular organismal development
1675	GO:0055085	transmembrane transport
1676	GO:0043433	negative regulation of DNA-binding transcription factor activity
1677	GO:0009209	pyrimidine ribonucleoside triphosphate biosynthetic process
1678	GO:1901135	carbohydrate derivative metabolic process
1679	GO:0010499	proteasomal ubiquitin-independent protein catabolic process
1680	GO:0036294	cellular response to decreased oxygen levels
1681	GO:0046834	lipid phosphorylation
1682	GO:1904062	regulation of cation transmembrane transport
1683	GO:0071375	cellular response to peptide hormone stimulus
1684	GO:0035295	tube development
1685	GO:0009123	nucleoside monophosphate metabolic process
1686	GO:0042816	vitamin B6 metabolic process
1687	GO:0019693	ribose phosphate metabolic process
1688	GO:0007159	leukocyte cell-cell adhesion
1689	GO:0046883	regulation of hormone secretion
1690	GO:0032446	protein modification by small protein conjugation
1691	GO:0006167	AMP biosynthetic process
1692	GO:0050482	arachidonic acid secretion
1693	GO:0008653	lipopolysaccharide metabolic process
1694	GO:0000028	ribosomal small subunit assembly
1695	GO:0042157	lipoprotein metabolic process
1696	GO:0044205	'de novo' UMP biosynthetic process
1697	GO:1902850	microtubule cytoskeleton organization involved in mitosis
1698	GO:0000966	RNA 5'-end processing
1699	GO:0051130	positive regulation of cellular component organization
1700	GO:0033673	negative regulation of kinase activity
1701	GO:0002253	activation of immune response
1702	GO:0051174	regulation of phosphorus metabolic process
1703	GO:0043087	regulation of GTPase activity
1704	GO:0051235	maintenance of location
1705	GO:0042558	pteridine-containing compound metabolic process
1706	GO:0006342	chromatin silencing
1707	GO:0016053	organic acid biosynthetic process
1708	GO:0046928	regulation of neurotransmitter secretion
1709	GO:0009069	serine family amino acid metabolic process
1710	GO:0072522	purine-containing compound biosynthetic process
1711	GO:0050663	cytokine secretion
1712	GO:0007093	mitotic cell cycle checkpoint
1713	GO:0051171	regulation of nitrogen compound metabolic process
1714	GO:0042098	T cell proliferation
1715	GO:0098781	ncRNA transcription
1716	GO:0043269	regulation of ion transport
1717	GO:0030182	neuron differentiation
1718	GO:0098662	inorganic cation transmembrane transport
1719	GO:0031032	actomyosin structure organization
1720	GO:0006879	cellular iron ion homeostasis
1721	GO:0006888	endoplasmic reticulum to Golgi vesicle-mediated transport
1722	GO:0031123	RNA 3'-end processing
1723	GO:0043406	positive regulation of MAP kinase activity
1724	GO:0007050	cell cycle arrest
1725	GO:0043405	regulation of MAP kinase activity
1726	GO:0000470	maturation of LSU-rRNA
1727	GO:0034289	detection of maltose stimulus
1728	GO:0009226	nucleotide-sugar biosynthetic process
1729	GO:0072593	reactive oxygen species metabolic process
1730	GO:0015718	monocarboxylic acid transport
1731	GO:0009405	pathogenesis
1732	GO:0006082	organic acid metabolic process
1733	GO:0010769	regulation of cell morphogenesis involved in differentiation
1734	GO:0051258	protein polymerization
1735	GO:0009161	ribonucleoside monophosphate metabolic process
1736	GO:0006027	glycosaminoglycan catabolic process
1737	GO:0045596	negative regulation of cell differentiation
1738	GO:0051056	regulation of small GTPase mediated signal transduction
1739	GO:1903509	liposaccharide metabolic process
1740	GO:0072511	divalent inorganic cation transport
1741	GO:1903034	regulation of response to wounding
1742	GO:0002819	regulation of adaptive immune response
1743	GO:0090087	regulation of peptide transport
1744	GO:0072330	monocarboxylic acid biosynthetic process
1745	GO:0032880	regulation of protein localization
1746	GO:1905037	autophagosome organization
1747	GO:0046036	CTP metabolic process
1748	GO:0015908	fatty acid transport
1749	GO:0070301	cellular response to hydrogen peroxide
1750	GO:0043038	amino acid activation
1751	GO:0120039	plasma membrane bounded cell projection morphogenesis
1752	GO:0031341	regulation of cell killing
1753	GO:0003008	system process
1754	GO:0051403	stress-activated MAPK cascade
1755	GO:0070085	glycosylation
1756	GO:0097553	calcium ion transmembrane import into cytosol
1757	GO:0033108	mitochondrial respiratory chain complex assembly
1758	GO:0030837	negative regulation of actin filament polymerization
1759	GO:0071241	cellular response to inorganic substance
1760	GO:0006511	ubiquitin-dependent protein catabolic process
1761	GO:0090130	tissue migration
1762	GO:0042956	maltodextrin transport
1763	GO:0005984	disaccharide metabolic process
1764	GO:0051093	negative regulation of developmental process
1765	GO:0019321	pentose metabolic process
1766	GO:0051715	cytolysis in other organism
1767	GO:0051606	detection of stimulus
1768	GO:0032868	response to insulin
1769	GO:0030449	regulation of complement activation
1770	GO:0009152	purine ribonucleotide biosynthetic process
1771	GO:0046649	lymphocyte activation
1772	GO:0042110	T cell activation
1773	GO:1903531	negative regulation of secretion by cell
1774	GO:0048523	negative regulation of cellular process
1775	GO:0019219	regulation of nucleobase-containing compound metabolic process
1776	GO:0030029	actin filament-based process
1777	GO:0042546	cell wall biogenesis
1778	GO:0019048	modulation by virus of host process
1779	GO:0072338	cellular lactam metabolic process
1780	GO:0000278	mitotic cell cycle
1781	GO:1902532	negative regulation of intracellular signal transduction
1782	GO:0006897	endocytosis
1783	GO:0045454	cell redox homeostasis
1784	GO:0009218	pyrimidine ribonucleotide metabolic process
1785	GO:0000280	nuclear division
1786	GO:0009066	aspartate family amino acid metabolic process
1787	GO:0046173	polyol biosynthetic process
1788	GO:0032872	regulation of stress-activated MAPK cascade
1789	GO:0097193	intrinsic apoptotic signaling pathway
1790	GO:0072599	establishment of protein localization to endoplasmic reticulum
1791	GO:0050853	B cell receptor signaling pathway
1792	GO:0009145	purine nucleoside triphosphate biosynthetic process
1793	GO:0006352	DNA-templated transcription, initiation
1794	GO:0040012	regulation of locomotion
1795	GO:0007281	germ cell development
1796	GO:0034330	cell junction organization
1797	GO:0009150	purine ribonucleotide metabolic process
1798	GO:0003013	circulatory system process
1799	GO:0010383	cell wall polysaccharide metabolic process
1800	GO:0006120	mitochondrial electron transport, NADH to ubiquinone
1801	GO:0070371	ERK1 and ERK2 cascade
1802	GO:0071219	cellular response to molecule of bacterial origin
1803	GO:0071902	positive regulation of protein serine/threonine kinase activity
1804	GO:0009312	oligosaccharide biosynthetic process
1805	GO:0072340	cellular lactam catabolic process
1806	GO:0006023	aminoglycan biosynthetic process
1807	GO:0044089	positive regulation of cellular component biogenesis
1808	GO:0046890	regulation of lipid biosynthetic process
1809	GO:0032956	regulation of actin cytoskeleton organization
1810	GO:0000082	G1/S transition of mitotic cell cycle
1811	GO:0110053	regulation of actin filament organization
1812	GO:0022603	regulation of anatomical structure morphogenesis
1813	GO:0061919	process utilizing autophagic mechanism
1814	GO:1902904	negative regulation of supramolecular fiber organization
1815	GO:0055072	iron ion homeostasis
1816	GO:0070925	organelle assembly
1817	GO:0045089	positive regulation of innate immune response
1818	GO:1902531	regulation of intracellular signal transduction
1819	GO:0031349	positive regulation of defense response
1820	GO:1901699	cellular response to nitrogen compound
1821	GO:0007167	enzyme linked receptor protein signaling pathway
1822	GO:0019221	cytokine-mediated signaling pathway
1823	GO:0044087	regulation of cellular component biogenesis
1824	GO:0048732	gland development
1825	GO:0034097	response to cytokine
1826	GO:0048545	response to steroid hormone
1827	GO:0044800	multi-organism membrane fusion
1828	GO:0001568	blood vessel development
1829	GO:0034728	nucleosome organization
1830	GO:0042742	defense response to bacterium
1831	GO:0002181	cytoplasmic translation
1832	GO:0009082	branched-chain amino acid biosynthetic process
1833	GO:0006551	leucine metabolic process
1834	GO:0007154	cell communication
1835	GO:0030655	beta-lactam antibiotic catabolic process
1836	GO:0044650	adhesion of symbiont to host cell
1837	GO:0000160	phosphorelay signal transduction system
1838	GO:0001659	temperature homeostasis
1839	GO:0034655	nucleobase-containing compound catabolic process
1840	GO:0010632	regulation of epithelial cell migration
1841	GO:0051246	regulation of protein metabolic process
1842	GO:0050817	coagulation
1843	GO:0010506	regulation of autophagy
1844	GO:0048519	negative regulation of biological process
1845	GO:0016054	organic acid catabolic process
1846	GO:0019692	deoxyribose phosphate metabolic process
1847	GO:0022402	cell cycle process
1848	GO:0032943	mononuclear cell proliferation
1849	GO:1902579	multi-organism localization
1850	GO:0051052	regulation of DNA metabolic process
1851	GO:0051656	establishment of organelle localization
1852	GO:0033554	cellular response to stress
1853	GO:0043413	macromolecule glycosylation
1854	GO:0042886	amide transport
1855	GO:0009060	aerobic respiration
1856	GO:0006874	cellular calcium ion homeostasis
1857	GO:0000387	spliceosomal snRNP assembly
1858	GO:0005976	polysaccharide metabolic process
1859	GO:0010628	positive regulation of gene expression
1860	GO:0009206	purine ribonucleoside triphosphate biosynthetic process
1861	GO:0043687	post-translational protein modification
1862	GO:0001818	negative regulation of cytokine production
1863	GO:0048598	embryonic morphogenesis
1864	GO:0034612	response to tumor necrosis factor
1865	GO:0071900	regulation of protein serine/threonine kinase activity
1866	GO:0046654	tetrahydrofolate biosynthetic process
1867	GO:0040008	regulation of growth
1868	GO:0051592	response to calcium ion
1869	GO:1901796	regulation of signal transduction by p53 class mediator
1870	GO:0002460	adaptive immune response based on somatic recombination of immune receptors built from immunoglobulin superfamily domains
1871	GO:0043436	oxoacid metabolic process
1872	GO:0016310	phosphorylation
1873	GO:0006289	nucleotide-excision repair
1874	GO:0070647	protein modification by small protein conjugation or removal
1875	GO:0050830	defense response to Gram-positive bacterium
1876	GO:0006479	protein methylation
1877	GO:0032506	cytokinetic process
1878	GO:0009273	peptidoglycan-based cell wall biogenesis
1879	GO:0097696	receptor signaling pathway via STAT
1880	GO:0019079	viral genome replication
1881	GO:0030855	epithelial cell differentiation
1882	GO:0001501	skeletal system development
1883	GO:0051494	negative regulation of cytoskeleton organization
1884	GO:0010948	negative regulation of cell cycle process
1885	GO:0002221	pattern recognition receptor signaling pathway
1886	GO:0008016	regulation of heart contraction
1887	GO:0034288	detection of disaccharide stimulus
1888	GO:0042273	ribosomal large subunit biogenesis
1889	GO:0030245	cellulose catabolic process
1890	GO:0044772	mitotic cell cycle phase transition
1891	GO:0046467	membrane lipid biosynthetic process
1892	GO:0070646	protein modification by small protein removal
1893	GO:0043414	macromolecule methylation
1894	GO:0051168	nuclear export
1895	GO:0006865	amino acid transport
1896	GO:0022900	electron transport chain
1897	GO:0009636	response to toxic substance
1898	GO:0006613	cotranslational protein targeting to membrane
1899	GO:0042594	response to starvation
1900	GO:0006740	NADPH regeneration
1901	GO:0051049	regulation of transport
1902	GO:0104004	cellular response to environmental stimulus
1903	GO:0015749	monosaccharide transmembrane transport
1904	GO:0010565	regulation of cellular ketone metabolic process
1905	GO:0000154	rRNA modification
1906	GO:0000723	telomere maintenance
1907	GO:0006721	terpenoid metabolic process
1908	GO:0033013	tetrapyrrole metabolic process
1909	GO:0090257	regulation of muscle system process
1910	GO:0018208	peptidyl-proline modification
1911	GO:1903169	regulation of calcium ion transmembrane transport
1912	GO:0034030	ribonucleoside bisphosphate biosynthetic process
1913	GO:0046033	AMP metabolic process
1914	GO:1903963	arachidonate transport
1915	GO:0018205	peptidyl-lysine modification
1916	GO:0009252	peptidoglycan biosynthetic process
1917	GO:0006402	mRNA catabolic process
1918	GO:2001242	regulation of intrinsic apoptotic signaling pathway
1919	GO:0010959	regulation of metal ion transport
1920	GO:0043161	proteasome-mediated ubiquitin-dependent protein catabolic process
1921	GO:0009176	pyrimidine deoxyribonucleoside monophosphate metabolic process
1922	GO:0009164	nucleoside catabolic process
1923	GO:0018212	peptidyl-tyrosine modification
1924	GO:0007169	transmembrane receptor protein tyrosine kinase signaling pathway
1925	GO:0009411	response to UV
1926	GO:0009895	negative regulation of catabolic process
1927	GO:0000910	cytokinesis
1928	GO:0061982	meiosis I cell cycle process
1929	GO:0039663	membrane fusion involved in viral entry into host cell
1930	GO:0010942	positive regulation of cell death
1931	GO:0006112	energy reserve metabolic process
1932	GO:0008637	apoptotic mitochondrial changes
1933	GO:0030832	regulation of actin filament length
1934	GO:0051607	defense response to virus
1935	GO:1904951	positive regulation of establishment of protein localization
1936	GO:0071103	DNA conformation change
1937	GO:0071826	ribonucleoprotein complex subunit organization
1938	GO:0070972	protein localization to endoplasmic reticulum
1939	GO:0062013	positive regulation of small molecule metabolic process
1940	GO:0008064	regulation of actin polymerization or depolymerization
1941	GO:0016226	iron-sulfur cluster assembly
1942	GO:0042773	ATP synthesis coupled electron transport
```
