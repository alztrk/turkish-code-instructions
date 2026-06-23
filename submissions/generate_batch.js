const fs = require('fs');

const items = [];

// PYTHON (10)
items.push({
  instruction: "Bir decorator yaz: herhangi bir fonksiyonun calisma suresini olcup 'Fonksiyon {isim} {sure} saniye surdu' seklinde yazdiran bir @timer decorator'i olusturun. Decorator, *args ve **kwargs ile calismali.",
  response: "import time\nimport functools\n\ndef timer(func):\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        baslangic = time.perf_counter()\n        sonuc = func(*args, **kwargs)\n        gecen = time.perf_counter() - baslangic\n        print(f\"Fonksiyon {func.__name__} {gecen:.4f} saniye surdu\")\n        return sonuc\n    return wrapper\n\n@timer\ndef hesapla(n):\n    toplam = 0\n    for i in range(n):\n        toplam += i ** 2\n    return toplam\n\nprint(hesapla(10_000_000))",
  language: "python",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Bir generator fonksiyonu olan fibonacci(n) yazin. n'e kadar olan Fibonacci sayilarini yield ile uretsin. Ardindan bu generator'u kullanarak ilk 20 Fibonacci sayisini bir listeye cevirip yazdirin.",
  response: "def fibonacci(n):\n    a, b = 0, 1\n    while a < n:\n        yield a\n        a, b = b, a + b\n\nfib_gen = fibonacci(10000)\nilk_20 = [next(fib_gen) for _ in range(20)]\nprint(ilk_20)",
  language: "python",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "with blogu ile kullanilabilen bir DosyaYoneticisi context manager'i yazin. __enter__ dosyayi acsin, __exit__ dosyayi kapatsin ve hata varsa 'Hata olustu: {hata_tipi}' yazip True dondurerek hatayi yutmayi saglasin.",
  response: "class DosyaYoneticisi:\n    def __init__(self, dosya_adi, mod):\n        self.dosya_adi = dosya_adi\n        self.mod = mod\n        self.dosya = None\n\n    def __enter__(self):\n        self.dosya = open(self.dosya_adi, self.mod, encoding='utf-8')\n        return self.dosya\n\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        if self.dosya:\n            self.dosya.close()\n        if exc_type is not None:\n            print(f\"Hata olustu: {exc_type.__name__}\")\n            return True\n        return False\n\nwith DosyaYoneticisi('ornek.txt', 'w') as f:\n    f.write('Merhaba Dunya')\n\nwith DosyaYoneticisi('olmayan.txt', 'r') as f:\n    icerik = f.read()",
  language: "python",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Verilen bir sayi listesinde; cift sayilari 2 ile carpip, tek sayilari oldugu gibi birakan bir liste comprehension yazin. Ayrica sadece 3'e bolunen sayilari filtreleyen bir dict comprehension ile kuplerini sozluk olarak olusturun.",
  response: "sayilar = [1, 3, 6, 8, 9, 12, 15, 18, 20]\n\nislenmis = [x * 2 if x % 2 == 0 else x for x in sayilar]\nprint(f\"Islenmis liste: {islenmis}\")\n\nkup_sozluk = {x: x ** 3 for x in sayilar if x % 3 == 0}\nprint(f\"3'e bolunenlerin kupleri: {kup_sozluk}\")",
  language: "python",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "map, filter ve reduce kullanarak su islemi yapin: Bir tam sayi listesindeki tek sayilari filtreleyip, her birinin karesini alin ve son olarak tum bu karelerin toplamini reduce ile hesaplayin. Lambda fonksiyonlari kullanin.",
  response: "from functools import reduce\n\nsayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n\ntek_karesi = map(lambda x: x ** 2, filter(lambda x: x % 2 == 1, sayilar))\ntoplam = reduce(lambda a, b: a + b, tek_karesi)\n\nprint(f\"Tek sayilarin kareleri toplami: {toplam}\")",
  language: "python",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Sinif hiyerarsisi olusturun: abstract base class Hayvan (isim, ses_cikar abstract metodu), ondan tureyen Memeli (dogurma ozelligi) ve Kusu (yumurtla metodu) siniflarini yazin. Son olarak Yarasam, hem Memeli hem Kusu'dan coklu kalitim alsin ve ses_cikar'i implemente etsin.",
  response: "from abc import ABC, abstractmethod\n\nclass Hayvan(ABC):\n    def __init__(self, isim):\n        self.isim = isim\n\n    @abstractmethod\n    def ses_cikar(self):\n        pass\n\nclass Memeli(Hayvan):\n    def dogurma(self):\n        return f\"{self.isim} yavru dogurdu\"\n\nclass Kusu(Hayvan):\n    def yumurtla(self):\n        return f\"{self.isim} yumurtladi\"\n\nclass Yarasam(Memeli, Kusu):\n    def ses_cikar(self):\n        return \"Cit cit!\"\n\ny = Yarasam(\"Golge\")\nprint(y.ses_cikar())\nprint(y.dogurma())\nprint(y.yumurtla())\nprint(Yarasam.__mro__)",
  language: "python",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "__str__, __repr__, __len__, __getitem__, __add__ magic metodlarini uygulayan bir OzelListe sinifi yazin. Bu sinif, bir listeyi sarar (wrap) ve dilimleme, toplama, uzunluk alma gibi islemleri desteklesin.",
  response: "class OzelListe:\n    def __init__(self, elemanlar):\n        self.elemanlar = list(elemanlar)\n\n    def __str__(self):\n        return f\"OzelListe({self.elemanlar})\"\n\n    def __repr__(self):\n        return f\"OzelListe({self.elemanlar!r})\"\n\n    def __len__(self):\n        return len(self.elemanlar)\n\n    def __getitem__(self, index):\n        if isinstance(index, slice):\n            return OzelListe(self.elemanlar[index])\n        return self.elemanlar[index]\n\n    def __add__(self, other):\n        if isinstance(other, OzelListe):\n            return OzelListe(self.elemanlar + other.elemanlar)\n        return NotImplemented\n\nl1 = OzelListe([1, 2, 3])\nl2 = OzelListe([4, 5])\nprint(l1 + l2)\nprint(l1[1:])\nprint(len(l1))",
  language: "python",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "itertools.product, itertools.permutations, itertools.combinations ve itertools.cycle kullanarak su islemleri yapin: 1) 'A','B','C' harflerinin 2'li permutasyonlari, 2) [1,2,3,4] kumesinin 3'lu kombinasyonlari, 3) iki zar atisindaki tum olasiliklar (product).",
  response: "from itertools import product, permutations, combinations, cycle\n\nharfler = ['A', 'B', 'C']\nprint(\"2'li permutasyonlar:\", list(permutations(harfler, 2)))\n\nsayilar = [1, 2, 3, 4]\nprint(\"3'lu kombinasyonlar:\", list(combinations(sayilar, 3)))\n\nzar = [1, 2, 3, 4, 5, 6]\nprint(\"Iki zar olasiliklari:\", list(product(zar, repeat=2)))\n\nsonsuz = cycle(['a', 'b', 'c'])\nprint(\"Ilk 5 cycle:\", [next(sonsuz) for _ in range(5)])",
  language: "python",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "functools modulunden partial, lru_cache ve wraps kullanimini gosteren bir ornek yazin. lru_cache ile fibonacci hesaplamasini hizlandirin, partial ile sabit argumanli fonksiyon olusturun ve wraps ile decorator metadata koruyun.",
  response: "from functools import partial, lru_cache, wraps\n\n@lru_cache(maxsize=128)\ndef fibonacci(n):\n    if n < 2:\n        return n\n    return fibonacci(n - 1) + fibonacci(n - 2)\n\ndef loglama(func):\n    @wraps(func)\n    def wrapper(*args, **kwargs):\n        print(f\"{func.__name__} cagrildi: args={args}\")\n        return func(*args, **kwargs)\n    return wrapper\n\n@loglama\ndef us_al(taban, us):\n    return taban ** us\n\niki_uzerinden = partial(us_al, taban=2)\n\nprint(f\"fibonacci(50) = {fibonacci(50)}\")\nprint(f\"fibonacci hit info: {fibonacci.cache_info()}\")\nprint(f\"2^10 = {iki_uzerinden(10)}\")\nprint(f\"3^4 = {us_al(3, 4)}\")",
  language: "python",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "threading modulu ile 3 adet thread olusturun. Her thread 1'den 5'e kadar sayilari yazdirsin, threadler arasinda Lock kullanarak ciktilarin karismasini engelleyin. Ayrica ThreadPoolExecutor ile bir url listesini paralel isleyin.",
  response: "import threading\nfrom concurrent.futures import ThreadPoolExecutor\nimport time\n\nyazdirma_kilidi = threading.Lock()\n\ndef guvenli_yazdirma(isim, baslangic):\n    for i in range(baslangic, baslangic + 5):\n        with yazdirma_kilidi:\n            print(f\"Thread-{isim}: {i}\")\n        time.sleep(0.1)\n\nthreadler = []\nfor idx in range(3):\n    t = threading.Thread(target=guvenli_yazdirma, args=(idx, idx * 10))\n    threadler.append(t)\n    t.start()\n\nfor t in threadler:\n    t.join()\n\nprint(\"\\n--- ThreadPoolExecutor ornegi ---\")\n\ndef url_getir(url):\n    time.sleep(0.5)\n    return f\"{url} verisi alindi\"\n\nurls = [\"https://site1.com\", \"https://site2.com\", \"https://site3.com\"]\n\nwith ThreadPoolExecutor(max_workers=3) as havuz:\n    sonuclar = list(havuz.map(url_getir, urls))\n\nfor sonuc in sonuclar:\n    print(sonuc)",
  language: "python",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

// JAVASCRIPT (6)
items.push({
  instruction: "Bir closure ornegi yazin: dis_fonksiyon adinda bir fonksiyon olusturun. Bu fonksiyon bir sayac degeri alsin ve icteki fonksiyon her cagrildiginda sayaci 1 artirip dondursun. Ayni pattern ile 3 bagimsiz sayac olusturun.",
  response: "function sayaOlustur(baslangic) {\n    let sayac = baslangic;\n    return function() {\n        sayac += 1;\n        return sayac;\n    };\n}\n\nconst saya1 = sayaOlustur(0);\nconst saya2 = sayaOlustur(100);\nconst saya3 = sayaOlustur(50);\n\nconsole.log(`saya1: ${saya1()}`);\nconsole.log(`saya1: ${saya1()}`);\nconsole.log(`saya2: ${saya2()}`);\nconsole.log(`saya3: ${saya3()}`);\nconsole.log(`saya3: ${saya3()}`);\nconsole.log(`saya2: ${saya2()}`);\nconsole.log(`saya1 son: ${saya1()}`);",
  language: "javascript",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Promise ve async/await kullanarak su senaryoyu kodlayin: once kullaniciBul(id) 1 sn'de kullanici dondursun, sonra siparisleriniGetir(userId) 1.5 sn'de siparisleri getirsin, en son siparisDetaylari(orderId) 1 sn'de detaylari getirsin.",
  response: "function kullaniciBul(id) {\n    return new Promise(resolve =>\n        setTimeout(() => resolve({ id, ad: 'Ali', email: 'ali@ornek.com' }), 1000)\n    );\n}\n\nfunction siparisleriGetir(userId) {\n    return new Promise(resolve =>\n        setTimeout(() => resolve([{ id: 101, urun: 'Laptop' }, { id: 102, urun: 'Fare' }]), 1500)\n    );\n}\n\nfunction siparisDetaylari(orderId) {\n    return new Promise(resolve =>\n        setTimeout(() => resolve({ orderId, durum: 'Kargoya verildi', tarih: '2024-01-15' }), 1000)\n    );\n}\n\nkullaniciBul(1)\n    .then(k => { console.log('Kullanici:', k); return siparisleriGetir(k.id); })\n    .then(s => { console.log('Siparisler:', s); return siparisDetaylari(s[0].id); })\n    .then(d => console.log('Detay:', d));\n\nasync function siparisDetayiniGetir(id) {\n    try {\n        const k = await kullaniciBul(id);\n        console.log('Kullanici:', k);\n        const s = await siparisleriGetir(k.id);\n        console.log('Siparisler:', s);\n        const d = await siparisDetaylari(s[0].id);\n        console.log('Detay:', d);\n        return d;\n    } catch (h) { console.error('Hata:', h); }\n}\nsiparisDetayiniGetir(1);",
  language: "javascript",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Prototype kalitimi kullanarak bir Hayvan -> Memeli -> Kopek zinciri olusturun. Her seviyede yeni ozellik/metot ekleyin (Hayvan: canliMi=true, Memeli: sutVer(), Kopek: havla()). Object.create ile prototype zincirini kurun.",
  response: "const Hayvan = {\n    canliMi: true,\n    nefesAl: function() { return 'Nefes aliyorum'; },\n    init: function(isim) { this.isim = isim; return this; }\n};\n\nconst Memeli = Object.create(Hayvan);\nMemeli.sutVer = function() { return `${this.isim} sut veriyor`; };\nMemeli.tuyluMu = true;\n\nconst Kopek = Object.create(Memeli);\nKopek.havla = function() { return `${this.isim}: Hav hav!`; };\nKopek.bacakSayisi = 4;\n\nconst karabas = Object.create(Kopek).init('Karabas');\nconsole.log(karabas.havla());\nconsole.log(karabas.sutVer());\nconsole.log(karabas.nefesAl());\nconsole.log(karabas.canliMi);\nconsole.log(Hayvan.isPrototypeOf(karabas));\nconsole.log(Kopek.isPrototypeOf(karabas));",
  language: "javascript",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "ES6 modulleri (import/export) ile bir matematik kutuphanesi olusturun. Bir modulde topla, carp, bol fonksiyonlarini export edin (default ve named export karisik). Ana dosyada import edip kullanin. Re-export ile ara modul yapin.",
  response: "// math/aritmetik.js\nexport function topla(...s) { return s.reduce((a,b) => a+b, 0); }\nexport function carp(...s) { return s.reduce((a,b) => a*b, 1); }\nexport default function bol(a,b) { if(b===0) throw Error('Sifira bolunemez'); return a/b; }\n\n// math/geometri.js\nexport function daireAlan(r) { return Math.PI * r**2; }\nexport function dikdortgenAlan(g,y) { return g*y; }\n\n// math/index.js (re-export)\nexport { topla, carp } from './aritmetik.js';\nexport { default as bolme } from './aritmetik.js';\nexport { daireAlan, dikdortgenAlan } from './geometri.js';",
  language: "javascript",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "reduce metodunu kullanarak: 1) Bir dizideki kelimelerin frekansini cikaran fonksiyon, 2) Ic ice diziyi duzlestiren (flatten) fonksiyon, 3) Bir nesne dizisini belirli bir anahtara gore gruplandiran fonksiyon yazin.",
  response: "const kelimeler = ['elma','armut','elma','kiraz','armut','elma'];\nconst frekans = kelimeler.reduce((acc, k) => { acc[k] = (acc[k]||0)+1; return acc; }, {});\nconsole.log('Frekans:', frekans);\n\nconst icIce = [1, [2,3], [4,[5,6]], 7];\nfunction duzlestir(d) {\n    return d.reduce((acc, e) => acc.concat(Array.isArray(e) ? duzlestir(e) : e), []);\n}\nconsole.log('Duz:', duzlestir(icIce));\n\nconst kullanicilar = [\n    { ad: 'Ali', sehir: 'Istanbul' }, { ad: 'Veli', sehir: 'Ankara' },\n    { ad: 'Ayse', sehir: 'Istanbul' }, { ad: 'Fatma', sehir: 'Ankara' }\n];\nconst gruplanmis = kullanicilar.reduce((acc, k) => {\n    (acc[k.sehir] = acc[k.sehir] || []).push(k); return acc;\n}, {});\nconsole.log('Gruplanmis:', gruplanmis);",
  language: "javascript",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Proxy ve Symbol kullanarak bir nesnenin tum property'lerine erisimi loglayan ve property silme islemini engelleyen bir korumali nesne olusturun. Ayrica Symbol.iterator ile bir nesneyi iterate edilebilir yapin.",
  response: "const handler = {\n    get: (h, p) => { console.log(`[ERISIM] ${String(p)}`); return p in h ? h[p] : `'${String(p)}' bulunamadi`; },\n    set: (h, p, v) => { console.log(`[SET] ${String(p)} = ${v}`); h[p] = v; return true; },\n    deleteProperty: (h, p) => { console.log(`[ENGELLENDI] ${String(p)} silinemez!`); return false; }\n};\n\nconst k = new Proxy({ ad: 'Ali', yas: 30 }, handler);\nconsole.log(k.ad);\nk.yas = 31;\ndelete k.ad;\n\nconst takim = {\n    uyeler: ['Ali','Veli','Ayse'],\n    [Symbol.iterator]: function* () { for (const u of this.uyeler) yield u; }\n};\nfor (const u of takim) console.log('Uye:', u);",
  language: "javascript",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

// JAVA (5)
items.push({
  instruction: "Stream API ve lambda ifadeleri kullanarak bir ogrenci listesini filtreleyin, siralayin ve donusturun. Ogrenci sinifi (isim, notOrtalamasi, bolum) alanlarina sahip olsun. Not ortalamasi 70+ ogrencileri notlarina gore azalan siralayip, DTO'ya map'leyin.",
  response: "import java.util.*;\nimport java.util.stream.*;\n\nclass Ogrenci {\n    String isim; double not; String bolum;\n    Ogrenci(String i, double n, String b) { isim=i; not=n; bolum=b; }\n    public String getIsim() { return isim; }\n    public double getNotOrtalamasi() { return not; }\n    public String getBolum() { return bolum; }\n}\nclass OgrenciDTO {\n    String isim, bolum;\n    OgrenciDTO(String i, String b) { isim=i; bolum=b; }\n    public String toString() { return isim+\" - \"+bolum; }\n}\npublic class Main {\n    public static void main(String[] a) {\n        List<Ogrenci> o = Arrays.asList(\n            new Ogrenci(\"Ali\",85.5,\"Bilg. Muh.\"), new Ogrenci(\"Veli\",45,\"Elektrik\"),\n            new Ogrenci(\"Ayse\",92.3,\"Bilg. Muh.\"), new Ogrenci(\"Fatma\",70.5,\"Makine\"),\n            new Ogrenci(\"Mehmet\",60,\"Insaat\"), new Ogrenci(\"Zeynep\",88,\"Endustri\"));\n        o.stream().filter(x->x.getNotOrtalamasi()>70)\n            .sorted(Comparator.comparingDouble(Ogrenci::getNotOrtalamasi).reversed())\n            .map(x->new OgrenciDTO(x.getIsim(),x.getBolum()))\n            .collect(Collectors.toList())\n            .forEach(System.out::println);\n    }\n}",
  language: "java",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Optional kullanarak null-safe bir zincirleme islem yazin. Kullanici (adres, sehir) alanlarini icersin. Optional.ofNullable ile ic ice Optional'lari flatMap ile birlestirip, orElseThrow ile hata firlatin. orElse, ifPresent ve filter kullanimini gosterin.",
  response: "import java.util.Optional;\nclass Adres { String sehir, ilce; Adres(String s, String i) { sehir=s; ilce=i; } public String getSehir() { return sehir; } }\nclass Kullanici { String isim; Adres adres; Kullanici(String i, Adres a) { isim=i; adres=a; } public Optional<Adres> getAdres() { return Optional.ofNullable(adres); } }\npublic class Main {\n    public static void main(String[] a) {\n        Kullanici k1 = new Kullanici(\"Ali\", new Adres(\"Istanbul\",\"Kadikoy\"));\n        Kullanici k2 = new Kullanici(\"Veli\", null);\n        Kullanici k3 = null;\n        String s = Optional.ofNullable(k1).flatMap(Kullanici::getAdres).map(Adres::getSehir).orElse(\"Bilinmiyor\");\n        System.out.println(\"Sehir: \"+s);\n        try { Optional.ofNullable(k2).flatMap(Kullanici::getAdres).map(Adres::getSehir).orElseThrow(()->new RuntimeException(\"Adres yok\")); }\n        catch(Exception e) { System.out.println(\"Hata: \"+e.getMessage()); }\n        Optional.ofNullable(k3).ifPresentOrElse(k->System.out.println(\"Var\"), ()->System.out.println(\"Null\"));\n        Optional.ofNullable(k1).flatMap(Kullanici::getAdres).filter(a->a.getSehir().equals(\"Istanbul\")).ifPresent(a->System.out.println(\"Istanbul\"));\n    }\n}",
  language: "java",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "CompletableFuture kullanarak 3 asenkron gorevi paralel calistirip sonuclarini birlestirin. allOf ile tum gorevlerin bitmesini bekleyin, thenApply ile sonuclari isleyin. Ayrica exceptionally ile hata yonetimi ve thenCompose ile zincirleme islem yapin.",
  response: "import java.util.concurrent.*;\nimport java.util.stream.*;\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        CompletableFuture<Integer> s1 = CompletableFuture.supplyAsync(()->{ sleep(1000); return 250; });\n        CompletableFuture<Integer> s2 = CompletableFuture.supplyAsync(()->{ sleep(1500); return 180; });\n        CompletableFuture<Integer> s3 = CompletableFuture.supplyAsync(()->{ sleep(800); return 320; });\n        CompletableFuture<Integer> t = CompletableFuture.allOf(s1,s2,s3)\n            .thenApply(v->Stream.of(s1,s2,s3).map(CompletableFuture::join).mapToInt(Integer::intValue).sum());\n        System.out.println(\"Toplam: \"+t.get());\n        CompletableFuture<String> h = CompletableFuture.supplyAsync(()->{ if(Math.random()>0.5) throw new RuntimeException(\"Hata\"); return \"OK\"; })\n            .exceptionally(e->\"Hata: \"+e.getMessage()).thenApply(x->\"Sonuc: \"+x);\n        System.out.println(h.get());\n        CompletableFuture<String> z = CompletableFuture.supplyAsync(()->\"K-42\").thenCompose(id->CompletableFuture.supplyAsync(()->id+\" yuklendi\"));\n        System.out.println(z.get());\n    }\n    static void sleep(int m) { try { Thread.sleep(m); } catch(InterruptedException e){} }\n}",
  language: "java",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "FunctionalInterface kullanarak kendi fonksiyonel arayuzunuzu olusturun (Donusturucu<T,R>). Lambda, method referanslari ve Stream ile kullanin. Consumer, Supplier, Function ve Predicate ornekleyin.",
  response: "import java.util.*;\nimport java.util.function.*;\nimport java.util.stream.*;\n\n@FunctionalInterface\ninterface Donusturucu<T,R> { R donustur(T g); default Donusturucu<T,R> once(Consumer<T> i) { return t->{i.accept(t); return donustur(t);}; } }\n\npublic class Main {\n    public static void main(String[] a) {\n        Donusturucu<String,Integer> u = String::length;\n        Donusturucu<String,String> b = String::toUpperCase;\n        System.out.println(u.donustur(\"Merhaba\")+\" \"+b.donustur(\"merhaba\"));\n        Consumer<String> y = System.out::println; y.accept(\"Consumer\");\n        Supplier<Double> r = Math::random; System.out.println(\"Rastgele: \"+r.get());\n        Function<Integer,Integer> kare = x->x*x, ikiEkle = x->x+2;\n        System.out.println(\"5: \"+kare.andThen(ikiEkle).apply(5));\n        Predicate<Integer> cift = x->x%2==0;\n        List<Integer> s = Arrays.asList(1,2,3,4,5,6);\n        System.out.println(\"Cift: \"+s.stream().filter(cift).collect(Collectors.toList()));\n    }\n}",
  language: "java",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Enum icinde metot ve alan tanimlayarak bir HaftalikMesai enum'u olusturun. Her gun icin calisma saati ve mesai tipi (TAM/YARIM) tutsun. hesaplaMaas(int) metodu olsun. Enum sabitlerini Stream ile isleyin.",
  response: "import java.util.stream.*;\nenum HaftalikMesai {\n    PAZARTESI(8,Tip.TAM), SALI(8,Tip.TAM), CARSAMBA(8,Tip.TAM),\n    PERSEMBE(8,Tip.TAM), CUMA(6,Tip.YARIM), CUMARTESI(0,Tip.TATIL), PAZAR(0,Tip.TATIL);\n    enum Tip { TAM, YARIM, TATIL }\n    private final int s; private final Tip t;\n    HaftalikMesai(int s, Tip t) { this.s=s; this.t=t; }\n    public int getS() { return s; } public Tip getT() { return t; }\n    public double maas(int ucret) { return s*ucret; }\n    public static int toplamSaat() { return Stream.of(values()).mapToInt(HaftalikMesai::getS).sum(); }\n}\npublic class Main {\n    public static void main(String[] a) {\n        int u=150;\n        Stream.of(HaftalikMesai.values()).forEach(g->System.out.printf(\"%s: %ds -> %.0f TL%n\",g,g.getS(),g.maas(u)));\n        System.out.println(\"Toplam saat: \"+HaftalikMesai.toplamSaat());\n        double t = Stream.of(HaftalikMesai.values()).mapToDouble(g->g.maas(u)).sum();\n        System.out.println(\"Toplam maas: \"+t);\n    }\n}",
  language: "java",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

// TYPESCRIPT (4)
items.push({
  instruction: "Conditional Types ve Generic Constraints kullanarak ExtractPropertyNamesOfType<T,U> ile T tipindeki U turundeki property isimlerini cikarsin. DeepReadonly<T> ile ic ice property'leri readonly yapan mapped type olusturun.",
  response: "type ExtractPropertyNamesOfType<T, U> = { [K in keyof T]: T[K] extends U ? K : never }[keyof T];\ntype DeepReadonly<T> = { readonly [K in keyof T]: T[K] extends object ? (T[K] extends Function ? T[K] : DeepReadonly<T[K]>) : T[K]; };\n\ninterface Kullanici { ad: string; yas: number; email: string; }\ntype StringKeys = ExtractPropertyNamesOfType<Kullanici, string>; // \"ad\" | \"email\"\n\ninterface Config { sunucu: { host: string; port: number; kimlik: { user: string; pass: string; }; }; }\ntype SabitConfig = DeepReadonly<Config>;\nconst c: SabitConfig = { sunucu: { host: \"localhost\", port: 8080, kimlik: { user: \"admin\", pass: \"1234\" } } };",
  language: "typescript",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Mapped Types ve Template Literal Types kullanarak CRUD ({entity}Get, {entity}Post, {entity}Put, {entity}Delete) tiplerini otomatik ureten generic yazin. Ayrica entity event tipleri ({entity}Created, {entity}Updated, {entity}Deleted) olusturun.",
  response: "type CrudEndpoints<T extends string> = {\n    [K in T as `${Capitalize<K>}GetRequest`]: { id: number };\n    [K in T as `${Capitalize<K>}GetResponse`]: Record<string, unknown>;\n    [K in T as `${Capitalize<K>}PostRequest`]: Record<string, unknown>;\n    [K in T as `${Capitalize<K>}PostResponse`]: { id: number };\n    [K in T as `${Capitalize<K>}PutRequest`]: { id: number } & Record<string, unknown>;\n    [K in T as `${Capitalize<K>}PutResponse`]: { success: boolean };\n    [K in T as `${Capitalize<K>}DeleteRequest`]: { id: number };\n    [K in T as `${Capitalize<K>}DeleteResponse`]: { success: boolean };\n};\ntype EntityEvents<T extends string> = {\n    [K in T as `${Capitalize<K>}Created`]: { entityId: number; timestamp: Date };\n    [K in T as `${Capitalize<K>}Updated`]: { entityId: number; degisenAlanlar: string[]; timestamp: Date };\n    [K in T as `${Capitalize<K>}Deleted`]: { entityId: number; timestamp: Date };\n};\ntype FullApi<T extends string> = CrudEndpoints<T> & EntityEvents<T>;\ntype KullaniciApi = FullApi<\"kullanici\">;",
  language: "typescript",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Discriminated Unions, satisfies operator ve never tipi ile exhaustive type checking yapin. API response tiplerini discriminator ile ayirt edin. satisfies ile bir nesnenin bir tipe uydugunu dogrulayin.",
  response: "type ApiResponse =\n    | { durum: \"basarili\"; veri: unknown; mesaj: string }\n    | { durum: \"hata\"; hataKodu: number; hataMesaji: string }\n    | { durum: \"yukleniyor\"; yuzde: number };\n\nfunction handler(y: ApiResponse): string {\n    switch (y.durum) {\n        case \"basarili\": return `OK: ${y.mesaj}`;\n        case \"hata\": return `Hata ${y.hataKodu}: ${y.hataMesaji}`;\n        case \"yukleniyor\": return `%${y.yuzde}`;\n        default: const _: never = y; return _;\n    }\n}\n\ninterface Kullanici { ad: string; yas: number; email: string; }\nconst k = { ad: \"Ali\", yas: 30, email: \"a@b.com\" } satisfies Kullanici;\n\nconst cfg = { apiUrl: \"https://x.com\", timeout: 5000 } satisfies Record<string, string | number>;",
  language: "typescript",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Infer keyword'unu kullanarak Conditional Types ile ReturnType, PromiseType, ArrayElementType ve FunctionArguments yardimci tiplerini yazin. Gercek fonksiyonlar uzerinde test edin.",
  response: "type MyReturnType<T> = T extends (...args: unknown[]) => infer R ? R : never;\ntype PromiseType<T> = T extends Promise<infer U> ? U : T;\ntype ArrayElementType<T> = T extends (infer U)[] ? U : never;\ntype FunctionArguments<T> = T extends (...args: infer A) => unknown ? A : never;\n\nfunction kullaniciGetir(id: number, page: number): Promise<string[]> {\n    return Promise.resolve([\"Ali\", \"Veli\"]);\n}\nfunction toplama(...s: number[]): number { return s.reduce((a,b)=>a+b, 0); }\n\ntype R1 = MyReturnType<typeof kullaniciGetir>;       // Promise<string[]>\ntype R2 = PromiseType<R1>;                            // string[]\ntype R3 = ArrayElementType<R2>;                       // string\ntype R4 = FunctionArguments<typeof kullaniciGetir>;   // [id: number, page: number]\ntype R5 = FunctionArguments<typeof toplama>;          // [...s: number[]]\n\nconst args: R4 = [1, 10];\nconst elem: R3 = \"test\";",
  language: "typescript",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

// GO (5)
items.push({
  instruction: "Goroutines ve channels kullanarak bir isci havuzu (worker pool) olusturun. 5 isci, 20 isi paralel issin. Her isci bir isi alip islesin ve sonucu result kanalina gondesin. sync.WaitGroup ile tum iscilerin bitmesini bekleyin.",
  response: 'package main\nimport (\n\t"fmt"\n\t"sync"\n\t"time"\n)\ntype Job struct { ID int; Data int }\ntype Result struct { JobID int; Output int; WorkerID int }\nfunc worker(id int, jobs <-chan Job, results chan<- Result, wg *sync.WaitGroup) {\n\tdefer wg.Done()\n\tfor job := range jobs {\n\t\ttime.Sleep(time.Millisecond * time.Duration(100+job.Data%50))\n\t\tresults <- Result{job.ID, job.Data * 2, id}\n\t}\n}\nfunc main() {\n\tconst nw, nj = 5, 20\n\tjobs := make(chan Job, nj)\n\tresults := make(chan Result, nj)\n\tvar wg sync.WaitGroup\n\tfor i := 1; i <= nw; i++ { wg.Add(1); go worker(i, jobs, results, &wg) }\n\tfor i := 1; i <= nj; i++ { jobs <- Job{i, i * 10} }\n\tclose(jobs)\n\tgo func() { wg.Wait(); close(results) }()\n\tfor r := range results { fmt.Printf("Isci %d -> Job %d: %d\\n", r.WorkerID, r.JobID, r.Output) }\n}',
  language: "go",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "select ile kanal islemlerini yonetin. Iki farkli sensor (sensor1, sensor2) verilerini dinleyen sistem simule edin. timeout ve default case kullanarak kanallarin bloke olmasini engelleyin.",
  response: 'package main\nimport (\n\t"fmt"\n\t"math/rand"\n\t"time"\n)\nfunc sensorOku(isim string, k chan<- int) {\n\tfor i := 1; i <= 5; i++ {\n\t\ttime.Sleep(time.Duration(rand.Intn(500)+100) * time.Millisecond)\n\t\tk <- i * rand.Intn(100)\n\t}\n}\nfunc main() {\n\ts1 := make(chan int); s2 := make(chan int)\n\tgo sensorOku("Sicaklik", s1); go sensorOku("Nem", s2)\n\ttimeout := time.After(3 * time.Second)\n\tfor {\n\t\tselect {\n\t\tcase v := <-s1: fmt.Printf("Sicaklik: %d\\u00b0C\\n", v)\n\t\tcase v := <-s2: fmt.Printf("Nem: %d%%\\n", v)\n\t\tdefault: time.Sleep(200 * time.Millisecond); fmt.Print(".")\n\t\tcase <-timeout: fmt.Println("\\nZaman asimi!"); return\n\t\t}\n\t}\n}',
  language: "go",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "sync.Mutex ile thread-safe Counter yapin. Increment, Decrement ve Value metotlari olsun. 1000 goroutine ile sayaci 1000 kez artirip dogrulugunu test edin. Ayrica sync.RWMutex ile SafeCache yapin.",
  response: 'package main\nimport (\n\t"fmt"\n\t"sync"\n)\ntype Counter struct { mu sync.Mutex; val int }\nfunc (c *Counter) Inc() { c.mu.Lock(); defer c.mu.Unlock(); c.val++ }\nfunc (c *Counter) Dec() { c.mu.Lock(); defer c.mu.Unlock(); c.val-- }\nfunc (c *Counter) Val() int { c.mu.Lock(); defer c.mu.Unlock(); return c.val }\ntype Cache struct { mu sync.RWMutex; data map[string]string }\nfunc (c *Cache) Get(k string) string { c.mu.RLock(); defer c.mu.RUnlock(); return c.data[k] }\nfunc (c *Cache) Set(k, v string) { c.mu.Lock(); defer c.mu.Unlock(); if c.data==nil {c.data=make(map[string]string)}; c.data[k]=v }\nfunc main() {\n\tvar cnt Counter; var wg sync.WaitGroup\n\tfor i:=0;i<1000;i++{wg.Add(1);go func(){defer wg.Done();cnt.Inc()}()}\n\twg.Wait(); fmt.Printf("Counter: %d\\n", cnt.Val())\n\tcache:=Cache{data:make(map[string]string)}\n\tfor i:=0;i<100;i++{wg.Add(1);go func(i int){defer wg.Done();k:=fmt.Sprintf("k-%d",i);cache.Set(k,"v")}(i)}\n\twg.Wait(); fmt.Println("Cache OK")\n}',
  language: "go",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Go interface'leri ile bir odeme sistemi tasarlayin. OdemeYontemi (Ode(miktar float64) error) interface'i tanimlayin. KrediKarti, Havale, Cuzdan struct'lari implemente etsin. Fatura struct'i ile cok bicimli odeme yapin.",
  response: 'package main\nimport (\n\t"errors"\n\t"fmt"\n\t"math"\n)\ntype OdemeYontemi interface { Ode(float64) error; Ad() string }\ntype KK struct { bakiye float64 }\nfunc (k *KK) Ode(m float64) error { if k.bakiye<m {return errors.New("yetersiz")}; k.bakiye-=m+m*0.03; return nil }\nfunc (k *KK) Ad() string { return "Kredi Karti" }\ntype Havale struct { iban string }\nfunc (h *Havale) Ode(m float64) error { if m>50000 {return errors.New("limit");}; fmt.Printf("Havale: %s %.2f\\n",h.iban,m); return nil }\nfunc (h *Havale) Ad() string { return "Havale" }\ntype Cuzdan struct { bakiye float64 }\nfunc (c *Cuzdan) Ode(m float64) error { if c.bakiye<m {return fmt.Errorf("yetersiz %.2f",c.bakiye)}; c.bakiye-=m; return nil }\nfunc (c *Cuzdan) Ad() string { return "Cuzdan" }\ntype Fatura struct { no string; tutar float64; yontem OdemeYontemi }\nfunc (f *Fatura) Odeme() error {\n\tfmt.Printf("%s: %.2f [%s]\\n",f.no,f.tutar,f.yontem.Ad())\n\tif err:=f.yontem.Ode(math.Round(f.tutar*100)/100); err!=nil {return fmt.Errorf("basarisiz: %w",err)}\n\tfmt.Println("OK"); return nil\n}\nfunc main() {\n\tk:=&KK{bakiye:10000}; h:=&Havale{iban:"TR123"}; c:=&Cuzdan{bakiye:500}\n\tfor _,f:=range []Fatura{{"F1",250,k},{"F2",15000,h},{"F3",75.99,c}}{if err:=f.Odeme(); err!=nil{fmt.Printf("HATA: %v\\n",err)}}\n}',
  language: "go",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Go'da hata sarma (error wrapping) ve defer kullanimini gosteren bir dosya isleme ornegi yazin. Dosyayi okuyup sayilari toplayan fonksiyon yazin. errors.Is ve errors.As ile hata turu kontrolu yapin.",
  response: 'package main\nimport (\n\t"bufio"\n\t"errors"\n\t"fmt"\n\t"os"\n\t"strconv"\n\t"strings"\n)\ntype ParseError struct { Line int; Val string; Err error }\nfunc (e *ParseError) Error() string { return fmt.Sprintf("satir %d: %s - %v", e.Line, e.Val, e.Err) }\nfunc (e *ParseError) Unwrap() error { return e.Err }\nfunc topla(path string) (int, error) {\n\tf, err := os.Open(path)\n\tif err != nil { return 0, fmt.Errorf("acilamadi: %w", err) }\n\tdefer func() { f.Close(); fmt.Println("Kapatildi") }()\n\tsc := bufio.NewScanner(f); sum := 0; line := 0\n\tfor sc.Scan() {\n\t\tline++\n\t\tt := strings.TrimSpace(sc.Text())\n\t\tif t == "" { continue }\n\t\tn, err := strconv.Atoi(t)\n\t\tif err != nil { return 0, &ParseError{line, t, err} }\n\t\tsum += n\n\t}\n\treturn sum, sc.Err()\n}\nfunc main() {\n\tdefer func() { if r := recover(); r != nil { fmt.Printf("Panik: %v\\n", r) } }()\n\ts, err := topla("sayilar.txt")\n\tif err != nil {\n\t\tvar pe *ParseError\n\t\tswitch {\n\t\tcase errors.As(err, &pe): fmt.Printf("Parse: %v\\n", pe)\n\t\tcase errors.Is(err, os.ErrNotExist): fmt.Println("Dosya yok")\n\t\tdefault: fmt.Printf("Hata: %v\\n", err)\n\t\t}\n\t\treturn\n\t}\n\tfmt.Printf("Toplam: %d\\n", s)\n}',
  language: "go",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

// SQL (5)
items.push({
  instruction: "WITH (CTE) ve window function (ROW_NUMBER, RANK, DENSE_RANK) kullanarak her departmandaki en yuksek maasli 3 calisani getirin. employees ve departments tablolari. LAG ile maas farkini hesaplayin.",
  response: "WITH sirali AS (\n    SELECT e.id, e.name, e.salary, d.name AS dept,\n        ROW_NUMBER() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS sira,\n        RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS rnk,\n        LAG(e.salary) OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS onceki,\n        e.salary - LAG(e.salary) OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS fark\n    FROM employees e JOIN departments d ON e.department_id = d.id\n)\nSELECT dept, sira, name, salary, onceki, fark\nFROM sirali WHERE sira <= 3\nORDER BY dept, sira;",
  language: "sql",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Recursive CTE ile organizasyon semasindaki hiyerarsiyi sorgulayin. employees (id, name, manager_id, position). Her calisanin seviyesini, yonetici zincirini ve altindaki kisi sayisini gosterin.",
  response: "WITH RECURSIVE org AS (\n    SELECT id, name, position, manager_id, 0 AS seviye, CAST(name AS VARCHAR(500)) AS zincir\n    FROM employees WHERE manager_id IS NULL\n    UNION ALL\n    SELECT e.id, e.name, e.position, e.manager_id, o.seviye+1, CONCAT(o.zincir, ' → ', e.name)\n    FROM employees e JOIN org o ON e.manager_id = o.id\n), alt AS (\n    SELECT manager_id, COUNT(*) AS sayi FROM employees WHERE manager_id IS NOT NULL GROUP BY manager_id\n)\nSELECT o.id, o.name, o.position, o.seviye, o.zincir, COALESCE(a.sayi,0) AS alt_sayi\nFROM org o LEFT JOIN alt a ON o.id = a.manager_id\nORDER BY o.seviye, o.name;",
  language: "sql",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "PIVOT (CASE ile) ve window function kullanarak aylik satis raporu. Her kategori-ay toplam satisi ve kategorinin genel toplam icindeki yuzdesini (SUM OVER) hesaplayin.",
  response: "WITH aylik AS (\n    SELECT p.category, EXTRACT(MONTH FROM s.sale_date) AS ay, SUM(s.amount) AS t\n    FROM sales s JOIN products p ON s.product_id = p.id\n    WHERE s.sale_date >= '2024-01-01' AND s.sale_date < '2025-01-01'\n    GROUP BY p.category, EXTRACT(MONTH FROM s.sale_date)\n), pivot AS (\n    SELECT category,\n        SUM(CASE WHEN ay=1 THEN t ELSE 0 END) AS ocak,\n        SUM(CASE WHEN ay=2 THEN t ELSE 0 END) AS subat,\n        SUM(CASE WHEN ay=3 THEN t ELSE 0 END) AS mart,\n        SUM(t) AS toplam\n    FROM aylik GROUP BY category\n), gt AS (SELECT SUM(toplam) AS gtop FROM pivot)\nSELECT p.*, ROUND(p.toplam*100.0/gt.gtop,2) AS yuzde\nFROM pivot p CROSS JOIN gt ORDER BY p.toplam DESC;",
  language: "sql",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "Complex JOIN'ler ve alt sorgular ile e-ticaret sorgusu. Siparis tarihinden son 30 gunde ayni kategoriden kac urun satildigini ve musterinin toplam harcamasini alt sorgularla hesaplayin.",
  response: "SELECT c.id AS mid, c.name AS mad, o.id AS sid, o.order_date, p.name AS urun,\n    cat.name AS kat, oi.quantity, oi.unit_price,\n    (SELECT SUM(oi2.quantity) FROM order_items oi2\n     JOIN products p2 ON oi2.product_id = p2.id\n     JOIN orders o2 ON oi2.order_id = o2.id\n     WHERE p2.category_id = p.category_id\n       AND o2.order_date BETWEEN o.order_date - INTERVAL '30 days' AND o.order_date\n    ) AS son30_kat_satis,\n    (SELECT COALESCE(SUM(oi3.quantity*oi3.unit_price),0)\n     FROM order_items oi3 JOIN orders o3 ON oi3.order_id = o3.id\n     WHERE o3.customer_id = c.id AND o3.order_date <= o.order_date\n    ) AS toplam_harcama,\n    ROW_NUMBER() OVER (PARTITION BY o.id ORDER BY (oi.quantity*oi.unit_price) DESC) AS sira\nFROM customers c\nJOIN orders o ON c.id = o.customer_id\nJOIN order_items oi ON o.id = oi.order_id\nJOIN products p ON oi.product_id = p.id\nJOIN categories cat ON p.category_id = cat.id\nORDER BY c.id, o.order_date, sira;",
  language: "sql",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "UNION, CASE WHEN ile kapsamli veri analizi. Aktif/pasif musterileri karsilastirin. Her segment icin min, max, ortalama siparis degerlerini CASE ile kategorize edip tek sonuc kumesinde birlestirin.",
  response: "WITH analiz AS (\n    SELECT c.id, c.segment, c.is_active,\n        COUNT(DISTINCT o.id) AS sip_say,\n        COALESCE(SUM(oi.quantity*oi.unit_price),0) AS harca,\n        COALESCE(AVG(oi.quantity*oi.unit_price),0) AS ort\n    FROM customers c\n    LEFT JOIN orders o ON c.id = o.customer_id\n    LEFT JOIN order_items oi ON o.id = oi.order_id\n    GROUP BY c.id, c.segment, c.is_active\n)\nSELECT 'Aktif' AS tip, segment, COUNT(*) AS sayi,\n    ROUND(AVG(harca),2) AS ort_harca,\n    ROUND(MAX(harca),2) AS maks, ROUND(MIN(harca),2) AS min,\n    CASE WHEN AVG(ort) > 1000 THEN 'Premium'\n         WHEN AVG(ort) > 500 THEN 'Standart'\n         WHEN AVG(ort) > 100 THEN 'Ekonomik' ELSE 'Dusuk' END AS kat\nFROM analiz WHERE is_active = TRUE GROUP BY segment\nUNION ALL\nSELECT 'Pasif', segment, COUNT(*), ROUND(AVG(harca),2),\n    ROUND(MAX(harca),2), ROUND(MIN(harca),2), 'Pasif'\nFROM analiz WHERE is_active = FALSE GROUP BY segment\nORDER BY tip, sayi DESC;",
  language: "sql",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

// WEB (5)
items.push({
  instruction: "Flexbox ile responsive kart duzeni. Her kartta baslik, aciklama, buton. Kartlar min 250px, max 1fr. Ilk kart 2x genislikte. Ayni yukseklikte hizalansin.",
  response: '<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Flexbox</title><style>\n*{margin:0;padding:0;box-sizing:border-box}\nbody{font-family:"Segoe UI",sans-serif;background:#f0f2f5;padding:2rem;display:flex;flex-direction:column;align-items:center}\n.container{display:flex;flex-wrap:wrap;gap:1.5rem;justify-content:center;max-width:1200px;width:100%}\n.card{flex:1 1 250px;background:#fff;border-radius:12px;padding:1.5rem;box-shadow:0 4px 6px rgba(0,0,0,0.07);display:flex;flex-direction:column}\n.card.wide{flex:2 1 500px}\n.card h2{font-size:1.25rem;color:#1a1a2e;margin-bottom:.75rem;padding-bottom:.75rem;border-bottom:2px solid #e0e0e0}\n.card p{font-size:.9rem;color:#555;flex:1;margin-bottom:1rem;line-height:1.6}\n.btn{display:inline-block;padding:.6rem 1.2rem;background:#4361ee;color:#fff;border-radius:6px;text-decoration:none;font-weight:600;align-self:flex-start}\n</style></head><body><div class="container">\n<article class="card wide"><h2>One Cikan</h2><p>Profesyonel danismanlik.</p><a href="#" class="btn">Detay</a></article>\n<article class="card"><h2>Web Tasarim</h2><p>Modern web siteleri.</p><a href="#" class="btn">Incele</a></article>\n<article class="card"><h2>Mobil App</h2><p>iOS & Android.</p><a href="#" class="btn">Incele</a></article>\n<article class="card"><h2>SEO</h2><p>Ust sira garanti.</p><a href="#" class="btn">Incele</a></article>\n</div></body></html>',
  language: "web",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "CSS Grid ile magazine sayfasi: header, ana haber (2 kolon), 3 kucuk haber, sidebar, footer. grid-template-areas kullanin. Tablet/mobil media queries.",
  response: '<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Grid</title><style>\n*{margin:0;padding:0;box-sizing:border-box}\nbody{font-family:Georgia,serif;background:#fafafa;padding:1rem}\n.sayfa{display:grid;grid-template-columns:2fr 1fr;gap:1.5rem;max-width:1200px;margin:0 auto;grid-template-areas:"header header" "ana ana" "kucuk sidebar" "footer footer"}\nheader{grid-area:header;text-align:center;padding:2rem;background:linear-gradient(135deg,#1a1a2e,#16213e);color:#fff;border-radius:12px}\n.ana{grid-area:ana;display:grid;grid-template-columns:2fr 1fr;gap:1rem;background:#fff;border-radius:12px;padding:1.5rem}\n.kucuk{grid-area:kucuk;display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}\n.kucuk article{background:#fff;border-radius:8px;padding:1rem}\naside{grid-area:sidebar;background:#fff;border-radius:12px;padding:1.5rem}\nfooter{grid-area:footer;text-align:center;padding:1.5rem;background:#1a1a2e;color:#fff;border-radius:12px}\n@media(max-width:768px){.sayfa{grid-template-columns:1fr;grid-template-areas:"header""ana""kucuk""sidebar""footer"}.ana{grid-template-columns:1fr}.kucuk{grid-template-columns:repeat(2,1fr)}}\n@media(max-width:480px){.kucuk{grid-template-columns:1fr}}\n</style></head><body><div class="sayfa">\n<header><h1>HABER</h1><p>Son Dakika</p></header>\n<main class="ana"><div style="background:linear-gradient(45deg,#667eea,#764ba2);border-radius:8px;min-height:200px"></div><div><h2>Yeni Gezegen Kesfi</h2><p>Bilim insanlari yeni bir gezegen buldu.</p></div></main>\n<section class="kucuk"><article><h3>Teknoloji</h3><p>Zirve basladi</p></article><article><h3>Borsa</h3><p>Rektor</p></article><article><h3>Spor</h3><p>Sampiyon</p></article></section>\n<aside><h3>Populer</h3><p>1. Ekonomi</p><p>2. Egitim</p></aside>\n<footer>&copy; 2024</footer>\n</div></body></html>',
  language: "web",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "CSS animasyonlari ile toast bildirimi. Slide-in girsin, 3 sn gorunsun, slide-out ciksin. Hover'da olceklenip donen spinner. CSS degiskenleri ile yonetim.",
  response: '<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Toast</title><style>\n:root{--yesil:#43e97b;--kirmizi:#f5576c;--sari:#ffd93d;--spinner:#4361ee;--sure:.5s}\n*{margin:0;padding:0;box-sizing:border-box}\nbody{font-family:"Segoe UI",sans-serif;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;background:#f0f2f5;gap:2rem}\n.btn-group{display:flex;gap:1rem}\n.btn-group button{padding:.75rem 1.5rem;border:none;border-radius:8px;font-weight:600;cursor:pointer}\n.btn-yesil{background:var(--yesil);color:#fff}\n.btn-kirmizi{background:var(--kirmizi);color:#fff}\n.btn-sari{background:var(--sari);color:#333}\n#toastBox{position:fixed;top:1.5rem;right:1.5rem;z-index:1000;display:flex;flex-direction:column;gap:.75rem;pointer-events:none}\n.toast{pointer-events:auto;padding:1rem 1.5rem;border-radius:10px;color:#fff;font-weight:500;box-shadow:0 8px 20px rgba(0,0,0,0.15);animation:gir var(--sure) ease-out}\n.toast.yesil{background:var(--yesil)}.toast.kirmizi{background:var(--kirmizi)}.toast.sari{background:var(--sari);color:#333}\n.toast.cik{animation:cik var(--sure) ease-in forwards}\n@keyframes gir{from{transform:translateX(120%);opacity:0}to{transform:translateX(0);opacity:1}}\n@keyframes cik{from{transform:translateX(0);opacity:1}to{transform:translateX(120%);opacity:0}}\n.spinner{width:50px;height:50px;border:5px solid #e0e0e0;border-top-color:var(--spinner);border-radius:50%;animation:don 1s linear infinite;transition:transform .3s}\n.spinner:hover{animation:don 1s linear infinite,buyu .3s forwards}\n@keyframes don{to{transform:rotate(360deg)}}@keyframes buyu{to{transform:rotate(360deg) scale(1.3)}}\n</style></head><body>\n<div id="toastBox"></div>\n<div class="btn-group">\n<button class="btn-yesil" onclick="t(\'yesil\',\'OK\')">Basarili</button>\n<button class="btn-kirmizi" onclick="t(\'kirmizi\',\'Hata\')">Hata</button>\n<button class="btn-sari" onclick="t(\'sari\',\'Uyari\')">Uyari</button>\n</div>\n<div style="text-align:center"><div class="spinner"></div><p>Yukleniyor...</p></div>\n<script>function t(tip,m){const c=document.getElementById(\'toastBox\');const e=document.createElement(\'div\');e.className=\'toast \'+tip;e.textContent=m;c.appendChild(e);setTimeout(()=>{e.classList.add(\'cik\');e.addEventListener(\'animationend\',()=>e.remove())},3000)}</script>\n</body></html>',
  language: "web",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "CSS transform, transition, :before/:after ile 3D buton ve kart efektleri. Butonlarda press efekti (translateY). Kartlarda 3D flip ve gradient border animasyonu.",
  response: '<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>3D</title><style>\n*{margin:0;padding:0;box-sizing:border-box}\nbody{font-family:"Segoe UI",sans-serif;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:100vh;background:#0f0f1a;padding:2rem;gap:3rem}\n.btns{display:flex;gap:2rem}\n.btn{position:relative;padding:1rem 2.5rem;border:none;border-radius:12px;font-weight:700;color:#fff;cursor:pointer;background:linear-gradient(135deg,#667eea,#764ba2);box-shadow:0 8px 0 #4a3f7a,0 12px 20px rgba(0,0,0,0.3);transition:all .15s;text-transform:uppercase}\n.btn:active{transform:translateY(6px);box-shadow:0 2px 0 #4a3f7a,0 8px 16px rgba(0,0,0,0.2)}\n.btn.green{background:linear-gradient(135deg,#43e97b,#38f9d7);box-shadow:0 8px 0 #2ba86b,0 12px 20px rgba(0,0,0,0.3)}\n.btn.red{background:linear-gradient(135deg,#f093fb,#f5576c);box-shadow:0 8px 0 #c44a7a,0 12px 20px rgba(0,0,0,0.3)}\n.btn::after{content:"";position:absolute;inset:0;border-radius:12px;background:linear-gradient(135deg,rgba(255,255,255,0.2),transparent);opacity:0;transition:opacity .3s}\n.btn:hover::after{opacity:1}.btn:hover{transform:translateY(-2px);box-shadow:0 10px 0 #4a3f7a,0 16px 24px rgba(0,0,0,0.4)}\n.flip{width:260px;height:340px;perspective:1000px}\n.flip-inner{position:relative;width:100%;height:100%;transition:transform .8s cubic-bezier(.175,.885,.32,1.275);transform-style:preserve-3d}\n.flip:hover .flip-inner{transform:rotateY(180deg)}\n.flip-front,.flip-back{position:absolute;width:100%;height:100%;backface-visibility:hidden;border-radius:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:1.5rem;text-align:center}\n.flip-front{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff}\n.flip-front::before{content:"";position:absolute;top:-3px;left:-3px;right:-3px;bottom:-3px;border-radius:18px;background:conic-gradient(#667eea,#764ba2,#f093fb,#f5576c,#ffd93d,#43e97b,#667eea);z-index:-1;animation:borderDon 4s linear infinite}\n@keyframes borderDon{to{transform:rotate(360deg)}}\n.flip-back{background:#1a1a2e;color:#fff;transform:rotateY(180deg);border:2px solid #667eea}\n.cards{display:flex;gap:2rem}\n</style></head><body>\n<div class="btns"><button class="btn">Tikla</button><button class="btn green">Basarili</button><button class="btn red">Sil</button></div>\n<div class="cards"><div class="flip"><div class="flip-inner"><div class="flip-front"><p style="font-size:3rem">🃏</p><p>Cevir</p></div><div class="flip-back"><h3>Premium</h3><p>Sinirsiz erisim</p></div></div></div><div class="flip"><div class="flip-inner"><div class="flip-front"><p style="font-size:3rem">🚀</p><p>Cevir</p></div><div class="flip-back"><h3>Hizli</h3><p>Ayni gun kargo</p></div></div></div></div>\n</body></html>',
  language: "web",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

items.push({
  instruction: "CSS custom properties, clamp(), min()/max(), media queries ile responsive typography sistemi ve kart bileseni. Karanlik/aydinlik tema destegi.",
  response: '<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Tema</title><style>\n:root{--bg:#f8f9fa;--card:#fff;--text:#1a1a2e;--sec:#555;--accent:#4361ee;--border:#e0e0e0;--font:"Segoe UI",sans-serif;--fs:clamp(.95rem,1.2vw+.5rem,1.1rem);--h1:clamp(2rem,4vw+.5rem,2.8rem);--space:clamp(1rem,2vw,1.5rem);--radius:clamp(8px,1.5vw,16px);--container:min(1200px,95vw)}\n[data-theme=dark]{--bg:#0f0f1a;--card:#16213e;--text:#e0e0e0;--sec:#a0aec0;--border:#2d2d4a}\n*{margin:0;padding:0;box-sizing:border-box}\nbody{font-family:var(--font);font-size:var(--fs);background:var(--bg);color:var(--text);padding:var(--space);transition:background .3s,color .3s}\n.container{max-width:var(--container);margin:0 auto}\nbutton{padding:.5rem 1rem;background:var(--accent);color:#fff;border:none;border-radius:var(--radius);cursor:pointer;font-weight:600;margin-bottom:var(--space)}\nh1{font-size:var(--h1);margin-bottom:var(--space)}p{color:var(--sec)}\n.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(280px,100%),1fr));gap:var(--space);margin-top:var(--space)}\n.kart{background:var(--card);border-radius:var(--radius);padding:var(--space);border:1px solid var(--border)}\n.kart .fiyat{font-size:var(--h1);font-weight:700;color:var(--accent)}\n.kart .btn{display:inline-block;padding:.5rem 1rem;background:var(--accent);color:#fff;border-radius:var(--radius);text-decoration:none;margin-top:.5rem}\n</style></head><body>\n<div class="container">\n<button onclick="t()" id="btn">🌙 Karanlik</button>\n<h1>Modern Tasarim</h1><p>clamp() ile responsive sistem.</p>\n<div class="grid">\n<div class="kart"><h3>Baslangic</h3><p>Temel</p><div class="fiyat">49</div><a href="#" class="btn">Basla</a></div>\n<div class="kart"><h3>Pro</h3><p>Ideal</p><div class="fiyat">149</div><a href="#" class="btn">Basla</a></div>\n<div class="kart"><h3>Kurumsal</h3><p>Sinirsiz</p><div class="fiyat">399</div><a href="#" class="btn">Basla</a></div>\n</div></div>\n<script>function t(){const h=document.documentElement,b=document.getElementById("btn");h.getAttribute("data-theme")==="dark"?(h.removeAttribute("data-theme"),b.textContent="🌙 Karanlik"):(h.setAttribute("data-theme","dark"),b.textContent="☀️ Aydinlik")}</script>\n</body></html>',
  language: "web",
  category: "advanced",
  type: "manual",
  format: "advanced"
});

// Write JSON
const outPath = 'C:\\Users\\agnes\\Desktop\\projects\\turkish-code-instructions\\submissions\\advanced_batch.json';
fs.writeFileSync(outPath, JSON.stringify(items, null, 2), 'utf8');
console.log(`Written ${items.length} items to ${outPath}`);
