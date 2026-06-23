$entries = @()

function New-Entry {
    param($instr, $code, $lang)
    return @{
        instruction = $instr
        response = $code.Trim()
        language = $lang
        category = "project"
        type = "manual"
        format = "project"
    }
}

# ==================== GENERATE ALL 500 ENTRIES ====================

# --- PYTHON (150 entries) ---
$pyDir = "C:\Users\agnes\Desktop\projects\turkish-code-instructions\data_py"

# Not defteri (10)
$entries += New-Entry "Basit bir not defteri uygulamasi yap. Kullanici not ekleyebilmeli, silebilmeli ve listeleyebilmeli. Notlar hafizada tutulacak." @"
class NotDefteri:
    def __init__(self):
        self.notlar = []
    def not_ekle(self, baslik, icerik):
        self.notlar.append({"id": len(self.notlar)+1, "baslik": baslik, "icerik": icerik})
        print(f"'{baslik}' baslikli not eklendi.")
    def not_sil(self, not_id):
        for n in self.notlar:
            if n["id"] == not_id:
                self.notlar.remove(n)
                print(f"{not_id} numarali not silindi.")
                return
        print("Not bulunamadi.")
    def not_listele(self):
        if not self.notlar:
            print("Henuz not yok.")
            return
        for n in self.notlar:
            print(f"[{n['id']}] {n['baslik']}: {n['icerik'][:30]}...")
    def not_ara(self, kelime):
        sonuc = [n for n in self.notlar if kelime.lower() in n['baslik'].lower() or kelime.lower() in n['icerik'].lower()]
        return sonuc
if __name__ == "__main__":
    uyg = NotDefteri()
    uyg.not_ekle("Alisveris", "Marketten sut, ekmek, yumurta alinacak")
    uyg.not_ekle("Is", "Proje teslimi 15 Mart")
    uyg.not_listele()
    uyg.not_sil(1)
    uyg.not_listele()
"@ "python"

$entries += New-Entry "JSON dosyasina kaydeden bir not defteri yap. Notlar kalici olarak saklansin ve uygulama acildiginda yuklensin." @"
import json
class NotDefteriJSON:
    def __init__(self, dosya="notlar.json"):
        self.dosya = dosya
        self.notlar = self.yukle()
    def yukle(self):
        try:
            with open(self.dosya, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    def kaydet(self):
        with open(self.dosya, "w", encoding="utf-8") as f:
            json.dump(self.notlar, f, ensure_ascii=False, indent=2)
    def ekle(self, baslik, icerik):
        self.notlar.append({"id": len(self.notlar)+1, "baslik": baslik, "icerik": icerik})
        self.kaydet()
    def sil(self, not_id):
        self.notlar = [n for n in self.notlar if n["id"] != not_id]
        self.kaydet()
    def listele(self):
        for n in self.notlar:
            print(f"[{n['id']}] {n['baslik']}")
nd = NotDefteriJSON()
nd.ekle("Python ogren", "Decorator konusunu calis")
nd.ekle("Kitap oku", "Temiz Kod kitabi")
print("=== NOTLAR ===")
nd.listele()
"@ "python"

# We'll generate the rest programmatically
$pythonProjects = @(
    @{instr="Not defterine renk kodlariyla kategorize etme ozelligi ekle. Her notun bir kategorisi ve rengi olsun. Kategoriye gore filtrele."; code=@"
class KategoriliNotDefteri:
    def __init__(self):
        self.notlar = []
    def ekle(self, baslik, icerik, kategori="Genel", renk="#ff0"):
        self.notlar.append({"baslik": baslik, "icerik": icerik, "kategori": kategori, "renk": renk})
    def kategoriye_gore(self, kategori):
        return [n for n in self.notlar if n["kategori"] == kategori]
    def tumunu_listele(self):
        for n in self.notlar:
            print(f"[{n['kategori']}] {n['baslik']} - Renk: {n['renk']}")
    def kategorileri_getir(self):
        return list(set(n["kategori"] for n in self.notlar))
def = KategoriliNotDefteri()
"@},
    @{instr="Not defterine arama ve filtreleme ekle. Kullanici baslik veya icerikte arama yapabilsin. Sonuclari vurgula."; code=@"
class NotArama:
    def __init__(self):
        self.notlar = []
    def ekle(self, baslik, icerik):
        self.notlar.append({"baslik": baslik, "icerik": icerik})
    def ara(self, sorgu):
        sorgu = sorgu.lower()
        sonuc = []
        for n in self.notlar:
            b = sorgu in n["baslik"].lower()
            i = sorgu in n["icerik"].lower()
            if b or i:
                sonuc.append(n)
        return sonuc
    def filtrele(self, kw):
        for n in self.ara(kw):
            print(f"{n['baslik']}: {n['icerik'][:50]}")
na = NotArama()
na.ekle("Python Proje", "Not defteri uygulamasi")
na.ekle("Django Ogren", "Web framework")
na.ekle("Proje Plan", "Takvim olusturulacak")
na.filtrele("Proje")
"@}
)

# Actually, let me write a script that generates the Python code more efficiently
Write-Host "Starting generation..."

# I'll write the code templates directly to avoid the complexity of here-strings

# Helper function to add entries from a file
function Add-PythonEntries {
    $entries
}

# Let me write the massive file using a different approach - write directly to JSON
$allEntries = @()

# Read from template files if they exist
$pyTemplates = @"
Yapilacaklar listesi uygulamasi yap. Gorev ekle, tamamla, sil, listele islemleri olsun. Her gorevin bir ID'si olsun.
Hesap makinesi yap. Toplama, cikarma, carpma, bolme islemleri olsun. Konsoldan calissin.
Telefon rehberi uygulamasi yap. Kisi ekle, sil, guncelle, ara ve listele islemleri olsun.
Alisveris sepeti uygulamasi yap. Urun ekle, cikar, miktar guncelle, toplam fiyat hesapla.
Sayi tahmin oyunu yap. Bilgisayar 1-100 arasi sayi tutsun, kullanici tahmin etsin.
Quiz uygulamasi yap. Sorulari bir listede tut, kullanici cevaplasn, puan hesapla.
Sifre yoneticisi yap. Kullanici adi, sifre, URL bilgilerini sifreli olarak sakla.
Ogrenci not sistemi yap. Ogrenci ekle, not gir, ortalama hesapla, gecme/kalma durumunu goster.
Film rehberi yap. Film adi, yil, tur, puan bilgilerini tut. Listele ve ara.
Gelir gider takibi yap. Gelir ve gider ekle, kategorilere ayir, bakiye hesapla.
Kullanici giris sistemi yap. Kullanici adi ve sifre ile giris yap, kayit ol.
Rastgele sifre olusturucu yap. Uzunluk, karakter turu secenekleri olsun.
Dosya duzenleyici yap. Klasordeki dosyalari turune, boyutuna, tarihine gore listele.
JSON veri saklama uygulamasi yap. Verileri JSON dosyasina kaydet ve yukle.
E-posta dogrulama araci yap. Girilen e-posta adresinin gecerli olup olmadigini kontrol et.
Flask ile REST API yap. GET, POST, PUT, DELETE endpointleri olan not API'si olustur.
Blog sistemi yap. Baslik, icerik, yazar, tarih bilgileri olan blog yazilari yayinla.
Basit chat uygulamasi yap. Kullanicilarin mesaj gonderip alabilecegi sunucu-istemci modeli kur.
Hava durumu uygulamasi yap. Sehir adina gore API'den hava durumu verisi cek ve goster.
Para birimi cevrici yap. TL, USD, EUR arasi donusum yap. Kur bilgilerini guncelle.
Kronometre/sayac uygulamasi yap. Baslat, durdur, sifirla ozellikleri olsun.
Kelime oyunu yap. Karisik harflerden kelime bulma oyunu. Kullanici tahmin etsin.
Recete defteri yap. Ilac adi, dozaj, kullanim talimati bilgilerini tut.
Adres defteri yap. Kisi adi, adres, telefon, e-posta bilgilerini kaydet.
Kitap koleksiyonu yap. Kitap adi, yazar, tur, sayfa sayisi bilgilerini tut.
Muzik calma listesi yap. Sarki adi, sanatci, album, sure bilgilerini tut.
Tarif defteri yap. Yemek adi, malzemeler, hazirlanis adimlarini kaydet.
Egzersiz takipcisi yap. Egzersiz turu, sure, tekrar sayisi, yapilan tarih kaydet.
Su icme hatirlaticisi yap. Gunluk hedef belirle, icilen su miktarini takip et.
Ilac hatirlaticisi yap. Ilac adi, dozaj, saat bilgisi gir. Hatirlatma zamaninda uyar.
Konser bilet sistemi yap. Konser adi, tarih, mekan, bilet fiyati, kalan bilet sayisi tut.
Otobus bileti rezervasyonu yap. Sefer bilgisi, koltuk seci, bilet olustur.
Film koleksiyonu yap. Film adi, yonetmen, yil, izlenme durumu bilgilerini tut.
Dizi takipcisi yap. Dizi adi, sezon, bolum, izlenme durumu takip et.
Podcast yoneticisi yap. Podcast adi, bolum, sure, dinlenme durumu kaydet.
Not alma asistani yap. Sesli not al, metne cevir (simulasyon), kaydet.
Gunluk uygulamasi yap. Gunluk giris yap, tarih damgasi ekle, gunlere gore listele.
Haber okuyucu yap. RSS beslemesinden haber basliklarini cek ve goster.
RSS besleme yoneticisi yap. RSS URL ekle, beslemeleri oku, kaydet.
URL kisaltma aracı yap. Uzun URL'yi kisa URL'ye donustur ve kaydet.
Dosya donusturucu yap. JSON'dan CSV'ye, CSV'den JSON'a donusum yap.
QR kod olusturucu yap. Girilen metin veya URL'den QR kodu olustur ve kaydet.
Barkod tarama uygulamasi yap. Barkod numarasi gir, urun bilgisini goster (simulasyon).
Renk secici yap. RGB, HEX, HSL degerleri arasinda donusum yap ve renk goster.
Font gosterici yap. Sistemdeki fontlari listele ve ornek metinle goster.
Emoji arayici yap. Emoji listesinde ada gore ara ve emojiyi goster.
Renk paleti olusturucu yap. Ana renge gore uyumlu renk paleti olustur.
"@

# Parse templates into array
$pyLines = $pyTemplates -split "`n" | Where-Object { $_.Trim() -ne "" }

# Generate Python code snippets for each template
$pyCodeSnippets = @()
$pyCodeSnippets += @"
class Yapilacaklar:
    def __init__(self):
        self.gorevler = []
    def ekle(self, baslik):
        self.gorevler.append({"id": len(self.gorevler)+1, "baslik": baslik, "tamamlandi": False})
        print(f"Eklendi: {baslik}")
    def tamamla(self, gid):
        for g in self.gorevler:
            if g["id"] == gid:
                g["tamamlandi"] = True
                print(f"Tamamlandi: {g['baslik']}")
                return
    def sil(self, gid):
        self.gorevler = [g for g in self.gorevler if g["id"] != gid]
    def listele(self):
        for g in self.gorevler:
            d = "[X]" if g["tamamlandi"] else "[ ]"
            print(f"{d} {g['id']}. {g['baslik']}")
t = Yapilacaklar()
t.ekle("Market")
t.ekle("Proje")
t.listele()
"@

$pyCodeSnippets += @"
class HesapMakinesi:
    def __init__(self):
        self.sonuc = 0
    def topla(self, a, b):
        self.sonuc = a + b; return self.sonuc
    def cikar(self, a, b):
        self.sonuc = a - b; return self.sonuc
    def carp(self, a, b):
        self.sonuc = a * b; return self.sonuc
    def bol(self, a, b):
        if b == 0: return "Hata"
        self.sonuc = a / b; return self.sonuc
    def menu(self):
        while True:
            s = input("1:Topla 2:Cikar 3:Carp 4:Bol 5:Cikis: ")
            if s == "5": break
            if s in "1234":
                a, b = float(input("a: ")), float(input("b: "))
                print({"1":self.topla,"2":self.cikar,"3":self.carp,"4":self.bol}[s](a,b))
HesapMakinesi().menu()
"@

$pyCodeSnippets += @"
class TelefonRehberi:
    def __init__(self):
        self.kisiler = {}
    def ekle(self, isim, tel, email=""):
        self.kisiler[isim] = {"tel": tel, "email": email}
    def sil(self, isim):
        self.kisiler.pop(isim, None)
    def ara(self, kelime):
        return {k:v for k,v in self.kisiler.items() if kelime.lower() in k.lower()}
    def listele(self):
        for i,b in sorted(self.kisiler.items()):
            print(f"{i}: {b['tel']} ({b['email']})")
r = TelefonRehberi()
r.ekle("Ahmet", "0532-123-4567", "ahmet@x.com")
r.ekle("Ayse", "0533-987-6543")
r.listele()
"@

$pyCodeSnippets += @"
class AlisverisSepeti:
    def __init__(self):
        self.urunler = {}
    def ekle(self, ad, fiyat, miktar=1):
        if ad in self.urunler:
            self.urunler[ad]["miktar"] += miktar
        else:
            self.urunler[ad] = {"fiyat": fiyat, "miktar": miktar}
    def cikar(self, ad, miktar=1):
        if ad in self.urunler:
            if self.urunler[ad]["miktar"] <= miktar:
                del self.urunler[ad]
            else:
                self.urunler[ad]["miktar"] -= miktar
    def toplam(self):
        return sum(u["fiyat"]*u["miktar"] for u in self.urunler.values())
    def listele(self):
        for a,u in self.urunler.items():
            print(f"{a}: {u['miktar']}x{u['fiyat']}TL = {u['miktar']*u['fiyat']}TL")
        print(f"Toplam: {self.toplam()}TL")
s = AlisverisSepeti()
s.ekle("Ekmek", 10, 2)
s.ekle("Sut", 35, 1)
s.listele()
"@

$pyCodeSnippets += @"
import random
class SayiTahmin:
    def __init__(self):
        self.hedef = random.randint(1, 100)
        self.deneme = 0
    def tahmin(self, sayi):
        self.deneme += 1
        if sayi == self.hedef:
            return f"Bildin! {self.deneme}. deneme"
        return "Yuksek!" if sayi < self.hedef else "Dusuk!"
    def oyna(self):
        print("1-100 arasi sayi tuttum.")
        while True:
            try:
                t = int(input("Tahmin: "))
                s = self.tahmin(t)
                print(s)
                if "Bildin" in s: break
            except: break
SayiTahmin().oyna()
"@

$pyCodeSnippets += @"
class Quiz:
    def __init__(self):
        self.sorular = [
            {"s":"Python'un yaraticisi?","c":0,"siklar":["Guido van Rossum","Linus Torvalds","B.Stroustrup","D.Ritchie"]},
            {"s":"Liste hangi indexten baslar?","c":0,"siklar":["0","1","-1","random"]}
        ]
        self.puan = 0
    def baslat(self):
        for q in self.sorular:
            print(q["s"])
            for i,s in enumerate(q["siklar"],1):
                print(f" {i}. {s}")
            cvp = int(input("Cevap: "))-1
            if cvp == q["c"]:
                print("DOGRU! +10")
                self.puan += 10
            else:
                print(f"YANLIS! Dogru: {q['siklar'][q['c']]}")
        print(f"Puan: {self.puan}")
Quiz().baslat()
"@

$pyCodeSnippets += @"
import json, hashlib, os
class SifreYoneticisi:
    def __init__(self, dosya="sifreler.json"):
        self.dosya = dosya
        self.veriler = self.yukle()
    def yukle(self):
        try:
            with open(self.dosya) as f: return json.load(f)
        except: return []
    def kaydet(self):
        with open(self.dosya,"w") as f: json.dump(self.veriler,f,indent=2)
    def ekle(self, site, kadi, sifre):
        self.veriler.append({"site":site,"kadi":kadi,"sifre":sifre})
        self.kaydet()
    def getir(self, site):
        return [v for v in self.veriler if site.lower() in v["site"].lower()]
    def listele(self):
        for v in self.veriler:
            print(f"{v['site']}: {v['kadi']} / {v['sifre'][:3]}***")
sy = SifreYoneticisi()
sy.ekle("github.com", "user1", "sifre123")
sy.listele()
"@

$pyCodeSnippets += @"
class OgrenciNotSistemi:
    def __init__(self):
        self.ogrenciler = {}
    def ekle(self, no, isim):
        self.ogrenciler[no] = {"isim":isim, "notlar":[]}
    def not_ekle(self, no, ders, not_degeri):
        if no in self.ogrenciler:
            self.ogrenciler[no]["notlar"].append({"ders":ders,"not":not_degeri})
    def ortalama(self, no):
        if no not in self.ogrenciler: return 0
        n = self.ogrenciler[no]["notlar"]
        if not n: return 0
        return sum(x["not"] for x in n)/len(n)
    def gecti_mi(self, no):
        return self.ortalama(no) >= 60
    def listele(self):
        for no,o in self.ogrenciler.items():
            ort = self.ortalama(no)
            durum = "GECTI" if ort>=60 else "KALDI"
            print(f"{no}: {o['isim']} - Ort: {ort:.1f} - {durum}")
ons = OgrenciNotSistemi()
ons.ekle("101","Ali")
ons.ekle("102","Ayse")
ons.not_ekle("101","Mat",85)
ons.not_ekle("101","Fiz",70)
ons.not_ekle("102","Mat",45)
ons.listele()
"@

$pyCodeSnippets += @"
class FilmRehberi:
    def __init__(self):
        self.filmler = []
    def ekle(self, ad, yil, tur, puan):
        self.filmler.append({"ad":ad,"yil":yil,"tur":tur,"puan":puan})
    def ara(self, kelime):
        return [f for f in self.filmler if kelime.lower() in f["ad"].lower()]
    def tur_ara(self, tur):
        return [f for f in self.filmler if f["tur"].lower()==tur.lower()]
    def en_iyiler(self, n=3):
        return sorted(self.filmler, key=lambda f:f["puan"], reverse=True)[:n]
    def listele(self):
        for f in sorted(self.filmler, key=lambda x:x["yil"]):
            print(f"{f['yil']} {f['ad']:25s} {f['tur']:15s} {f['puan']}/10")
fr = FilmRehberi()
fr.ekle("Esaretin Bedeli",1994,"Dram",9.3)
fr.ekle("Inception",2010,"Bilim Kurgu",8.8)
fr.ekle("The Matrix",1999,"Aksiyon",8.7)
fr.listele()
print("En iyiler:", [f["ad"] for f in fr.en_iyiler()])
"@

$pyCodeSnippets += @"
class GelirGiderTakip:
    def __init__(self):
        self.islemler = []
    def gelir_ekle(self, miktar, kategori, aciklama=""):
        self.islemler.append({"tip":"gelir","miktar":miktar,"kategori":kategori,"aciklama":aciklama})
    def gider_ekle(self, miktar, kategori, aciklama=""):
        self.islemler.append({"tip":"gider","miktar":miktar,"kategori":kategori,"aciklama":aciklama})
    def bakiye(self):
        g = sum(i["miktar"] for i in self.islemler if i["tip"]=="gelir")
        gi = sum(i["miktar"] for i in self.islemler if i["tip"]=="gider")
        return g-gi
    def kategori_ozeti(self):
        ozet = {}
        for i in self.islemler:
            ozet[i["kategori"]] = ozet.get(i["kategori"],0) + (i["miktar"] if i["tip"]=="gelir" else -i["miktar"])
        return ozet
    def listele(self):
        for i in self.islemler:
            isaret = "+" if i["tip"]=="gelir" else "-"
            print(f"{isaret}{i['miktar']:7.2f}TL [{i['kategori']}] {i['aciklama']}")
        print(f"Bakiye: {self.bakiye():.2f}TL")
gt = GelirGiderTakip()
gt.gelir_ekle(5000,"Maas","Ocak ayi")
gt.gider_ekle(1500,"Kira","Ev kirosi")
gt.gider_ekle(500,"Fatura","Elektrik")
gt.listele()
"@

$pyCodeSnippets += @"
import hashlib
class KullaniciGiris:
    def __init__(self):
        self.kullanicilar = {}
    def kayit(self, kadi, sifre):
        hash_sifre = hashlib.sha256(sifre.encode()).hexdigest()
        self.kullanicilar[kadi] = hash_sifre
        print(f"{kadi} kaydedildi.")
    def giris(self, kadi, sifre):
        if kadi not in self.kullanicilar:
            return False
        hash_sifre = hashlib.sha256(sifre.encode()).hexdigest()
        return self.kullanicilar[kadi] == hash_sifre
    def sifre_degistir(self, kadi, eski_sifre, yeni_sifre):
        if self.giris(kadi, eski_sifre):
            self.kayit(kadi, yeni_sifre)
            print("Sifre degistirildi.")
            return True
        print("Basarisiz.")
        return False
kg = KullaniciGiris()
kg.kayit("admin","123456")
print("Giris:", kg.giris("admin","123456"))
print("Giris:", kg.giris("admin","wrong"))
"@

$pyCodeSnippets += @"
import random, string
class SifreOlusturucu:
    def __init__(self):
        self.kucuk_harf = string.ascii_lowercase
        self.buyuk_harf = string.ascii_uppercase
        self.rakam = string.digits
        self.sembol = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    def olustur(self, uzunluk=12, kucuk=True, buyuk=True, rakam=True, sembol=True):
        havuz = ""
        if kucuk: havuz += self.kucuk_harf
        if buyuk: havuz += self.buyuk_harf
        if rakam: havuz += self.rakam
        if sembol: havuz += self.sembol
        if not havuz: havuz = self.kucuk_harf
        return ''.join(random.choice(havuz) for _ in range(uzunluk))
    def olustur_kolay(self):
        return self.olustur(8, True, False, True, False)
    def olustur_orta(self):
        return self.olustur(12, True, True, True, False)
    def olustur_guclu(self):
        return self.olustur(16, True, True, True, True)
so = SifreOlusturucu()
print("Kolay:", so.olustur_kolay())
print("Orta:", so.olustur_orta())
print("Guclu:", so.olustur_guclu())
"@

$pyCodeSnippets += @"
import os, datetime
class DosyaDuzenleyici:
    def __init__(self, yol="."):
        self.yol = yol
    def listele(self, tur=None):
        dosyalar = os.listdir(self.yol)
        for d in dosyalar:
            tam = os.path.join(self.yol, d)
            boyut = os.path.getsize(tam)
            mod = os.path.getmtime(tam)
            tarih = datetime.datetime.fromtimestamp(mod).strftime("%d.%m.%Y %H:%M")
            tip = "K" if os.path.isdir(tam) else "D"
            if tur and not d.endswith(tur):
                continue
            print(f"{tip} {boyut//1024:5d}KB {tarih} {d}")
    def ara(self, pattern):
        sonuc = [d for d in os.listdir(self.yol) if pattern.lower() in d.lower()]
        for s in sonuc:
            print(f"Bulundu: {s}")
        return sonuc
    def boyuta_gore(self, min_kb=0):
        for d in os.listdir(self.yol):
            tam = os.path.join(self.yol,d)
            if os.path.isfile(tam) and os.path.getsize(tam)//1024 >= min_kb:
                print(f"{d}: {os.path.getsize(tam)//1024}KB")
dd = DosyaDuzenleyici(".")
dd.listele(".py")
"@

$pyCodeSnippets += @"
import json, os
class JSONVeriSaklama:
    def __init__(self, dosya="veri.json"):
        self.dosya = dosya
        self.veri = self.yukle()
    def yukle(self):
        if not os.path.exists(self.dosya):
            return []
        with open(self.dosya,"r",encoding="utf-8") as f:
            return json.load(f)
    def kaydet(self):
        with open(self.dosya,"w",encoding="utf-8") as f:
            json.dump(self.veri,f,ensure_ascii=False,indent=2)
    def ekle(self, kayit):
        if isinstance(kayit,dict):
            self.veri.append(kayit)
        else:
            self.veri.extend(kayit)
        self.kaydet()
    def getir(self, anahtar, deger):
        return [v for v in self.veri if v.get(anahtar)==deger]
    def sil(self, anahtar, deger):
        self.veri = [v for v in self.veri if v.get(anahtar)!=deger]
        self.kaydet()
    def listele(self):
        for v in self.veri:
            print(json.dumps(v,ensure_ascii=False))
js = JSONVeriSaklama()
js.ekle({"ad":"Ali","yas":30,"sehir":"Istanbul"})
js.ekle({"ad":"Ayse","yas":25,"sehir":"Ankara"})
js.listele()
"@

$pyCodeSnippets += @"
import re
class EpostaDogrulama:
    def __init__(self):
        self.pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    def dogrula(self, eposta):
        return bool(re.match(self.pattern, eposta))
    def aciklama(self, eposta):
        if not self.dogrula(eposta):
            if "@" not in eposta:
                return "@ isareti eksik"
            if "." not in eposta.split("@")[-1]:
                return "Alan adi gecersiz"
            return "Gecersiz format"
        return "Gecerli e-posta"
    def domain_getir(self, eposta):
        if self.dogrula(eposta):
            return eposta.split("@")[1]
        return None
    def toplu_dogrula(self, epostalar):
        return {e: self.dogrula(e) for e in epostalar}
ed = EpostaDogrulama()
testler = ["test@example.com", "gecersiz@", "user@site.com", "merhaba"]
for t in testler:
    print(f"{t:25s} -> {ed.dogrula(t)} - {ed.aciklama(t)}")
"@

$pyCodeSnippets += @"
from flask import Flask, jsonify, request
app = Flask(__name__)
notlar = []
counter = 1
@app.route("/api/notlar", methods=["GET"])
def listele():
    return jsonify(notlar)
@app.route("/api/notlar", methods=["POST"])
def ekle():
    global counter
    data = request.get_json()
    yeni = {"id":counter, "baslik":data["baslik"], "icerik":data.get("icerik","")}
    notlar.append(yeni)
    counter += 1
    return jsonify(yeni), 201
@app.route("/api/notlar/<int:nid>", methods=["PUT"])
def guncelle(nid):
    data = request.get_json()
    for n in notlar:
        if n["id"]==nid:
            n.update(data)
            return jsonify(n)
    return jsonify({"hata":"bulunamadi"}), 404
@app.route("/api/notlar/<int:nid>", methods=["DELETE"])
def sil(nid):
    global notlar
    notlar = [n for n in notlar if n["id"]!=nid]
    return jsonify({"mesaj":"silindi"})
if __name__=="__main__":
    app.run(debug=True)
"@

$pyCodeSnippets += @"
from datetime import datetime
class BlogSistemi:
    def __init__(self):
        self.yazilar = []
    def yazi_ekle(self, baslik, icerik, yazar):
        self.yazilar.append({
            "id": len(self.yazilar)+1,
            "baslik": baslik,
            "icerik": icerik,
            "yazar": yazar,
            "tarih": datetime.now().strftime("%d.%m.%Y %H:%M"),
            "yorumlar": []
        })
    def yazi_getir(self, yazi_id):
        for y in self.yazilar:
            if y["id"]==yazi_id:
                return y
        return None
    def yorum_ekle(self, yazi_id, yorumcu, metin):
        y = self.yazi_getir(yazi_id)
        if y:
            y["yorumlar"].append({"yorumcu":yorumcu,"metin":metin,"tarih":datetime.now().strftime("%d.%m.%Y %H:%M")})
    def listele(self):
        for y in self.yazilar:
            print(f"[{y['id']}] {y['baslik']} - {y['yazar']} ({y['tarih']})")
    def ara(self, kelime):
        return [y for y in self.yazilar if kelime.lower() in y["baslik"].lower() or kelime.lower() in y["icerik"].lower()]
b = BlogSistemi()
b.yazi_ekle("Python Ogreniyorum","Python temel konular...","Ali")
b.yazi_ekle("Flask API Gelistirme","REST API nasil yapilir...","Veli")
b.listele()
b.yorum_ekle(1,"Ayse","Harika yazi!")
"@

$pyCodeSnippets += @"
import socket, threading
class ChatSunucu:
    def __init__(self, host="127.0.0.1", port=5555):
        self.host = host
        self.port = port
        self.kullanicilar = {}
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def baslat(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen()
        print(f"Sunucu {self.host}:{self.port}'de dinliyor...")
        while True:
            client, addr = self.socket.accept()
            t = threading.Thread(target=self.istemci_yonet, args=(client,))
            t.start()
    def istemci_yonet(self, client):
        kadi = client.recv(1024).decode()
        self.kullanicilar[client] = kadi
        while True:
            try:
                mesaj = client.recv(1024).decode()
                if not mesaj: break
                for c in self.kullanicilar:
                    if c != client:
                        c.send(f"{kadi}: {mesaj}".encode())
            except:
                break
        del self.kullanicilar[client]
        client.close()
class ChatIstemci:
    def __init__(self, host="127.0.0.1", port=5555):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
    def giris(self, kadi):
        self.socket.send(kadi.encode())
    def mesaj_gonder(self, mesaj):
        self.socket.send(mesaj.encode())
if __name__=="__main__":
    print("Chat sunucu baslatiliyor... (Ctrl+C ile durdur)")
    ChatSunucu().baslat()
"@

$pyCodeSnippets += @"
import requests
class HavaDurumu:
    def __init__(self, api_key="demo"):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    def getir(self, sehir):
        try:
            params = {"q":sehir, "appid":self.api_key, "lang":"tr", "units":"metric"}
            r = requests.get(self.base_url, params=params)
            if r.status_code == 200:
                data = r.json()
                return {
                    "sehir": data["name"],
                    "sicaklik": data["main"]["temp"],
                    "hissedilen": data["main"]["feels_like"],
                    "durum": data["weather"][0]["description"],
                    "nem": data["main"]["humidity"],
                    "ruzgar": data["wind"]["speed"]
                }
            return None
        except:
            return None
    def goster(self, sehir):
        v = self.getir(sehir)
        if v:
            print(f"{v['sehir']}: {v['durum']}")
            print(f"Sicaklik: {v['sicaklik']}C (Hissedilen: {v['hissedilen']}C)")
            print(f"Nem: %{v['nem']}, Ruzgar: {v['ruzgar']} m/s")
        else:
            print("Veri alinamadi.")
h = HavaDurumu()
h.goster("Istanbul")
"@

$pyCodeSnippets += @"
class ParaBirimiCevirici:
    def __init__(self):
        self.kurlar = {"USD":30.0, "EUR":32.5, "GBP":38.0, "JPY":0.20, "CHF":34.0, "TL":1.0}
    def guncelle(self, yeni_kurlar):
        self.kurlar.update(yeni_kurlar)
    def cevir(self, miktar, kaynak, hedef):
        if kaynak not in self.kurlar or hedef not in self.kurlar:
            return None
        tl_deger = miktar * self.kurlar[kaynak]
        return tl_deger / self.kurlar[hedef]
    def listele(self):
        print("Guncel Kurlar (TL karsiligi):")
        for kur, deger in sorted(self.kurlar.items()):
            print(f"  1 {kur} = {deger:.2f} TL")
pb = ParaBirimiCevirici()
pb.listele()
print(f"100 USD = {pb.cevir(100,'USD','EUR'):.2f} EUR")
print(f"200 EUR = {pb.cevir(200,'EUR','TL'):.2f} TL")
"@

$pyCodeSnippets += @"
import time
class Kronometre:
    def __init__(self):
        self.baslangic = None
        self.bitis = None
        self.tur_suresi = []
    def baslat(self):
        self.baslangic = time.time()
        self.bitis = None
        self.tur_suresi = []
        print("Kronometre basladi.")
    def durdur(self):
        if self.baslangic:
            self.bitis = time.time()
            print(f"Gecen sure: {self.bitis-self.baslangic:.2f} sn")
    def tur(self):
        if self.baslangic:
            an = time.time()
            sured = an-self.baslangic
            self.tur_suresi.append(sured)
            print(f"Tur {len(self.tur_suresi)}: {sured:.2f} sn")
    def sifirla(self):
        self.baslangic = None
        self.bitis = None
        self.tur_suresi = []
        print("Sifirlandi.")
    def goster(self):
        if self.baslangic:
            print(f"Gecen: {time.time()-self.baslangic:.2f} sn")
k = Kronometre()
k.baslat()
time.sleep(0.5)
k.tur()
time.sleep(0.3)
k.durdur()
"@

$pyCodeSnippets += @"
import random, sys
class KelimeOyunu:
    def __init__(self):
        self.kelimeler = ["python","kitap","bilgisayar","program","yazilim","veri","algoritma","fonksiyon"]
    def karistir(self, kelime):
        harfler = list(kelime)
        random.shuffle(harfler)
        return ''.join(harfler)
    def oyna(self):
        kelime = random.choice(self.kelimeler)
        karisik = self.karistir(kelime)
        hak = 5
        print(f"Karisik harfler: {karisik}")
        print(f"{hak} hakkin var.")
        while hak > 0:
            tahmin = input("Tahminin: ").lower().strip()
            if tahmin == kelime:
                print("Tebrikler! Dogru bildin!")
                return True
            hak -= 1
            if hak > 0:
                ipucu = kelime[:len(kelime)-hak+1]
                print(f"Yanlis! Kalan hak: {hak}. Ipucu: {ipucu}")
        print(f"Kaybettin! Kelime: {kelime}")
        return False
if __name__=="__main__":
    KelimeOyunu().oyna()
"@

$pyCodeSnippets += @"
class ReceteDefteri:
    def __init__(self):
        self.receteler = []
    def ekle(self, ilac_adi, dozaj, kullanim, baslama_tarihi, bitis_tarihi):
        self.receteler.append({
            "ilac": ilac_adi,
            "dozaj": dozaj,
            "kullanim": kullanim,
            "baslama": baslama_tarihi,
            "bitis": bitis_tarihi,
            "devam": False
        })
    def alindi(self, index):
        if 0 <= index < len(self.receteler):
            self.receteler[index]["devam"] = True
    devam_eden(self):
        return [r for r in self.receteler if r["devam"]]
    def listele(self):
        for i,r in enumerate(self.receteler):
            durum = "[DEVAM]" if r["devam"] else "[BITTI]"
            print(f"{durum} {r['ilac']} {r['dozaj']} - {r['kullanim']}")
rd = ReceteDefteri()
def listele(self):
    for i,r in enumerate(self.receteler):
        durum = "[DEVAM]" if r["devam"] else "[BITTI]"
        print(f"{durum} {r['ilac']} {r['dozaj']} - {r['kullanim']}")
"@

# Continue with more... but let me check what we have now
$count = $entries.Count
Write-Host "Current entries: $count"

# Since we need 500 and this approach is too manual, let me write a generator function
Write-Host "Need to generate more entries..." -ForegroundColor Yellow
