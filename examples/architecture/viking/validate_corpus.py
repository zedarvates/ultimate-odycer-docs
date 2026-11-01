# SPDX-License-Identifier: MIT
"""Bounded consistency check for this research exchange; no ingestion."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
registry = json.loads((root / 'sources.json').read_text(encoding='utf-8'))
assert registry['format'] == 'uo-architecture-research/v1'
sources = {s['id']: s for s in registry['sources']}
assert len(sources) == len(registry['sources']), 'duplicate source ID'
facts = [json.loads(line) for line in (root / 'facts.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
assert len({f['id'] for f in facts}) == len(facts), 'duplicate fact ID'
required = {'format','id','site','period','date','subject','predicate','value','unit','qualifier','dataset_kind','source_id','source_url','source_locator','accessed_date','uncertainties'}
allowed = {'archaeological_measurement','museum_reconstruction','interpretation','derived'}
for f in facts:
    assert required <= f.keys(), f['id']
    assert f['format'] == registry['format'], f['id']
    assert f['dataset_kind'] in allowed, f['id']
    assert f['source_id'] in sources, f['id']
    assert f['source_url'] == sources[f['source_id']]['url'], f['id']
    assert f['source_url'].startswith('https://'), f['id']
    assert f['accessed_date'] == '2026-11-01', f['id']
    assert isinstance(f['uncertainties'], list), f['id']
    assert f['value'] is not None or f['uncertainties'], f['id']
assert len(facts) >= 30
print(json.dumps({'status':'passed','facts':len(facts),'sources':len(sources),'format':registry['format'],'ingestion_performed':False}))
