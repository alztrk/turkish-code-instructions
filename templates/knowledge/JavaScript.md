# JavaScript Bilgi Referansi

## Genel Bakis

JavaScript, Brendan Eich tarafindan 1995 yilinda Netscape'te sadece 10 gunde gelistirilmistir. Ilk amaci web tarayicilarinda basit etkilesimler saglamakti. Zamanla ECMAScript standarti altinda evrilerek dunyanin en populer programlama dili haline gelmistir.

Gunumuzde sadece tarayici tarafli degil, Node.js ile sunucu tarafli, React Native/Electron ile masaustu ve mobil uygulama gelistirmede de kullanilir. ECMAScript 6 (ES6/ES2015) sonrasi dil buyuk bir donusum gecirmis, class, module, arrow function, promise, async/await gibi modern ozellikler eklenmistir. Netflix, Facebook, Google, Microsoft gibi sirketler yogun olarak JS kullanir. NPM (Node Package Manager) dunyanin en buyuk paket ekosistemidir.

## Temel Syntax

```javascript
// --- Degiskenler ---
let isim = "Ali";               // blok-scoped, degistirilebilir
const yas = 25;                 // blok-scoped, sabit
var eskisi = "Kullanma";        // function-scoped (oneriLMEZ)

// --- Veri Tipleri ---
let str = "Merhaba";            // String
let sayi = 42;                  // Number
let ondalik = 3.14;            // Number (tek tip)
let aktif = true;               // Boolean
let bos = null;                 // null
let tanimsiz = undefined;       // undefined
let sembol = Symbol("id");      // Symbol (benzersiz)
let bigInt = 1234567890123456789n; // BigInt

// --- String Islemleri ---
let mesaj = `Merhaba, ${isim}!`; // Template literal (ES6)
console.log(mesaj.length);       // 13
console.log(mesaj.toUpperCase());
console.log(mesaj.includes("Ali"));

// --- Diziler (Array) ---
let meyveler = ["elma", "armut", "muz"];
meyveler.push("cilek");          // sona ekle
meyveler.pop();                  // sondan cikar
meyveler.unshift("portakal");    // basa ekle
meyveler.shift();                // bastan cikar
console.log(meyveler[0]);        // indeks erisim

// --- Nesneler (Object) ---
let kisi = {
    ad: "Ali",
    yas: 25,
    merhaba() {                  // metod (shorthand)
        return `Merhaba, ben ${this.ad}`;
    }
};
kisi.soyad = "Yilmaz";           // dinamik ozellik ekleme

// --- Kosullar ---
if (yas >= 18) {
    console.log("Yetiskin");
} else if (yas > 12) {
    console.log("Ergen");
} else {
    console.log("Cocuk");
}

// Switch
switch (yas) {
    case 18: console.log("Yeni yetiskin"); break;
    case 25: console.log("Genc"); break;
    default: console.log("Diger");
}

// Ternary
let durum = yas >= 18 ? "Yetiskin" : "Cocuk";

// --- Donguler ---
for (let i = 0; i < 5; i++) {
    console.log(i);
}

for (let meyve of meyveler) {    // for...of (degerler)
    console.log(meyve);
}

for (let anahtar in kisi) {      // for...in (anahtarlar)
    console.log(anahtar, kisi[anahtar]);
}

meyveler.forEach(m => console.log(m)); // dizi metodu

// --- Fonksiyonlar ---
function topla(a, b) {
    return a + b;
}

// Arrow function (ES6)
const carp = (a, b) => a * b;

// Default parametre
const selamla = (isim = "Misafir") => `Merhaba ${isim}`;

// Rest parametre
const birlestir = (...parametreler) => parametreler.join(", ");

// --- Promise ve Async/Await ---
const veriCek = new Promise((resolve, reject) => {
    setTimeout(() => resolve("Veri geldi"), 1000);
});

async function getir() {
    try {
        const sonuc = await veriCek;
        console.log(sonuc);
    } catch (hata) {
        console.error("Hata:", hata);
    }
}

// --- Hata Yakalama ---
try {
    JSON.parse("gecersiz json");
} catch (e) {
    console.error("JSON hatasi:", e.message);
} finally {
    console.log("Her zaman calisir");
}

// --- Module Sistemi (ES6) ---
// dosya1.js: export const PI = 3.14;
// dosya2.js: import { PI } from './dosya1.js';

// --- Sinif ---
class Araba {
    #plaka = "";                 // private alan

    constructor(marka, model) {
        this.marka = marka;
        this.model = model;
    }

    static tekerlekSayisi() {
        return 4;
    }

    get plaka() {
        return this.#plaka;
    }

    set plaka(yeniPlaka) {
        this.#plaka = yeniPlaka;
    }
}
```

## Yaygin Patternler

1. **Destructuring**: `const {ad, yas} = kisi;` veya `const [ilk, ...kalan] = dizi;`
2. **Spread Operator**: `const yeni = [...dizi, eleman];` veya `const nesne = {...eski, yeniAlan: deger};`
3. **Promise/Async-Await**: Asenkron islemleri senkron gibi yazma
4. **Module Pattern**: `import/export` ile moduler yapi
5. **Event Delegation**: Ust ogede tek event listener ile alt ogeleri yonetme
6. **Closure**: Fonksiyon icinde fonksiyon ile private degisken olusturma
7. **Memoization**: Pahali hesaplamalari cacheleme
8. **Debounce/Throttle**: Tekrarlayan eventleri kontrol etme
9. **Singleton**: Tek bir ornek ile calisma
10. **Factory Pattern**: Fonksiyonla nesne olusturma
11. **Proxy Pattern**: Nesne erisimini aracilama
12. **Observer Pattern**: Event emitter ile yayin/abone mekanizmasi

```javascript
// Destructuring
const { ad, yas } = kisi;
const [birinci, ikinci] = meyveler;

// Spread ile kopyalama
const kopyaDizi = [...meyveler];
const kopyaNesne = { ...kisi, yas: 26 }; // override

// Closure
const sayaç = () => {
    let sayi = 0;
    return () => ++sayi;
};
const artir = sayaç();
console.log(artir()); // 1
console.log(artir()); // 2

// Debounce
const debounce = (fn, ms) => {
    let timeout;
    return (...args) => {
        clearTimeout(timeout);
        timeout = setTimeout(() => fn(...args), ms);
    };
};

// Memoization
const faktoriyel = (() => {
    const cache = {};
    return (n) => {
        if (n in cache) return cache[n];
        if (n <= 1) return 1;
        return cache[n] = n * faktoriyel(n - 1);
    };
})();
```

## Onemli Kutuphaneler

1. **React**: Bilesen tabanli frontend kutuphanesi
   `const App = () => <h1>Merhaba</h1>`
2. **Vue.js**: Progressive frontend frameworku
3. **Angular**: Kapsamli frontend framework (TypeScript)
4. **Node.js**: Sunucu tarafli JavaScript runtime
5. **Express.js**: Minimal web frameworku
   `app.get("/", (req, res) => res.send("Merhaba"))`
6. **Next.js**: React icin full-stack framework (SSR, SSG)
7. **Axios**: HTTP istemci kutuphanesi
   `axios.get("/api/kullanicilar").then(r => r.data)`
8. **Lodash**: Yardimci fonksiyonlar koleksiyonu
   `_.uniqBy(dizi, "id"); _.debounce(fn, 300)`
9. **Jest**: Test frameworku
   `expect(sayi).toBe(42)`
10. **Mocha/Chai**: Test frameworku + assertion
11. **Mongoose**: MongoDB ODM
    `const Kullanici = mongoose.model("Kullanici", schema)`
12. **Prisma**: Modern ORM (JS/TS)
13. **Socket.io**: Gercek zamanli iletisim (WebSocket)
14. **D3.js**: Veri gorsellestirme
15. **Three.js**: 3D grafikler (WebGL)
16. **Chart.js**: Basit grafik olusturma
17. **Zustand / Redux**: State yonetimi
18. **React Query / SWR**: Veri fetching ve cache
19. **Passport.js**: Kimlik dogrulama
20. **Tailwind CSS**: Utility-first CSS (JS/React ile birlikte)

```javascript
// React ornegi
import { useState } from 'react';
function Sayaç() {
    const [sayi, setSayi] = useState(0);
    return <button onClick={() => setSayi(sayi + 1)}>{sayi}</button>;
}

// Express ornegi
const express = require('express');
const app = express();
app.listen(3000);
```

## Yaygin Hatalar

1. **`==` yerine `===` kullanmamak**: `==` type coercion yapar, `===` tip kontrolu de ekler
   `"5" == 5  // True;  "5" === 5  // False`
2. **`var` ile degisken tanimlamak**: Function-scoped, hoisting sorunlari yaratir, `let/const` kullanilmali
3. **Callback Hell**: Ic ice callback yerine Promise/async-await kullanmamak
4. **`const` ile array/obje degistirilebilecegini unutmak**: `const` referansi sabitler, icerigi degil
5. **Asenkron kodu `await` ile beklemeden kullanmak**: `fetch()` donen Promise beklenmezse hata alinir
6. **`this` baglamini kaybetmek**: Callback icinde `this` undefined olur, arrow function veya `.bind()` cozer
7. **`parseInt` base belirtmemek**: `parseInt("08")` -> 0 (eski tarayicilar), `parseInt("08", 10)` -> 8
8. **Floating point hatalari**: `0.1 + 0.2 === 0.3` -> `false` (binary floating point)
9. **DOM erisimi olmadan once element hazir degil**: `DOMContentLoaded` eventi beklenmeli
10. **`delete` ile dizi elemani silmek**: `delete arr[0]` bosluk birakir, `splice()` kullanilmali
11. **Memory leak**: Kullanilmayan timer/event listener temizlenmemesi
12. **`null`/`undefined` kontrolu yapmamak**: `Cannot read property of null` hatasi

## Performans Ipuclari

1. **DOM manipülasyonunu azaltmak**: `documentFragment` veya `innerHTML` ile toplu guncelleme
   ```javascript
   const frag = document.createDocumentFragment();
   for (const item of items) {
       const li = document.createElement('li');
       li.textContent = item;
       frag.appendChild(li);
   }
   list.appendChild(frag);
   ```

2. **Debounce/Throttle kullanmak**: Scroll, resize, input eventlerinde frekansi azaltma
3. **`requestAnimationFrame` kullanmak**: Animasyonlarda `setInterval` yerine daha verimli
4. **Immutability**: Obje/dizi kopyalarken spread/spread operatoru kullanmak
5. **Web Worker kullanmak**: Agir hesaplamalari ayri thread'de calistirmak
6. **Lazy loading**: Kod bolme (code splitting) ile ihtiyac aninda yukleme
7. **CDN kullanmak**: Statik dosyalari CDN'den servis etme

```javascript
// requestAnimationFrame
function animasyon() {
    element.style.left = x + 'px';
    requestAnimationFrame(animasyon);
}

// Web Worker
const worker = new Worker('worker.js');
worker.postMessage({ data: buyukVeri });
```

## Ekosistem

**Frameworkler (Frontend)**: React, Vue.js, Angular, Svelte, Solid.js, Qwik

**Frameworkler (Backend)**: Express.js, Koa, Fastify, Hapi, NestJS (TypeScript)

**Full-Stack**: Next.js (React), Nuxt.js (Vue), Remix, SvelteKit

**Build Araclari**: Webpack, Vite, Rollup, Parcel, esbuild, TurboPack

**Paket Yoneticileri**: npm, yarn, pnpm, bun

**Test**: Jest, Vitest, Cypress, Playwright, Testing Library

**Linter/Formatter**: ESLint, Prettier

**Runtime**: Node.js, Deno, Bun

**State Management**: Redux, Zustand, Pinia, MobX, Jotai

**Type Checking**: TypeScript (superset), Flow

## Kaynaklar

**Resmi Dokuman**: developer.mozilla.org (MDN), ecma-international.org

**Kitaplar**:
- You Don't Know JS (Kyle Simpson)
- Eloquent JavaScript (Marijn Haverbeke)
- JavaScript: The Good Parts (Douglas Crockford)
- Clean Code in JavaScript

**Web Siteleri**:
- javascript.info
- freecodecamp.org
- scrimba.com (interaktif)
- w3schools.com/js

**Interaktif Ogrenme**:
- exercism.org/tracks/javascript
- codewars.com
- leetcode.com
- frontendmentor.io (projeler)

**Topluluk**: JSConf, Turkey JS Meetup, reddit.com/r/javascript, Stack Overflow
