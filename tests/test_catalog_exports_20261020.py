"""Synthetic publication seals and dependent scoring gates; no model calls."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


export = load('catalog_export', 'export_catalog_scores_20261020.py')
watch = load('derived_score_watch', 'watch_p09_derived_score_20261020.py')


class SealTests(unittest.TestCase):
    def test_unavailable_or_nan_primary_is_not_complete(self):
        self.assertFalse(export.all_finite({'spearman': None}))
        self.assertFalse(export.all_finite({'spearman': float('nan')}))
        self.assertTrue(export.all_finite({'spearman': 0.003}))

    def test_reference_member_cannot_enter_trajectory_archive(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(export, 'ROOT', Path(temp)):
            folder = Path(temp) / 'run';folder.mkdir()
            (folder / 'prediction_lock.json').write_text('{}')
            with self.assertRaisesRegex(ValueError, 'references must stay separate'):
                export.trajectory(folder, 'synthetic', {'files_sha256': {'scorer_references.jsonl': 'x'}}, Mock())

    def test_tampered_output_cannot_enter_archive(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(export, 'ROOT', Path(temp)):
            folder = Path(temp) / 'run';(folder / 'responses').mkdir(parents=True)
            (folder / 'prediction_lock.json').write_text('{}')
            (folder / 'responses/a.json').write_text('{}')
            with self.assertRaisesRegex(ValueError, 'member changed'):
                export.trajectory(folder, 'synthetic', {'files_sha256': {'responses/a.json': 'wrong'}}, Mock())

    def test_preparation_without_completion_cannot_trigger_p09_scoring(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(watch, 'P08', Path(temp)):
            (Path(temp) / 'progress.json').write_text(json.dumps({'terminal': 12851}))
            self.assertFalse(watch.ready())

    def test_incomplete_or_changed_seal_blocks_dependent_score(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(watch, 'P08', Path(temp)):
            path = Path(temp) / 'completion.json'
            path.write_text(json.dumps({'planned': 12851, 'terminal': 12850}))
            with self.assertRaisesRegex(ValueError, 'incomplete'):
                watch.ready()
            path.write_text(json.dumps({'planned': 12851, 'terminal': 12851,
                                        'prediction_lock_sha256': 'wrong'}))
            (Path(temp) / 'prediction_lock.json').write_text('{}')
            with self.assertRaisesRegex(ValueError, 'seal changed'):
                watch.ready()
