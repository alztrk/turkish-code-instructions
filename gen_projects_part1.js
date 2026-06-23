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

const projects = [
    ["Not Defteri","Kullanici not ekleyebilmeli, silebilmeli ve listeleyebilmeli. Notlar JSON ile kalici olarak kaydedilsin."],
    ["Yapilacaklar Listesi","Gorev ekle, tamamla, sil ve listele. Tamamlanma durumuna gore filtreleme yap."],
    ["Hesap Makinesi","Toplama, cikarma, carpma ve bolme islemlerini yap. Islem gecmisi tutulsun."],
    ["Telefon Rehberi","Kisi ekle, sil, guncelle, ara ve listele. Her kisi icin isim, telefon, email gir."],
    ["Alisveris Sepeti","Urun ekle, cikar, miktar guncelle ve toplam fiyati hesapla."],
    ["Sayi Tahmin Oyunu","Bilgisayar 1-100 arasi rastgele sayi tutsun. Kullanici 10 hakta tahmin etsin."]
];
const langDist = { python: 150, javascript: 100, java: 80, go: 70, typescript: 50, web: 50 };
