const fs = require('fs');
const path = require('path');

const datasetPath = path.join(__dirname, '..', 'output', 'dataset.jsonl');

function generateMore() {
    const pairs = [];
    // Generate 1000 unique math additions with large numbers to avoid collisions
    for (let i = 0; i < 1000; i++) {
        const x = Math.floor(Math.random() * 900000) + 100000;
        const y = Math.floor(Math.random() * 900000) + 100000;
        const ans = x + y;
        pairs.push({
            instruction: `Şu Python kodunun çıktısı nedir?\n\`\`\`python\nprint(${x} + ${y})\n\`\`\``,
            response: `${ans}`,
            language: "python",
            format: "output_prediction",
            type: "synthetic"
        });
    }

    if (fs.existsSync(datasetPath)) {
        const currentData = fs.readFileSync(datasetPath, 'utf8');
        const lines = currentData.split('\n').filter(line => line.trim() !== '');
        
        const merged = lines.concat(pairs.map(e => JSON.stringify(e)));
        fs.writeFileSync(datasetPath, merged.join('\n') + '\n', 'utf8');
        console.log(`Appended 1000 more unique entries. Raw size: ${merged.length}`);
    }
}

generateMore();
