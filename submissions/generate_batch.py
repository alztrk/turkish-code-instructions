import json

items = []

# ============ PYTHON (10) ============

items.append({
    "instruction": "Bir decorator yaz: herhangi bir fonksiyonun calisma suresini olcup 'Fonksiyon {isim} {sure} saniye surdu' seklinde yazdiran bir @timer decorator'i olusturun. Decorator, *args ve **kwargs ile calismali.",
    "response": "import time\nimport functools\n\ndef timer(func):\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        baslangic = time.perf_counter()\n        sonuc = func(*args, **kwargs)\n        gecen = time.perf_counter() - baslangic\n        print(f\"Fonksiyon {func.__name__} {gecen:.4f} saniye surdu\")\n        return sonuc\n    return wrapper\n\n@timer\ndef hesapla(n):\n    toplam = 0\n    for i in range(n):\n        toplam += i ** 2\n    return toplam\n\nprint(hesapla(10_000_000))",
    "language": "python",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Bir generator fonksiyonu olan fibonacci(n) yazin. n'e kadar olan Fibonacci sayilarini yield ile uretsin. Ardindan bu generator'u kullanarak ilk 20 Fibonacci sayisini bir listeye cevirip yazdirin.",
    "response": "def fibonacci(n):\n    a, b = 0, 1\n    while a < n:\n        yield a\n        a, b = b, a + b\n\nfib_gen = fibonacci(10000)\nilk_20 = [next(fib_gen) for _ in range(20)]\nprint(ilk_20)",
    "language": "python",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "with blogu ile kullanilabilen bir DosyaYoneticisi context manager'i yazin. __enter__ dosyayi acsin, __exit__ dosyayi kapatsin ve hata varsa 'Hata olustu: {hata_tipi}' yazip True dondurerek hatayi yutmayi saglasin.",
    "response": "class DosyaYoneticisi:\n    def __init__(self, dosya_adi, mod):\n        self.dosya_adi = dosya_adi\n        self.mod = mod\n        self.dosya = None\n\n    def __enter__(self):\n        self.dosya = open(self.dosya_adi, self.mod, encoding='utf-8')\n        return self.dosya\n\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        if self.dosya:\n            self.dosya.close()\n        if exc_type is not None:\n            print(f\"Hata olustu: {exc_type.__name__}\")\n            return True\n        return False\n\nwith DosyaYoneticisi('ornek.txt', 'w') as f:\n    f.write('Merhaba Dunya')\n\nwith DosyaYoneticisi('olmayan.txt', 'r') as f:\n    icerik = f.read()",
    "language": "python",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Verilen bir sayi listesinde; cift sayilari 2 ile carpip, tek sayilari oldugu gibi birakan bir liste comprehension yazin. Ayrica sadece 3'e bolunen sayilari filtreleyen bir dict comprehension ile kuplerini sozluk olarak olusturun.",
    "response": "sayilar = [1, 3, 6, 8, 9, 12, 15, 18, 20]\n\nislenmis = [x * 2 if x % 2 == 0 else x for x in sayilar]\nprint(f\"Islenmis liste: {islenmis}\")\n\nkup_sozluk = {x: x ** 3 for x in sayilar if x % 3 == 0}\nprint(f\"3'e bolunenlerin kupleri: {kup_sozluk}\")",
    "language": "python",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "map, filter ve reduce kullanarak su islemi yapin: Bir tam sayi listesindeki tek sayilari filtreleyip, her birinin karesini alin ve son olarak tum bu karelerin toplamini reduce ile hesaplayin. Lambda fonksiyonlari kullanin.",
    "response": "from functools import reduce\n\nsayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n\ntek_karesi = map(lambda x: x ** 2, filter(lambda x: x % 2 == 1, sayilar))\ntoplam = reduce(lambda a, b: a + b, tek_karesi)\n\nprint(f\"Tek sayilarin kareleri toplami: {toplam}\")",
    "language": "python",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Sinif hiyerarsisi olusturun: abstract base class Hayvan (isim, ses_cikar abstract metodu), ondan tureyen Memeli (dogurma ozelligi) ve Kusu (yumurtla metodu) siniflarini yazin. Son olarak Yarasam, hem Memeli hem Kusu'dan coklu kalitim alsin ve ses_cikar'i implemente etsin.",
    "response": "from abc import ABC, abstractmethod\n\nclass Hayvan(ABC):\n    def __init__(self, isim):\n        self.isim = isim\n\n    @abstractmethod\n    def ses_cikar(self):\n        pass\n\nclass Memeli(Hayvan):\n    def dogurma(self):\n        return f\"{self.isim} yavru dogurdu\"\n\nclass Kusu(Hayvan):\n    def yumurtla(self):\n        return f\"{self.isim} yumurtladi\"\n\nclass Yarasam(Memeli, Kusu):\n    def ses_cikar(self):\n        return \"Cit cit!\"\n\ny = Yarasam(\"Golge\")\nprint(y.ses_cikar())\nprint(y.dogurma())\nprint(y.yumurtla())\nprint(Yarasam.__mro__)",
    "language": "python",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "__str__, __repr__, __len__, __getitem__, __add__ magic metodlarini uygulayan bir OzelListe sinifi yazin. Bu sinif, bir listeyi sarar (wrap) ve dilimleme, toplama, uzunluk alma gibi islemleri desteklesin.",
    "response": "class OzelListe:\n    def __init__(self, elemanlar):\n        self.elemanlar = list(elemanlar)\n\n    def __str__(self):\n        return f\"OzelListe({self.elemanlar})\"\n\n    def __repr__(self):\n        return f\"OzelListe({self.elemanlar!r})\"\n\n    def __len__(self):\n        return len(self.elemanlar)\n\n    def __getitem__(self, index):\n        if isinstance(index, slice):\n            return OzelListe(self.elemanlar[index])\n        return self.elemanlar[index]\n\n    def __add__(self, other):\n        if isinstance(other, OzelListe):\n            return OzelListe(self.elemanlar + other.elemanlar)\n        return NotImplemented\n\nl1 = OzelListe([1, 2, 3])\nl2 = OzelListe([4, 5])\nprint(l1 + l2)\nprint(l1[1:])\nprint(len(l1))",
    "language": "python",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "itertools.product, itertools.permutations, itertools.combinations ve itertools.cycle kullanarak su islemleri yapin: 1) 'A','B','C' harflerinin 2'li permutasyonlari, 2) [1,2,3,4] kumesinin 3'lu kombinasyonlari, 3) iki zar atisindaki tum olasiliklar (product).",
    "response": "from itertools import product, permutations, combinations, cycle\n\nharfler = ['A', 'B', 'C']\nprint(\"2'li permutasyonlar:\", list(permutations(harfler, 2)))\n\nsayilar = [1, 2, 3, 4]\nprint(\"3'lu kombinasyonlar:\", list(combinations(sayilar, 3)))\n\nzar = [1, 2, 3, 4, 5, 6]\nprint(\"Iki zar olasiliklari:\", list(product(zar, repeat=2)))\n\nsonsuz = cycle(['a', 'b', 'c'])\nprint(\"Ilk 5 cycle:\", [next(sonsuz) for _ in range(5)])",
    "language": "python",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "functools modulunden partial, lru_cache ve wraps kullanimini gosteren bir ornek yazin. lru_cache ile fibonacci hesaplamasini hizlandirin, partial ile sabit argumanli fonksiyon olusturun ve wraps ile decorator metadata koruyun.",
    "response": "from functools import partial, lru_cache, wraps\n\n@lru_cache(maxsize=128)\ndef fibonacci(n):\n    if n < 2:\n        return n\n    return fibonacci(n - 1) + fibonacci(n - 2)\n\ndef loglama(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        print(f\"{func.__name__} cagrildi: args={args}\")\n        return func(*args, **kwargs)\n    return wrapper\n\n@loglama\ndef us_al(taban, us):\n    return taban ** us\n\niki_uzerinden = partial(us_al, taban=2)\n\nprint(f\"fibonacci(50) = {fibonacci(50)}\")\nprint(f\"fibonacci hit info: {fibonacci.cache_info()}\")\nprint(f\"2^10 = {iki_uzerinden(10)}\")\nprint(f\"3^4 = {us_al(3, 4)}\")",
    "language": "python",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "threading modulu ile 3 adet thread olusturun. Her thread 1'den 5'e kadar sayilari yazdirsin, threadler arasinda Lock kullanarak ciktilarin karismasini engelleyin. Ayrica ThreadPoolExecutor ile bir url listesini paralel isleyin.",
    "response": "import threading\nfrom concurrent.futures import ThreadPoolExecutor\nimport time\n\nyazdirma_kilidi = threading.Lock()\n\ndef guvenli_yazdirma(isim, baslangic):\n    for i in range(baslangic, baslangic + 5):\n        with yazdirma_kilidi:\n            print(f\"Thread-{isim}: {i}\")\n        time.sleep(0.1)\n\nthreadler = []\nfor idx in range(3):\n    t = threading.Thread(target=guvenli_yazdirma, args=(idx, idx * 10))\n    threadler.append(t)\n    t.start()\n\nfor t in threadler:\n    t.join()\n\nprint(\"\\n--- ThreadPoolExecutor ornegi ---\")\n\ndef url_getir(url):\n    time.sleep(0.5)\n    return f\"{url} verisi alindi\"\n\nurls = [\"https://site1.com\", \"https://site2.com\", \"https://site3.com\"]\n\nwith ThreadPoolExecutor(max_workers=3) as havuz:\n    sonuclar = list(havuz.map(url_getir, urls))\n\nfor sonuc in sonuclar:\n    print(sonuc)",
    "language": "python",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

# ============ JAVASCRIPT (6) ============

items.append({
    "instruction": "Bir closure ornegi yazin: dis_fonksiyon adinda bir fonksiyon olusturun. Bu fonksiyon bir sayac degeri alsin ve icteki fonksiyon her cagrildiginda sayaci 1 artirip dondursun. Ayni pattern ile 3 bagimsiz sayac olusturun ve her birini farkli miktarlarda cagirin.",
    "response": "function sayaOlustur(baslangic) {\n    let sayac = baslangic;\n    return function() {\n        sayac += 1;\n        return sayac;\n    };\n}\n\nconst saya1 = sayaOlustur(0);\nconst saya2 = sayaOlustur(100);\nconst saya3 = sayaOlustur(50);\n\nconsole.log(`saya1: ${saya1()}`);\nconsole.log(`saya1: ${saya1()}`);\nconsole.log(`saya2: ${saya2()}`);\nconsole.log(`saya3: ${saya3()}`);\nconsole.log(`saya3: ${saya3()}`);\nconsole.log(`saya2: ${saya2()}`);\nconsole.log(`saya1 son: ${saya1()}`);",
    "language": "javascript",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Promise ve async/await kullanarak su senaryoyu kodlayin: once kullaniciBul(id) 1 sn'de kullanici dondursun, sonra siparisleriniGetir(userId) 1.5 sn'de siparisleri getirsin, en son siparisDetaylari(orderId) 1 sn'de detaylari getirsin. Zincirleme Promise ve ardindan async/await ile iki versiyonunu yazin.",
    "response": "function kullaniciBul(id) {\n    return new Promise(resolve =>\n        setTimeout(() => resolve({ id, ad: 'Ali', email: 'ali@ornek.com' }), 1000)\n    );\n}\n\nfunction siparisleriGetir(userId) {\n    return new Promise(resolve =>\n        setTimeout(() => resolve([{ id: 101, urun: 'Laptop' }, { id: 102, urun: 'Fare' }]), 1500)\n    );\n}\n\nfunction siparisDetaylari(orderId) {\n    return new Promise(resolve =>\n        setTimeout(() => resolve({ orderId, durum: 'Kargoya verildi', tarih: '2024-01-15' }), 1000)\n    );\n}\n\nkullaniciBul(1)\n    .then(kullanici => {\n        console.log('Kullanici:', kullanici);\n        return siparisleriGetir(kullanici.id);\n    })\n    .then(siparisler => {\n        console.log('Siparisler:', siparisler);\n        return siparisDetaylari(siparisler[0].id);\n    })\n    .then(detay => console.log('Siparis Detayi:', detay));\n\nasync function siparisDetayiniGetir(kullaniciId) {\n    try {\n        const kullanici = await kullaniciBul(kullaniciId);\n        console.log('Kullanici:', kullanici);\n        const siparisler = await siparisleriGetir(kullanici.id);\n        console.log('Siparisler:', siparisler);\n        const detay = await siparisDetaylari(siparisler[0].id);\n        console.log('Siparis Detayi:', detay);\n        return detay;\n    } catch (hata) {\n        console.error('Hata:', hata);\n    }\n}\n\nsiparisDetayiniGetir(1);",
    "language": "javascript",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Prototype kalitimi kullanarak bir Hayvan → Memeli → Kopek zinciri olusturun. Her seviyede yeni ozellik/metot ekleyin (Hayvan: canliMi=true, Memeli: sutVer(), Kopek: havla()). Object.create ile prototype zincirini kurun.",
    "response": "const Hayvan = {\n    canliMi: true,\n    nefesAl: function() {\n        return 'Nefes aliyorum';\n    },\n    init: function(isim) {\n        this.isim = isim;\n        return this;\n    }\n};\n\nconst Memeli = Object.create(Hayvan);\nMemeli.sutVer = function() {\n    return `${this.isim} sut veriyor`;\n};\nMemeli.tuyluMu = true;\n\nconst Kopek = Object.create(Memeli);\nKopek.havla = function() {\n    return `${this.isim}: Hav hav!`;\n};\nKopek.bacakSayisi = 4;\n\nconst karabas = Object.create(Kopek).init('Karabas');\nconsole.log(karabas.havla());\nconsole.log(karabas.sutVer());\nconsole.log(karabas.nefesAl());\nconsole.log(karabas.canliMi);\nconsole.log(karabas.bacakSayisi);\nconsole.log(Hayvan.isPrototypeOf(karabas));\nconsole.log(Kopek.isPrototypeOf(karabas));",
    "language": "javascript",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "ES6 modulleri (import/export) ile bir matematik kutuphanesi olusturun. Bir modulde topla, carp, bol fonksiyonlarini export edin (default ve named export karisik kullanarak). Ana dosyada import edip kullanin. Ayrica re-export ile bir ara modul yapin.",
    "response": "// math/aritmetik.js\nexport function topla(...sayilar) {\n    return sayilar.reduce((a, b) => a + b, 0);\n}\n\nexport function carp(...sayilar) {\n    return sayilar.reduce((a, b) => a * b, 1);\n}\n\nexport default function bol(a, b) {\n    if (b === 0) throw new Error('Sifira bolunemez');\n    return a / b;\n}\n\n// math/geometri.js\nexport function daireAlan(yaricap) {\n    return Math.PI * yaricap ** 2;\n}\n\nexport function dikdortgenAlan(genislik, yukseklik) {\n    return genislik * yukseklik;\n}\n\n// math/index.js (re-export)\nexport { topla, carp } from './aritmetik.js';\nexport { default as bolme } from './aritmetik.js';\nexport { daireAlan, dikdortgenAlan } from './geometri.js';",
    "language": "javascript",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "reduce metodunu kullanarak su islemleri gerceklestirin: 1) Bir dizideki kelimelerin frekansini cikaran bir fonksiyon, 2) Ic ice diziyi (nested array) duzlestiren (flatten) bir fonksiyon, 3) Bir nesne dizisini belirli bir anahtara gore gruplandiran bir fonksiyon.",
    "response": "const kelimeler = ['elma', 'armut', 'elma', 'kiraz', 'armut', 'elma'];\n\nconst frekans = kelimeler.reduce((acc, kelime) => {\n    acc[kelime] = (acc[kelime] || 0) + 1;\n    return acc;\n}, {});\nconsole.log('Frekans:', frekans);\n\nconst icIceDizi = [1, [2, 3], [4, [5, 6]], 7];\n\nfunction duzlestir(dizi) {\n    return dizi.reduce((acc, eleman) => {\n        return acc.concat(Array.isArray(eleman) ? duzlestir(eleman) : eleman);\n    }, []);\n}\nconsole.log('Duzlestirilmis:', duzlestir(icIceDizi));\n\nconst kullanicilar = [\n    { ad: 'Ali', sehir: 'Istanbul' },\n    { ad: 'Veli', sehir: 'Ankara' },\n    { ad: 'Ayse', sehir: 'Istanbul' },\n    { ad: 'Fatma', sehir: 'Ankara' }\n];\n\nconst gruplanmis = kullanicilar.reduce((acc, kullanici) => {\n    (acc[kullanici.sehir] = acc[kullanici.sehir] || []).push(kullanici);\n    return acc;\n}, {});\nconsole.log('Gruplanmis:', gruplanmis);",
    "language": "javascript",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Proxy ve Symbol kullanarak bir nesnenin tum property'lerine erisimi loglayan ve property silme islemini engelleyen bir korumali nesne olusturun. Ayrica Symbol.iterator ile bir nesneyi iterate edilebilir yapin.",
    "response": "const korumaliHandler = {\n    get: function(hedef, prop) {\n        console.log(`[ERISIM] ${String(prop)} okundu`);\n        if (prop in hedef) {\n            return hedef[prop];\n        }\n        return `Property '${String(prop)}' bulunamadi`;\n    },\n    set: function(hedef, prop, deger) {\n        console.log(`[GUNCELLEME] ${String(prop)} = ${deger}`);\n        hedef[prop] = deger;\n        return true;\n    },\n    deleteProperty: function(hedef, prop) {\n        console.log(`[ENGELLENDI] ${String(prop)} silinemez!`);\n        return false;\n    }\n};\n\nconst kullanici = new Proxy({ ad: 'Ali', yas: 30 }, korumaliHandler);\nconsole.log(kullanici.ad);\nkullanici.yas = 31;\ndelete kullanici.ad;\n\nconst takim = {\n    uyeler: ['Ali', 'Veli', 'Ayse', 'Fatma'],\n    [Symbol.iterator]: function* () {\n        for (const uye of this.uyeler) {\n            yield uye;\n        }\n    }\n};\n\nfor (const uye of takim) {\n    console.log('Takim uyesi:', uye);\n}",
    "language": "javascript",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

# ============ JAVA (5) ============

items.append({
    "instruction": "Stream API ve lambda ifadeleri kullanarak bir ogrenci listesini filtreleyin, siralayin ve donusturun. Ogrenci sinifi (isim, notOrtalamasi, bolum) alanlarina sahip olsun. Not ortalamasi 70'in uzerindeki ogrencileri notlarina gore azalan siralayip, sadece isimlerini ve bolumlerini iceren yeni bir listeye map'leyin.",
    "response": "import java.util.*;\nimport java.util.stream.*;\n\nclass Ogrenci {\n    private String isim;\n    private double notOrtalamasi;\n    private String bolum;\n    public Ogrenci(String isim, double notOrtalamasi, String bolum) {\n        this.isim = isim; this.notOrtalamasi = notOrtalamasi; this.bolum = bolum;\n    }\n    public String getIsim() { return isim; }\n    public double getNotOrtalamasi() { return notOrtalamasi; }\n    public String getBolum() { return bolum; }\n}\n\nclass OgrenciDTO {\n    private String isim;\n    private String bolum;\n    public OgrenciDTO(String isim, String bolum) {\n        this.isim = isim; this.bolum = bolum;\n    }\n    @Override\n    public String toString() { return isim + \" - \" + bolum; }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        List<Ogrenci> ogrenciler = Arrays.asList(\n            new Ogrenci(\"Ali\", 85.5, \"Bilgisayar Muh.\"),\n            new Ogrenci(\"Veli\", 45.0, \"Elektrik Muh.\"),\n            new Ogrenci(\"Ayse\", 92.3, \"Bilgisayar Muh.\"),\n            new Ogrenci(\"Fatma\", 70.5, \"Makine Muh.\"),\n            new Ogrenci(\"Mehmet\", 60.0, \"Insaat Muh.\"),\n            new Ogrenci(\"Zeynep\", 88.0, \"Endustri Muh.\")\n        );\n\n        List<OgrenciDTO> basariliOgrenciler = ogrenciler.stream()\n            .filter(o -> o.getNotOrtalamasi() > 70)\n            .sorted(Comparator.comparingDouble(Ogrenci::getNotOrtalamasi).reversed())\n            .map(o -> new OgrenciDTO(o.getIsim(), o.getBolum()))\n            .collect(Collectors.toList());\n\n        System.out.println(\"Basariili ogrenciler (not > 70):\");\n        basariliOgrenciler.forEach(System.out::println);\n    }\n}",
    "language": "java",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Optional kullanarak null-safe bir zincirleme islem yazin. Bir kullanici nesnesi (adres, sehir) alanlarini icersin. Optional.ofNullable ile ic ice gecmis Optional'lari flatMap ile birlestirip, orElseThrow ile hata firlatin. Ayrica orElse, ifPresent ve filter kullanimini da gosterin.",
    "response": "import java.util.Optional;\n\nclass Adres {\n    private String sehir;\n    private String ilce;\n    public Adres(String sehir, String ilce) { this.sehir = sehir; this.ilce = ilce; }\n    public String getSehir() { return sehir; }\n    public String getIlce() { return ilce; }\n}\n\nclass Kullanici {\n    private String isim;\n    private Adres adres;\n    public Kullanici(String isim, Adres adres) { this.isim = isim; this.adres = adres; }\n    public Optional<Adres> getAdres() { return Optional.ofNullable(adres); }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Kullanici k1 = new Kullanici(\"Ali\", new Adres(\"Istanbul\", \"Kadikoy\"));\n        Kullanici k2 = new Kullanici(\"Veli\", null);\n        Kullanici k3 = null;\n\n        String sehir = Optional.ofNullable(k1)\n            .flatMap(Kullanici::getAdres)\n            .map(Adres::getSehir)\n            .orElse(\"Bilinmiyor\");\n        System.out.println(\"K1 sehri: \" + sehir);\n\n        try {\n            Optional.ofNullable(k2)\n                .flatMap(Kullanici::getAdres)\n                .map(Adres::getSehir)\n                .orElseThrow(() -> new RuntimeException(\"Adres bulunamadi\"));\n        } catch (Exception e) {\n            System.out.println(\"Hata: \" + e.getMessage());\n        }\n\n        Optional.ofNullable(k3).ifPresentOrElse(\n            k -> System.out.println(\"Kullanici var: \" + k),\n            () -> System.out.println(\"Kullanici null\")\n        );\n\n        Optional.ofNullable(k1)\n            .flatMap(Kullanici::getAdres)\n            .filter(a -> a.getSehir().equals(\"Istanbul\"))\n            .ifPresent(a -> System.out.println(\"Istanbul'da yasiyor: \" + a.getIlce()));\n    }\n}",
    "language": "java",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "CompletableFuture kullanarak 3 farkli asenkron gorevi paralel calistirip sonuclarini birlestirin. allOf ile tum gorevlerin bitmesini bekleyin, ardindan thenApply ile sonuclari isleyin. Ayrica exceptionally ile hata yonetimi ve thenCompose ile zincirleme islem yapin.",
    "response": "import java.util.concurrent.*;\nimport java.util.stream.*;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        CompletableFuture<Integer> s1 = CompletableFuture.supplyAsync(() -> { sleep(1000); return 250; });\n        CompletableFuture<Integer> s2 = CompletableFuture.supplyAsync(() -> { sleep(1500); return 180; });\n        CompletableFuture<Integer> s3 = CompletableFuture.supplyAsync(() -> { sleep(800); return 320; });\n\n        CompletableFuture<Integer> toplamFuture = CompletableFuture\n            .allOf(s1, s2, s3)\n            .thenApply(v -> Stream.of(s1, s2, s3).map(CompletableFuture::join).mapToInt(Integer::intValue).sum());\n        System.out.println(\"Toplam: \" + toplamFuture.get() + \" TL\");\n\n        CompletableFuture<String> hatali = CompletableFuture\n            .supplyAsync(() -> { if (Math.random() > 0.5) throw new RuntimeException(\"Hata!\"); return \"OK\"; })\n            .exceptionally(e -> \"Hata: \" + e.getMessage())\n            .thenApply(s -> \"Sonuc: \" + s);\n        System.out.println(hatali.get());\n\n        CompletableFuture<String> zincir = CompletableFuture\n            .supplyAsync(() -> \"Kullanici-42\")\n            .thenCompose(id -> CompletableFuture.supplyAsync(() -> id + \" verileri yuklendi\"));\n        System.out.println(zincir.get());\n    }\n    static void sleep(int ms) { try { Thread.sleep(ms); } catch (InterruptedException e) {} }\n}",
    "language": "java",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "FunctionalInterface kullanarak kendi fonksiyonel arayuzunuzu olusturun (Donusturucu<T,R>). Lambda ifadeleri, method referanslari ve Stream ile birlikte kullanin. Ayrica Consumer, Supplier, Function ve Predicate gibi hazir fonksiyonel arayuzleri ornekleyin.",
    "response": "import java.util.*;\nimport java.util.function.*;\nimport java.util.stream.*;\n\n@FunctionalInterface\ninterface Donusturucu<T, R> {\n    R donustur(T girdi);\n    default Donusturucu<T, R> once(Consumer<T> islem) {\n        return t -> { islem.accept(t); return donustur(t); };\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Donusturucu<String, Integer> uzunluk = String::length;\n        Donusturucu<String, String> buyukHarfeCevir = String::toUpperCase;\n        System.out.println(\"Uzunluk: \" + uzunluk.donustur(\"Merhaba\"));\n        System.out.println(\"Buyuk harf: \" + buyukHarfeCevir.donustur(\"merhaba\"));\n\n        Consumer<String> yazdir = System.out::println;\n        yazdir.accept(\"Consumer ornegi\");\n\n        Supplier<Double> rastgele = Math::random;\n        System.out.println(\"Rastgele: \" + rastgele.get());\n\n        Function<Integer, Integer> kare = x -> x * x;\n        Function<Integer, Integer> ikiEkle = x -> x + 2;\n        System.out.println(\"Once kare sonra +2: \" + kare.andThen(ikiEkle).apply(5));\n\n        Predicate<Integer> ciftMi = x -> x % 2 == 0;\n        List<Integer> sayilar = Arrays.asList(1, 2, 3, 4, 5, 6);\n        System.out.println(\"Cift sayilar: \" + sayilar.stream().filter(ciftMi).collect(Collectors.toList()));\n    }\n}",
    "language": "java",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Enum icinde metot ve alan tanimlayarak bir HaftalikMesai enum'u olusturun. Her gun icin calisma saati (int) ve mesai tipi (TAM/YARIM) bilgisini tutsun. Enum'un icinde bir hesaplaMaas(int saatlikUcret) metodu olsun. Ayrica enum sabitlerini Stream ile isleyin.",
    "response": "import java.util.stream.*;\n\nenum HaftalikMesai {\n    PAZARTESI(8, MesaiTipi.TAM), SALI(8, MesaiTipi.TAM), CARSAMBA(8, MesaiTipi.TAM),\n    PERSEMBE(8, MesaiTipi.TAM), CUMA(6, MesaiTipi.YARIM),\n    CUMARTESI(0, MesaiTipi.TATIL), PAZAR(0, MesaiTipi.TATIL);\n\n    enum MesaiTipi { TAM, YARIM, TATIL }\n    private final int calismaSaati;\n    private final MesaiTipi tip;\n\n    HaftalikMesai(int calismaSaati, MesaiTipi tip) {\n        this.calismaSaati = calismaSaati; this.tip = tip;\n    }\n    public int getCalismaSaati() { return calismaSaati; }\n    public MesaiTipi getTip() { return tip; }\n    public double hesaplaMaas(int saatlikUcret) { return calismaSaati * saatlikUcret; }\n    public static int haftalikToplamSaat() {\n        return Stream.of(values()).mapToInt(HaftalikMesai::getCalismaSaati).sum();\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        int ucret = 150;\n        for (HaftalikMesai gun : HaftalikMesai.values()) {\n            System.out.printf(\"%s: %d saat -> %.0f TL%n\", gun, gun.getCalismaSaati(), gun.hesaplaMaas(ucret));\n        }\n        System.out.println(\"Haftalik toplam: \" + HaftalikMesai.haftalikToplamSaat() + \" saat\");\n        double toplamMaas = Stream.of(HaftalikMesai.values()).mapToDouble(g -> g.hesaplaMaas(ucret)).sum();\n        System.out.println(\"Haftalik maas: \" + toplamMaas + \" TL\");\n    }\n}",
    "language": "java",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

# ============ TYPESCRIPT (4) ============

items.append({
    "instruction": "Conditional Types ve Generic Constraints kullanarak bir tur yardimcisi (utility type) yazin. ExtractPropertyNamesOfType<T, U> ile T tipindeki U turundeki property'lerin isimlerini cikarsin. Ayrica DeepReadonly<T> ile tum ic ice property'leri readonly yapan bir mapped type olusturun.",
    "response": "type ExtractPropertyNamesOfType<T, U> = {\n    [K in keyof T]: T[K] extends U ? K : never;\n}[keyof T];\n\ntype DeepReadonly<T> = {\n    readonly [K in keyof T]: T[K] extends object\n        ? T[K] extends Function ? T[K] : DeepReadonly<T[K]>\n        : T[K];\n};\n\ninterface Kullanici {\n    ad: string; yas: number; email: string; dogumTarihi: Date; aktifMi: boolean;\n}\n\ntype StringKeys = ExtractPropertyNamesOfType<Kullanici, string>;\ntype NumberKeys = ExtractPropertyNamesOfType<Kullanici, number>;\n\ninterface Config {\n    sunucu: { host: string; port: number; kimlik: { kullaniciAdi: string; sifre: string; }; };\n    ayarlar: { tema: string; dil: string; };\n}\n\ntype SabitConfig = DeepReadonly<Config>;\n\nconst config: SabitConfig = {\n    sunucu: { host: \"localhost\", port: 8080, kimlik: { kullaniciAdi: \"admin\", sifre: \"1234\" } },\n    ayarlar: { tema: \"karanlik\", dil: \"tr\" }\n};",
    "language": "typescript",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Mapped Types ve Template Literal Types kullanarak bir API yanit tipi olusturun. Tum CRUD metotlari icin ({entity}Get, {entity}Post, {entity}Put, {entity}Delete) tiplerini otomatik ureten bir generic yazin. Ayrica bir entity tipinden event tipleri olusturun.",
    "response": "type CrudEndpoints<T extends string> = {\n    [K in T as `${Capitalize<K>}GetRequest`]: { id: number };\n    [K in T as `${Capitalize<K>}GetResponse`]: Record<string, unknown>;\n    [K in T as `${Capitalize<K>}PostRequest`]: Record<string, unknown>;\n    [K in T as `${Capitalize<K>}PostResponse`]: { id: number };\n    [K in T as `${Capitalize<K>}PutRequest`]: { id: number } & Record<string, unknown>;\n    [K in T as `${Capitalize<K>}PutResponse`]: { success: boolean };\n    [K in T as `${Capitalize<K>}DeleteRequest`]: { id: number };\n    [K in T as `${Capitalize<K>}DeleteResponse`]: { success: boolean };\n};\n\ntype EntityEvents<T extends string> = {\n    [K in T as `${Capitalize<K>}Created`]: { entityId: number; timestamp: Date };\n    [K in T as `${Capitalize<K>}Updated`]: { entityId: number; degisenAlanlar: string[]; timestamp: Date };\n    [K in T as `${Capitalize<K>}Deleted`]: { entityId: number; timestamp: Date };\n};\n\ntype FullApi<T extends string> = CrudEndpoints<T> & EntityEvents<T>;\ntype KullaniciApi = FullApi<\"kullanici\">;\n\ndeclare const brand: unique symbol;\ntype Branded<T, B> = T & { [brand]: B };\ntype KullaniciId = Branded<number, \"KullaniciId\">;\nfunction kullaniciBul(id: KullaniciId): string { return `Kullanici ${String(id)}`; }\nconst kid = 42 as KullaniciId;",
    "language": "typescript",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Discriminated Unions, satisfies operator ve never tipi ile exhaustive type checking yapin. Bir API'dan donen farkli response tiplerini discriminator ile ayirt edin. satisfies ile bir nesnenin belirli bir tipe uydugunu dogrulayin.",
    "response": "type ApiResponse =\n    | { durum: \"basarili\"; veri: unknown; mesaj: string }\n    | { durum: \"hata\"; hataKodu: number; hataMesaji: string }\n    | { durum: \"yukleniyor\"; yuzde: number }\n    | { durum: \"abort\"; sebep: string };\n\nfunction apiHandler(yanit: ApiResponse): string {\n    switch (yanit.durum) {\n        case \"basarili\": return `Basariili: ${yanit.mesaj} - ${JSON.stringify(yanit.veri)}`;\n        case \"hata\": return `Hata ${yanit.hataKodu}: ${yanit.hataMesaji}`;\n        case \"yukleniyor\": return `Yukleniyor: %${yanit.yuzde}`;\n        case \"abort\": return `Iptal: ${yanit.sebep}`;\n        default: const _exhaustiveCheck: never = yanit; return _exhaustiveCheck;\n    }\n}\n\ninterface Kullanici { ad: string; yas: number; email: string; }\nconst kullanici = { ad: \"Ali\", yas: 30, email: \"ali@ornek.com\" } satisfies Kullanici;\n\nconst yapilandirma = {\n    apiUrl: \"https://api.ornek.com\",\n    timeout: 5000,\n    retryCount: 3\n} satisfies Record<string, string | number>;",
    "language": "typescript",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Infer keyword'unu kullanarak Conditional Types ile ReturnType, PromiseType ve ArrayElementType gibi yardimci tipler yazin. Ayni zamanda FunctionArguments tipi ile fonksiyon parametrelerini cikarsayin.",
    "response": "type MyReturnType<T> = T extends (...args: unknown[]) => infer R ? R : never;\ntype PromiseType<T> = T extends Promise<infer U> ? U : T;\ntype ArrayElementType<T> = T extends (infer U)[] ? U : never;\ntype FunctionArguments<T> = T extends (...args: infer A) => unknown ? A : never;\n\nfunction kullaniciGetir(id: number, page: number): Promise<string[]> {\n    return Promise.resolve([\"Ali\", \"Veli\"]);\n}\nfunction toplama(...sayilar: number[]): number {\n    return sayilar.reduce((a, b) => a + b, 0);\n}\n\ntype R1 = MyReturnType<typeof kullaniciGetir>;\ntype R2 = PromiseType<R1>;\ntype R3 = ArrayElementType<R2>;\ntype R4 = FunctionArguments<typeof kullaniciGetir>;\ntype R5 = FunctionArguments<typeof toplama>;\n\nconst args: R4 = [1, 10];\nconst eleman: R3 = \"test\";\n\nclass VeriServisi {\n    async veriKaydet<T>(veri: T, kimlik: string): Promise<T> { return veri; }\n}\ntype KaydetArgs = FunctionArguments<VeriServisi[\"veriKaydet\"]>;\ntype KaydetReturn = MyReturnType<VeriServisi[\"veriKaydet\"]>;",
    "language": "typescript",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

# ============ GO (5) ============

items.append({
    "instruction": "Goroutines ve channels kullanarak bir isci havuzu (worker pool) olusturun. 5 isci (worker), 20 isi (job) paralel olarak issin. Her isci bir isi alip islesin ve sonucu bir result kanalina gondesin. sync.WaitGroup ile tum iscilerin bitmesini bekleyin.",
    "response": 'package main\n\nimport (\n\t"fmt"\n\t"sync"\n\t"time"\n)\n\ntype Job struct { ID int; Data int }\ntype Result struct { JobID int; Output int; WorkerID int }\n\nfunc worker(id int, jobs <-chan Job, results chan<- Result, wg *sync.WaitGroup) {\n\tdefer wg.Done()\n\tfor job := range jobs {\n\t\ttime.Sleep(time.Millisecond * time.Duration(100+job.Data%50))\n\t\tresults <- Result{JobID: job.ID, Output: job.Data * 2, WorkerID: id}\n\t}\n}\n\nfunc main() {\n\tconst workerSayisi = 5; const jobSayisi = 20\n\tjobs := make(chan Job, jobSayisi)\n\tresults := make(chan Result, jobSayisi)\n\tvar wg sync.WaitGroup\n\n\tfor i := 1; i <= workerSayisi; i++ {\n\t\twg.Add(1)\n\t\tgo worker(i, jobs, results, &wg)\n\t}\n\n\tfor i := 1; i <= jobSayisi; i++ {\n\t\tjobs <- Job{ID: i, Data: i * 10}\n\t}\n\tclose(jobs)\n\n\tgo func() {\n\t\twg.Wait()\n\t\tclose(results)\n\t}()\n\n\tfor result := range results {\n\t\tfmt.Printf("Isci %d -> Job %d: %d\\n", result.WorkerID, result.JobID, result.Output)\n\t}\n}',
    "language": "go",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "select ile kanal islemlerini yoneten bir ornek yazin. Iki farkli veri kaynagindan (sensor1, sensor2) gelen verileri dinleyen bir sistem simule edin. timeout ve default case kullanarak kanallarin bloke olmasini engelleyin.",
    "response": 'package main\n\nimport (\n\t"fmt"\n\t"math/rand"\n\t"time"\n)\n\nfunc sensorOku(isim string, kanal chan<- int) {\n\tfor i := 1; i <= 5; i++ {\n\t\tsure := time.Duration(rand.Intn(500)+100) * time.Millisecond\n\t\ttime.Sleep(sure)\n\t\tkanal <- i * rand.Intn(100)\n\t\tfmt.Printf("[%s] %d. veri (%v)\\n", isim, i, sure)\n\t}\n}\n\nfunc main() {\n\ts1 := make(chan int); s2 := make(chan int)\n\tgo sensorOku("Sicaklik", s1); go sensorOku("Nem", s2)\n\n\ttimeout := time.After(3 * time.Second)\n\tfor {\n\t\tselect {\n\t\tcase v1 := <-s1:\n\t\t\tfmt.Printf("\\u2192 Sicaklik: %d\\u00b0C\\n", v1)\n\t\tcase v2 := <-s2:\n\t\t\tfmt.Printf("\\u2192 Nem: %d%%\\n", v2)\n\t\tdefault:\n\t\t\ttime.Sleep(200 * time.Millisecond)\n\t\t\tfmt.Print(".")\n\t\tcase <-timeout:\n\t\t\tfmt.Println("\\nZaman asimi!")\n\t\t\treturn\n\t\t}\n\t}\n}',
    "language": "go",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "sync.Mutex ile thread-safe bir sayac yazin. Counter yapisi (struct) icinde bir mutex ve int deger tutsun. Increment, Decrement ve Value metotlari olsun. 1000 goroutine ile sayaci 1000 kez artirip dogrulugunu test edin.",
    "response": 'package main\n\nimport (\n\t"fmt"\n\t"sync"\n)\n\ntype Counter struct {\n\tmu    sync.Mutex\n\tdeger int\n}\n\nfunc (c *Counter) Increment() { c.mu.Lock(); defer c.mu.Unlock(); c.deger++ }\nfunc (c *Counter) Decrement() { c.mu.Lock(); defer c.mu.Unlock(); c.deger-- }\nfunc (c *Counter) Value() int { c.mu.Lock(); defer c.mu.Unlock(); return c.deger }\n\ntype SafeCache struct {\n\tmu   sync.RWMutex\n\tveri map[string]string\n}\n\nfunc (sc *SafeCache) Get(key string) string {\n\tsc.mu.RLock(); defer sc.mu.RUnlock()\n\treturn sc.veri[key]\n}\n\nfunc (sc *SafeCache) Set(key, value string) {\n\tsc.mu.Lock(); defer sc.mu.Unlock()\n\tif sc.veri == nil { sc.veri = make(map[string]string) }\n\tsc.veri[key] = value\n}\n\nfunc main() {\n\tvar c Counter; var wg sync.WaitGroup\n\tfor i := 0; i < 1000; i++ {\n\t\twg.Add(1)\n\t\tgo func() { defer wg.Done(); c.Increment() }()\n\t}\n\twg.Wait()\n\tfmt.Printf("Counter: %d (beklenen: 1000)\\n", c.Value())\n\n\tcache := SafeCache{veri: make(map[string]string)}\n\tvar wg2 sync.WaitGroup\n\tfor i := 0; i < 100; i++ {\n\t\twg2.Add(1)\n\t\tgo func(i int) {\n\t\t\tdefer wg2.Done()\n\t\t\tkey := fmt.Sprintf("anahtar-%d", i)\n\t\t\tcache.Set(key, "deger"); _ = cache.Get(key)\n\t\t}(i)\n\t}\n\twg2.Wait()\n\tfmt.Println("RWMutex test basariili")\n}',
    "language": "go",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Go interface'leri kullanarak bir odeme sistemi tasarlayin. OdemeYontemi interface'i (Ode(miktar float64) error) tanimlayin. KrediKarti, Havale, Cuzdan struct'lari bu interface'i implemente etsin. Bir fatura struct'i icinde bu interface'i kullanarak cok bicimli odeme islemi yapin.",
    "response": 'package main\n\nimport (\n\t"errors"\n\t"fmt"\n\t"math"\n)\n\ntype OdemeYontemi interface {\n\tOde(miktar float64) error\n\tAd() string\n}\n\ntype KrediKarti struct { kartNo string; bakiye float64 }\nfunc (k *KrediKarti) Ode(miktar float64) error {\n\tif miktar <= 0 { return errors.New("gecersiz") }\n\tif k.bakiye < miktar { return errors.New("yetersiz bakiye") }\n\tk.bakiye -= miktar + miktar*0.03; return nil\n}\nfunc (k *KrediKarti) Ad() string { return "Kredi Karti" }\n\ntype Havale struct { iban, bankaAdi string }\nfunc (h *Havale) Ode(miktar float64) error {\n\tif miktar > 50000 { return errors.New("limit asildi") }\n\tfmt.Printf("%s IBAN ile %.2f TL havale\\n", h.iban, miktar); return nil\n}\nfunc (h *Havale) Ad() string { return "Havale" }\n\ntype Cuzdan struct { bakiye float64 }\nfunc (c *Cuzdan) Ode(miktar float64) error {\n\tif c.bakiye < miktar { return fmt.Errorf("yetersiz: %.2f", c.bakiye) }\n\tc.bakiye -= miktar; return nil\n}\nfunc (c *Cuzdan) Ad() string { return "Cuzdan" }\n\ntype Fatura struct {\n\tfaturaNo string\n\ttutar    float64\n\todeme    OdemeYontemi\n}\n\nfunc (f *Fatura) OdemeYap() error {\n\tfmt.Printf("\\n%s odeniyor: %.2f TL [%s]\\n", f.faturaNo, f.tutar, f.odeme.Ad())\n\tif err := f.odeme.Ode(math.Round(f.tutar*100)/100); err != nil {\n\t\treturn fmt.Errorf("odeme basarisiz: %w", err)\n\t}\n\tfmt.Println("\\u2713 Odeme basariili"); return nil\n}\n\nfunc main() {\n\tkart := &KrediKarti{bakiye: 10000}\n\thavale := &Havale{iban: "TR123456789", bankaAdi: "Ziraat"}\n\tcuzdan := &Cuzdan{bakiye: 500}\n\tfor _, f := range []Fatura{{\"FTR-001\", 250.50, kart}, {\"FTR-002\", 15000, havale}, {\"FTR-003\", 75.99, cuzdan}} {\n\t\tif err := f.OdemeYap(); err != nil { fmt.Printf("\\u2717 %v\\n", err) }\n\t}\n}',
    "language": "go",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Go'da hata sarma (error wrapping) ve defer kullanimini gosteren bir dosya isleme ornegi yazin. Bir dosyayi okuyan, icindeki sayilari toplayan bir fonksiyon yazin. errors.Is ve errors.As ile hata turu kontrolu yapin.",
    "response": 'package main\n\nimport (\n\t"bufio"\n\t"errors"\n\t"fmt"\n\t"os"\n\t"strconv"\n\t"strings"\n)\n\ntype ParseError struct { Line int; Value string; Err error }\nfunc (e *ParseError) Error() string { return fmt.Sprintf("satir %d: %s - %v", e.Line, e.Value, e.Err) }\nfunc (e *ParseError) Unwrap() error { return e.Err }\n\nfunc topla(dosyaYolu string) (toplam int, err error) {\n\tdosya, err := os.Open(dosyaYolu)\n\tif err != nil { return 0, fmt.Errorf("acilamadi %s: %w", dosyaYolu, err) }\n\tdefer func() { dosya.Close(); fmt.Println("Dosya kapatildi") }()\n\n\tscanner := bufio.NewScanner(dosya)\n\tlineNo := 0\n\tfor scanner.Scan() {\n\t\tlineNo++\n\t\tline := strings.TrimSpace(scanner.Text())\n\t\tif line == "" { continue }\n\t\tsayi, err := strconv.Atoi(line)\n\t\tif err != nil { return 0, &ParseError{Line: lineNo, Value: line, Err: err} }\n\t\ttoplam += sayi\n\t}\n\tif err := scanner.Err(); err != nil { return 0, fmt.Errorf("okuma hatasi: %w", err) }\n\treturn toplam, nil\n}\n\nfunc main() {\n\tdefer func() {\n\t\tif r := recover(); r != nil { fmt.Printf("Panik: %v\\n", r) }\n\t}()\n\ttoplam, err := topla("sayilar.txt")\n\tif err != nil {\n\t\tvar pe *ParseError\n\t\tif errors.As(err, &pe) { fmt.Printf("Ayristirma: %v\\n", pe)\n\t\t} else if errors.Is(err, os.ErrNotExist) { fmt.Println("Dosya yok!")\n\t\t} else { fmt.Printf("Hata: %v\\n", err) }\n\t\treturn\n\t}\n\tfmt.Printf("Toplam: %d\\n", toplam)\n}',
    "language": "go",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

# ============ SQL (5) ============

items.append({
    "instruction": "WITH (CTE) ve window function (ROW_NUMBER, RANK, DENSE_RANK) kullanarak her departmandaki en yuksek maasli 3 calisani getiren bir sorgu yazin. employees (id, name, salary, department_id) ve departments (id, name) tablolarini kullanin. Ayrica LAG ile her calisanin bir onceki calisana gore maas farkini hesaplayin.",
    "response": "WITH calisan_siralamasi AS (\n    SELECT\n        e.id, e.name, e.salary, d.name AS departman,\n        ROW_NUMBER() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS sira,\n        RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS rank,\n        DENSE_RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS dense_rank,\n        LAG(e.salary) OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS onceki_maas,\n        e.salary - LAG(e.salary) OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS maas_farki\n    FROM employees e\n    JOIN departments d ON e.department_id = d.id\n)\nSELECT departman, sira, name, salary,\n    CASE WHEN rank = 1 THEN '★ En Yuksek' WHEN rank <= 3 THEN 'Ilk 3' ELSE 'Diger' END AS durum,\n    onceki_maas, maas_farki\nFROM calisan_siralamasi WHERE sira <= 3 ORDER BY departman, sira;",
    "language": "sql",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Recursive CTE kullanarak bir organizasyon semasindaki hiyerarsiyi sorgulayin. employees (id, name, manager_id, position) tablosu olsun. Her calisanin hiyerarsideki seviyesini, yonetici zincirini ve altinda kaci kisi oldugunu gosteren bir sorgu yazin.",
    "response": "WITH RECURSIVE org_semasi AS (\n    SELECT id, name, position, manager_id, 0 AS seviye,\n        CAST(name AS VARCHAR(500)) AS yonetici_zinciri\n    FROM employees WHERE manager_id IS NULL\n    UNION ALL\n    SELECT e.id, e.name, e.position, e.manager_id, os.seviye + 1,\n        CONCAT(os.yonetici_zinciri, ' → ', e.name)\n    FROM employees e JOIN org_semasi os ON e.manager_id = os.id\n),\nalt_calisan_sayisi AS (\n    SELECT manager_id, COUNT(*) AS alt_calisan\n    FROM employees WHERE manager_id IS NOT NULL GROUP BY manager_id\n)\nSELECT os.id, os.name, os.position, os.seviye, os.yonetici_zinciri,\n    COALESCE(acs.alt_calisan, 0) AS alt_calisan_sayisi,\n    CASE WHEN os.seviye = 0 THEN 'CEO' WHEN os.seviye = 1 THEN 'Direktor'\n         WHEN os.seviye = 2 THEN 'Mudur' ELSE 'Calisan' END AS seviye_adi\nFROM org_semasi os\nLEFT JOIN alt_calisan_sayisi acs ON os.id = acs.manager_id\nORDER BY os.seviye, os.name;",
    "language": "sql",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "PIVOT islemi (CASE ile) ve window function'lari kullanarak aylik satis raporu olusturun. Her urun kategorisinin aylara gore toplam satisini ve her kategorinin genel toplam icindeki yuzdesini (SUM OVER) hesaplayin.",
    "response": "WITH aylik_satislar AS (\n    SELECT p.category, EXTRACT(YEAR FROM s.sale_date) AS yil,\n        EXTRACT(MONTH FROM s.sale_date) AS ay, SUM(s.amount) AS toplam_satis\n    FROM sales s JOIN products p ON s.product_id = p.id\n    WHERE s.sale_date >= '2024-01-01' AND s.sale_date < '2025-01-01'\n    GROUP BY p.category, EXTRACT(YEAR FROM s.sale_date), EXTRACT(MONTH FROM s.sale_date)\n),\npivot_aylik AS (\n    SELECT category, yil,\n        SUM(CASE WHEN ay = 1 THEN toplam_satis ELSE 0 END) AS ocak,\n        SUM(CASE WHEN ay = 2 THEN toplam_satis ELSE 0 END) AS subat,\n        SUM(CASE WHEN ay = 3 THEN toplam_satis ELSE 0 END) AS mart,\n        SUM(CASE WHEN ay = 4 THEN toplam_satis ELSE 0 END) AS nisan,\n        SUM(CASE WHEN ay = 5 THEN toplam_satis ELSE 0 END) AS mayis,\n        SUM(CASE WHEN ay = 6 THEN toplam_satis ELSE 0 END) AS haziran,\n        SUM(CASE WHEN ay = 7 THEN toplam_satis ELSE 0 END) AS temmuz,\n        SUM(CASE WHEN ay = 8 THEN toplam_satis ELSE 0 END) AS agustos,\n        SUM(CASE WHEN ay = 9 THEN toplam_satis ELSE 0 END) AS eylul,\n        SUM(CASE WHEN ay = 10 THEN toplam_satis ELSE 0 END) AS ekim,\n        SUM(CASE WHEN ay = 11 THEN toplam_satis ELSE 0 END) AS kasim,\n        SUM(CASE WHEN ay = 12 THEN toplam_satis ELSE 0 END) AS aralik,\n        SUM(toplam_satis) AS genel_toplam\n    FROM aylik_satislar GROUP BY category, yil\n),\ngenel_toplam AS (SELECT SUM(genel_toplam) AS toplam FROM pivot_aylik)\nSELECT pa.category, pa.yil, pa.ocak, pa.subat, pa.mart, pa.nisan, pa.mayis,\n    pa.haziran, pa.temmuz, pa.agustos, pa.eylul, pa.ekim, pa.kasim, pa.aralik,\n    pa.genel_toplam, ROUND(pa.genel_toplam * 100.0 / gt.toplam, 2) AS yuzde\nFROM pivot_aylik pa CROSS JOIN genel_toplam gt\nORDER BY pa.genel_toplam DESC;",
    "language": "sql",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "Complex JOIN'ler ve alt sorgular kullanarak bir e-ticaret veritabani sorgusu yazin. Siparislerdeki her urun icin; siparis tarihinden son 30 gun icinde ayni kategoriden kac urun satildigini ve musterinin o ana kadar yaptigi toplam harcamayi alt sorgularla hesaplayin.",
    "response": "SELECT c.id AS musteri_id, c.name AS musteri_adi, o.id AS siparis_id,\n    o.order_date, p.name AS urun_adi, cat.name AS kategori,\n    oi.quantity, oi.unit_price, (oi.quantity * oi.unit_price) AS satir_toplami,\n    (SELECT SUM(oi2.quantity) FROM order_items oi2\n     JOIN products p2 ON oi2.product_id = p2.id\n     JOIN orders o2 ON oi2.order_id = o2.id\n     WHERE p2.category_id = p.category_id\n       AND o2.order_date BETWEEN o.order_date - INTERVAL '30 days' AND o.order_date\n    ) AS son_30_gun_satis,\n    (SELECT COALESCE(SUM(oi3.quantity * oi3.unit_price), 0)\n     FROM order_items oi3 JOIN orders o3 ON oi3.order_id = o3.id\n     WHERE o3.customer_id = c.id AND o3.order_date <= o.order_date\n    ) AS toplam_harcama,\n    ROW_NUMBER() OVER (PARTITION BY o.id ORDER BY (oi.quantity * oi.unit_price) DESC) AS urun_sirasi\nFROM customers c\nJOIN orders o ON c.id = o.customer_id\nJOIN order_items oi ON o.id = oi.order_id\nJOIN products p ON oi.product_id = p.id\nJOIN categories cat ON p.category_id = cat.id\nWHERE o.order_date >= '2024-01-01'\nORDER BY c.id, o.order_date, urun_sirasi;",
    "language": "sql",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "UNION, CASE WHEN ve window function kullanarak kapsamli bir veri analizi sorgusu yazin. Ayni sirketteki aktif ve pasif musterileri karsilastirin. Her musteri segmenti icin minimum, maksimum ve ortalama siparis degerlerini CASE ile kategorize ederek tek bir sonuc kumesinde birlestirin.",
    "response": "WITH musteri_analizi AS (\n    SELECT c.id, c.name, c.segment, c.is_active,\n        COUNT(DISTINCT o.id) AS siparis_sayisi,\n        COALESCE(SUM(oi.quantity * oi.unit_price), 0) AS toplam_harcama,\n        COALESCE(AVG(oi.quantity * oi.unit_price), 0) AS ortalama_siparis\n    FROM customers c\n    LEFT JOIN orders o ON c.id = o.customer_id\n    LEFT JOIN order_items oi ON o.id = oi.order_id\n    GROUP BY c.id, c.name, c.segment, c.is_active\n)\nSELECT 'Aktif Musteriler' AS rapor_tipi, segment,\n    COUNT(*) AS musteri_sayisi,\n    ROUND(AVG(toplam_harcama), 2) AS ortalama_harcama,\n    ROUND(MAX(toplam_harcama), 2) AS maks,\n    ROUND(MIN(toplam_harcama), 2) AS min,\n    CASE WHEN AVG(ortalama_siparis) > 1000 THEN 'Premium'\n         WHEN AVG(ortalama_siparis) > 500 THEN 'Standart'\n         WHEN AVG(ortalama_siparis) > 100 THEN 'Ekonomik'\n         ELSE 'Dusuk' END AS kategori\nFROM musteri_analizi WHERE is_active = TRUE GROUP BY segment\nUNION ALL\nSELECT 'Pasif Musteriler', segment,\n    COUNT(*), ROUND(AVG(toplam_harcama), 2),\n    ROUND(MAX(toplam_harcama), 2), ROUND(MIN(toplam_harcama), 2), 'Pasif'\nFROM musteri_analizi WHERE is_active = FALSE GROUP BY segment\nORDER BY rapor_tipi, musteri_sayisi DESC;",
    "language": "sql",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

# ============ WEB (5) ============

items.append({
    "instruction": "Flexbox ile 3 sutunlu, responsive bir kart duzeni olusturun. Her kartta bir baslik, aciklama ve buton olsun. Kartlar esnek genislikte olsun (min 250px, max 1fr). Ilk kart 2 kat genislikte olsun. Tum kartlar ayni yukseklikte hizalansin.",
    "response": "<!DOCTYPE html>\n<html lang=\"tr\">\n<head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\">\n<title>Flexbox Kart Duzeni</title>\n<style>\n*{margin:0;padding:0;box-sizing:border-box}\nbody{font-family:'Segoe UI',sans-serif;background:#f0f2f5;padding:2rem;min-height:100vh;display:flex;flex-direction:column;align-items:center}\n.kart-konteyner{display:flex;flex-wrap:wrap;gap:1.5rem;justify-content:center;max-width:1200px;width:100%}\n.kart{flex:1 1 250px;background:#fff;border-radius:12px;padding:1.5rem;box-shadow:0 4px 6px rgba(0,0,0,0.07);display:flex;flex-direction:column}\n.kart.genis{flex:2 1 500px}\n.kart-baslik{font-size:1.25rem;font-weight:700;color:#1a1a2e;margin-bottom:0.75rem;padding-bottom:0.75rem;border-bottom:2px solid #e0e0e0}\n.kart-aciklama{font-size:.9rem;color:#555;line-height:1.6;flex:1;margin-bottom:1rem}\n.kart-buton{display:inline-block;padding:.6rem 1.2rem;background:#4361ee;color:#fff;border-radius:6px;font-weight:600;text-decoration:none;text-align:center;align-self:flex-start;border:none;cursor:pointer}\n.kart-buton:hover{background:#3a56d4}\n</style>\n</head>\n<body>\n<div class=\"kart-konteyner\">\n  <article class=\"kart genis\"><h2 class=\"kart-baslik\">One Cikan Hizmet</h2><p class=\"kart-aciklama\">Profesyonel danismanlik hizmetimiz ile isinizi bir ust seviyeye tasiyin.</p><a href=\"#\" class=\"kart-buton\">Detayli Bilgi</a></article>\n  <article class=\"kart\"><h2 class=\"kart-baslik\">Web Tasarim</h2><p class=\"kart-aciklama\">Modern ve responsive web siteleri ile markanizi dijital dunyada temsil edin.</p><a href=\"#\" class=\"kart-buton\">Incele</a></article>\n  <article class=\"kart\"><h2 class=\"kart-baslik\">Mobil Uygulama</h2><p class=\"kart-aciklama\">iOS ve Android icin mobil uygulama gelistirme hizmeti.</p><a href=\"#\" class=\"kart-buton\">Incele</a></article>\n  <article class=\"kart\"><h2 class=\"kart-baslik\">SEO Optimizasyonu</h2><p class=\"kart-aciklama\">Arama motorlarinda ust siraya cikmak icin SEO hizmetleri.</p><a href=\"#\" class=\"kart-buton\">Incele</a></article>\n</div>\n</body>\n</html>",
    "language": "web",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "CSS Grid ile bir magazine-style haber sayfasi duzeni olusturun. Header, ana haber (2 kolon), 3 kucuk haber, sag sidebar ve footer bolumleri olsun. grid-template-areas kullanarak yerlestimi tanimlayin. Tablet ve mobil icin media queries ile duzeni degistirin.",
    "response": "<!DOCTYPE html>\n<html lang=\"tr\">\n<head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\">\n<title>CSS Grid Haber Sayfasi</title>\n<style>\n*{margin:0;padding:0;box-sizing:border-box}\nbody{font-family:Georgia,serif;background:#fafafa;color:#222;padding:1rem}\n.haber-sayfasi{display:grid;grid-template-columns:2fr 1fr;gap:1.5rem;max-width:1200px;margin:0 auto;grid-template-areas:\"header header\" \"ana-haber ana-haber\" \"kucuk-haberler sidebar\" \"footer footer\"}\n.header{grid-area:header;text-align:center;padding:2rem;background:linear-gradient(135deg,#1a1a2e,#16213e);color:#fff;border-radius:12px}\n.ana-haber{grid-area:ana-haber;display:grid;grid-template-columns:2fr 1fr;gap:1.5rem;background:#fff;border-radius:12px;padding:1.5rem}\n.ana-haber .haber-gorsel{background:linear-gradient(45deg,#667eea,#764ba2);border-radius:8px;min-height:250px}\n.kucuk-haberler{grid-area:kucuk-haberler;display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}\n.kucuk-haber{background:#fff;border-radius:8px;padding:1rem}\n.sidebar{grid-area:sidebar;background:#fff;border-radius:12px;padding:1.5rem}\n.footer{grid-area:footer;text-align:center;padding:1.5rem;background:#1a1a2e;color:#fff;border-radius:12px}\n@media(max-width:768px){.haber-sayfasi{grid-template-columns:1fr;grid-template-areas:\"header\" \"ana-haber\" \"kucuk-haberler\" \"sidebar\" \"footer\"}.ana-haber{grid-template-columns:1fr}.kucuk-haberler{grid-template-columns:repeat(2,1fr)}}\n@media(max-width:480px){.kucuk-haberler{grid-template-columns:1fr}}\n</style>\n</head>\n<body>\n<div class=\"haber-sayfasi\">\n<header class=\"header\"><h1>HABER GAZETESI</h1><p>Son Dakika | Gundem | Ekonomi | Spor</p></header>\n<main class=\"ana-haber\"><div class=\"haber-gorsel\"></div><div><h2>Buyuk Kesif: Yeni Bir Gezegen Bulundu</h2><p>Gokbilimciler, yasanabilir bolgede Dunya benzeri bir gezegen kesfetti.</p></div></main>\n<section class=\"kucuk-haberler\">\n<article class=\"kucuk-haber\"><h3>Teknoloji Zirvesi</h3><p>Teknoloji sirketleri Istanbul'da bulustu.</p></article>\n<article class=\"kucuk-haber\"><h3>Borsada Rekor</h3><p>BIST 100 zirvede.</p></article>\n<article class=\"kucuk-haber\"><h3>Sampiyon Belli Oluyor</h3><p>Heyecan dorukta.</p></article></section>\n<aside class=\"sidebar\"><h3>Populer</h3><p>1. Ekonomi</p><p>2. Egitim</p><p>3. Saglik</p></aside>\n<footer class=\"footer\"><p>&copy; 2024 Haber Gazetesi</p></footer>\n</div>\n</body>\n</html>",
    "language": "web",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "CSS animasyonlari ve transition kullanarak interaktif bir toast bildirimi olusturun. Bildirim ekranin sag ust kosesinden slide-in ile girsin, 3 saniye gorunsun, sonra slide-out ile ciksin. Ayrica hover'da olceklenen ve donen bir loading spinner yapin. CSS degiskenleri kullanin.",
    "response": "<!DOCTYPE html>\n<html lang=\"tr\">\n<head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\">\n<title>Toast & Spinner</title>\n<style>\n:root{--toast-success:#43e97b;--toast-error:#f5576c;--toast-warning:#ffd93d;--spinner-color:#4361ee;--spinner-size:50px;--anim-sure:0.5s}\n*{margin:0;padding:0;box-sizing:border-box}\nbody{font-family:'Segoe UI',sans-serif;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;background:#f0f2f5;gap:2rem}\n.kontrol-panel{display:flex;gap:1rem}\n.kontrol-panel button{padding:.75rem 1.5rem;border:none;border-radius:8px;font-weight:600;cursor:pointer}\n.btn-basarili{background:var(--toast-success);color:#fff}\n.btn-hata{background:var(--toast-error);color:#fff}\n.btn-uyari{background:var(--toast-warning);color:#333}\n.toast-container{position:fixed;top:1.5rem;right:1.5rem;z-index:1000;display:flex;flex-direction:column;gap:.75rem;pointer-events:none}\n.toast{pointer-events:auto;padding:1rem 1.5rem;border-radius:10px;color:#fff;font-weight:500;box-shadow:0 8px 20px rgba(0,0,0,0.15);animation:slideIn var(--anim-sure) ease-out}\n.toast.basarili{background:var(--toast-success)}\n.toast.hata{background:var(--toast-error)}\n.toast.uyari{background:var(--toast-warning);color:#333}\n.toast.kapaniyor{animation:slideOut var(--anim-sure) ease-in forwards}\n@keyframes slideIn{from{transform:translateX(120%);opacity:0}to{transform:translateX(0);opacity:1}}\n@keyframes slideOut{from{transform:translateX(0);opacity:1}to{transform:translateX(120%);opacity:0}}\n.spinner{width:var(--spinner-size);height:var(--spinner-size);border:5px solid #e0e0e0;border-top-color:var(--spinner-color);border-radius:50%;animation:spin 1s linear infinite;transition:transform .3s}\n.spinner:hover{animation:spin 1s linear infinite,scaleUp .3s forwards}\n@keyframes spin{to{transform:rotate(360deg)}}@keyframes scaleUp{to{transform:rotate(360deg) scale(1.3)}}\n</style>\n</head>\n<body>\n<div class=\"toast-container\" id=\"tC\"></div>\n<div class=\"kontrol-panel\">\n<button class=\"btn-basarili\" onclick=\"t('basarili','Islem tamam!')\">Basarili</button>\n<button class=\"btn-hata\" onclick=\"t('hata','Hata olustu!')\">Hata</button>\n<button class=\"btn-uyari\" onclick=\"t('uyari','Emin misiniz?')\">Uyari</button>\n</div>\n<div style=\"text-align:center\"><div class=\"spinner\"></div><p style=\"margin-top:.75rem\">Yukleniyor...</p></div>\n<script>\nfunction t(tip,m){\n  const c=document.getElementById('tC')\n  const e=document.createElement('div')\n  e.className='toast '+tip;e.innerHTML=m;c.appendChild(e)\n  setTimeout(()=>{e.classList.add('kapaniyor');e.addEventListener('animationend',()=>e.remove())},3000)\n}\n</script>\n</body>\n</html>",
    "language": "web",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "CSS transform, transition ve pseudo-element'ler (:before, :after) kullanarak 3D buton ve kart hover efektleri olusturun. Butonlarda press efekti (translateY), kartlarda perspective ile 3D flip efekti ve gradient border animasyonu yapin.",
    "response": "<!DOCTYPE html>\n<html lang=\"tr\">\n<head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\">\n<title>3D Efektler</title>\n<style>\n*{margin:0;padding:0;box-sizing:border-box}\nbody{font-family:'Segoe UI',sans-serif;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;background:#0f0f1a;padding:2rem;gap:3rem}\n.butonlar{display:flex;gap:2rem}\n.btn-3d{position:relative;padding:1rem 2.5rem;border:none;border-radius:12px;font-weight:700;color:#fff;cursor:pointer;background:linear-gradient(135deg,#667eea,#764ba2);box-shadow:0 8px 0 #4a3f7a,0 12px 20px rgba(0,0,0,0.3);transition:all .15s ease;text-transform:uppercase}\n.btn-3d:active{transform:translateY(6px);box-shadow:0 2px 0 #4a3f7a,0 8px 16px rgba(0,0,0,0.2)}\n.btn-3d.yeil{background:linear-gradient(135deg,#43e97b,#38f9d7);box-shadow:0 8px 0 #2ba86b,0 12px 20px rgba(0,0,0,0.3)}\n.btn-3d.kirmizi{background:linear-gradient(135deg,#f093fb,#f5576c);box-shadow:0 8px 0 #c44a7a,0 12px 20px rgba(0,0,0,0.3)}\n.btn-3d::after{content:'';position:absolute;inset:0;border-radius:12px;background:linear-gradient(135deg,rgba(255,255,255,0.2),transparent);opacity:0;transition:opacity .3s}\n.btn-3d:hover::after{opacity:1}\n.btn-3d:hover{transform:translateY(-2px);box-shadow:0 10px 0 #4a3f7a,0 16px 24px rgba(0,0,0,0.4)}\n.flip-kart{width:280px;height:360px;perspective:1000px}\n.flip-kart-icerik{position:relative;width:100%;height:100%;transition:transform .8s cubic-bezier(.175,.885,.32,1.275);transform-style:preserve-3d}\n.flip-kart:hover .flip-kart-icerik{transform:rotateY(180deg)}\n.flip-kart-on,.flip-kart-arka{position:absolute;width:100%;height:100%;backface-visibility:hidden;border-radius:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:1.5rem;text-align:center}\n.flip-kart-on{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff}\n.flip-kart-on::before{content:'';position:absolute;top:-3px;left:-3px;right:-3px;bottom:-3px;border-radius:18px;background:conic-gradient(#667eea,#764ba2,#f093fb,#f5576c,#ffd93d,#43e97b,#667eea);z-index:-1;animation:rotateBorder 4s linear infinite}\n@keyframes rotateBorder{to{transform:rotate(360deg)}}\n.flip-kart-arka{background:#1a1a2e;color:#fff;transform:rotateY(180deg);border:2px solid #667eea}\n.kartlar{display:flex;gap:2rem}\n</style>\n</head>\n<body>\n<div class=\"butonlar\">\n<button class=\"btn-3d\">Tikla</button>\n<button class=\"btn-3d yeil\">Basarili</button>\n<button class=\"btn-3d kirmizi\">Sil</button>\n</div>\n<div class=\"kartlar\">\n<div class=\"flip-kart\"><div class=\"flip-kart-icerik\">\n<div class=\"flip-kart-on\"><p style=\"font-size:3rem\">🃏</p><p>Cevir</p></div>\n<div class=\"flip-kart-arka\"><h3>Premium</h3><p>Sinirsiz erisim</p></div>\n</div></div>\n<div class=\"flip-kart\"><div class=\"flip-kart-icerik\">\n<div class=\"flip-kart-on\"><p style=\"font-size:3rem\">🚀</p><p>Cevir</p></div>\n<div class=\"flip-kart-arka\"><h3>Hizli Teslimat</h3><p>Ayni gun kargoda</p></div>\n</div></div>\n</div>\n</body>\n</html>",
    "language": "web",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

items.append({
    "instruction": "CSS custom properties, media queries, clamp() ve min()/max() fonksiyonlarini kullanarak fully responsive bir typography sistemi ve kart bileseni olusturun. Karanlik/aydinlik tema destegi ekleyin.",
    "response": "<!DOCTYPE html>\n<html lang=\"tr\">\n<head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\">\n<title>Responsive Tema Sistemi</title>\n<style>\n:root{--bg:#f8f9fa;--bg-card:#fff;--text:#1a1a2e;--text-sec:#555;--accent:#4361ee;--border:#e0e0e0;--shadow:0 4px 12px rgba(0,0,0,0.06);--font:'Segoe UI',system-ui,sans-serif;--fs-xs:clamp(.7rem,.5vw+.5rem,.8rem);--fs-sm:clamp(.8rem,1vw+.5rem,.95rem);--fs-base:clamp(.95rem,1.2vw+.5rem,1.1rem);--fs-lg:clamp(1.2rem,2vw+.5rem,1.5rem);--fs-xl:clamp(1.5rem,3vw+.5rem,2rem);--fs-xxl:clamp(2rem,4vw+.5rem,2.8rem);--space-sm:clamp(.5rem,1vw,.75rem);--space-md:clamp(1rem,2vw,1.5rem);--space-lg:clamp(1.5rem,3vw,2.5rem);--radius:clamp(8px,1.5vw,16px);--container:min(1200px,95vw)}\n[data-theme=dark]{--bg:#0f0f1a;--bg-card:#16213e;--text:#e0e0e0;--text-sec:#a0aec0;--border:#2d2d4a;--shadow:0 4px 12px rgba(0,0,0,0.3)}\n*{margin:0;padding:0;box-sizing:border-box}\nbody{font-family:var(--font);font-size:var(--fs-base);background:var(--bg);color:var(--text);transition:background .3s,color .3s;padding:var(--space-lg)}\n.konteyner{max-width:var(--container);margin:0 auto}\n.tema-btn{padding:var(--space-sm) var(--space-md);background:var(--accent);color:#fff;border:none;border-radius:var(--radius);cursor:pointer;font-weight:600;margin-bottom:var(--space-lg)}\nh1{font-size:var(--fs-xxl);margin-bottom:var(--space-md)}\np{color:var(--text-sec);line-height:1.7}\n.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(280px,100%),1fr));gap:var(--space-md);margin-top:var(--space-lg)}\n.kart{background:var(--bg-card);border-radius:var(--radius);padding:var(--space-lg);box-shadow:var(--shadow);border:1px solid var(--border)}\n.kart-fiyat{font-size:var(--fs-xl);font-weight:700;color:var(--accent)}\n.kart-btn{display:inline-block;padding:var(--space-sm) var(--space-md);background:var(--accent);color:#fff;border-radius:var(--radius);text-decoration:none;font-weight:600;margin-top:var(--space-sm)}\n</style>\n</head>\n<body>\n<div class=\"konteyner\">\n<button class=\"tema-btn\" onclick=\"tema()\" id=\"temaBtn\">🌙 Karanlik Tema</button>\n<h1>Modern Tasarim</h1><p>clamp(), min(), max() ile responsive sistem.</p>\n<div class=\"grid\">\n<div class=\"kart\"><h3>Baslangic</h3><p>Temel ozellikler</p><div class=\"kart-fiyat\">₺49</div><a href=\"#\" class=\"kart-btn\">Basla</a></div>\n<div class=\"kart\"><h3>Profesyonel</h3><p>Ideal cozum</p><div class=\"kart-fiyat\">₺149</div><a href=\"#\" class=\"kart-btn\">Basla</a></div>\n<div class=\"kart\"><h3>Kurumsal</h3><p>Sinirsiz erisim</p><div class=\"kart-fiyat\">₺399</div><a href=\"#\" class=\"kart-btn\">Basla</a></div>\n</div></div>\n<script>\nfunction tema(){const h=document.documentElement,b=document.getElementById('temaBtn');if(h.getAttribute('data-theme')==='dark'){h.removeAttribute('data-theme');b.textContent='🌙 Karanlik Tema'}else{h.setAttribute('data-theme','dark');b.textContent='☀️ Aydinlik Tema'}}\n</script>\n</body>\n</html>",
    "language": "web",
    "category": "advanced",
    "type": "manual",
    "format": "advanced"
})

# Write the JSON file
output_path = r"C:\Users\agnes\Desktop\projects\turkish-code-instructions\submissions\advanced_batch.json"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"Written {len(items)} items to {output_path}")
