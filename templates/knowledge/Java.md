# Java Bilgi Referansi

## Genel Bakis
Java, James Gosling tarafindan 1995'te Sun Microsystems'te olusturulmustur. "Bir kere yaz, her yerde calistir" (JVM) felsefesiyle bilinir. Kurumsal uygulamalar, Android gelistirme ve buyuk olcekli sistemlerde yaygindir. Guclu tip guvenligi ve OOP temelleri ile bilinir.

## Temel Syntax

```java
// Degiskenler
String isim = "Ali";
int yas = 25;
double pi = 3.14;
boolean aktif = true;

// Fonksiyon
public String merhaba(String kisi) {
    return "Merhaba, " + kisi + "!";
}

// Kosul
if (yas >= 18) {
    System.out.println("Yetiskin");
} else {
    System.out.println("Cocuk");
}

// Dongu
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

// Dizi
String[] meyveler = {"elma", "armut"};
List<String> liste = new ArrayList<>();
liste.add("muz");
```

## Yaygin Patternler

- **POJO/Bean**: Private alanlar, getter/setter
- **Singleton**: Tek ornek kalibi
- **Builder Pattern**: Karmasik nesne olusumu
- **Strategy/Factory**: Tasarim desenleri
- **Dependency Injection**: Spring ile
- **Stream API**: `list.stream().filter(x -> ...).collect(...)`

## Onemli Kutuphaneler

- **Spring Boot**: Kurumsal uygulama frameworku
- **Hibernate/JPA**: ORM ve veritabani
- **Apache Maven/Gradle**: Build araclari
- **JUnit**: Test frameworku
- **Log4j/SLF4J**: Loglama
- **Jackson/Gson**: JSON serilestirme
- **Lombok**: Kod tekrarlarini azaltma

## Yaygin Hatalar

- Checked exception'lari ignore etmek (bos catch blogu)
- `==` ile String karsilastirmak (`equals()` kullanilmali)
- NullPointerException (optional/null kontrolu)
- `final` kullanmamak (degismezlik)
- Memory leak (kaynaklari kapatmamak, `try-with-resources`)
