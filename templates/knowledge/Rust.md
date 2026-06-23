# Rust Bilgi Referansi

## Genel Bakis
Rust, Mozilla tarafindan 2010'da Graydon Hoare tarafindan baslatilmis, 2015'te kararli surume ulasmistir. Bellek guvenligi (borrow checker), hiz ve eszamanliliga odaklanir. Sistem programlama, WASM, CLI araclari ve oyun motorlarinda kullanilir.

## Temel Syntax

```rust
let isim: &str = "Ali";
let mut yas: u32 = 25;
let aktif: bool = true;

fn merhaba(kisi: &str) -> String {
    format!("Merhaba, {}!", kisi)
}

if yas >= 18 { println!("Yetiskin") } else { println!("Cocuk") }

for i in 0..5 { println!("{}", i) }

let mut meyveler = vec!["elma", "armut"];
meyveler.push("muz");

match yas { 0..=17 => println!("Cocuk"), _ => println!("Yetiskin") }
```

## Yaygin Patternler

- **Option/Result**: `Some(T)`, `None`, `Ok(T)`, `Err(E)`
- **Pattern Matching**: `match`, `if let`, `while let`
- **Iterator chain**: `iter().map().filter().collect()`
- **Traits**: Yetenek tanimlama (interface benzeri)
- **Lifetime**: Referans omru (`'a`, `'static`)
- **Error handling**: `?` operatoru ile error propagation

## Onemli Kutuphaneler

- **Tokio/async-std**: Asenkron runtime
- **Serde**: Serilestirme/deserilestirme
- **Rocket/Actix-web/Axum**: Web frameworkleri
- **Clap**: CLI arguman ayristirma
- **Diesel/SQLx**: ORM/veritabani
- **Rustfmt/Clippy**: Formatlama/lint
- **wasm-pack**: WebAssembly

## Yaygin Hatalar

- Borrow checker kurallarini delmeye calismak (ownership)
- `mut` unutmak (degisken degistirme)
- Lifetimelari gereksiz yere karmasiklastirmak
- `unwrap()`/`expect()` kullanimini canliya birakmak
- `dyn Trait` vs generics karari (performance)
- `unsafe` blogunu gereksiz kullanmak
