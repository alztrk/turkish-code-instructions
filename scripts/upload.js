const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const token = process.env.HF_TOKEN;
const repoName = 'alztrk/turkish-code-instructions';
const repoUrl = 'https://USER:' + token + '@huggingface.co/datasets/' + repoName;
const tmpDir = path.join(require('os').tmpdir(), 'hf-upload-' + Date.now());
const srcDir = 'C:\\Users\\agnes\\Desktop\\projects\\turkish-code-instructions';

function run(cmd) {
  console.log('> ' + cmd);
  return execSync(cmd, { encoding: 'utf-8', shell: true, cwd: tmpDir });
}

try {
  fs.mkdirSync(tmpDir, { recursive: true });

  // Init git and set up
  run('git init');
  run('git config user.email "alztrk@users.noreply.github.com"');
  run('git config user.name "alztrk"');
  run('git remote add origin ' + repoUrl);

  // Copy dataset file
  const content = fs.readFileSync(path.join(srcDir, 'output', 'dataset.jsonl'), 'utf-8');
  fs.mkdirSync(path.join(tmpDir, 'data'), { recursive: true });
  fs.writeFileSync(path.join(tmpDir, 'data', 'train-00000-of-00001.jsonl'), content);

  // Write proper README with YAML frontmatter
  const readme = `---
language:
- tr
license: mit
tags:
- code
- turkish
- instruction-tuning
datasets:
- alztrk/turkish-code-instructions
---

# Turkish Code Instructions

1003 instruction-code pairs for LLM fine-tuning.

## Formats

- standard: 695
- bug_fix: 70
- code_review: 50
- code_to_desc: 43
- cross_lang: 30
- test: 45
- project: 30
- advanced: 40

## Languages

Python (240), JavaScript (156), Java (124), Go (88), SQL (88), TypeScript (87), Web (67), C++ (51), Algorithms (45), Rust (37), Knowledge (20)

## Usage

\`\`\`python
from datasets import load_dataset
dataset = load_dataset("alztrk/turkish-code-instructions")
\`\`\`
`;
  fs.writeFileSync(path.join(tmpDir, 'README.md'), readme);

  // Push
  run('git add -A');
  run('git commit -m "Initial upload: 1003 Turkish code instruction pairs"');
  run('git branch -M main');
  run('git push -u origin main --force');

  console.log('Done: https://huggingface.co/datasets/' + repoName);

} catch (e) {
  console.error('Error:', e.message);
} finally {
  try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch {}
}
