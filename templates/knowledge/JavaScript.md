# JavaScript Bilgi Referansi

## Genel Bakis
JavaScript, Brendan Eich tarafindan 1995'te olusturulmus, web tarayicilarinda calisan bir dildir. Web sayfalarina interaktivite kazandirir. Node.js ile sunucu tarafli da calisabilir. ECMAScript (ES6+) standartlariyla surekli gelismektedir.

## Temel Syntax

```javascript
// Degiskenler
let isim = "Ali";
const yas = 25;
var eskisi = "Kullanma"; // let/const tercih edilir

// Fonksiyon
function merhaba(kisi) {
    return `Merhaba, ${kisi}!`;
}

// Arrow fonksiyon
const topla = (a, b) => a + b;

// Kosul
if (yas >= 18) {
    console.log("Yetiskin");
} else {
    console.log("Cocuk");
}

// Dongu
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// Dizi
let meyveler = ["elma", "armut"];
meyveler.push("muz");
```

## Yaygin Patternler

- **Destructuring**: `const {ad, yas} = kisi;`
- **Spread operator**: `const yeni = [...dizi, eleman];`
- **Promise/async-await**: Asenkron islemler
- **Module sistemi**: `import/export` (ES6+)
- **Event delegation**: Olay yonetimi
- **Closure**: Ic ice fonksiyonlarda kapsam

## Onemli Kutuphaneler

- **React/Vue/Angular**: Frontend frameworkleri
- **Node.js/Express**: Sunucu tarafli gelistirme
- **Axios/Fetch**: HTTP istekleri
- **Lodash**: Yardimci fonksiyonlar
- **Jest/Mocha**: Test frameworkleri
- **Mongoose**: MongoDB ORM
- **Webpack/Vite**: Module bundler

## Yaygin Hatalar

- `==` yerine `===` kullanmamak (type coercion)
- `var` ile degisken tanimlamak (scope problemi)
- Callback hell (Promise/async-await kullanmamak)
- `const` ile array/obje degistirmenin mumkun oldugunu unutmak
- Asenkron kodu `await` ile beklemeden kullanmak
