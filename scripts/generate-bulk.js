const fs = require("fs");

function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }

// Output prediction - 40 unique patterns
const outputs = [
  ["print(2 + 3)", "5"], ["print(2 ** 10)", "1024"], ["print(len('istanbul'))", "7"],
  ["print([1, 2, 3][-1])", "3"], ["print(10 % 3)", "1"], ["print(round(3.7))", "4"],
  ["print(bool(0))", "False"], ["print('merhaba'.upper())", "MERHABA"],
  ["print('merhaba'.count('a'))", "3"], ["print(type(42))", "<class 'int'>"],
  ["print(min(5, 2, 8))", "2"], ["print(max(5, 2, 8))", "8"],
  ["print(abs(-7))", "7"], ["print(str(123))", "123"], ["print(int('45'))", "45"],
  ["print([1, 2, 3, 4][1:3])", "[2, 3]"], ["print([0] * 4)", "[0, 0, 0, 0]"],
  ["print(3 ** 3)", "27"], ["print(15 / 4)", "3.75"], ["print(15 // 4)", "3"],
  ["console.log(2 + 3)", "5"], ["console.log(typeof 'a')", "string"],
  ["console.log('hi'.length)", "2"], ["console.log(Math.max(1,5))", "5"],
  ["console.log([1,2,3].pop())", "3"], ["console.log(!!0)", "false"],
  ["console.log('5' - 2)", "3"], ["console.log(3 > 5)", "false"],
  ["System.out.println(2 + 3);", "5"], ["System.out.println('a'.length());", "1"],
  ["System.out.println(10 / 3);", "3"], ["System.out.println(Math.min(2,7));", "2"],
  ["fmt.Println(2 + 3)", "5"], ["fmt.Println(len('go'))", "2"],
  ["fmt.Println(10 > 5)", "true"], ["fmt.Println(3 * 4)", "12"],
  ["SELECT COUNT(*) FROM users;", "Tablodaki kayit sayisi"], ["SELECT 5 + 3;", "8"],
  ["SELECT UPPER('merhaba');", "MERHABA"], ["SELECT LENGTH('test');", "4"]
];
const langs = [
  "python","python","python","python","python","python","python","python","python","python",
  "python","python","python","python","python","python","python","python","python","python",
  "javascript","javascript","javascript","javascript","javascript","javascript","javascript","javascript",
  "java","java","java","java","go","go","go","go","sql","sql","sql","sql"
];
let pred = outputs.map(([code, out], i) => ({
  instruction: "Su kodun ciktisi nedir?\n" + code,
  response: out, language: langs[i], format: "output_prediction", type: "generated"
}));
fs.writeFileSync("test_output/output_prediction.jsonl", pred.map(d => JSON.stringify(d)).join("\n"));
console.log("output_prediction: " + pred.length);

// Complexity - 30 unique
const comp = [
  "O(log n) - Her adimda alan yariya iner.","O(n)","O(n^2)","O(n log n)","O(1)","O(2^n)","O(n!)","O(n^3)",
  "O(log n)","O(n)","O(n^2)","O(n log n)","O(1)","O(n)","O(n^2)","O(n)","O(log n)","O(n log n)",
  "O(1)","O(n)","O(n^2)","O(n log n)","O(2^n)","O(n!)","O(log n)","O(n)","O(n log n)","O(1)","O(n)","O(n^2)"
];
const compQ = [
  "Binary search","Bubble sort","Ici ice iki for","Merge sort","Hash table arama","Fibonacci recursive","TSP brute force","Matrix multiplication",
  "Binary tree search","Linear search","Selection sort","Quick sort","Diziye eleman ekleme","Dizide arama","Insertion sort","En buyuk eleman","Balanced tree traversal","Heap sort",
  "Stack push/pop","Listede maksimum bulma","Nested loop toplama","Counting sort","Hanoi kuleleri","Permutation generation","Balanced BST search","Array copy","Radix sort","HashMap get","LinkedList get","Bubble sort best case"
];
let comps = compQ.map((q, i) => ({
  instruction: q + " karmasikligi nedir?",
  response: comp[i], language: "algorithms", format: "complexity", type: "generated"
}));
fs.writeFileSync("test_output/complexity.jsonl", comps.map(d => JSON.stringify(d)).join("\n"));
console.log("complexity: " + comps.length);

// Error explain - 30 unique
const errQ = [
  ["int object is not iterable", "int uzerinde for ile gezilmez. range(sayi) kullan."],
  ["list index out of range", "Olmayan index. Uzunlugu kontrol et."],
  ["KeyError", "Olmayan anahtar. .get() kullan."],
  ["invalid literal for int()", "int() e sayi olmayan deger."],
  ["ZeroDivisionError", "Sifira bolme."],
  ["ModuleNotFoundError", "Modul bulunamadi. pip install ile yukle."],
  ["FileNotFoundError", "Dosya bulunamadi. Yolu kontrol et."],
  ["NoneType has no attribute", "None degerinin ozelligi alinamaz."],
  ["NameError", "Tanimlanmamis degisken."],
  ["TypeError: can only concatenate", "Farkli tipler birlestirilemez. Orn: str + int"],
  ["ValueError: math domain error", "Matematiksel tanimsiz islem. sqrt(-1) gibi."],
  ["RecursionError", "Fazla recursion. Base case ekle."],
  ["IndexError: string index", "String'de olmayan index."],
  ["TypeError: not enough arguments", "Fonksiyona az parametre."],
  ["AttributeError: module has no", "Modulde olmayan fonksiyon."],
  ["IndentationError", "Girinti hatasi."],
  ["TabError", "Sekme ve bosluk karisik."],
  ["UnboundLocalError", "Yerel degisken tanimlanmamis."],
  ["TypeError: unsupported operand", "Desteklenmeyen operator."],
  ["OverflowError", "Sayi cok buyuk."],
  ["TypeError: not subscriptable", "Indexlenemez nesne."],
  ["ValueError: too many values", "Cok fazla deger."],
  ["TypeError: can't multiply sequence", "String * string yapilamaz."],
  ["RuntimeError: dictionary changed", "Sozluk uzerinde gezinirken degisiklik."],
  ["TypeError: 'NoneType' is not callable", "None olan nesneyi fonksiyon gibi cagirma."],
  ["SyntaxError: unexpected EOF", "Beklenmeyen dosya sonu. Parantez eksik."],
  ["TypeError: 'float' object cannot be", "Float indexlenemez."],
  ["ValueError: cannot convert float", "Float string'e cevrilemez."],
  ["TypeError: 'int' object is not callable", "int'i fonksiyon gibi cagirma."],
  ["TypeError: unhashable type", "Hashlenemez tip. List'ler dict key olamaz."]
];
let errs = errQ.map(([q, a]) => ({
  instruction: "TypeError: " + q + " hatasi ne demek? Nasil cozulur?",
  response: a, language: "python", format: "error_explain", type: "generated"
}));
fs.writeFileSync("test_output/error_explain.jsonl", errs.map(d => JSON.stringify(d)).join("\n"));
console.log("error_explain: " + errs.length);

// Best practice - 30 unique
const bp = [
  ["Dosya okurken neden with kullanmaliyiz?", "with blogu dosyayi otomatik kapatir. Hata olursa bile kapanma garantilidir."],
  ["String birlestirmede + mi join mi?", "join() daha hizlidir. + operatoru her seferinde yeni string olusturur."],
  ["Liste kopyalamada hangi yontem dogru?", "new_list = old_list[:] veya .copy() kullan. = sadece referans kopyalar."],
  ["Varsayilan parametre olarak neden [] kullanilmaz?", "Varsayilan parametreler bir kez degerlendirilir. None + if kontrolu kullan."],
  ["Exception yakalarken neden spesifik olmali?", "except: tum hatalari gizler. except ValueError: dogru kullanim."],
  ["Global degisken kullanimi neden onerilmez?", "Global degiskenler fonksiyonlar arasi bagimlilik yaratir. Parametre olarak gec."],
  ["Birim test neden onemlidir?", "Kodun dogrulugunu otomatik kontrol eder. Degisikliklerde gerileme olmadigini garanti eder."],
  ["Docstring ne ise yarar?", "Fonksiyonun ne yaptigini, parametrelerini ve donus degerini aciklar. Help() ile goruntulenir."],
  ["Type hint kullanmanin faydasi nedir?", "Kodu daha okunabilir yapar, IDE uyarilari alir, hatalari erken yakalar."],
  ["Neden kisaltma yerine aciklayici isim kullanmaliyiz?", "Kod bir kez yazilir ama defalarca okunur. Anlamli isimler bakimi kolaylastirir."],
  ["Her seyi try/catch ile cevrelemek neden kotu?", "Hatalari gizler ve debug zorlastirir. Sadece tahmin ettigin hatalari yakala."],
  ["Config bilgileri neden env variable'da tutulmali?", "Sifre, API key gibi bilgiler kodda olmamali. .env dosyasi veya env kullan."],
  ["Commit mesaji nasil yazilmali?", "Ne degistigini anlatan kisa ama acik mesaj. 'fix bug' yerine 'fix login redirect bug'."],
  ["Neden sihirli sayi kullanmamaliyiz?", "Anlamsiz sabitler. Yerine const/sabit ismi kullan. Orn: MAX_RETRY_COUNT = 3."],
  ["Kod tekrari neden kotudur?", "DRY prensibi: Ayni kodu iki yerde degistirme. Fonksiyon veya sinif cikar."],
  ["Enum kullanmanin faydasi nedir?", "Sabit degerleri gruplar, tip guvenligi saglar, okunabilirligi artirir."],
  ["Unittest ile integration test farki nedir?", "Unit test tek fonksiyonu test eder. Integration test birden cok bilesimin birlikte calismasini test eder."],
  ["Neden DUZ metin sifre saklanmamali?", "Veritabani calinda sifreler ele gecer. Hash + salt ile sakla."],
  ["ORM kullanmanin avantaji nedir?", "SQL yazmadan veritabani islemleri. Enjeksiyon korumasi. Kod ile tutarli."],
  ["Log seviyeleri nelerdir?", "DEBUG, INFO, WARNING, ERROR, CRITICAL. Uretimde INFO ve uzeri kullanilir."],
  ["API rate limiting neden gereklidir?", "Kotuye kullanim ve DDoS engelleme. Kaynaklari korur."],
  ["Dependency injection nedir?", "Bagimliliklari disardan vermek. Test edilebilirligi artirir, baglari azaltir."],
  ["Git branch stratejisi neden onemli?", "Takim ici paralel calismayi saglar. Main branch her zaman kararli kalir."],
  ["Code review neden yapilmali?", "Hatalari erken yakalar, takim bilgisini yayar, kod standartlarini korur."],
  ["Continuous Integration nedir?", "Kod her push'ta otomatik test edilir ve build alinir. Hatalar hizli bulunur."],
  ["Kucuk commit'ler mi buyuk commit'ler mi?", "Kucuk commit. Her commit tek bir degisiklik icermeli. Revert kolay."],
  ["Neden production'da console.log birakilmamali?", "Performans kaybi, log kirliligi, guvenlik riski."],
  ["HTTPS neden zorunludur?", "Veri sifrelenir, aradaki adam saldirisi engellenir."],
  ["CORS hatasi nedir?", "Farkli domain'den API cagrisina izin verilmez. Server'da Access-Control-Allow-Origin ayarlanmali."],
  ["Prepared statement nedir?", "SQL sorgusunu parametrelerden ayirir. SQL injection'u engeller."]
];
let bps = bp.map(([q, a]) => ({
  instruction: q, response: a, language: "python", format: "best_practice", type: "generated"
}));
fs.writeFileSync("test_output/best_practice.jsonl", bps.map(d => JSON.stringify(d)).join("\n"));
console.log("best_practice: " + bps.length);

console.log("\nDone. 4 format, toplam " + (pred.length + comps.length + errs.length + bps.length) + " benzersiz kayit.");
