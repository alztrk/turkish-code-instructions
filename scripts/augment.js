const fs = require('fs');
const path = require('path');

const datasetPath = path.join(__dirname, '..', 'output', 'dataset.jsonl');

const turkishMap = [
    [/\basagidaki\b/g, "aşağıdaki"],
    [/\bAsagidaki\b/g, "Aşağıdaki"],
    [/\bfonksiyon\b/g, "fonksiyon"],
    [/\bfonksiyonu\b/g, "fonksiyonu"],
    [/\bicin\b/g, "için"],
    [/\bIcin\b/g, "İçin"],
    [/\byaz\b/g, "yaz"],
    [/\bYaz\b/g, "yaz"],
    [/\bhatayi\b/g, "hatayı"],
    [/\bduzelt\b/g, "düzelt"],
    [/\bduzelt:\b/g, "düzelt:"],
    [/\bkarmasikligi\b/g, "karmaşıklığı"],
    [/\bKarmasikligi\b/g, "karmaşıklığı"],
    [/\bnedir\b/g, "nedir"],
    [/\bciktisi\b/g, "çıktısı"],
    [/\bCiktisi\b/g, "Çıktısı"],
    [/\bnasil\b/g, "nasıl"],
    [/\bNasil\b/g, "Nasıl"],
    [/\bcozulur\b/g, "çözülür"],
    [/\bcozumu\b/g, "çözümü"],
    [/\bdegisken\b/g, "değişken"],
    [/\bdegiskeni\b/g, "değişkeni"],
    [/\bdeger\b/g, "değer"],
    [/\bdegeri\b/g, "değeri"],
    [/\bdegerini\b/g, "değerini"],
    [/\bcalisan\b/g, "çalışan"],
    [/\bcalisir\b/g, "çalışır"],
    [/\bprogramini\b/g, "programını"],
    [/\bprogrami\b/g, "programı"],
    [/\byazdiran\b/g, "yazdıran"],
    [/\byazdir\b/g, "yazdır"],
    [/\bsayinin\b/g, "sayının"],
    [/\bsayi\b/g, "sayı"],
    [/\bsayilari\b/g, "sayıları"],
    [/\bkullanicidan\b/g, "kullanıcıdan"],
    [/\bKullanicidan\b/g, "Kullanıcıdan"],
    [/\balinan\b/g, "alınan"],
    [/\btoplamini\b/g, "toplamını"],
    [/\bkarakter\b/g, "karakter"],
    [/\bkarakteri\b/g, "karakteri"],
    [/\bkontrol\b/g, "kontrol"],
    [/\beden\b/g, "eden"],
    [/\bdiziyi\b/g, "diziyi"],
    [/\bceviren\b/g, "çeviren"],
    [/\ben\b/g, "en"],
    [/\bbuyuk\b/g, "büyük"],
    [/\bkucuk\b/g, "küçük"],
    [/\bsirali\b/g, "sıralı"],
    [/\beleman\b/g, "eleman"],
    [/\belemanli\b/g, "elemanlı"],
    [/\belemanini\b/g, "elemanını"],
    [/\bulas\b/g, "ulaş"],
    [/\bgosteren\b/g, "gösteren"],
    [/\bhesaplayan\b/g, "hesaplayan"],
    [/\buret\b/g, "üret"],
    [/\bureten\b/g, "üreten"],
    [/\bdongusu\b/g, "döngüsü"],
    [/\bdongu\b/g, "döngü"],
    [/\bic\b/g, "iç"],
    [/\bice\b/g, "içe"],
    [/\bturrkce\b/g, "Türkçe"],
    [/\bturkce\b/g, "Türkçe"],
    [/\bTurkce\b/g, "Türkçe"]
];

function makeTurkish(text) {
    let modified = text;
    for (const [regex, replacement] of turkishMap) {
        modified = modified.replace(regex, replacement);
    }
    return modified;
}

function augment() {
    if (!fs.existsSync(datasetPath)) {
        console.error("Dataset not found at: " + datasetPath);
        return;
    }

    const data = fs.readFileSync(datasetPath, 'utf8');
    const lines = data.split('\n').filter(line => line.trim() !== '');
    
    const entries = lines.map(line => JSON.parse(line));
    console.log(`Original entries count: ${entries.length}`);

    const seenInstructions = new Set(entries.map(e => e.instruction));
    const augmentedEntries = [];

    for (const entry of entries) {
        const origInstr = entry.instruction;
        const turkishInstr = makeTurkish(origInstr);

        if (turkishInstr !== origInstr && !seenInstructions.has(turkishInstr)) {
            const newEntry = { ...entry };
            newEntry.instruction = turkishInstr;
            newEntry.type = "augmented_turkish";
            augmentedEntries.push(newEntry);
            seenInstructions.add(turkishInstr);
        }
    }

    console.log(`Generated ${augmentedEntries.length} new entries with proper Turkish characters.`);

    const allEntries = entries.concat(augmentedEntries);
    const outputData = allEntries.map(e => JSON.stringify(e)).join('\n') + '\n';

    fs.writeFileSync(datasetPath, outputData, 'utf8');
    console.log(`Total entries now: ${allEntries.length}`);
}

augment();
