// Test uretim scripti
// Kullanim: node scripts/generate-test.js
// output: test_output/format_adi.json (JSONL)

const fs = require('fs');

const TARGET = 50; // once 50 test edelim
const outputDir = 'test_output';

if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir);

function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }

// ---- TEST FORMATI ----
const testTemplates = [
  // Python test templates
  {
    patterns: [
      'Asagidaki {func} icin unit test yaz',
      '{func} fonksiyonunu test eden kod yaz',
      '{func} icin pytest ile test yaz',
      '{func} fonksiyonunun dogru calistigini kontrol eden test yaz'
    ],
    slots: {
      func: ['topla', 'cikar', 'carp', 'bol', 'faktoriyel', 'fibonacci', 'palindrom_mu', 'asal_mi', 'ters_cevir', 'tek_mi', 'cift_mi', 'buyuk_harf_yap', 'kucuk_harf_yap', 'ortalamabul', 'maksimum_bul', 'minimum_bul', 'uzunluk_bul', 'birlestir', 'tekrar_eden_sil', 'sirala']
    },
    language: 'python',
    generateResponse: (slots) => {
      const fn = slots.func;
      const tests = [];
      if (fn === 'topla') {
        tests.push({ args: '(2, 3)', expected: '5' });
        tests.push({ args: '(-1, 1)', expected: '0' });
        tests.push({ args: '(0, 0)', expected: '0' });
      } else if (fn === 'faktoriyel') {
        tests.push({ args: '(0)', expected: '1' });
        tests.push({ args: '(5)', expected: '120' });
        tests.push({ args: '(3)', expected: '6' });
      } else if (fn === 'fibonacci') {
        tests.push({ args: '(0)', expected: '0' });
        tests.push({ args: '(1)', expected: '1' });
        tests.push({ args: '(10)', expected: '55' });
      } else if (fn === 'palindrom_mu') {
        tests.push({ args: '("kek")', expected: 'True' });
        tests.push({ args: '("merhaba")', expected: 'False' });
        tests.push({ args: '("")', expected: 'True' });
      } else if (fn === 'asal_mi') {
        tests.push({ args: '(7)', expected: 'True' });
        tests.push({ args: '(4)', expected: 'False' });
        tests.push({ args: '(1)', expected: 'False' });
      } else if (fn === 'ters_cevir') {
        tests.push({ args: '("abc")', expected: '"cba"' });
        tests.push({ args: '("")', expected: '""' });
        tests.push({ args: '("a")', expected: '"a"' });
      } else {
        tests.push({ args: '()', expected: 'None' });
        tests.push({ args: '()', expected: 'None' });
        tests.push({ args: '()', expected: 'None' });
      }
      let code = `def test_${fn}():\n`;
      tests.forEach(t => {
        code += `    assert ${fn}${t.args} == ${t.expected}\n`;
      });
      code += `    print('test_${fn}: OK')\n`;
      return code;
    }
  },
  // JavaScript test templates
  {
    patterns: [
      'Asagidaki {func} fonksiyonu icin Jest testi yaz',
      '{func} icin birim test yaz (JavaScript)',
      '{func} fonksiyonunu test et'
    ],
    slots: {
      func: ['topla', 'carp', 'tersCevir', 'filtrele', 'buyukHarfeCevir', 'diziSirala', 'tekSayilariBul', 'ortalamaHesapla', 'enBuyukBul', 'kareAl', 'kucukHarfeCevir', 'birlestir', 'terstenYaz', 'karakterSayisi', 'kelimeSayisi']
    },
    language: 'javascript',
    generateResponse: (slots) => {
      const fn = slots.func;
      return `test('${fn} testi', () => {\n  expect(${fn}(2, 3)).toBe(5);\n  expect(${fn}(-1, 1)).toBe(0);\n  expect(${fn}(0, 0)).toBe(0);\n});`;
    }
  }
];

// ---- OUTPUT_PREDICTION FORMATI ----
const predictionTemplates = [
  {
    patterns: [
      'Su kodun ciktisi nedir?\n{kod}',
      'Bu kod ne yazdirir?\n{kod}'
    ],
    slots: {
      kod: [
        'print(2 + 3 * 4)',
        'print(2 ** 10)',
        'print("Merhaba " + "Dunya")',
        'print([1, 2, 3][1])',
        'print(len("istanbul"))',
        'print(list(range(5)))',
        'print(10 / 3)',
        'print(10 // 3)',
        'print(10 % 3)',
        "print('abc' * 3)",
      ]
    },
    language: 'python',
    generateResponse: (slots) => {
      const kod = slots.kod;
      if (kod.includes('2 + 3 * 4')) return '14';
      if (kod.includes('2 ** 10')) return '1024';
      if (kod.includes('Merhaba')) return 'Merhaba Dunya';
      if (kod.includes('[1, 2, 3][1]')) return '2';
      if (kod.includes('len("istanbul")')) return '7';
      if (kod.includes('list(range(5))')) return '[0, 1, 2, 3, 4]';
      if (kod.includes('10 / 3')) return '3.3333333333333335';
      if (kod.includes('10 // 3')) return '3';
      if (kod.includes('10 % 3')) return '1';
      if (kod.includes("'abc' * 3")) return 'abcabcabc';
      return '';
    }
  }
];

// ---- GENERATE ----
const formats = [
  { name: 'test', templates: testTemplates, target: TARGET },
  { name: 'output_prediction', templates: predictionTemplates, target: TARGET }
];

formats.forEach(format => {
  const entries = [];
  const { templates, target, name } = format;

  while (entries.length < target) {
    const tmpl = pick(templates);
    const pattern = pick(tmpl.patterns);
    const slots = {};
    Object.entries(tmpl.slots).forEach(([key, vals]) => {
      slots[key] = pick(vals);
    });

    let instruction = pattern;
    Object.entries(slots).forEach(([key, val]) => {
      instruction = instruction.replace('{' + key + '}', val);
    });

    const response = tmpl.generateResponse(slots);

    entries.push({
      instruction,
      response,
      language: tmpl.language,
      category: name,
      type: 'generated',
      format: name
    });
  }

  const filePath = `${outputDir}/${name}.jsonl`;
  fs.writeFileSync(filePath, entries.map(e => JSON.stringify(e)).join('\n'));
  console.log(`${name}: ${entries.length} kayit -> ${filePath}`);
});

console.log('\nTest dosyalari olusturuldu. Incelemek icin:');
console.log('  notepad test_output/test.jsonl');
console.log('  notepad test_output/output_prediction.jsonl');
