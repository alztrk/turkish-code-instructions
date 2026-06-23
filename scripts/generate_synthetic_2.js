const fs = require('fs');
const path = require('path');

const datasetPath = path.join(__dirname, '..', 'output', 'dataset.jsonl');

const turkishWords = [
    "veri", "tabani", "sistem", "agac", "bellek", "islemci", "degisken", "dongu", 
    "fonksiyon", "nesne", "sinif", "siralama", "arama", "yigin", "kuyruk", "liste"
];

function generatePythonDict() {
    const pairs = [];
    // 1. print(dict[key])
    for (let i = 0; i < 600; i++) {
        const dict = {
            "a": Math.floor(Math.random() * 100),
            "b": Math.floor(Math.random() * 100),
            "c": Math.floor(Math.random() * 100)
        };
        const keys = ["a", "b", "c"];
        const key = keys[Math.floor(Math.random() * 3)];
        const ans = dict[key];
        pairs.push({
            instruction: `Şu Python kodunun çıktısı nedir?\n\`\`\`python\nveri = ${JSON.stringify(dict)}\nprint(veri["${key}"])\n\`\`\`,`,
            response: `${ans}`,
            language: "python",
            format: "output_prediction",
            type: "synthetic"
        });
    }

    // 2. Python slicing: "word"[i:j]
    for (let i = 0; i < 600; i++) {
        const word = turkishWords[i % turkishWords.length];
        const start = Math.floor(Math.random() * (word.length - 2));
        const end = start + Math.floor(Math.random() * (word.length - start - 1)) + 1;
        const ans = word.slice(start, end);
        pairs.push({
            instruction: `Şu Python kodunun çıktısı nedir?\n\`\`\`python\nkelime = "${word}"\nprint(kelime[${start}:${end}])\n\`\`\``,
            response: `${ans}`,
            language: "python",
            format: "output_prediction",
            type: "synthetic"
        });
    }

    return pairs;
}

function generateJSSlicing() {
    const pairs = [];
    for (let i = 0; i < 600; i++) {
        const word = turkishWords[i % turkishWords.length];
        const start = Math.floor(Math.random() * (word.length - 2));
        const end = start + Math.floor(Math.random() * (word.length - start - 1)) + 1;
        const ans = word.slice(start, end);
        pairs.push({
            instruction: `Şu JavaScript kodunun çıktısı nedir?\n\`\`\`javascript\nlet kelime = "${word}";\nconsole.log(kelime.slice(${start}, ${end}));\n\`\`\``,
            response: `${ans}`,
            language: "javascript",
            format: "output_prediction",
            type: "synthetic"
        });
    }
    return pairs;
}

function generateGo() {
    const pairs = [];
    for (let i = 0; i < 600; i++) {
        const x = Math.floor(Math.random() * 500);
        const y = Math.floor(Math.random() * 500);
        const ans = x + y;
        pairs.push({
            instruction: `Şu Go kodunun çıktısı nedir?\n\`\`\`go\npackage main\nimport "fmt"\nfunc main() {\n    fmt.Println(${x} + ${y})\n}\n\`\`\``,
            response: `${ans}`,
            language: "go",
            format: "output_prediction",
            type: "synthetic"
        });
    }
    return pairs;
}

function generateCPP() {
    const pairs = [];
    for (let i = 0; i < 600; i++) {
        const x = Math.floor(Math.random() * 500);
        const y = Math.floor(Math.random() * 500);
        const ans = x + y;
        pairs.push({
            instruction: `Şu C++ kodunun çıktısı nedir?\n\`\`\`cpp\n#include <iostream>\nint main() {\n    std::cout << ${x} + ${y} << std::endl;\n    return 0;\n}\n\`\`\``,
            response: `${ans}`,
            language: "cpp",
            format: "output_prediction",
            type: "synthetic"
        });
    }
    return pairs;
}

function run() {
    console.log("Generating synthetic part 2 output predictions...");
    const py = generatePythonDict();
    const js = generateJSSlicing();
    const go = generateGo();
    const cpp = generateCPP();

    const allNew = [...py, ...js, ...go, ...cpp];
    console.log(`Generated ${allNew.length} new entries (slicing, maps, etc.).`);

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
