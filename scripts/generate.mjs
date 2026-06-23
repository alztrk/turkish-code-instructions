import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { execSync } from 'child_process';

const config = JSON.parse(readFileSync('config.json', 'utf-8'));
const knowledgeIndex = JSON.parse(readFileSync('templates/knowledge/knowledge_index.json', 'utf-8'));
const knowledgeDir = 'templates/knowledge';

const LANG_FILE_MAP = {
  python: 'python.json',
  javascript: 'javascript.json',
  typescript: 'typescript.json',
  java: 'java.json',
  cpp: 'cpp.json',
  go: 'go.json',
  rust: 'rust.json',
  sql: 'sql.json',
  web: 'web.json',
  algorithms: 'algorithms.json'
};

function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }

function loadTemplates(lang) {
  const file = `templates/${LANG_FILE_MAP[lang]}`;
  const data = JSON.parse(readFileSync(file, 'utf-8'));
  return data;
}

function fillPattern(pattern, slots) {
  let result = pattern;
  for (const [key, values] of Object.entries(slots)) {
    const placeholder = `{${key}}`;
    if (result.includes(placeholder)) {
      result = result.replace(placeholder, Array.isArray(values) ? pick(values) : values);
    }
  }
  return result;
}

function generateInstructions(lang) {
  const data = loadTemplates(lang);
  const instructions = [];

  // Template-based generation
  data.templates.forEach(t => {
    const count = Math.floor(config.target_per_language / data.templates.length / 2);
    for (let i = 0; i < count; i++) {
      instructions.push({
        instruction: fillPattern(t.pattern, t.slots),
        language: lang,
        category: lang,
        type: 'template'
      });
    }
  });

  // Direct instructions
  data.direct_instructions.forEach(i => {
    if (instructions.length < config.target_per_language) {
      instructions.push({ instruction: i, language: lang, category: lang, type: 'direct' });
    }
  });

  return instructions.sort(() => Math.random() - 0.5).slice(0, config.target_per_language);
}

function generateKnowledgeInstructions() {
  const instructions = [];
  const langs = knowledgeIndex.language_map;

  knowledgeIndex.knowledge_instructions.forEach(ki => {
    for (const [displayName, fileKey] of Object.entries(langs)) {
      const filePath = `${knowledgeDir}/${ki.file.replace('{lang}', fileKey)}`;
      try {
        const content = readFileSync(filePath, 'utf-8');
        const sections = content.split('## ');
        let response = '';
        if (ki.source === 'Genel Bakis') {
          response = content.split('##')[0] + (sections.find(s => s.includes('Genel Bakis')) || '');
        } else {
          const section = sections.find(s => s.startsWith(ki.source));
          if (section) response = '## ' + section;
        }
        if (response) {
          instructions.push({
            instruction: ki.pattern.replace('{language}', displayName),
            code: response.trim(),
            language: fileKey,
            category: 'knowledge',
            type: 'knowledge'
          });
        }
      } catch {}
    }
  });

  return instructions;
}

function buildPrompt(instruction) {
  if (instruction.type === 'knowledge') {
    return `Asagidaki soruyu detayli sekilde cevapla:\n\nSoru: ${instruction.instruction}\n\nCevap:`;
  }
  return `Asagidaki istegi dikkatlice oku ve sadece kod ile cevapla. Kod aciklamasi, yorum veya fazladan metin ekleme. SADECE KOD.\n\nDil: ${instruction.language}\nIstek: ${instruction.instruction}\n\nKod:`;
}

function generateBatch(batch) {
  const prompts = batch.map(b => buildPrompt(b));
  const input = prompts.join('\n---NEXT---\n');

  const { command, args, type } = config.model;
  let cmd;
  if (type === 'ollama') {
    cmd = `echo ${JSON.stringify(input)} | ${command} ${args.join(' ')}`;
  } else if (type === 'pipe') {
    cmd = `${command} ${args.join(' ')} "${input}"`;
  } else {
    cmd = `echo ${JSON.stringify(input)} | ${command}`;
  }

  const output = execSync(cmd, { encoding: 'utf-8', timeout: config.model.timeout || 300000, shell: true });
  const responses = output.split('---NEXT---').filter(r => r.trim());

  return batch.map((item, i) => ({
    instruction: item.instruction,
    response: (responses[i] || '').trim(),
    language: item.language,
    category: item.category,
    type: item.type
  }));
}

// Config
config.target_per_language = Math.floor((config.output.total || 10000) / Object.keys(LANG_FILE_MAP).length);
const languages = Object.keys(LANG_FILE_MAP);

console.log(`Target per language: ${config.target_per_language}`);
console.log(`Languages: ${languages.length}`);

// Generate instruction pool
let pool = [];
languages.forEach(lang => {
  pool.push(...generateInstructions(lang));
});
pool.push(...generateKnowledgeInstructions());
pool = pool.sort(() => Math.random() - 0.5);

console.log(`Total instructions to generate: ${pool.length}`);

// Generate in batches
let dataset = [];
let batchNum = 0;
const BATCH_SIZE = config.output.batch_size || 25;

for (let i = 0; i < pool.length; i += BATCH_SIZE) {
  const batch = pool.slice(i, i + BATCH_SIZE);
  console.log(`Generating batch ${batchNum + 1} (${batch.length} items)...`);
  try {
    const results = generateBatch(batch);
    dataset.push(...results);
    const dir = `${config.output.dir}/batch_${String(batchNum).padStart(4, '0')}`;
    mkdirSync(dir, { recursive: true });
    writeFileSync(`${dir}/data.jsonl`, results.map(d => JSON.stringify(d)).join('\n'));
    console.log(`  Saved batch_${batchNum}`);
  } catch (e) {
    console.error(`  Batch ${batchNum} failed:`, e.message);
  }
  batchNum++;
}

// Save combined
writeFileSync(`${config.output.dir}/dataset.jsonl`, dataset.map(d => JSON.stringify(d)).join('\n'));
console.log(`\nDone! Generated ${dataset.length} items`);
console.log(`Saved to ${config.output.dir}/`);
