# Rust Bilgi Referansi

## Genel Bakis

Rust, Graydon Hoare tarafindan 2006'da kisisel bir proje olarak baslatilmis, Mozilla'nin destegiyle 2010'da halka acilmis, 2015'te Rust 1.0 kararli surumune ulasmistir. Guvenli sistem programlama ihtiyacindan dogmus, C/C++'in performansini korurken bellek guvenligini (memory safety) garanti etmeyi hedefler.

Rust gunumuzde sistem programlama, WebAssembly (wasm-pack ile), CLI araclari (bat, fd, ripgrep, alacritty Rust ile yazilmis), oyun motorlari (Bevy, Amethyst), isletim sistemi bilesenleri, ag servisleri ve kripto alaninda kullanilir. Borrow checker ile derleme zamaninda bellek hatalarini onler. Stack Overflow anketlerinde yillarca "en sevilen dil" secilmistir. Microsoft, Google (Android, Fuchsia), Amazon (AWS), Meta gibi sirketler Rust kullaniyor. Rust 2024 edition'u ile dil gelismeye devam etmektedir.

## Temel Syntax

```rust
// --- Degiskenler ---
fn main() {
    let isim: &str = "Ali";        // degismez string referansi
    let mut yas: u32 = 25;         // mut ile degistirilebilir
    let pi: f64 = 3.14159;
    let aktif: bool = true;
    let harf: char = 'A';

    // Shadowing
    let x = 5;
    let x = x + 1;                 // onceki x'i gizler
    let x = String::from("Merhaba"); // tip bile degisebilir

    // --- String ---
    let mut metin = String::from("Merhaba");
    metin.push_str(", Dunya!");
    println!("{}", metin);
    println!("Uzunluk: {}", metin.len());

    // --- Dizi ve Vektor ---
    let dizi: [i32; 3] = [1, 2, 3];
    let mut vektor: Vec<i32> = vec![1, 2, 3];
    vektor.push(4);
    vektor.pop();
    println!("{}", vektor[0]);      // 1

    // --- HashMap ---
    use std::collections::HashMap;
    let mut yaslar = HashMap::new();
    yaslar.insert(String::from("Ali"), 25);
    yaslar.insert(String::from("Veli"), 30);
    match yaslar.get(&String::from("Ali")) {
        Some(yas) => println!("Yas: {}", yas),
        None => println!("Bulunamadi"),
    }

    // --- Kosul ---
    if yas >= 18 {
        println!("Yetiskin");
    } else if yas > 12 {
        println!("Ergen");
    } else {
        println!("Cocuk");
    }

    // if let
    let option = Some(5);
    if let Some(deger) = option {
        println!("Deger: {}", deger);
    }

    // --- Match ---
    match yas {
        0..=17 => println!("Cocuk"),
        18..=65 => println!("Yetiskin"),
        _ => println!("Yasli"),
    }

    // --- Donguler ---
    for i in 0..5 {
        println!("{}", i);
    }

    for meyve in vec!["elma", "armut", "muz"] {
        println!("{}", meyve);
    }

    let mut sayac = 0;
    while sayac < 5 {
        println!("{}", sayac);
        sayac += 1;
    }

    // --- Fonksiyonlar ---
    println!("{}", topla(3, 4));

    // Expression vs statement
    let kare = {
        let sayi = 5;
        sayi * sayi                // son ifade return edilir
    };

    // Closure
    let ekle = |a: i32, b: i32| a + b;
    println!("{}", ekle(5, 3));

    // Closure ile capture
    let faktor = 2;
    let katla = |x| x * faktor;

    // --- Pattern Matching ---
    let sayi = 7;
    match sayi {
        1 | 2 => println!("Kucuk"),
        3..=5 => println!("Orta"),
        _ if sayi % 2 == 0 => println!("Cift"),
        _ => println!("Diger"),
    }

    // --- Struct ---
    let kisi = Kisi {
        ad: String::from("Ali"),
        yas: 25,
    };
    println!("{}", kisi.selam_ver());

    // --- Enum ---
    let renk = Renk::Kirmizi;
    renk.goster();

    // --- Option ve Result ---
    let bolum = bol(10, 0);
    match bolum {
        Ok(sonuc) => println!("{}", sonuc),
        Err(hata) => println!("Hata: {}", hata),
    }

    // --- Hata Yakalama ---
    // std::fs::read_to_string("dosya.txt").unwrap(); // hata firlatir
    let dosya = std::fs::read_to_string("dosya.txt");
    match dosya {
        Ok(icerik) => println!("{}", icerik),
        Err(e) => eprintln!("Dosya okunamadi: {}", e),
    }

    // --- ? operator ---
    fn dosya_oku() -> Result<String, std::io::Error> {
        let icerik = std::fs::read_to_string("dosya.txt")?;
        Ok(icerik)
    }

    // --- Iterator ---
    let sayilar = vec![1, 2, 3, 4, 5];
    let cift_kareler: Vec<i32> = sayilar
        .iter()
        .filter(|x| *x % 2 == 0)
        .map(|x| x * x)
        .collect();
    println!("{:?}", cift_kareler);
}

// --- Fonksiyon ---
fn topla(a: i32, b: i32) -> i32 {
    a + b  // son ifade return (; yok)
}

// --- Struct ---
struct Kisi {
    ad: String,
    yas: u32,
}

// Struct metodu
impl Kisi {
    fn selam_ver(&self) -> String {
        format!("Merhaba, ben {}!", self.ad)
    }

    fn yasi_buyult(&mut self) {
        self.yas += 1;
    }

    // associated function (static)
    fn yeni(ad: &str, yas: u32) -> Kisi {
        Kisi {
            ad: String::from(ad),
            yas,
        }
    }
}

// --- Enum ---
enum Renk {
    Kirmizi,
    Yesil(u8),        // tuple variant
    Mavi { r: u8, g: u8, b: u8 },  // struct variant
}

impl Renk {
    fn goster(&self) {
        match self {
            Renk::Kirmizi => println!("Kirmizi"),
            Renk::Yesil(d) => println!("Yesil: {}", d),
            Renk::Mavi { r, g, b } => println!("RGB: {},{},{}", r, g, b),
        }
    }
}

// --- Result ---
fn bol(x: i32, y: i32) -> Result<i32, String> {
    if y == 0 {
        Err(String::from("Sifira bolme!"))
    } else {
        Ok(x / y)
    }
}

// --- Trait ---
trait Hayvan {
    fn ses_cikar(&self) -> String;
    fn uyu(&self) -> String {
        String::from("Uyuyor...")  // default
    }
}

struct Kopek { ad: String }
impl Hayvan for Kopek {
    fn ses_cikar(&self) -> String {
        format!("{}: Hav hav!", self.ad)
    }
}

// --- Generic ---
fn ilk<T>(slice: &[T]) -> Option<&T> {
    slice.first()
}

// --- Lifetime ---
fn en_uzun<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

## Yaygin Patternler

1. **Option/Result**: `Some(T)`, `None`, `Ok(T)`, `Err(E)` ile hata yonetimi
2. **Pattern Matching**: `match`, `if let`, `while let` ile guclu desen esleme
3. **Iterator Chain**: `iter().map().filter().fold().collect()` fonksiyonel stilde islem
4. **Traits**: Java interface benzeri, tip'e yetenek kazandirma
5. **Lifetime**: `'a`, `'static` ile referans omru belirtme (borrow checker)
6. **Error Handling with `?`**: `fs::read_to_string("dosya.txt")?;` ile error propagation
7. **Builder Pattern**: Struct ile builder deseni (derive builder)
8. **Newtype Pattern**: Tek alanli tuple struct ile tip guvenligi
9. **Deref Pattern**: `Deref` trait'i ile smart pointer davranisi
10. **RAII**: Rust'ta ownership sistemi ile RAII otomatik
11. **Rc/Arc**: Reference counted / Atomic reference counted paylasim
12. **Interior Mutability**: `RefCell`, `Mutex`, `RwLock` ile immutable icinden mutable erisim

```rust
// Iterator chain
let toplam: i32 = (1..=100)
    .filter(|x| x % 2 == 0)
    .map(|x| x * 2)
    .sum();

// Builder pattern (ilkel)
#[derive(Default)]
struct Config {
    host: String,
    port: u16,
}
impl Config {
    fn host(mut self, h: &str) -> Self { self.host = h.into(); self }
    fn port(mut self, p: u16) -> Self { self.port = p; self }
}
let cfg = Config::default().host("localhost").port(8080);

// Newtype
struct Euro(f64);
struct Dolar(f64);
fn topla_euro(a: Euro, b: Euro) -> Euro {
    Euro(a.0 + b.0)
}
```

## Onemli Kutuphaneler

1. **Tokio**: Asenkron runtime (async/await tabanli)
   `tokio::spawn(async { ... });`
2. **async-std**: Alternatif asenkron runtime
3. **Serde**: Serilestirme/deserilestirme (JSON, YAML, bincode)
   `#[derive(Serialize, Deserialize)] struct Kullanici { ... }`
4. **Rocket**: Tip guvenli web frameworku
5. **Actix-web**: Actor tabanli yuksek performansli web frameworku
6. **Axum (Tokio ekosistemi)**: Modern async web frameworku (Tower tabanli)
   `Router::new().route("/", get(|| async { "Merhaba" }))`
7. **Clap**: CLI arguman ayristirma (derive macro ile)
   `#[derive(Parser)] struct Args { #[arg(short)] name: String }`
8. **Diesel**: Tip guvenli ORM (compile-time sorgu kontrolu)
9. **SQLx**: Async SQL surucu (ORM degil, compile-time sorgu kontrolu ile)
10. **Reqwest**: HTTP istemci (async ve blocking)
    `reqwest::get("https://api.example.com").await?.text().await?`
11. **wasm-pack**: Rust'tan WebAssembly derleme
12. **rustfmt / clippy**: Formatlama ve lint (rust official)
13. **Criterion**: Benchmark kutuphanesi
14. **tokio-tungstenite**: WebSocket
15. **Bevy**: Oyun motoru (ECS tabanli)
16. **Egui / iced / Druid**: GUI frameworkleri
17. **tui-rs / ratatui**: Terminal UI
18. **Chrono**: Tarih/zaman islemleri
19. **Rand**: Rastgele sayi uretme
20. **Anyhow / thiserror**: Hata yonetimi kolaylastirma

```rust
// axum ornegi
use axum::{Router, routing::get};
async fn merhaba() -> &'static str { "Merhaba Dunya!" }
#[tokio::main]
async fn main() {
    let app = Router::new().route("/", get(merhaba));
    axum::Server::bind(&"0.0.0.0:3000".parse().unwrap())
        .serve(app.into_make_service())
        .await
        .unwrap();
}

// anyhow/thiserror ornegi
use anyhow::Result;
use thiserror::Error;
#[derive(Error, Debug)]
enum VeriHatasi { #[error("Veri bulunamadi")] Bulunamadi }
fn islem() -> Result<()> {
    anyhow::bail!("Bilinmeyen hata");
    Ok(())
}
```

## Yaygin Hatalar

1. **Borrow checker kurallarini delmeye calismak**: Ayni anda 1 mutable reference veya N immutable reference
2. **`mut` unutmak**: Degiskeni degistirmek icin `let mut` tanimlanmali
3. **Lifetimelari gereksiz yere karmasiklastirmak**: Cogunlukla elided lifetime yeterli
4. **`unwrap()`/`expect()` canliya birakmak**: Production'da hata firlatir, `?` veya match kullan
5. **`dyn Trait` vs generics**: Box<dyn Trait> runtime cost'u, generics static dispatch
6. **`unsafe` blogunu gereksiz kullanmak**: Rust guvenlik garantilerini kaybetmek
7. **Recursive type**: Dogrudan kendini referans alan struct'lar `Box` icinde olmali
8. **RefCell/Mutex deadlock**: Icerdeki kilit disariyi beklerken kilitlenme
9. **String vs &str karistirmak**: String owned, &str borrowed (karma modeli)
10. **`Copy` vs `Clone`**: Copy bitwise kopya (stack), Clone explicit kopya
11. **Dangling pointer**: Rust'da borrow checker sayesinde derleme zamaninda engellenir
12. **Overflow**: Debug'da panic, release'da wrap eder (`overflow-checks: true`)
13. **`async` fonksiyonda `Send` trait'i**: Tokio gibi runtime'lar Send gerektirir

## Performans Ipuclari

1. **Zero-cost abstraction kullanmak**: Iterator, closure, generic'lerin runtime cost'u yoktur
   ```rust
   // Derleyici bunu direk donguye cevirir
   let toplam: i32 = (0..1000).filter(|x| x % 2 == 0).sum();
   ```

2. **Vec capacity onceden ayirmak**: `Vec::with_capacity(n)` ile reallocation'lari azaltma
3. **String vs &str**: Mumkunse &str kullanmak (heap allocation'u onler)
4. **LTO (Link Time Optimization)**: `[profile.release] lto = true` ile daha iyi optimizasyon
5. **Box&lt;dyn Trait&gt; yerine generics**: Static dispatch hizli, monomorphization ek yok
6. **Arena allocator**: Cok sayida kucuk obje icin bump allocation
7. **`#[inline]`**: Kucuk fonksiyonlarda inline cagri
8. **Profil kullanmak**: `perf` (Linux), `flamegraph-rs`, `cargo bench`

```rust
// Cargo.toml'da release optimizasyonlari
[profile.release]
lto = true
codegen-units = 1
opt-level = 3
```

## Ekosistem

**Build/Paket Yoneticisi**: Cargo (dahili - build, test, doc, publish, bench)

**Frameworkler (Web)**: Axum, Actix-web, Rocket, Warp, Tide, Poem

**Frameworkler (Oyun)**: Bevy, Fyrox, Amethyst (bakimda)

**GUI**: Tauri (desktop app framework), Egui, iced, Slint, Dioxus

**WebAssembly**: wasm-bindgen, wasm-pack, yew, leptos, sycamore

**Asenkron Runtime**: Tokio, async-std, smol, glommio

**Test**: cargo test (dahili), criterion (benchmark), proptest, quickcheck

**Lint/Format**: clippy, rustfmt (official)

**Dokumantasyon**: rustdoc (dahili), docs.rs

**CI/CD**: cargo test, clippy check, GitHub Actions

**IDE Desteji**: Rust Analyzer (VS Code), IntelliJ Rust, CLion

## Kaynaklar

**Resmi Dokuman**: doc.rust-lang.org (kitap, referans, Rust by Example)

**Turkce Kaynak**:
- rust.istihza.com - Kapsamli Turkce Rust kaynagi
- rust.bootsvermek.com - Rust'a baslangic

**Kitaplar**:
- The Rust Programming Language (Steve Klabnik, Carol Nichols) - Ucretsiz
- Rust in Action (Tim McNamara)
- Programming Rust (Jim Blandy, Jason Orendorff)
- Rust for Rustaceans (Jon Gjengset)

**Web Siteleri**:
- rust-by-example.org
- rust-lang.org/learn
- exercism.org/tracks/rust
- tour of Rust (rust-tour.com)

**Interaktif Ogrenme**:
- rustlings.cool (interaktif egzersizler)
- codewars.com (Rust kata'lari)
- leetcode.com
- adventofcode.com

**Topluluk**: reddit.com/r/rust, Rust Discord, Stack Overflow, Rust Turkey, RustConf (yillik)
