/**
 * HuggingFace'e yukleme scripti.
 * Kullanim: HF_TOKEN=hf_your_token node scripts/upload-to-hf.js
 */

const fs = require('fs');
const path = require('path');

const HF_TOKEN = process.env.HF_TOKEN;
const DATASET_NAME = 'alztrk/turkish-code-instructions';
const FILE_PATH = 'output/dataset.jsonl';

async function upload() {
  if (!HF_TOKEN) {
    console.log('HF_TOKEN ortam degiskeni gerekli.');
    console.log('Al: https://huggingface.co/settings/tokens');
    console.log('Kullan: $env:HF_TOKEN=\"hf_...\" ; node scripts/upload-to-hf.js');
    return;
  }

  const content = fs.readFileSync(FILE_PATH, 'utf-8');
  const lines = content.trim().split('\n').length;

  // 1. Dataset olustur
  const createRes = await fetch(`https://huggingface.co/api/datasets/${DATASET_NAME}`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${HF_TOKEN}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      private: false,
      license: 'mit',
      description: `Turkish code instruction dataset. ${lines} examples across 8 formats and 11 languages.`
    })
  });

  if (!createRes.ok && createRes.status !== 409) {
    console.log('Dataset olusturulamadi:', await createRes.text());
    return;
  }
  console.log(`Dataset hazir: https://huggingface.co/datasets/${DATASET_NAME}`);

  // 2. Dosyayi yukle
  const uploadRes = await fetch(`https://huggingface.co/api/datasets/${DATASET_NAME}/upload`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${HF_TOKEN}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      path: 'data/train-00000-of-00001.jsonl',
      content: content,
      split: 'train'
    })
  });

  if (uploadRes.ok) {
    console.log('Dosya yuklendi!');
    console.log(`Kullanim: datasets.load_dataset("${DATASET_NAME}")`);
  } else {
    console.log('Yukleme hatasi:', await uploadRes.text());
  }
}

upload();
