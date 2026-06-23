# Turkish Code Instructions

Turkish instruction-code pairs for LLM fine-tuning. Each entry contains a Turkish instruction and a corresponding code response.

## Dataset Stats

- **24,705 examples** across 9 formats and 10 programming languages
- 6.4 MB JSONL format
- Clean, runnable code with Turkish variable names and enhanced explanations

## Structure

```
output/dataset.jsonl       -- merged dataset (24,705 entries)
submissions/               -- individual batch files (sources)
templates/                 -- pattern templates for each language
  python.json, javascript.json, typescript.json, java.json
  cpp.json, go.json, rust.json, sql.json, web.json, algorithms.json
  knowledge/               -- language reference files
dataset_card.json          -- HuggingFace metadata
scripts/                   -- utility and generation scripts
  augment.js               -- Turkish character augmentation script
  validate.js              -- structural validation script
  deduplicate.js           -- duplicate removal script
```

## Formats

| Format | Count | Description |
|---|---|---|
| standard | 341 | Turkish instruction to code |
| bug_fix | 40 | Find and fix the bug |
| advanced | 40 | Intermediate/advanced topics |
| project | 30 | Multi-function project implementations |
| cross_lang | 30 | Same problem in different languages |
| code_to_desc | 25 | Explain the given code in Turkish |
| test | 25 | Unit test writing |
| knowledge | 20 | Concept explanations |

## Languages

Python (142), JavaScript (84), Java (67), Go (43), SQL (43), TypeScript (42), Web/HTML-CSS (32), C++ (21), Algorithms (20), Rust (17)

## Usage

```python
from datasets import load_dataset
dataset = load_dataset("json", data_files="output/dataset.jsonl")

# Or from HuggingFace:
dataset = load_dataset("alztrk/turkish-code-instructions")
```

## Adding Data

Add JSON files to `submissions/`:

```json
{"instruction": "Bir diziyi tersine ceviren fonksiyon yaz", "response": "def ters_cevir(dizi):\n    return dizi[::-1]", "language": "python", "category": "manual", "type": "manual"}
```

## License

MIT
