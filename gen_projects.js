const fs = require("fs");
const entries = [];

function E(instr, code, lang) {
    entries.push({
        instruction: instr,
        response: code.trim(),
        language: lang,
        category: "project",
        type: "manual",
        format: "project"
    });
}

// 50 unique project types from user's list
const projects = [
    ["Not Defteri", "Kullanici not ekleyebilmeli, silebilmeli ve listeleyebilmeli."],
    ["Yapilacaklar Listesi", "Gorev ekle, tamamla, sil ve listele."],
    ["Hesap Makinesi", "Toplama, cikarma, carpma ve bolme islemlerini yap."],
    ["Telefon Rehberi", "Kisi ekle, sil, guncelle, ara ve listele."],
    ["Alisveris Sepeti", "Urun ekle, cikar, miktar guncelle, toplam fiyat hesapla."],
    ["Sayi Tahmin Oyunu", "Bilgisayar 1-100 arasi sayi tutsun, kullanici tahmin etsin."],
    ["Quiz", "Sorulari listede tut, kullanici cevaplasn, puan hesapla."],
    ["Sifre Yoneticisi", "Kullanici adi, sifre ve URL bilgilerini sakla."],
    ["Ogrenci Not Sistemi", "Ogrenci ekle, not gir, ortalama hesapla, gecme/kalma durumu goster."],
    ["Film Rehberi", "Film adi, yil, tur, puan bilgilerini tut."],
    ["Finans Takip", "Gelir ve gider ekle, kategorilere ayir, bakiye hesapla."],
    ["Kullanici Giris Sistemi", "Kullanici adi ve sifre ile kayit ol ve giris yap."],
    ["Rastgele Sifre Olusturucu", "Belirtilen uzunlukta rastgele sifre olustur."],
    ["Dosya Duzenleyici", "Klasordeki dosyalari turune, boyutuna gore listele."],
    ["JSON Veri Saklama", "Verileri JSON dosyasina kaydet ve yukle."],
    ["E-posta Dogrulama", "Girilen e-posta adresinin gecerli olup olmadigini kontrol et."],
    ["REST API", "Express.js ile GET, POST, PUT, DELETE endpointleri olan API yap."],
    ["Blog Sistemi", "Blog yazisi ekle, listele, ara. Yorum ekleme ozelligi olsun."],
    ["Chat Uygulamasi", "Kullanicilarin mesaj gonderip alabilecegi basit sohbet uygulamasi yap."],
    ["Hava Durumu", "Sehir adina gore APIden hava durumu verisi cek ve goster."],
    ["Para Birimi Cevirici", "TL, USD, EUR arasinda donusum yap."],
    ["Kronometre", "Baslat, durdur, sifirla ve tur alma fonksiyonlari olsun."],
    ["Kelime Oyunu", "Karistirilmis harflerden dogru kelimeyi bulma oyunu yap."],
    ["Recete Defteri", "Ilac adi, dozaj, kullanim talimati bilgilerini tut."],
    ["Adres Defteri", "Kisi adi, adres, telefon ve e-posta bilgilerini sakla."],
    ["Alisveris Listesi", "Alisveris listesi olustur, urun ekle/cikar, alinanlari isaretle."],
    ["Okuma Listesi", "Okunacak kitap ve makaleleri listele, okunma durumunu takip et."],
    ["Kitap Koleksiyonu", "Kitap adi, yazar, tur, sayfa sayisi bilgilerini tut."],
    ["Muzik Calma Listesi", "Sarki adi, sanatci, album bilgilerini tut."],
    ["Tarif Defteri", "Yemek adi, malzemeler ve yapilis adimlarini kaydet."],
    ["Egzersiz Takipcisi", "Egzersiz turu, sure ve tekrar sayisini kaydet."],
    ["Su Icme Hatirlatici", "Gunluk su hedefi belirle, icilen su miktarini takip et."],
    ["Ilac Hatirlatici", "Ilac adi ve saat bilgisi gir, hatirlatma uyarisi ver."],
    ["Konser Bilet Sistemi", "Konser adi, tarih, mekan, bilet fiyati bilgilerini tut."],
    ["Otobus Bileti", "Sefer bilgisi gir, koltuk sec, bilet olustur."],
    ["Film Koleksiyonu", "Film adi, yonetmen, yil, izlenme durumu bilgilerini tut."],
    ["Dizi Takipcisi", "Dizi adi, sezon, bolum sayisi, izlenme durumunu takip et."],
    ["Podcast Yoneticisi", "Podcast adi, bolum, sure ve dinlenme durumunu kaydet."],
    ["Not Alma Asistani", "Sesli not al (simulasyon), metni kaydet."],
    ["Gunluk Uygulamasi", "Gunluk yazi ekle, tarih damgasi ekle, gunlere gore listele."],
    ["Haber Okuyucu", "RSS kaynagindan haber basliklarini cek ve listele."],
    ["RSS Besleme", "RSS URL ekle, beslemeleri oku ve guncelle."],
    ["URL Kisaltma", "Uzun URLyi kisa koda donustur (hash tabanli)."],
    ["Dosya Donusturucu", "JSONdan CSVye ve CSVden JSONa donusum yap."],
    ["QR Kod Olusturma", "Girilen metin icin QR kodu olustur."],
    ["Barkod Tarama", "Barkod numarasi gir, urun bilgisi goster (simulasyon)."],
    ["Renk Secici", "RGB, HEX ve HSL degerleri arasinda donusum yap."],
    ["Font Gosterici", "Sistemdeki fontlari listele, ornek metinle goster."],
    ["Emoji Arayici", "Emoji listesinde ada gore ara ve emojiyi goster."],
    ["Renk Paleti Olusturucu", "Ana renge gore uyumlu renk paleti olustur."]
];

const langDist = { python: 150, javascript: 100, java: 80, go: 70, typescript: 50, web: 50 };

function pyCode(name) {
    var cn = name.replace(/ /g,"");
    if (name === "Hesap Makinesi") {
        return [
            "class " + cn + ":",
            "    def __init__(self): self.sonuc = 0",
            "    def topla(self, a, b): self.sonuc = a + b; return self.sonuc",
            "    def cikar(self, a, b): self.sonuc = a - b; return self.sonuc",
            "    def carp(self, a, b): self.sonuc = a * b; return self.sonuc",
            "    def bol(self, a, b):",
            "        if b == 0: return 'Hata: sifira bolme!'",
            "        self.sonuc = a / b; return self.sonuc",
            "    def menu(self):",
            "        while True:",
            "            s = input('1:Topla 2:Cikar 3:Carp 4:Bol 5:Cikis: ')",
            "            if s == '5': break",
            "            a = float(input('a: ')); b = float(input('b: '))",
            "            islem = {'1': self.topla, '2': self.cikar, '3': self.carp, '4': self.bol}[s]",
            "            print('Sonuc:', islem(a, b))",
            "",
            "if __name__ == '__main__':",
            "    " + cn + "().menu()"
        ].join("\n");
    }
    if (name === "Sayi Tahmin Oyunu") {
        return [
            "import random",
            "class " + cn + ":",
            "    def __init__(self):",
            "        self.hedef = random.randint(1, 100)",
            "        self.deneme = 0",
            "    def tahmin_et(self, sayi):",
            "        self.deneme += 1",
            "        if sayi == self.hedef:",
            "            return 'Tebrikler! ' + str(self.deneme) + '. denemede bildiniz!'",
            "        elif sayi < self.hedef:",
            "            return 'Daha yuksek!'",
            "        else:",
            "            return 'Daha dusuk!'",
            "    def oyna(self):",
            "        print('1-100 arasi sayi tuttum. Tahmin et!')",
            "        for i in range(10):",
            "            try:",
            "                t = int(input('Tahmin: '))",
            "                print(self.tahmin_et(t))",
            "                if t == self.hedef: break",
            "            except: print('Sayi girin!')",
            "",
            "if __name__ == '__main__':",
            "    " + cn + "().oyna()"
        ].join("\n");
    }
    if (name === "Sifre Yoneticisi") {
        return [
            "import json, hashlib, os",
            "class " + cn + ":",
            "    def __init__(self, dosya='sifreler.json'):",
            "        self.dosya = dosya",
            "        self.veriler = self.yukle()",
            "    def yukle(self):",
            "        try:",
            "            with open(self.dosya, 'r') as f: return json.load(f)",
            "        except: return []",
            "    def kaydet(self):",
            "        with open(self.dosya, 'w') as f: json.dump(self.veriler, f, indent=2)",
            "    def ekle(self, site, kadi, sifre):",
            "        sifre_hash = hashlib.sha256(sifre.encode()).hexdigest()",
            "        self.veriler.append({'site': site, 'kadi': kadi, 'sifre': sifre_hash})",
            "        self.kaydet()",
            "    def listele(self):",
            "        for v in self.veriler:",
            "            print(v['site'] + ': ' + v['kadi'] + ' ***')",
            "",
            "sy = " + cn + "()",
            "sy.ekle('github.com', 'kullanici1', 'sifre123')",
            "sy.ekle('gmail.com', 'kullanici2', 'abc456')",
            "sy.listele()"
        ].join("\n");
    }
    // Generic template
    return [
        "class " + cn + ":",
        "    def __init__(self):",
        "        self.veriler = []",
        "    def ekle(self, deger):",
        "        self.veriler.append(deger)",
        "    def listele(self):",
        "        for i, v in enumerate(self.veriler, 1):",
        "            print(f'{i}. {v}')",
        "    def ara(self, kelime):",
        "        return [v for v in self.veriler if kelime.lower() in str(v).lower()]",
        "    def sil(self, index):",
        "        if 0 <= index < len(self.veriler):",
        "            return self.veriler.pop(index)",
        "",    
        "if __name__ == '__main__':",
        "    uyg = " + cn + "()",
        "    uyg.ekle('Ornek deger 1')",
        "    uyg.ekle('Ornek deger 2')",
        "    uyg.listele()",
        "    print('Arama:', uyg.ara('ornek'))"
    ].join("\n");
}

function jsCode(name) {
    var cn = name.replace(/ /g,"");
    if (name === "Hesap Makinesi") {
        return [
            "class " + cn + " {",
            "    constructor() { this.sonuc = 0; }",
            "    topla(a, b) { return this.sonuc = a + b; }",
            "    cikar(a, b) { return this.sonuc = a - b; }",
            "    carp(a, b) { return this.sonuc = a * b; }",
            "    bol(a, b) { return b === 0 ? 'Hata' : this.sonuc = a / b; }",
            "    menu() {",
            "        const s = prompt('Islem (1:Topla 2:Cikar 3:Carp 4:Bol):');",
            "        const a = +prompt('a:'), b = +prompt('b:');",
            "        const map = {1:this.topla,2:this.cikar,3:this.carp,4:this.bol};",
            "        console.log('Sonuc:', map[s].call(this, a, b));",
            "    }",
            "}",
            "new " + cn + "().menu();"
        ].join("\n");
    }
    if (name === "Sayi Tahmin Oyunu") {
        return [
            "class " + cn + " {",
            "    constructor() {",
            "        this.hedef = Math.floor(Math.random() * 100) + 1;",
            "        this.deneme = 0;",
            "    }",
            "    tahmin(sayi) {",
            "        this.deneme++;",
            "        if (sayi === this.hedef) return 'Bildin! ' + this.deneme + '. deneme';",
            "        return sayi < this.hedef ? 'Yuksek!' : 'Dusuk!';",
            "    }",
            "}",
            "const o = new " + cn + "();",
            "console.log('1-100 arasi sayi tuttum.');",
            "for (let i = 0; i < 10; i++) {",
            "    const t = +prompt('Tahmin:');",
            "    const s = o.tahmin(t); console.log(s);",
            "    if (t === o.hedef) break;",
            "}"
        ].join("\n");
    }
    return [
        "class " + cn + " {",
        "    constructor() { this.veriler = []; }",
        "    ekle(deger) { this.veriler.push(deger); }",
        "    listele() { this.veriler.forEach((v, i) => console.log((i+1) + '. ' + v)); }",
        "    ara(kelime) { return this.veriler.filter(v => v.toLowerCase().includes(kelime.toLowerCase())); }",
        "}",
        "const uyg = new " + cn + "();",
        "uyg.ekle('Ornek 1'); uyg.ekle('Ornek 2');",
        "uyg.listele(); console.log('Arama:', uyg.ara('ornek'));"
    ].join("\n");
}

function javaCode(name) {
    var cn = name.replace(/ /g,"");
    return [
        "import java.util.*;",
        "public class " + cn + " {",
        "    private List<String> veriler = new ArrayList<>();",
        "    public void ekle(String d) { veriler.add(d); }",
        "    public void listele() { for (int i=0; i<veriler.size(); i++) System.out.println((i+1) + '. ' + veriler.get(i)); }",
        "    public static void main(String[] args) {",
        "        " + cn + " u = new " + cn + "();",
        "        u.ekle('Ornek1'); u.ekle('Ornek2');",
        "        u.listele();",
        "    }",
        "}"
    ].join("\n");
}

function goCode(name) {
    var cn = name.replace(/ /g,"");
    return [
        "package main",
        "import \"fmt\"",
        "type " + cn + " struct {",
        "    veriler []string",
        "}",
        "func (u *" + cn + ") ekle(d string) { u.veriler = append(u.veriler, d) }",
        "func (u *" + cn + ") listele() { for i, v := range u.veriler { fmt.Printf(\"%d. %s\\n\", i+1, v) } }",
        "func main() {",
        "    u := &" + cn + "{}",
        "    u.ekle(\"Ornek1\"); u.ekle(\"Ornek2\")",
        "    u.listele()",
        "}"
    ].join("\n");
}

function tsCode(name) {
    var cn = name.replace(/ /g,"");
    return [
        "class " + cn + " {",
        "    private veriler: string[] = [];",
        "    ekle(d: string): void { this.veriler.push(d); }",
        "    listele(): void { this.veriler.forEach((v, i) => console.log((i+1) + '. ' + v)); }",
        "}",
        "const uyg = new " + cn + "();",
        "uyg.ekle('Ornek1'); uyg.ekle('Ornek2'); uyg.listele();"
    ].join("\n");
}

function webCode(name) {
    return [
        "<!DOCTYPE html>",
        "<html><head><meta charset='UTF-8'><title>" + name + "</title></head><body>",
        "<h1>" + name + " Uygulamasi</h1>",
        "<input id='giris' placeholder='Deger girin'>",
        "<button onclick='ekle()'>Ekle</button>",
        "<button onclick='listele()'>Listele</button>",
        "<ul id='liste'></ul>",
        "<script>",
        "var veriler = [];",
        "function ekle() { var d=document.getElementById('giris').value; if(d){veriler.push(d);document.getElementById('giris').value='';} }",
        "function listele() { document.getElementById('liste').innerHTML=veriler.map(function(v,i){return '<li>'+(i+1)+'. '+v+'</li>';}).join(''); }",
        "</script></body></html>"
    ].join("\n");
}

var idx = 0;
for (var lang in langDist) {
    var count = langDist[lang];
    var codeGen = { python: pyCode, javascript: jsCode, java: javaCode, go: goCode, typescript: tsCode, web: webCode }[lang];
    for (var i = 0; i < count; i++) {
        var proj = projects[idx % projects.length];
        var instr = proj[0] + " uygulamasi yap. " + proj[1];
        E(instr, codeGen(proj[0]), lang);
        idx++;
    }
}

var out = "C:\\Users\\agnes\\Desktop\\projects\\turkish-code-instructions\\submissions\\project_extra.json";
fs.writeFileSync(out, JSON.stringify(entries, null, 2), "utf8");
console.log("Generated " + entries.length + " entries, saved to " + out);
