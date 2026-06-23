const fs = require('fs');
const path = require('path');

const datasetPath = path.join(__dirname, '..', 'output', 'dataset.jsonl');

function validate() {
    if (!fs.existsSync(datasetPath)) {
        console.error("Dataset not found!");
        return;
    }

    const data = fs.readFileSync(datasetPath, 'utf8');
    const lines = data.split('\n').filter(line => line.trim() !== '');
    
    let errors = 0;
    let warnings = 0;
    const seenInstructions = new Set();
    const duplicates = [];

    console.log(`=== Dataset Validation Started ===`);
    console.log(`Total lines to validate: ${lines.length}\n`);

    lines.forEach((line, index) => {
        const lineNum = index + 1;
        let entry;

        // Rule 1: Must be valid JSON
        try {
            entry = JSON.parse(line);
        } catch (e) {
            console.error(`[ERROR] Line ${lineNum}: Invalid JSON syntax.`);
            errors++;
            return;
        }

        // Rule 2: Required keys
        const requiredKeys = ['instruction', 'response', 'language'];
        for (const key of requiredKeys) {
            if (!entry[key]) {
                console.error(`[ERROR] Line ${lineNum}: Missing required key "${key}".`);
                errors++;
            }
        }

        if (entry.instruction && entry.response) {
            // Rule 3: Check for empty values
            if (entry.instruction.trim() === '') {
                console.error(`[ERROR] Line ${lineNum}: Empty instruction.`);
                errors++;
            }
            if (entry.response.trim() === '') {
                console.error(`[ERROR] Line ${lineNum}: Empty response.`);
                errors++;
            }

            // Rule 4: Duplicate checks
            const key = entry.instruction + "|||" + entry.response;
            if (seenInstructions.has(key)) {
                duplicates.push(lineNum);
                warnings++;
            } else {
                seenInstructions.add(key);
            }
        }
    });

    console.log(`\n=== Validation Summary ===`);
    console.log(`Total Entries: ${lines.length}`);
    console.log(`Errors: ${errors}`);
    console.log(`Duplicate warnings: ${duplicates.length}`);
    if (duplicates.length > 0) {
        console.log(`Duplicate lines: ${duplicates.slice(0, 10).join(', ')}${duplicates.length > 10 ? '...' : ''}`);
    }

    if (errors === 0) {
        console.log("\nResult: PASSED (No critical structural errors found)");
    } else {
        console.log("\nResult: FAILED (Critical errors must be resolved)");
    }
}

validate();
