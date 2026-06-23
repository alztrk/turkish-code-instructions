const fs = require('fs');
const token = process.env.HF_TOKEN;
const name = 'alztrk/turkish-code-instructions';

async function run() {
  const content = fs.readFileSync('output/dataset.jsonl', 'utf-8');

  const create = await fetch('https://huggingface.co/api/repos/create', {
    method: 'POST',
    headers: { 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json' },
    body: JSON.stringify({ type: 'dataset', name, license: 'mit', private: false })
  });
  if (!create.ok && create.status !== 409) {
    console.log('Error:', await create.text());
    return;
  }
  console.log('Repo ready');

  const commit = await fetch('https://huggingface.co/api/datasets/' + name + '/commit', {
    method: 'POST',
    headers: { 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      message: 'Initial upload of 1003 Turkish code instruction pairs',
      operations: [{ op: 'add-or-update', path: 'data/train-00000-of-00001.jsonl', content }]
    })
  });
  if (commit.ok) {
    console.log('Uploaded!');
    console.log('Usage: load_dataset("' + name + '")');
  } else {
    const err = await commit.text();
    console.log('Error:', err);
  }
}
run();
