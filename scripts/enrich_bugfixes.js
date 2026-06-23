const fs = require('fs');
const path = require('path');

const datasetPath = path.join(__dirname, '..', 'output', 'dataset.jsonl');

const bugFixRules = [
    {
        pattern: /toplama\(5\)/,
        explanation: "Hata: `toplama` fonksiyonu iki parametre beklerken tek argümanla çağrılmıştı. Eksik olan ikinci argüman eklenerek düzeltildi:\n\n"
    },
    {
        pattern: /for i in range\(10\):\r?\nprint\(i\)/,
        explanation: "Hata: Python'da döngü gövdesi girintilenmediği için `IndentationError` oluşuyordu. `print` satırı girintilenerek düzeltildi:\n\n"
    },
    {
        pattern: /\[1, 2, 3\], 3/,
        explanation: "Hata: 3 elemanlı dizide 3. indekse erişilmeye çalışılıyordu. Bu durum `IndexError` hatasına yol açar. İndeks 0 tabanlı olduğu için son elemana `2` indeksiyle erişilerek düzeltildi:\n\n"
    },
    {
        pattern: /if x = 10:/,
        explanation: "Hata: Koşul ifadesinde atama operatörü (`=`) kullanılmıştı. Karşılaştırma için eşitlik operatörü (`==`) kullanılarak düzeltildi:\n\n"
    },
    {
        pattern: /selamla\(\)/,
        explanation: "Hata: `selamla` fonksiyonu bir isim parametresi beklerken argümansız çağrılmıştı. Fonksiyona değer gönderilerek düzeltildi:\n\n"
    },
    {
        pattern: /sayilar\.pop\(i\)/,
        explanation: "Hata: Döngü içerisinde diziden eleman silinmesi indeks kaymasına ve beklenmeyen sonuçlara yol açıyordu. Döngü içindeki silme işlemi kaldırılarak düzeltildi:\n\n"
    },
    {
        pattern: /str\(25\)/,
        explanation: "Hata: Metin (string) ile tam sayı (integer) doğrudan birleştirilmeye çalışılıyordu (`TypeError`). Sayı, `str()` fonksiyonuyla metne dönüştürülerek düzeltildi:\n\n"
    },
    {
        pattern: /if n < 0:\r?\n\s+return None/,
        explanation: "Hata: Negatif değerler için fonksiyonda çıkış koşulu bulunmuyordu. Bu durum sonsuz rekürsiyona (`RecursionError`) yol açıyordu. Negatif sayılar için kontrol eklenerek düzeltildi:\n\n"
    },
    {
        pattern: /from math import sqrt, pi/,
        explanation: "Hata: `pi` sabiti kullanılmak istenmiş ancak `math` kütüphanesinden içe aktarılmamıştı (`NameError`). İçe aktarma listesine eklenerek düzeltildi:\n\n"
    },
    {
        pattern: /notlar\.get\("Veli"/,
        explanation: "Hata: Sözlükte bulunmayan bir anahtara doğrudan erişilmeye çalışıldığı için `KeyError` oluşuyordu. Güvenli erişim sağlamak amacıyla `.get()` metodu kullanılarak düzeltildi:\n\n"
    },
    {
        pattern: /liste = None/,
        explanation: "Hata: Python'da varsayılan parametre olarak değiştirilebilir (mutable) bir nesne (boş liste `[]`) kullanıldığında, bu nesne tüm çağrılar arasında paylaşılır. Varsayılan değer `None` yapılıp fonksiyon içinde yeni liste oluşturularak düzeltildi:\n\n"
    },
    {
        pattern: /sayi \+= 1/,
        explanation: "Hata: `while` döngüsünde sayaç değişkeni güncellenmediği için sonsuz döngü (infinite loop) oluşuyordu. Döngü gövdesine `sayi += 1` eklenerek düzeltildi:\n\n"
    }
];

function enrich() {
    if (!fs.existsSync(datasetPath)) {
        console.error("Dataset not found!");
        return;
    }

    const data = fs.readFileSync(datasetPath, 'utf8');
    const lines = data.split('\n').filter(line => line.trim() !== '');
    
    let enrichedCount = 0;
    
    const enrichedLines = lines.map(line => {
        const entry = JSON.parse(line);
        
        if (entry.format === 'bug_fix') {
            for (const rule of bugFixRules) {
                if (rule.pattern.test(entry.instruction) || rule.pattern.test(entry.response)) {
                    // Check if it's already enriched
                    if (!entry.response.startsWith("Hata:")) {
                        entry.response = rule.explanation + entry.response;
                        enrichedCount++;
                        break;
                    }
                }
            }
        }
        return JSON.stringify(entry);
    });

    if (enrichedCount > 0) {
        fs.writeFileSync(datasetPath, enrichedLines.join('\n') + '\n', 'utf8');
        console.log(`Successfully enriched ${enrichedCount} bug_fix entries with detailed Turkish explanations.`);
    } else {
        console.log("No new bug_fix entries needed enrichment.");
    }
}

enrich();
