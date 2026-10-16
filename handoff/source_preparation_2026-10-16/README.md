# Source-preparation handoff — 16 October 2026

This folder preserves acquisition scripts and provenance for the [source-preparation audit](../../reports/SOURCE_PREPARATION_2026-10-16.md). It contains no raw evaluation questions, reference answers, images, article HTML, model weights or credentials. The full source bundle remains local for a private release.

The verified QA50 release has 193 questions over 50 images. Nineteen exact original images were recovered, covering 73 questions. The remaining 31 PMC article pages returned a browser/reCAPTCHA challenge after all 50 legacy archive links returned HTTP 404. No challenge bypass was attempted. Native GPT-4 judging remains held. Ryze's exact component manifests and NatureLM's temporal description test remain unrecovered.

The source bundle SHA-256 is `63ff12232b04294201ac9b46ea717a930774f5010e0999abebf70dc20778e4bb` (2,294,029 bytes; 64 members). `bundle_manifest.json` lists every member hash; `source_manifest.json` records the pinned publisher URLs, Git blob verification and LFS payload digests. The image manifests contain provenance and acquisition outcomes only. Historical publisher image hashes are unavailable; recovered image bytes match the original PMCID and exact source filename, with current SHA-256 recorded.

To reproduce source recovery, copy the four Python scripts into a **new local scratch directory**, then run them there in this order:

```bash
python3 acquire_sources.py
python3 acquire_v06_images.py
python3 acquire_v06_cdn_images.py
python3 prepare_metadata.py
```

The scripts resolve their output directory from their own location. They acquire public data and perform offline metadata validation; they make no model or judge requests. A fresh network attempt may encounter different availability and should receive a new dated audit. Keep the recorded snapshot unchanged. Do not solve or bypass a source access challenge. No execution approval, scoring substitution, extra prompts, context variants or changes to frozen runs follow from this handoff.
