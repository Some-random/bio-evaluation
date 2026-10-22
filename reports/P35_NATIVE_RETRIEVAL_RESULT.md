# ProtST text-to-protein retrieval

| Evaluation | Year | Evaluated model | Result | Accuracy |
|---|---|---|---|---|
| ProtST text-to-protein retrieval | [2023](https://proceedings.mlr.press/v202/xu23t.html) | Released ProtST-ESM1b/PubMedBERT | **5/5 queries delivered**, each with 20 ranked proteins from 34,464 inputs | Unavailable: the release supplies no relevance labels |

Qwen and GPT models were not used for this retrieval run. A completed retrieval produces ranked candidates; it does not establish that the candidates are correct.

The declared corpus projection retained 34,464 of 36,635 source candidates; 2,171 parser rejections were excluded before inference. This does not reproduce the full historical TorchDrug graph/cohort or guarantee the paper’s numerical rankings.

The five original query texts and their complete top-20 results are [available together](../results/native_retrieval/protst_released5_rdkit_cuda213_fp32_20261021/README.md). [Download the saved output archive](../results/trajectory_archives/P35_native_ProtST_ranked_delivery_20261021.tar.gz). The archive contains model outputs and validation records; no checkpoint, environment, credential or protected reference label is included.
