import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { execSync } from 'child_process';

const instructions = JSON.parse(readFileSync('templates/instructions.json', 'utf-8'));
const values = JSON.parse(readFileSync('templates/values.json', 'utf-8'));

const BATCH_SIZE = 50;
const TARGET_TOTAL = 2000;
const languages = Object.keys(instructions);
let dataset = [];
let batchNum = 0;

function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }

function fillTemplate(template, lang) {
  const pool = values.topics[lang] || {};
  let result = template;
  for (const [key, val] of Object.entries(pool)) {
    const placeholder = `{${key}}`;
    if (result.includes(placeholder)) {
      const replacement = Array.isArray(val) ? pick(val) : val;
      result = result.replace(placeholder, replacement);
    }
  }
  return result;
}

function buildPrompt(instruction, lang) {
  return `Asagidaki istegi dikkatlice oku ve sadece kod ile cevapla. Kod aciklamasi, yorum veya fazladan metin ekleme. SADECE KOD.

Dil: ${lang}
Istek: ${instruction}

Kod:`;
}

function generateBatch(batch) {
  const prompts = batch.map(b => buildPrompt(b.instruction, b.language));
  const input = prompts.join('\n---NEXT---\n');

  const modelPath = 'D:\\path\\to\\model.exe';
  const cmd = `echo ${JSON.stringify(input)} | ${modelPath}`;

  try {
    const output = execSync(cmd, { encoding: 'utf-8', timeout: 120000, shell: true });
    const responses = output.split('---NEXT---').filter(r => r.trim());

    return batch.map((item, i) => ({
      instruction: item.instruction,
      code: (responses[i] || '').trim(),
      language: item.language,
      category: item.category,
      source: 'synthetic'
    }));
  } catch (e) {
    console.error('Generation error:', e.message);
    return batch.map(item => ({
      instruction: item.instruction,
      code: '',
      language: item.language,
      category: item.category,
      source: 'synthetic'
    }));
  }
}

function saveBatch(batch, num) {
  const dir = `output/batch_${String(num).padStart(4, '0')}`;
  mkdirSync(dir, { recursive: true });
  writeFileSync(`${dir}/data.jsonl`, batch.map(d => JSON.stringify(d)).join('\n'));
  console.log(`Saved: batch_${num} (${batch.length} items)`);
}

let queue = [];
languages.forEach(lang => {
  const cat = lang;
  const pool = instructions[lang];
  const count = Math.max(10, Math.floor(TARGET_TOTAL / languages.length / pool.length));

  for (let i = 0; i < count; i++) {
    pool.forEach(template => {
      const instruction = fillTemplate(template, lang);
      queue.push({ instruction, language: lang, category: cat });
    });
  }
});

queue = queue.sort(() => Math.random() - 0.5).slice(0, TARGET_TOTAL);
console.log(`Total items to generate: ${queue.length}`);

for (let i = 0; i < queue.length; i += BATCH_SIZE) {
  const batch = queue.slice(i, i + BATCH_SIZE);
  const results = generateBatch(batch);
  dataset.push(...results);
  batchNum++;
  saveBatch(results, batchNum);
}

writeFileSync('output/dataset.jsonl', dataset.map(d => JSON.stringify(d)).join('\n'));
console.log(`\nDone! Total: ${dataset.length} items saved to output/`);
console.log(`Languages: ${[...new Set(dataset.map(d => d.language))].join(', ')}`);
