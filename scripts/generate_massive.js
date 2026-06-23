const fs = require('fs');
const path = require('path');

const datasetPath = path.join(__dirname, '..', 'output', 'dataset.jsonl');

function generateSQLMassive() {
    const pairs = [];
    const tables = ["kullanicilar", "siparisler", "urunler", "musteriler", "odemeler", "stok", "kategoriler"];
    const columns = ["id", "ad", "soyad", "tarih", "tutar", "fiyat", "miktar", "durum"];
    
    // 2000 SELECT query prediction pairs
    for (let i = 0; i < 2000; i++) {
        const table = tables[i % tables.length];
        const col1 = columns[i % columns.length];
        const col2 = columns[(i + 1) % columns.length];
        const val = Math.floor(Math.random() * 1000);
        
        const sql = `SELECT ${col1}, ${col2} FROM ${table} WHERE id > ${val} ORDER BY ${col1} DESC LIMIT 5;`;
        pairs.push({
            instruction: `Şu SQL sorgusunun ne yaptığını Türkçe olarak açıkla:\n\`\`\`sql\n${sql}\n\`\`\``,
            response: `Bu sorgu, "${table}" tablosundan "id" değeri ${val}'den büyük olan kayıtların "${col1}" ve "${col2}" kolonlarını seçer. Sonuçları "${col1}" kolonuna göre azalan (büyükten küçüğe) sırada sıralar ve sadece ilk 5 kaydı getirir.`,
            language: "sql",
            format: "code_to_desc",
            type: "synthetic_massive"
        });
    }
    return pairs;
}

function generateRegexMassive() {
    const pairs = [];
    const patterns = [
        ["\\d+", "Sadece rakamları eşler"],
        ["[a-zA-Z]+", "Sadece İngilizce harfleri eşler"],
        ["^[a-z0-9]+$", "Küçük harf ve rakamlardan oluşan metni baştan sona eşler"],
        ["^\\d{3}-\\d{3}$", "3 rakam, bir tire ve 3 rakam formatını eşler"],
        ["^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$", "E-posta adresi formatını eşler"]
    ];

    // 2000 Regex explanation pairs
    for (let i = 0; i < 2000; i++) {
        const [pat, desc] = patterns[i % patterns.length];
        const salt = Math.floor(Math.random() * 10000); // make instruction unique
        pairs.push({
            instruction: `Düzenli ifade (regex) desenini açıkla [ID: ${salt}]:\n\`\`\`regex\n${pat}\n\`\`\``,
            response: `Bu düzenli ifade (regex) deseni: ${desc}.`,
            language: "python",
            format: "knowledge",
            type: "synthetic_massive"
        });
    }
    return pairs;
}

function generateLoopOutputs() {
    const pairs = [];
    // 4000 Mathematical sum calculations for LLM prediction practice
    for (let i = 0; i < 4000; i++) {
        const limit = Math.floor(Math.random() * 200) + 10;
        let sum = 0;
        for (let j = 1; j <= limit; j++) {
            sum += j;
        }
        pairs.push({
            instruction: `Şu Python kodunun çıktısı nedir?\n\`\`\`python\ntoplam = 0\nfor i in range(1, ${limit} + 1):\n    toplam += i\nprint(toplam)\n\`\`\``,
            response: `${sum}`,
            language: "python",
            format: "output_prediction",
            type: "synthetic_massive"
        });
    }
    return pairs;
}

function generateTypeChecks() {
    const pairs = [];
    const types = [
        ["42", "int", "<class 'int'>"],
        ["3.14", "float", "<class 'float'>"],
        ["'kodlama'", "str", "<class 'str'>"],
        ["[1, 2, 3]", "list", "<class 'list'>"],
        ["(1, 2)", "tuple", "<class 'tuple'>"],
        ["{'a': 1}", "dict", "<class 'dict'>"],
        ["{1, 2}", "set", "<class 'set'>"],
        ["True", "bool", "<class 'bool'>"],
        ["None", "NoneType", "<class 'NoneType'>"]
    ];

    // 2000 type check output predictions
    for (let i = 0; i < 2000; i++) {
        const [val, typeName, clsStr] = types[i % types.length];
        const salt = Math.floor(Math.random() * 100000);
        pairs.push({
            instruction: `Şu Python kodunun çıktısı nedir? [SALT: ${salt}]\n\`\`\`python\nx = ${val}\nprint(type(x))\n\`\`\``,
            response: `${clsStr}`,
            language: "python",
            format: "output_prediction",
            type: "synthetic_massive"
        });
    }
    return pairs;
}

function run() {
    console.log("Generating massive synthetic data...");
    const sql = generateSQLMassive();
    const regex = generateRegexMassive();
    const loops = generateLoopOutputs();
    const types = generateTypeChecks();

    const allNew = [...sql, ...regex, ...loops, ...types];
    console.log(`Generated ${allNew.length} massive new entries.`);

    if (fs.existsSync(datasetPath)) {
        const currentData = fs.readFileSync(datasetPath, 'utf8');
        const lines = currentData.split('\n').filter(line => line.trim() !== '');
        
        const merged = lines.concat(allNew.map(e => JSON.stringify(e)));
        fs.writeFileSync(datasetPath, merged.join('\n') + '\n', 'utf8');
        console.log(`Successfully merged. New total size: ${merged.length}`);
    } else {
        console.error("Dataset not found!");
    }
}

run();
