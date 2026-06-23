const fs = require('fs');
const path = require('path');

const datasetPath = path.join(__dirname, '..', 'output', 'dataset.jsonl');

function generateMoreMath() {
    const pairs = [];
    // 8000 unique double-variable math equations for LLM logic tracing
    for (let i = 0; i < 8000; i++) {
        const x = Math.floor(Math.random() * 50000) + 1000;
        const y = Math.floor(Math.random() * 50000) + 1000;
        const ans = x + y;
        pairs.push({
            instruction: `Şu Python kodunun çıktısı nedir?\n\`\`\`python\nsayi1 = ${x}\nsayi2 = ${y}\ntoplam = sayi1 + sayi2\nprint(toplam)\n\`\`\``,
            response: `${ans}`,
            language: "python",
            format: "output_prediction",
            type: "synthetic_massive_2"
        });
    }
    return pairs;
}

function run() {
    console.log("Generating massive part 2 data...");
    const math = generateMoreMath();
    console.log(`Generated ${math.length} new entries.`);

    if (fs.existsSync(datasetPath)) {
        const currentData = fs.readFileSync(datasetPath, 'utf8');
        const lines = currentData.split('\n').filter(line => line.trim() !== '');
        
        const merged = lines.concat(math.map(e => JSON.stringify(e)));
        fs.writeFileSync(datasetPath, merged.join('\n') + '\n', 'utf8');
        console.log(`Successfully merged. New total size: ${merged.length}`);
    }
}

run();
