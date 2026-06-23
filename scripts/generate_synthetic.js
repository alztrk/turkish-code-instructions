const fs = require('fs');
const path = require('path');

const datasetPath = path.join(__dirname, '..', 'output', 'dataset.jsonl');

const turkishWords = [
    "bilgisayar", "yazilim", "kodlama", "turkiye", "istanbul", "ankara", "izmir", 
    "deniz", "gunes", "bulut", "yagmur", "toprak", "agac", "cicek", "orman", 
    "kitap", "kalem", "defter", "okul", "ogrenci", "ogretmen", "sinif", "ders"
];

function generatePython() {
    const pairs = [];
    
    // 1. Addition: print(X + Y)
    for (let i = 0; i < 500; i++) {
        const x = Math.floor(Math.random() * 1000);
        const y = Math.floor(Math.random() * 1000);
        const ans = x + y;
        pairs.push({
            instruction: `Şu Python kodunun çıktısı nedir?\n\`\`\`python\nprint(${x} + ${y})\n\`\`\``,
            response: `${ans}`,
            language: "python",
            format: "output_prediction",
            type: "synthetic"
        });
        pairs.push({
            instruction: `Su Python kodunun ciktisi nedir?\n\`\`\`python\nprint(${x} + ${y})\n\`\`\``,
            response: `${ans}`,
            language: "python",
            format: "output_prediction",
            type: "synthetic_ascii"
        });
    }

    // 2. Multiplication: print(X * Y)
    for (let i = 0; i < 500; i++) {
        const x = Math.floor(Math.random() * 50) + 1;
        const y = Math.floor(Math.random() * 50) + 1;
        const ans = x * y;
        pairs.push({
            instruction: `Şu Python kodunun çıktısı nedir?\n\`\`\`python\nprint(${x} * ${y})\n\`\`\``,
            response: `${ans}`,
            language: "python",
            format: "output_prediction",
            type: "synthetic"
        });
    }

    // 3. String Length: print(len('word'))
    for (let i = 0; i < 300; i++) {
        const word = turkishWords[i % turkishWords.length] + Math.floor(Math.random() * 100);
        const ans = word.length;
        pairs.push({
            instruction: `Şu Python kodunun çıktısı nedir?\n\`\`\`python\nprint(len('${word}'))\n\`\`\``,
            response: `${ans}`,
            language: "python",
            format: "output_prediction",
            type: "synthetic"
        });
    }

    // 4. List indexing: print([A, B, C][idx])
    for (let i = 0; i < 500; i++) {
        const arr = [
            Math.floor(Math.random() * 100),
            Math.floor(Math.random() * 100),
            Math.floor(Math.random() * 100),
            Math.floor(Math.random() * 100)
        ];
        const idx = Math.floor(Math.random() * 4);
        const ans = arr[idx];
        pairs.push({
            instruction: `Şu Python kodunun çıktısı nedir?\n\`\`\`python\nprint(${JSON.stringify(arr)}[${idx}])\n\`\`\``,
            response: `${ans}`,
            language: "python",
            format: "output_prediction",
            type: "synthetic"
        });
    }

    return pairs;
}

function generateJS() {
    const pairs = [];
    
    // 1. console.log(X + Y)
    for (let i = 0; i < 500; i++) {
        const x = Math.floor(Math.random() * 1000);
        const y = Math.floor(Math.random() * 1000);
        const ans = x + y;
        pairs.push({
            instruction: `Şu JavaScript kodunun çıktısı nedir?\n\`\`\`javascript\nconsole.log(${x} + ${y});\n\`\`\``,
            response: `${ans}`,
            language: "javascript",
            format: "output_prediction",
            type: "synthetic"
        });
        pairs.push({
            instruction: `Su JavaScript kodunun ciktisi nedir?\n\`\`\`javascript\nconsole.log(${x} + ${y});\n\`\`\``,
            response: `${ans}`,
            language: "javascript",
            format: "output_prediction",
            type: "synthetic_ascii"
        });
    }

    // 2. Math.max(A, B)
    for (let i = 0; i < 500; i++) {
        const x = Math.floor(Math.random() * 1000);
        const y = Math.floor(Math.random() * 1000);
        const ans = Math.max(x, y);
        pairs.push({
            instruction: `Şu JavaScript kodunun çıktısı nedir?\n\`\`\`javascript\nconsole.log(Math.max(${x}, ${y}));\n\`\`\``,
            response: `${ans}`,
            language: "javascript",
            format: "output_prediction",
            type: "synthetic"
        });
    }

    return pairs;
}

function generateSQL() {
    const pairs = [];
    
    // 1. SELECT X + Y;
    for (let i = 0; i < 500; i++) {
        const x = Math.floor(Math.random() * 500);
        const y = Math.floor(Math.random() * 500);
        const ans = x + y;
        pairs.push({
            instruction: `Şu SQL sorgusunun çıktısı nedir?\n\`\`\`sql\nSELECT ${x} + ${y};\n\`\`\``,
            response: `${ans}`,
            language: "sql",
            format: "output_prediction",
            type: "synthetic"
        });
        pairs.push({
            instruction: `Su SQL sorgusunun ciktisi nedir?\n\`\`\`sql\nSELECT ${x} + ${y};\n\`\`\``,
            response: `${ans}`,
            language: "sql",
            format: "output_prediction",
            type: "synthetic_ascii"
        });
    }

    return pairs;
}

function generateJava() {
    const pairs = [];
    
    // 1. System.out.println(X + Y);
    for (let i = 0; i < 400; i++) {
        const x = Math.floor(Math.random() * 500);
        const y = Math.floor(Math.random() * 500);
        const ans = x + y;
        pairs.push({
            instruction: `Şu Java kodunun çıktısı nedir?\n\`\`\`java\nSystem.out.println(${x} + ${y});\n\`\`\``,
            response: `${ans}`,
            language: "java",
            format: "output_prediction",
            type: "synthetic"
        });
    }

    return pairs;
}

function run() {
    console.log("Generating synthetic output predictions...");
    const py = generatePython();
    const js = generateJS();
    const sql = generateSQL();
    const java = generateJava();

    const allNew = [...py, ...js, ...sql, ...java];
    console.log(`Generated ${allNew.length} new high-quality deterministic expression matching entries.`);

    if (fs.existsSync(datasetPath)) {
        const currentData = fs.readFileSync(datasetPath, 'utf8');
        const lines = currentData.split('\n').filter(line => line.trim() !== '');
        console.log(`Current dataset size: ${lines.length}`);
        
        const merged = lines.concat(allNew.map(e => JSON.stringify(e)));
        fs.writeFileSync(datasetPath, merged.join('\n') + '\n', 'utf8');
        console.log(`Successfully appended entries. New dataset size: ${merged.length}`);
    } else {
        console.error("Dataset file not found at " + datasetPath);
    }
}

run();
