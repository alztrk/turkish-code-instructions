# Java Bilgi Referansi

## Genel Bakis

Java, James Gosling onderliginde Sun Microsystems'te 1991'de baslanan "Oak" projesinin 1995'te "Java" adiyla piyasaya surulmesiyle dogmustur. "Bir kere yaz, her yerde calistir" (Write Once, Run Anywhere - WORA) felsefesiyle Java Virtual Machine (JVM) uzerinde calisir. Sun Microsystems 2010'da Oracle tarafindan satin alinmistir.

Java gunumuzde kurumsal uygulamalar (Spring/Java EE), Android mobil uygulamalari (Kotlin ile birlikte), buyuk olcekli finans sistemleri, big data teknolojileri (Apache Hadoop, Spark), ve bulut uygulamalarinda yaygindir. Guclu tip guvenligi, OOP temelleri, zengin kutuphane ekosistemi ve genis topluluk destegi ile bilinir. Java 8 (2014) lambda ve Stream API ile modernlesme yolunda onemli bir adim atmistir. Oracle JDK yaninda OpenJDK acik kaynak alternatifi de yaygindir.

## Temel Syntax

```java
// --- Sinif ve Main Metodu ---
public class Main {
    public static void main(String[] args) {
        System.out.println("Merhaba Dunya!");
    }
}

// --- Degiskenler ve Veri Tipleri ---
String isim = "Ali";
int yas = 25;
double pi = 3.14159;
boolean aktif = true;
char harf = 'A';
byte kucukSayi = 127;
long buyukSayi = 1_000_000_000L;   // L son eki
float ondalik = 3.14f;             // f son eki

// Tip donusumu
int tamSayi = (int) 3.14;          // explicit casting
String metinSayi = String.valueOf(42);

// --- String Islemleri ---
String mesaj = "Merhaba, " + isim + "!";
System.out.println(mesaj.length());
System.out.println(mesaj.toUpperCase());
System.out.println(mesaj.contains("Ali"));
System.out.println(String.format("Yas: %d", yas));

// --- Diziler ---
int[] sayilar = {1, 2, 3, 4, 5};
String[] isimler = new String[3];
isimler[0] = "Ali";

// --- Collections Framework ---
import java.util.*;

List<String> liste = new ArrayList<>();
liste.add("elma");
liste.add("armut");
liste.get(0);                    // elma
for (String meyve : liste) { }   // enhanced for

Set<Integer> kume = new HashSet<>();
kume.add(1); kume.add(2);

Map<String, Integer> sozluk = new HashMap<>();
sozluk.put("Ali", 25);
sozluk.get("Ali");               // 25
sozluk.getOrDefault("Veli", 0);  // 0

// --- Kosullar ---
if (yas >= 18) {
    System.out.println("Yetiskin");
} else if (yas > 12) {
    System.out.println("Ergen");
} else {
    System.out.println("Cocuk");
}

// Switch (Java 14+)
String durum = switch (yas) {
    case 18, 19, 20 -> "Genc yetiskin";
    case 25 -> "Yirmi bes";
    default -> "Diger";
};

// --- Donguler ---
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

for (String meyve : liste) {
    System.out.println(meyve);
}

int i = 0;
while (i < 5) { System.out.println(i++); }

// --- Fonksiyonlar (Metodlar) ---
public static int topla(int a, int b) {
    return a + b;
}

// Overloading
public static double topla(double a, double b) {
    return a + b;
}

// Varargs
public static void yazdir(String... mesajlar) {
    for (String m : mesajlar) System.out.println(m);
}

// --- Sinif ve Nesne Yonelim ---
public class Araba {
    // Alanlar
    private String marka;
    private String model;
    public static final int TEKERLEK = 4;  // sabit

    // Constructor
    public Araba(String marka, String model) {
        this.marka = marka;
        this.model = model;
    }

    // Getter/Setter
    public String getMarka() { return marka; }
    public void setMarka(String marka) { this.marka = marka; }

    // Metod
    public void calistir() {
        System.out.println(marka + " calisiyor...");
    }

    // Static metod
    public static void bilgi() {
        System.out.println("Araba sinifi");
    }
}

// Kalitim
public class ElektrikliAraba extends Araba {
    private int pilKapasitesi;

    public ElektrikliAraba(String marka, String model, int pilKapasitesi) {
        super(marka, model);
        this.pilKapasitesi = pilKapasitesi;
    }

    @Override
    public void calistir() {
        System.out.println("Sessiz calisiyor...");
    }
}

// --- Enum ---
public enum SiparisDurumu {
    BEKLIYOR, HAZIRLANIYOR, KARGODA, TESLIM_EDILDI
}

// --- Interface ---
public interface Hayvan {
    void sesCikar();
    default void uyu() {           // default metod (Java 8+)
        System.out.println("Uyuyor...");
    }
}

public class Kopek implements Hayvan {
    public void sesCikar() { System.out.println("Hav hav!"); }
}

// --- Lambda ve Stream API (Java 8+) ---
List<String> isimler2 = Arrays.asList("Ali", "Veli", "Ayse");
isimler2.stream()
    .filter(s -> s.startsWith("A"))
    .map(String::toUpperCase)
    .forEach(System.out::println);

// --- Hata Yakalama ---
try {
    int bolum = 10 / 0;
} catch (ArithmeticException e) {
    System.err.println("Sifira bolme: " + e.getMessage());
} catch (Exception e) {
    System.err.println("Genel hata: " + e);
} finally {
    System.out.println("Her zaman calisir");
}

// try-with-resources (Java 7+)
try (BufferedReader br = new BufferedReader(new FileReader("dosya.txt"))) {
    System.out.println(br.readLine());
} catch (IOException e) {
    e.printStackTrace();
}

// --- Generic ---
public class Kutu<T> {
    private T icerik;
    public void set(T icerik) { this.icerik = icerik; }
    public T get() { return icerik; }
}
Kutu<String> kutu = new Kutu<>();
kutu.set("Merhaba");

// --- Anotasyonlar ---
@Override
@Deprecated
@SuppressWarnings("unchecked")
```

## Yaygin Patternler

1. **POJO/JavaBean**: Private alanlar, public getter/setter, no-arg constructor
2. **Singleton**: `private static final` ile tek ornek, `getInstance()` metodu
3. **Builder Pattern**: Karmasik nesne olusumu (Lombok @Builder)
4. **Factory Pattern**: Nesne olusturma mantigini merkezilestirme
5. **Dependency Injection**: Spring IoC container ile bagimliliklari yonetme
6. **Strategy Pattern**: Arayuz ile degisen algoritmalari temsil etme
7. **Observer Pattern**: Event listener mekanizmasi (Swing, Spring events)
8. **MVC Pattern**: Model-View-Controller (Spring MVC, JSF)
9. **DAO/Repository Pattern**: Veri erisim katmani soyutlamasi
10. **DTO Pattern**: Veri transfer nesnesi ile katmanlar arasi iletisim
11. **Template Method**: Abstract sinif ile iskeptik algoritma
12. **Proxy Pattern**: Nesne erisimini aracilama (Spring AOP)

```java
// Singleton
public class Veritabani {
    private static final Veritabani INSTANCE = new Veritabani();
    private Veritabani() {}
    public static Veritabani getInstance() { return INSTANCE; }
}

// Builder Pattern
public class Kullanici {
    private final String ad;
    private final String soyad;
    private Kullanici(Builder builder) {
        this.ad = builder.ad;
        this.soyad = builder.soyad;
    }
    public static class Builder {
        private String ad; private String soyad;
        public Builder ad(String ad) { this.ad = ad; return this; }
        public Builder soyad(String soyad) { this.soyad = soyad; return this; }
        public Kullanici build() { return new Kullanici(this); }
    }
}
// Kullanim: new Kullanici.Builder().ad("Ali").soyad("Yilmaz").build()
```

## Onemli Kutuphaneler

1. **Spring Boot**: Kurumsal uygulama frameworku (auto-config, embedded server)
2. **Spring Framework**: IoC, AOP, MVC, Security
3. **Spring Data JPA**: Repository tabanli veri erisim
4. **Hibernate**: ORM frameworku (JPA implementasyonu)
5. **Apache Maven**: Build ve proje yonetim araci
6. **Gradle**: Modern build sistemi (Groovy/Kotlin DSL)
7. **JUnit 5**: Unit test frameworku
   `@Test void testTopla() { assertEquals(5, topla(2,3)); }`
8. **Mockito**: Mock nesne olusturma
   `when(servis.kullaniciBul(1)).thenReturn(kullanici);`
9. **Lombok**: Kod tekrarlarini azaltma
   `@Data @Builder @AllArgsConstructor`
10. **Log4j / Logback / SLF4J**: Loglama frameworkleri
11. **Jackson / Gson**: JSON serilestirme/deserilestirme
    `new ObjectMapper().writeValueAsString(obje)`
12. **Apache Kafka**: Mesaj kuyrugu ve event streaming
13. **MapStruct**: Tip donusturucu (DTO <-> Entity)
14. **Thymeleaf**: Server-side template engine
15. **Flyway / Liquibase**: Veritabani migration araclari
16. **H2 / PostgreSQL / MySQL**: Veritabani suruculeri
17. **Resilience4j**: Devre kirici, retry, rate limiter
18. **Testcontainers**: Test icin Docker container yonetimi
19. **Selenium**: Web test otomasyonu
20. **Swagger / OpenAPI**: API dokuman olusturma

```java
// Spring Boot REST Controller
@RestController
@RequestMapping("/api/kullanicilar")
public class KullaniciController {
    @GetMapping("/{id}")
    public ResponseEntity<Kullanici> getKullanici(@PathVariable Long id) {
        return ResponseEntity.ok(kullaniciServisi.bul(id));
    }
}

// Lombok ornegi
@Data @Builder @AllArgsConstructor @NoArgsConstructor
public class KullaniciDTO {
    private Long id;
    private String ad;
    private String soyad;
}
```

## Yaygin Hatalar

1. **Checked exception'lari ignore etmek**: Bos `catch(Exception e) {}` blogu hatalari gizler, en azindan logla
2. **`==` ile String karsilastirmak**: `==` referans karsilastirir, `equals()` kullanilmali
   `"ali".equals("ali")` -> True, `"ali" == new String("ali")` -> False
3. **NullPointerException**: Nesne null iken metod cagirmak, `Optional` kullanilmali
4. **`final` kullanmamak**: Degismezlik (immutability) icin sinif/degisken `final` yapilmali
5. **Kaynaklari kapatmamak**: Stream/Connection `try-with-resources` kullanmamak memory leak yaratir
6. **ConcurrentModificationException**: Dongu icinde listeyi degistirmek, iterator kullanilmali
7. **Integer cache araligi**: `Integer.valueOf(127) == Integer.valueOf(127)` True ama `128` icin False (-128..127 cache)
8. **Autoboxing/Unboxing performansi**: Dongulerde primitif `int` yerine `Integer` kullanmak yavas
9. **`switch` icinde `break` unutmak**: Fall-through olur (Java 12+ arrow syntax cozer)
10. **Overriding'de `@Override` unutmak**: Metod imzasi yanlislikla degisirse compiler uyarmaz
11. **Mutable koleksiyonlari public yapmak**: `Collections.unmodifiableList()` ile sabitlenmeli
12. **Serializable implement etmemek**: Cache/RMI gerektiren siniflarda hata

## Performans Ipuclari

1. **StringBuilder kullanmak**: String birlestirmede `+` yerine StringBuilder
   ```java
   // Yavas
   String s = "";
   for (int i = 0; i < 1000; i++) s += i;
   // Hizli
   StringBuilder sb = new StringBuilder();
   for (int i = 0; i < 1000; i++) sb.append(i);
   String s = sb.toString();
   ```

2. **Primitif tipleri tercih etmek**: Wrapper siniflar yerine `int`, `double` kullanmak
3. **Stream parallel() dikkat**: Kucuk verilerde parallel Stream yavas, buyuk verilerde avantajli
4. **ArrayList vs LinkedList**: Rastgele erisim coksa ArrayList, ekleme/silme coksa LinkedList
5. **Profil kullanmak**: JProfiler, VisualVM ile dar bogaz tespiti
6. **Garbage Collection ayarlari**: JVM heap boyutu ve GC algoritmasi secimi
7. **Lazy initialization**: Pahali nesneleri ihtiyac aninda olusturma

## Ekosistem

**Frameworkler**: Spring Boot/Cloud, Jakarta EE, Micronaut, Quarkus, Helidon

**Build Araclari**: Maven, Gradle, Ant + Ivy

**Paket Yoneticisi**: Maven Central, JCenter (eskiden), Gradle Portal

**JVM Dilleri**: Java, Kotlin, Groovy, Scala, Clojure, JRuby

**Application Server**: Tomcat, Jetty, WildFly, GlassFish, Payara

**IDE**: IntelliJ IDEA, Eclipse, NetBeans, VS Code

**Test**: JUnit, TestNG, Mockito, AssertJ, Cucumber (BDD), Selenium

**Monitoring**: Prometheus, Grafana, Micrometer, Spring Actuator

**CI/CD**: Jenkins, GitHub Actions, GitLab CI, CircleCI

**Cloud**: Spring Cloud, AWS SDK, Azure SDK, GCP SDK

## Kaynaklar

**Resmi Dokuman**: docs.oracle.com/en/java, openjdk.org

**Kitaplar**:
- Effective Java (Joshua Bloch) - Java'nin Incili
- Java: The Complete Reference (Herbert Schildt)
- Clean Code (Robert C. Martin) - Java ornekli
- Head First Java (Kathy Sierra)
- Spring in Action (Craig Walls)

**Web Siteleri**:
- baeldung.com - Kapsamli Spring/Java egitimleri
- javatpoint.com
- w3schools.com/java
- dev.java (Oracle'un resmi ogrenme portali)

**Interaktif Ogrenme**:
- exercism.org/tracks/java
- codingbat.com/java
- leetcode.com (Java ile problem cozme)
- hyperskill.org (JetBrains Academy)

**Topluluk**: reddit.com/r/java, Java Discord sunuculari, Java User Groups (JUG), spring.io toplulugu, Stack Overflow
