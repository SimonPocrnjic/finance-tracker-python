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

## Instructions

- Rename / Copy constants_example.py > constants.py and rules.example.json > rules.json

### Navigating Menu

- Run program inside CLI with command python{version} main.py
- CLI menu, choose between 1-n options
- Typing 'h' HELP to show menu, '0' to exit program

### Importer
- Export .CSV report from bank DEFAULT_CSV_DELIMENTOR, DEFAULT_CSV_DELIMENTOR, DEFAULT_DATE_FORMAT, CSV_COLUMN_MAPPER 
to fit csv structure
- Try importing by running program selecting first option '1', typing in path to .csv file, if successful data should be stored inside root file transactions.jsonl

### Categories
- To categories transactions run program (if not running already) choose option '2', type in category and keyword (uppercase), example
category: Card Transfer, keyword: TRANSFERED TO CREDIT CARD

This will be saved to root .json file as KEY - keyword, VALUE - category:

\```json
{
  "TRANSFER TO CREDIT CARD": "Card Transfer"
}
\```

- Loads all stored transactions checks if any "Uncategorized", if keyword found inside description update category otherwise leave it "Uncategorized"

## Future plans

- Finishing Unit TESTS
- Using SQL as storage instead of jsonl
- Additional reports
- Option to sort stored transactions
- Display account credit, incoming expenses and expected credit after
- Savings strategy
- GUI display

## Running it

```bash
python3 main.py
```

Run unit tests with:

```bash
python3 main_test.py
```
