# finance-tracker-python

A simple personal finance tracker built as a learning project. It imports
transactions from bank CSV exports, auto-categorizes them using
keyword-based rules, stores everything in a plain-text JSONL log, and
generates spending reports (e.g. totals by category per month).

No database is used — transactions are persisted as newline-delimited
JSON (`transactions.jsonl`), one record per line, in the spirit of an
append-only log.

## Requirements

- Python 3.9+ (uses built-in `dataclasses`, `json`, and `pathlib`
  modules — no third-party dependencies required for the core app).
- Optional, for future reporting/testing features: `pytest` (tests),
  `matplotlib` (charts).
- Rename / Copy constants_example.py > constants.py
- Rename / Copy rules.example.json > rules.json

## Running it

```bash
python3 main.py
```

Run unit tests with:

```bash
python3 main_test.py
```
