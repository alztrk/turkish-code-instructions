# Python Bilgi Referansi

## Genel Bakis
Python, Guido van Rossum tarafindan 1991'de olusturulmus yuksek seviyeli, yorumlanan bir dildir. Veri bilimi, yapay zeka, web gelistirme (Django, Flask), otomasyon ve scripting alanlarinda yaygindir. Okunabilir syntax'i ve genis kutuphane ekosistemi ile bilinir.

## Temel Syntax

```python
# Degiskenler
isim = "Ali"
yas = 25
pi = 3.14
aktif = True

# Fonksiyon
def merhaba(kisi):
    return f"Merhaba, {kisi}!"

# Kosul
if yas >= 18:
    print("Yetiskin")
elif yas > 12:
    print("Ergen")
else:
    print("Cocuk")

# Donguler
for i in range(5):
    print(i)

# Liste
meyveler = ["elma", "armut", "muz"]
meyveler.append("cilek")
```

## Yaygin Patternler

- List comprehension: `[x**2 for x in range(10) if x % 2 == 0]`
- Context manager: `with open("dosya.txt") as f:`
- Duck typing: "Eger ordek gibi yuruyor ve ordek gibi ses cikariyorsa, o bir ordektir."
- Decorator: Fonksiyonlara dinamik ozellik ekleme
- `__str__` ve `__repr__` ozel metodlari

## Onemli Kutuphaneler

- **NumPy**: Sayisal hesaplama, dizi islemleri
- **Pandas**: Veri analizi, DataFrame
- **Matplotlib/Seaborn**: Veri gorsellestirme
- **Scikit-learn**: Makine ogrenmesi
- **Django/Flask**: Web gelistirme
- **Requests**: HTTP istekleri
- **Selenium**: Tarayici otomasyonu

## Yaygin Hatalar

- `==` ile `is` karistirmak (deger vs referans karsilastirmasi)
- mutable default argument: `def func(lst=[]) ` yerine `def func(lst=None)`
- Global Interpreter Lock (GIL) farkinda olmamak
- `except:` ile tum hatali yakalamak (specific olmali)
- Dosya acarken `with` kullanmamak
