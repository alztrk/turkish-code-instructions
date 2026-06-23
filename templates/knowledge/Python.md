# Python Bilgi Referansi

## Genel Bakis

Python, Guido van Rossum tarafindan 1989 yilinda Amsterdam'da baslatilmis ve 1991'de ilk surumu yayinlanmis yuksek seviyeli, yorumlanan bir programlama dilidir. "Zarif, acik ve okunabilir" kod felsefesiyle tasarlanmistir. Adini Monty Python'dan almistir.

Python gunumuzde veri bilimi, yapay zeka, web gelistirme (Django, Flask), otomasyon, scripting, siber guvenlik ve egitim alanlarinda en cok kullanilan dillerden biridir. Google, Netflix, Spotify, NASA gibi kurumlar Python kullanmaktadir. TIOBE ve Stack Overflow anketlerinde surekli ilk 3'te yer alir. Genis kutuphane ekosistemi, okunabilir syntax'i ve topluluk destegi en guclu yonleridir.

## Temel Syntax

```python
# --- Degiskenler ve Veri Tipleri ---
isim: str = "Ali"               # type hint (istege bagli)
yas: int = 25
pi: float = 3.14159
aktif: bool = True
deger = None                     # None tipi
karmasik = 3 + 4j                # karmasik sayi

# --- String Islemleri ---
metin = "Merhaba Dunya"
print(metin.upper())             # MERHABA DUNYA
print(metin.split())             # ['Merhaba', 'Dunya']
print(f"Yas: {yas}")             # f-string interpolasyonu

# --- Temel Veri Yapilari ---
liste = [1, 2, 3, 4, 5]
liste.append(6)                  # sona ekle
liste.insert(0, 0)               # basa ekle
liste.pop()                      # sondan cikar

demet = (1, 2, 3)                # tuple (degistirilemez)
kume = {1, 2, 3, 3}              # set (benzersiz) -> {1, 2, 3}
sozluk = {"ad": "Ali", "yas": 25}
print(sozluk["ad"])              # Ali
print(sozluk.get("soyad", "yok"))# varsayilan deger

# --- Kosul Ifadeleri ---
if yas >= 18:
    print("Yetiskin")
elif yas > 12:
    print("Ergen")
else:
    print("Cocuk")

# Ternary operator
durum = "Yetiskin" if yas >= 18 else "Cocuk"

# Match-case (Python 3.10+)
komut = "ekle"
match komut:
    case "ekle":
        print("Ekleniyor...")
    case "sil":
        print("Siliniyor...")
    case _:
        print("Bilinmeyen komut")

# --- Donguler ---
for i in range(5):
    print(i)                     # 0 1 2 3 4

for index, deger in enumerate(liste):
    print(f"{index}: {deger}")

for anahtar, deger in sozluk.items():
    print(f"{anahtar}: {deger}")

while yas > 0:
    yas -= 1

# --- Fonksiyonlar ---
def merhaba(kisi: str) -> str:
    """Belirtilen kisiye selam verir."""
    return f"Merhaba, {kisi}!"

# Varsayilan arguman
def us_al(taban, us=2):
    return taban ** us

# *args ve **kwargs
def topla(*sayilar):
    return sum(sayilar)

def bilgi_goster(**bilgiler):
    for k, v in bilgiler.items():
        print(f"{k}: {v}")

# Lambda (anonim fonksiyon)
kare = lambda x: x ** 2
print(kare(5))                   # 25

# Dekorator
def zaman_olcer(func):
    import time
    def wrapper(*args, **kwargs):
        basla = time.time()
        sonuc = func(*args, **kwargs)
        print(f"{func.__name__}: {time.time()-basla:.2f}s")
        return sonuc
    return wrapper

@zaman_olcer
def yavas_fonksiyon():
    import time; time.sleep(1)

# --- Sinif ve Nesne Yonelim ---
class Hayvan:
    tur = "memeli"               # sinif degiskeni

    def __init__(self, ad: str):
        self.ad = ad             # instance degiskeni

    def ses_cikar(self) -> str:
        return "..."

class Kopek(Hayvan):
    def __init__(self, ad: str, cins: str):
        super().__init__(ad)
        self.cins = cins

    def ses_cikar(self) -> str:
        return "Hav hav!"

# --- Hata Yakalama ---
try:
    sayi = int(input("Sayi: "))
    print(10 / sayi)
except ValueError:
    print("Gecerli bir sayi girin!")
except ZeroDivisionError:
    print("Sifira bolme hatasi!")
except Exception as e:
    print(f"Bilinmeyen hata: {e}")
finally:
    print("Bu blok her zaman calisir.")

# --- Module Sistemi ---
# from math import sqrt, pi
# import json
# import requests as req
# from datetime import datetime, timedelta

# --- Asenkron Programlama ---
import asyncio

async def veri_cek(url: str):
    await asyncio.sleep(1)       # simulasyon
    return f"{url} verisi"

async def main():
    sonuclar = await asyncio.gather(
        veri_cek("site1.com"),
        veri_cek("site2.com"),
    )
    print(sonuclar)

# asyncio.run(main())
```

## Yaygin Patternler

1. **List Comprehension**: `[x**2 for x in range(10) if x % 2 == 0]` -> tek satirda kosullu liste olusturma
2. **Dictionary Comprehension**: `{x: x**2 for x in range(5)}`
3. **Context Manager (with)**: `with open("dosya.txt") as f:` ile otomatik kaynak yonetimi
4. **Decorator Pattern**: Fonksiyonlara dinamik ozellik ekleme (loglama, zaman olcme, yetki kontrolu)
5. **Generator**: `def sayilar(): yield 1; yield 2` -> buyuk verilerde bellek verimliligi
6. **Duck Typing**: `Eger ordek gibi yuruyor ve ordek gibi ses cikariyorsa o bir ordektir`
7. **Singleton**: Metaclass veya modul seviyesinde tek ornek
8. **Factory Pattern**: Sinif/metot ile nesne olusturma merkezi
9. **Strategy Pattern**: Fonksiyon/strategy parametresi olarak gecme
10. **Observer Pattern**: Event system, signal/slot mekanizmasi
11. **Pipeline Pattern**: Fonksiyon zinciri ile veri isleme
12. **Mixin Pattern**: Coklu kalitim ile yetenek ekleme

```python
# Comprehension ornegi
cift_kareler = [x**2 for x in range(20) if x % 2 == 0]

# Generator ornegi
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Context manager ornegi (kendi yazma)
class Dosya:
    def __enter__(self):
        print("Dosya acildi")
        return self
    def __exit__(self, *args):
        print("Dosya kapandi")
```

## Onemli Kutuphaneler

1. **NumPy**: Sayisal hesaplama, N-boyutlu dizi islemleri
   `np.array([1,2,3]).mean()`
2. **Pandas**: Veri analizi, DataFrame yapisi
   `df.groupby("sehir")["gelir"].mean()`
3. **Matplotlib**: Veri gorsellestirme
   `plt.plot(x, y); plt.show()`
4. **Seaborn**: Istatistiksel gorsellestirme (Matplotlib ustune)
5. **Scikit-learn**: Makine ogrenmesi (siniflandirma, regresyon, kumeleme)
   `model = RandomForestClassifier(); model.fit(X, y)`
6. **TensorFlow / PyTorch**: Derin ogrenme frameworkleri
7. **Django**: Full-stack web framework (ORM, admin panel, auth)
8. **Flask**: Hafif web frameworku
   `app = Flask(__name__)`
9. **FastAPI**: Modern, hizli API frameworku (async, OpenAPI)
10. **Requests**: HTTP istekleri
    `requests.get("https://api.example.com").json()`
11. **Selenium / Playwright**: Tarayici otomasyonu ve web kazima
12. **BeautifulSoup / lxml**: HTML/XML ayristirma
13. **Pillow (PIL)**: Goruntu isleme
14. **OpenCV**: Bilgisayarli goru (goruntu/video isleme)
15. **SQLAlchemy / Django ORM**: Veritabani ORM
16. **Celery**: Zamanlanmis gorev kuyrugu ve asenkron islem
17. **Pydantic**: Veri dogrulama ve ayarlar yonetimi (type hints ile)
18. **pytest**: Test frameworku
    `pytest test_dosyasi.py -v`
19. **Logging (stdlib)**: Loglama sistemi
20. **Rich / Click**: CLI uygulamalari (renkli cikti, arguman)

```python
# Pandas ornegi
import pandas as pd
df = pd.read_csv("veri.csv")
print(df.describe())
print(df.isnull().sum())

# FastAPI ornegi
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"mesaj": "Merhaba API"}
```

## Yaygin Hatalar

1. **`==` ile `is` karistirmak**: `==` deger karsilastirir, `is` referans karsilastirir
   ```python
   a = [1, 2, 3]; b = [1, 2, 3]
   a == b  # True (deger)
   a is b  # False (farkli nesne)
   ```
2. **Mutable default argument**: `def func(lst=[])` -> lst her cagrida ayni nesne olur
   ```python
   def dogru_kullanim(lst=None):
       if lst is None:
           lst = []
       lst.append(1)
       return lst
   ```
3. **GIL farkinda olmamak**: Global Interpreter Lock, CPU-bounded islemlerde threading yerine multiprocessing kullanilmali
4. **`except:` ile tum hatalari yakalamak**: Specific exception kullanilmali (`except ValueError:`)
5. **Dosya acarken `with` kullanmamak**: `f = open(...)` -> unutulan `f.close()` kaynak sizintisi
6. **`copy` vs `deepcopy` karistirmak**: Icinek obje referanslari da kopyalanmazsa sorun olur
7. **Modifikasyon sirasinda liste uzerinde iterasyon**: `for x in listem: listem.remove(x)` -> atlama olur, kopya ile cozulur
8. **`is` ile None karsilastirmasi**: `if x is None` dogru, `if x == None` yanlis (custom `__eq__` override durumu)
9. **Integer vs float karistirmak**: `3/2` -> `1.5` (Python 3), `3//2` -> `1`
10. **Asenkron kodda `await` unutmak**: Coroutine obje doner, calismaz
11. **Global degisken degistirmek**: Fonksiyon icinde `global` anahtari gerekir
12. **`__init__` yerine `__init__` disinda init**: Konstruktor disinda baslatma yapmak

## Performans Ipuclari

1. **List comprehension kullanmak**: `for` dongusunden daha hizlidir
   ```python
   # Yavas
   kareler = []
   for i in range(1000):
       kareler.append(i**2)
   # Hizli
   kareler = [i**2 for i in range(1000)]
   ```

2. **`join()` ile string birlestirme**: `+` operatoru yerine `"".join(liste)` kullanmak
   ```python
   # Yavas (O(n^2))
   sonuc = ""
   for s in kelimeler:
       sonuc += s + " "
   # Hizli (O(n))
   sonuc = " ".join(kelimeler)
   ```

3. **`in` ile arama icin set kullanmak**: `listede in` O(n), `sette in` O(1)
4. **Generator kullanmak**: Buyuk verilerde bellek tuketimini azaltir
5. **Yerlesik fonksiyonlari kullanmak**: `map()`, `filter()`, `sum()`, `any()`, `all()` C seviyesinde calisir
6. **`__slots__` ile bellek tasarrufu**: Cok sayida obje olustururken siniflarda `__slots__` tanimlamak
7. **Profil kullanmak**: `cProfile` ile dar bogaz bulma

```python
# Set ile hizli arama
kullanici_idleri_set = set(kullanici_idleri)
if hedef_id in kullanici_idleri_set:  # O(1)
    print("Bulundu")
```

## Ekosistem

**Frameworkler**: Django (full-stack), Flask (mikro), FastAPI (API), Pyramid, Tornado, Sanic

**Araclar**: Jupyter Notebook/Lab (interaktif), pip (paket yoneticisi), virtualenv/venv (sanal ortam), conda (veri bilimi), mypy (tip kontrol), black (formatlama), isort (import sirala)

**Build/Package**: setuptools, wheel, pip, twine (PyPI yayin)

**Paket Yoneticisi**: pip, conda, poetry, pipenv

**Test**: pytest, unittest, nose2, tox

**CI/CD**: GitHub Actions, GitLab CI, Jenkins

**Surum Kontrol**: CPython (ana), PyPy (hizli), Cython (C eklentisi), Numba (JIT)

## Kaynaklar

**Resmi Dokuman**: docs.python.org (3. dili)

**Kitaplar**:
- Python ile Programlama - Fırat Ozgul
- Python 3 icin Turkce Kaynak - python-istihza
- Automate the Boring Stuff with Python
- Fluent Python (Luciano Ramalho)

**Web Siteleri**:
- realpython.com
- pythontutorial.net
- fullstackpython.com
- w3schools.com/python

**Interaktif Ogrenme**:
- exercism.org/tracks/python
- codingbat.com/python
- leetcode.com (problem cozme)
- codewars.com

**Topluluk**: reddit.com/r/Python, stackoverflow (python etiketi), Python Discord, Telegram gruplari, Python Istanbul
