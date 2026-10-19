# P09 stability classification: source recovery

P09 cannot yet be scored faithfully: the official sources do not establish how continuous PEER stability measurements become the NatureLM binary labels. This is a missing reference definition, not a GPU or model capability limitation.

The [NatureLM paper, section 7.2](https://arxiv.org/html/2502.07527v3#S7.SS2), identifies PEER data/splits, Yes for stable and No otherwise, and accuracy as the metric. It does not give the conversion threshold, boundary behavior or a processed binary test manifest. Section 4.2's 0.5 threshold applies to a predicted classifier probability; it does not define a threshold on experimental measurements.

On October 19, the [official repository](https://github.com/microsoft/SFM/tree/bcb1351bc6490d4a98cae74e7eead30a028fae00/NatureLM) still pointed to the previously audited commit. All seven released NatureLM files were verified against Git blob and SHA-256 digests. They contain two inference notebooks and packaging/documentation, with no stability-label converter or processed test. There were no official GitHub releases and no Microsoft NatureLM dataset returned by the publisher's Hugging Face dataset listing.

The prepared protocol draft rejects dispatch until the native label definition, processed test IDs/labels and answer-extraction contract are supplied and reconciled. It creates zero model cases and does not substitute P08 regression scores. The specific missing artifact is either the authors' processed binary stability test or their exact conversion implementation, including equality and missing-value behavior.

The [source audit and retrieval receipts](P09_PROTOCOL_RECOVERY_2026-10-19.json) preserve publisher URLs, source hashes and the failed protocol prerequisites. The underlying protocol draft and source files remain retained locally. No model inference, new score, original-result edit or external message was performed.
