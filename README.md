# Turkish Code Instructions

Turkish instruction-code pairs for LLM fine-tuning.

- **5859 examples** across 15 formats and 11 languages
- Hosted on HuggingFace: [alztrk/turkish-code-instructions](https://huggingface.co/datasets/alztrk/turkish-code-instructions)

## Usage

```python
from datasets import load_dataset
dataset = load_dataset("alztrk/turkish-code-instructions")
```

## Formats

standard (1044), project (770), cross_lang (681), code_review (550), test (540), advanced (540), bug_fix (540), refactoring (345), security (321), code_to_desc (246), output_prediction (90), knowledge (60), best_practice (55), error_explain (55), complexity (50)

## License

MIT
