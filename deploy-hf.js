const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const token = process.env.HF_TOKEN;
const repo = 'alztrk/turkish-code-instructions';
const repoUrl = 'https://USER:' + token + '@huggingface.co/datasets/' + repo;
const tmp = path.join(os.tmpdir(), 'hf-' + Date.now());

function run(cmd) { return execSync(cmd, { encoding: 'utf-8', shell: true, cwd: tmp }); }

fs.mkdirSync(tmp, { recursive: true });
run('git init');
run('git config user.email "alztrk@users.noreply.github.com"');
run('git config user.name "alztrk"');
run('git remote add origin ' + repoUrl);

const content = fs.readFileSync('output/dataset.jsonl', 'utf-8');
fs.mkdirSync(path.join(tmp, 'data'), { recursive: true });
fs.writeFileSync(path.join(tmp, 'data', 'train-00000-of-00001.jsonl'), content);

const readme = `---
language:
- tr
license: mit
tags:
- code
- turkish
- instruction-tuning
---
# Turkish Code Instructions
Turkish instruction-code pairs for LLM fine-tuning.`;
fs.writeFileSync(path.join(tmp, 'README.md'), readme);

run('git add -A');
run('git commit -m "Upload dataset"');
run('git branch -M main');
run('git push -u origin main --force');

console.log('Done: https://huggingface.co/datasets/' + repo);
try { fs.rmSync(tmp, { recursive: true, force: true }); } catch {}
