const fs = require('fs');
const path = require('path');

const datasetPath = path.join(__dirname, '..', 'output', 'dataset.jsonl');

function deduplicate() {
    if (!fs.existsSync(datasetPath)) {
        console.error("Dataset not found!");
        return;
    }

    const data = fs.readFileSync(datasetPath, 'utf8');
    const lines = data.split('\n').filter(line => line.trim() !== '');
    
    const uniqueEntries = [];
    const seen = new Set();
    let duplicateCount = 0;

    lines.forEach(line => {
        const entry = JSON.parse(line);
        const key = entry.instruction.trim() + "|||" + entry.response.trim();
        if (seen.has(key)) {
            duplicateCount++;
        } else {
            seen.add(key);
            uniqueEntries.push(entry);
        }
    });

    if (duplicateCount > 0) {
        const outputData = uniqueEntries.map(e => JSON.stringify(e)).join('\n') + '\n';
        fs.writeFileSync(datasetPath, outputData, 'utf8');
        console.log(`Successfully removed ${duplicateCount} duplicate entries.`);
        console.log(`Unique entries remaining: ${uniqueEntries.length}`);
    } else {
        console.log("No duplicate entries found.");
    }
}

deduplicate();
