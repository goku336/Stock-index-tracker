# Stock-index-tracker
A Python-based stock index calculator with corporate event handling and automated CSV reporting
# Stock Index Tracker & Rebalancer

A Python-based index calculation engine that simulates real-world 
index operations workflows.

## What it does
- Calculates index level based on constituent market caps
- Applies corporate events (stock splits) and validates index integrity
- Exports a timestamped daily report CSV — ready for client delivery
- Proves index level remains unchanged after a stock split (key QA check)

## Tech used
- Python 3.14
- Pandas
- SQLite (via Python)

## Files
| File | Purpose |
|------|---------|
| data.py | Stock universe and corporate event definitions |
| index_calculator.py | Index level calculation and event processing engine |
| export.py | Generates daily client-ready CSV report |

## Sample Output
- Index Level before split: 4746.0
- Index Level after split:  4746.0
- Index Change: 0.0 ✅ (split must never move the index)

## Skills demonstrated
Index calculation · Data validation · Corporate events · 
Quality assurance · Python · Pandas · Client reporting
