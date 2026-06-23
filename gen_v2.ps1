$outputPath = "C:\Users\agnes\Desktop\projects\turkish-code-instructions\submissions\project_extra.json"
$entries = [System.Collections.ArrayList]::new()

function Add-Entry($instr, $code, $lang) {
    $null = $entries.Add(@{
        instruction = $instr
        response = $code.Trim()
        language = $lang
        category = "project"
        type = "manual"
        format = "project"
    })
}

# Project definitions: [index, turkish_name, description]
$projects = @(
    "Not Defteri", "Yapilacaklar Listesi", "Hesap Makinesi", "Telefon Rehberi",
    "Alisveris Sepeti", "Sayi Tahmin Oyunu", "Quiz Uygulamasi", "Sifre Yoneticisi",
    "Ogrenci Not Sistemi", "Film Rehberi", "Gelir Gider Takibi", "Kullanici Giris Sistemi",
    "Rastgele Sifre Olusturucu", "Dosya Duzenleyici", "JSON Veri Saklama",
    "E-posta Dogrulama", "REST API", "Blog Sistemi", "Chat Uygulamasi",
    "Hava Durumu", "Para Birimi Cevirici", "Kronometre", "Kelime Oyunu",
    "Recete Defteri", "Adres Defteri", "Alisveris Listesi", "Okuma Listesi",
    "Kitap Koleksiyonu", "Muzik Calma Listesi", "Tarif Defteri",
    "Egzersiz Takipcisi", "Su Icme Hatirlatici", "Ilac Hatirlatici",
    "Konser Bilet Sistemi", "Otobus Bileti", "Film Koleksiyonu", "Dizi Takipcisi",
    "Podcast Yoneticisi", "Not Alma Asistani", "Gunluk Uygulamasi",
    "Haber Okuyucu", "RSS Besleme", "URL Kisaltma", "Dosya Donusturucu",
    "QR Kod Olusturma", "Barkod Tarama", "Renk Secici", "Font Gosterici",
    "Emoji Arayici", "Renk Paleti Olusturucu"
)

$projectDescs = @(
    "Kullanici not ekleyebilmeli, silebilmeli ve listeleyebilmeli. Her notun baslik ve icerik alanlari olsun.",
    "Gorev ekle, tamamla, sil ve listele. Gorevler tamamlanma durumuna gore filtrelenebilsin.",
    "Toplama, cikarma, carpma ve bolme islemlerini yap. Konsoldan komut alarak calissin.",
    "Kisi ekle, sil, guncelle, ara ve listele. Her kisi icin isim, telefon ve e-posta bilgisi tut.",
    "Urun ekle, cikar, miktar guncelle ve toplam fiyati hesapla. Sepet bosaltma ozelligi olsun.",
    "Bilgisayar 1-100 arasi rastgele sayi tutsun, kullanici tahmin etsin. Deneme hakki sinirli.",
    "Sorulari listede tut, kullanici cevaplasn, dogru/yanlis sayisina gore puan hesapla.",
    "Kullanici adi, sifre ve URL bilgilerini guvenli sekilde sakla. Sifreleri listeleyip arayabilsin.",
    "Ogrenci ekle, ders notu gir, ortalama hesapla, gecme/kalma durumunu goster.",
    "Film adi, yil, tur, puan bilgilerini tut. Ture gore filtreleme ve puana gore sirala.",
    "Gelir ve gider ekle, kategorilere ayir, bakiye hesapla, kategori bazli ozet goster.",
    "Kullanici adi ve sifre ile kayit ol ve giris yap. Sifre hashlenerek saklansin.",
    "Kullanici belirtilen uzunluk ve karakter turlerinde rastgele sifre olustursun.",
    "Klasordeki dosyalari turune, boyutuna ve tarihine gore listele, ara.",
    "Verileri JSON formatinda dosyaya kaydet ve dosyadan oku, listele.",
    "Girilen e-posta adresinin formatini regex ile dogrula, gecerli/gecersiz olarak bildir.",
    "Express.js ile GET, POST, PUT, DELETE endpointleri olan bir REST API yap.",
    "Blog yazisi ekle, listele, ara. Her yazinin baslik, icerik, yazar ve tarih bilgisi olsun.",
    "Kullanicilarin mesaj gonderip alabilecegi basit bir sohbet uygulamasi yap.",
    "Sehir adina gore API'den hava durumu bilgisi cek, sicaklik ve durumu goster.",
    "TL, USD, EUR arasinda para birimi donusumu yap. Guncel kurlar kullan.",
    "Baslat, durdur, sifirla fonksiyonlari olan kronometre yap. Tur alma ozelligi ekle.",
    "Karistirilmis harflerden dogru kelimeyi bulma oyunu. Puan sistemi olsun.",
    "Ilac adi, dozaj ve kullanim talimati bilgilerini tut. Listeleyip arayabilsin.",
    "Kisi adi, adres, telefon ve e-posta bilgilerini sakla. Sehre gore filtrele.",
    "Alisveris listesi olustur, urun ekle/cikar, alinanlari isaretle.",
    "Okunacak kitap ve makaleleri listele, okunma durumunu takip et.",
    "Kitap adi, yazar, tur, sayfa sayisi bilgilerini tut. Okunanlari isaretle.",
    "Sarki adi, sanatci, album bilgilerini tut. Karisik calma ozelligi ekle.",
    "Yemek adi, malzemeler ve yapilis adimlarini kaydet. Malzemeye gore ara.",
    "Egzersiz turu, sure ve tekrar sayisini kaydet. Haftalik rapor goster.",
    "Gunluk su hedefi belirle, icilen su miktarini kaydet, ilerlemeyi goster.",
    "Ilac adi ve saat bilgisi gir. Belirtilen saatte hatirlatma uyarisi ver.",
    "Konser adi, tarih, mekan, fiyat ve kalan bilet sayisi bilgilerini tut.",
    "Sefer bilgisi gir, koltuk sec, bilet olustur ve listele.",
    "Film adi, yonetmen, yil, izlenme durumu bilgilerini tut ve listele.",
    "Dizi adi, sezon/bolum sayisi, izlenen bolumleri takip et.",
    "Podcast adi, bolum, sure ve dinlenme durumunu kaydet.",
    "Sesli not al (simulasyon), metni kaydet, listele.",
    "Gunluk yazi ekle, tarih damgasi ekle, gunlere gore listele.",
    "RSS kaynagindan haber basliklarini cek ve listele.",
    "RSS URL'leri ekle, beslemeleri oku ve guncelle.",
    "Uzun URL'yi kisa koda donustur (hash tabanli), kaydet ve coz.",
    "JSON'dan CSV'ye ve CSV'den JSON'a donusum yap.",
    "Girilen metin icin QR kodu olustur (ASCII veya resim).",
    "Barkod numarasi gir, urun bilgisi goster (simulasyon).",
    "RGB, HEX ve HSL degerleri arasinda donusum yap, rengi goster.",
    "Sistemdeki fontlari listele, ornek metinle goster.",
    "Emoji listesinde ada gore ara ve emojiyi goster.",
    "Ana renge gore uyumlu renk paleti olustur, renkleri goster."
)

Write-Host "Loaded $($projects.Length) project types." -ForegroundColor Cyan

# Language distribution
$langDist = @{
    "python" = 150
    "javascript" = 100
    "java" = 80
    "go" = 70
    "typescript" = 50
    "web" = 50
}

# Generate entries
$entryIndex = 0
foreach ($lang in $langDist.Keys) {
    $needed = $langDist[$lang]
    Write-Host "Generating $needed entries for $lang..." -ForegroundColor Yellow
    
    for ($i = 0; $i -ne $needed; $i++) {
        $projIndex = $entryIndex % $projects.Length
        $projName = $projects[$projIndex]
        $projDesc = $projectDescs[$projIndex]
        
        if ($lang -eq "python") {
            Add-Entry "$projName uygulamasi yap. $projDesc" (New-PythonCode $projName) "python"
        } elseif ($lang -eq "javascript") {
            Add-Entry "$projName uygulamasi yap. $projDesc" (New-JavaScriptCode $projName) "javascript"
        } elseif ($lang -eq "java") {
            Add-Entry "$projName uygulamasi yap. $projDesc" (New-JavaCode $projName) "java"
        } elseif ($lang -eq "go") {
            Add-Entry "$projName uygulamasi yap. $projDesc" (New-GoCode $projName) "go"
        } elseif ($lang -eq "typescript") {
            Add-Entry "$projName uygulamasi yap. $projDesc" (New-TypeScriptCode $projName) "typescript"
        } elseif ($lang -eq "web") {
            Add-Entry "$projName uygulamasi yap. $projDesc" (New-WebCode $projName) "web"
        }
        
        $entryIndex++
    }
}

Write-Host "Total entries: $($entries.Count)" -ForegroundColor Green

$json = $entries | ConvertTo-Json -Depth 3
[System.IO.File]::WriteAllText($outputPath, $json, [System.Text.UTF8Encoding]::new($false))
Write-Host "Saved to $outputPath" -ForegroundColor Green

# Check count per language
$entries | Group-Object language | Select-Object Name, Count | Format-Table -AutoSize
