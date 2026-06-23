# HTML-CSS Bilgi Referansi

## Genel Bakis

HTML (HyperText Markup Language), Tim Berners-Lee tarafindan 1991'de CERN'de gelistirilmistir. Web sayfalarinin yapisini tanimlayan isaretleme dilidir. HTML5 (2014) ile birlikte semantik ogeler (header, nav, main), multimedia (video, audio), canvas, SVG ve form API'leri eklenmistir.

CSS (Cascading Style Sheets), 1996'da Hakon Wium Lie tarafindan onerilmistir. Web sayfalarini gorsel olarak bicimlendiren stil dilidir. CSS3 ile animasyon, transition, flexbox, grid, media queries gibi gelismis ozellikler eklenmistir.

Gunumuzde HTML ve CSS web'in temel yapi taslaridir. Her web tarayicisi HTML/CSS'i yorumlar. React, Vue, Angular gibi frameworkler HTML'i JSX/Template ile genisletirken, temel HTML bilgisi zorunludur. Erisilebilirlik (a11y), responsive tasarim ve performans en onemli konulardir.

## Temel Syntax

### HTML

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sayfa Basligi</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="/">Ana Sayfa</a></li>
                <li><a href="/hakkimizda">Hakkimizda</a></li>
                <li><a href="/iletisim">Iletisim</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section>
            <h1>Hos Geldiniz</h1>
            <p>Bu bir <strong>paragraf</strong>tir.</p>
            <p>Bu <em>vurgulanmis</em> bir metindir.</p>
        </section>

        <article>
            <h2>Blog Yazisi</h2>
            <p>Icerik burada yer alir.</p>
            <time datetime="2026-06-23">23 Haziran 2026</time>
        </article>

        <aside>
            <h3>Kenar Cubugu</h3>
            <ul>
                <li>Madde 1</li>
                <li>Madde 2</li>
            </ul>
        </aside>
    </main>

    <footer>
        <p>&copy; 2026 - Tum haklari saklidir.</p>
    </footer>
</body>
</html>
```

### Form Elemanlari

```html
<form action="/kayit" method="POST">
    <label for="ad">Ad:</label>
    <input type="text" id="ad" name="ad" required>

    <label for="eposta">E-posta:</label>
    <input type="email" id="eposta" name="eposta" placeholder="ornek@mail.com">

    <label for="yas">Yas:</label>
    <input type="number" id="yas" name="yas" min="0" max="150">

    <label for="mesaj">Mesaj:</label>
    <textarea id="mesaj" name="mesaj" rows="4"></textarea>

    <label>
        <input type="checkbox" name="onay"> Kabul ediyorum
    </label>

    <label for="sehir">Sehir:</label>
    <select id="sehir" name="sehir">
        <option value="">Seciniz</option>
        <option value="ist">Istanbul</option>
        <option value="ank">Ankara</option>
    </select>

    <fieldset>
        <legend>Cinsiyet</legend>
        <label><input type="radio" name="cinsiyet" value="erkek"> Erkek</label>
        <label><input type="radio" name="cinsiyet" value="kadin"> Kadin</label>
    </fieldset>

    <button type="submit">Gonder</button>
</form>
```

### CSS Temelleri

```css
/* --- CSS Variables --- */
:root {
    --primary: #3498db;
    --secondary: #2ecc71;
    --danger: #e74c3c;
    --dark: #2c3e50;
    --light: #ecf0f1;
    --spacing: 1rem;
    --border-radius: 8px;
}

/* --- Reset --- */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

/* --- Typography --- */
body {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    font-size: 16px;
    line-height: 1.6;
    color: var(--dark);
    background-color: var(--light);
}

h1, h2, h3, h4 {
    line-height: 1.2;
    margin-bottom: 0.5em;
}

/* --- Layout: Flexbox --- */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background: var(--primary);
    color: white;
}

.flex-container {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
}

.flex-item {
    flex: 1 1 300px;
}

/* --- Layout: CSS Grid --- */
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--spacing);
    padding: var(--spacing);
}

.grid-layout {
    display: grid;
    grid-template-areas:
        "header header header"
        "nav    main   aside"
        "footer footer footer";
    grid-template-columns: 200px 1fr 200px;
    grid-template-rows: auto 1fr auto;
    min-height: 100vh;
}

header { grid-area: header; }
nav { grid-area: nav; }
main { grid-area: main; }
aside { grid-area: aside; }
footer { grid-area: footer; }

/* --- Responsive Design --- */
@media (max-width: 768px) {
    .grid-layout {
        grid-template-areas:
            "header"
            "nav"
            "main"
            "aside"
            "footer";
        grid-template-columns: 1fr;
    }

    .navbar {
        flex-direction: column;
        gap: 0.5rem;
    }

    body {
        font-size: 14px;
    }
}

@media (max-width: 480px) {
    .flex-item {
        flex: 1 1 100%;
    }
}

/* --- Box Model --- */
.card {
    background: white;
    border: 1px solid #ddd;
    border-radius: var(--border-radius);
    padding: var(--spacing);
    margin-bottom: var(--spacing);
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

/* --- Butonlar --- */
.btn {
    display: inline-block;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: var(--border-radius);
    cursor: pointer;
    font-size: 1rem;
    transition: all 0.3s ease;
}

.btn-primary {
    background: var(--primary);
    color: white;
}

.btn-primary:hover {
    background: #2980b9;
    transform: translateY(-2px);
}

/* --- Animasyonlar --- */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.animate-in {
    animation: fadeIn 0.5s ease-out;
}

/* --- Position --- */
.modal-overlay {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(0,0,0,0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.modal {
    background: white;
    border-radius: 8px;
    padding: 2rem;
    max-width: 500px;
    width: 90%;
    position: relative;
}
```

## Yaygin Patternler

1. **Semantik HTML**: `header`, `main`, `nav`, `section`, `article`, `aside`, `footer` ile anlamli yapi
2. **BEM Metodolojisi**: `.block__element--modifier` sinif adlandirma sistemi
3. **Responsive Tasarim**: Mobile-first yaklasimi, `@media` queries ile cihaz uyumu
4. **Flexbox vs Grid**: Flexbox tek boyutlu (satir/sutun), Grid iki boyutlu duzenler icin
5. **CSS Variables**: `:root { --renk: #333; }` ile dinamik deger yonetimi
6. **CSS Reset/Normalize**: Tarayicilar arasi tutarlilik
7. **Atomic CSS (Tailwind)**: Utility-first, tek amacli class'lar
8. **Dark Mode**: `prefers-color-scheme: dark` medya sorgusu ile tema
9. **Lazy Loading Images**: `loading="lazy"` ile gorselleri erteleme
10. **CSS Animasyon/Transition**: `transition: 0.3s;` ve `@keyframes` ile etkilesim
11. **Custom Properties ile Theming**: `data-theme` attribute ile tema degistirme
12. **Accessible Forms**: `label`, `aria-*`, role ile erisilebilir form

```css
/* Dark Mode */
:root {
    --bg: white;
    --text: #333;
}

[data-theme="dark"] {
    --bg: #1a1a2e;
    --text: #eee;
}

@media (prefers-color-scheme: dark) {
    :root {
        --bg: #1a1a2e;
        --text: #eee;
    }
}

body {
    background: var(--bg);
    color: var(--text);
}
```

## Onemli Kutuphaneler/Frameworkler

1. **Bootstrap 5**: Populer CSS framework (bilesenler, grid, utilities)
   `<div class="container"><div class="row"><div class="col-md-6">...</div></div></div>`
2. **Tailwind CSS**: Utility-first CSS framework
   `<div class="flex items-center justify-between p-4 bg-blue-500 text-white">`
3. **Sass/SCSS**: CSS preprocessor (degisken, nesting, mixin, function)
   ```scss
   $primary: #3498db;
   .card { background: white; &--dark { background: #333; } }
   ```
4. **PostCSS**: CSS transformation araci (Autoprefixer, Tailwind)
5. **Styled Components**: CSS-in-JS (React)
   `const Button = styled.button'background: blue; color: white;'`
6. **CSS Modules**: Scoped CSS (create-react-app ile dahili)
7. **Bulma**: Modern CSS framework (Flexbox tabanli)
8. **Material UI (MUI)**: Google Material Design React bilesenleri
9. **Chakra UI / Radix UI**: Accessible React bilesen kutuphaneleri
10. **Font Awesome / Material Icons**: Ikon kutuphaneleri
11. **Animate.css / GSAP**: Animasyon kutuphaneleri
12. **Three.js**: 3D grafikler (WebGL)
13. **D3.js**: Veri gorsellestirme
14. **Chart.js / ApexCharts**: Grafik olusturma
15. **Swiper.js / Slick**: Slider/carousel kutuphaneleri
16. **Alpine.js / htmx**: Hafif interaktivite (JS framework gerektirmeyen)

```html
<!-- Bootstrap ornegi -->
<div class="container mt-4">
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Baslik</h5>
            <p class="card-text">Icerik metni</p>
            <a href="#" class="btn btn-primary">Buton</a>
        </div>
    </div>
</div>

<!-- Tailwind ornegi -->
<div class="max-w-sm mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl">
    <div class="md:flex">
        <div class="p-8">
            <div class="uppercase tracking-wide text-sm text-indigo-500 font-semibold">Kategori</div>
            <p class="mt-2 text-slate-500">Aciklama metni</p>
        </div>
    </div>
</div>
```

## Yaygin Hatalar

1. **`div` asirisi**: Semantik etiketler (`header`, `main`, `section`) yerine `div` kullanimi
2. **Inline CSS**: `style="..."` attribute'u ile CSS yazmak (bakim zorlasir, specificite sorunu)
3. **`!important` asirisi**: Specificity sorunlarini gecici cozer, uzun vadede karisikliga yol acar
4. **`alt` metni unutmak**: Gorsellerde `alt` attribute'u erisilebilirlik icin kritik
5. **`px` kullanimi**: Sabit piksel yerine `rem`/`em`/`%` kullanilmali (responsive)
6. **Cross-browser testi yapmamak**: Her tarayicida goruntuleme farkli olabilir
7. **`<br>` ile duzen olusturmak**: `padding`/`margin` yerine `<br>` kullanimi
8. **`<button>` yerine `<div>` kullanmak**: Form butonlari semantic `<button>` olmali
9. **CSS specificity kavramamak**: Secicilerin oncelik sirasini bilmemek
10. **Responsive yapmamak**: Sabit genislik (`width: 1200px`) mobilde tasar
11. **Form validation sadece JS ile**: HTML5 built-in validation (`required`, `type`) da kullanilmali
12. **Sayfa basina birden fazla `<h1>` kullanmak**: SEO ve erisilebilirlik sorunu

## Performans Ipuclari

1. **CSS sprite kullanmak**: Kucuk ikonlari tek bir gorselde birlestirme
   ```css
   .icon-home { width: 32px; height: 32px; background: url(sprite.png) -0 -0; }
   .icon-user { width: 32px; height: 32px; background: url(sprite.png) -32px -0; }
   ```

2. **Critical CSS**: Ilk acilista gorunen CSS'i inline, gerisini async yukleme
3. **Lazy loading**: Gorsellerde `loading="lazy"`, iframe'lerde `loading="lazy"` kullanimi
4. **Minification**: CSS/JS dosyalarini kucultme (ters bosluklari kaldirma)
5. **CDN kullanmak**: Statik dosyalari CDN'den servis etme
6. **Font subsetting**: Sadece kullanilan karakterleri iceren font dosyasi
7. **CSS contain**: `contain: layout style paint` ile tarayici render optimizasyonu

```html
<!-- Lazy loading -->
<img src="buyuk-resim.jpg" alt="Resim" loading="lazy" width="800" height="600">

<!-- Async CSS -->
<link rel="preload" href="style.css" as="style" onload="this.onload=null;this.rel='stylesheet'">

<!-- Critical CSS inline -->
<style>
/* Ilk ekranda gorunen CSS */
.header { background: blue; color: white; }
.hero { min-height: 100vh; }
</style>
```

## Ekosistem

**CSS Frameworkler**: Bootstrap, Tailwind, Bulma, Foundation, Materialize

**CSS Preprocessor**: Sass/SCSS, Less, Stylus, PostCSS

**CSS Methodolojileri**: BEM, SMACSS, OOCSS, ITCSS, Atomic CSS

**Build Araclari**: Webpack, Vite, Parcel, Gulp (task runner), Grunt

**Optimizasyon**: PurgeCSS, cssnano, Autoprefixer, Critters

**Test**: Cypress, Playwright, Percy (gorsel regression), Lighthouse

**Static Site Generator**: Hugo, 11ty, Jekyll, Astro, Next.js (SSG)

**Hosting**: Vercel, Netlify, GitHub Pages, Cloudflare Pages, Firebase

**Erisilebilirlik (a11y)**: axe-core, Lighthouse, WAVE, NVDA

**Design Tools**: Figma, Adobe XD, Sketch, Canva

## Kaynaklar

**Resmi Dokuman**: developer.mozilla.org (MDN), html.spec.whatwg.org, w3.org/Style/CSS/

**Kitaplar**:
- HTML and CSS: Design and Build Websites (Jon Duckett)
- CSS: The Definitive Guide (Eric Meyer)
- CSS Secrets (Lea Verou)
- Responsive Web Design (Ethan Marcotte)

**Web Siteleri**:
- css-tricks.com - Kapsamli CSS makaleleri (Flexbox, Grid rehberleri)
- web.dev (Google) - Web performansi ve en iyi uygulamalar
- frontendmentor.io - Gercek projelerle ogrenme
- codepen.io - Kod deneme ve paylasma

**Interaktif Ogrenme**:
- flexboxfroggy.com (Flexbox oyun)
- cssgridgarden.com (Grid oyun)
- freecodecamp.org (Responsive Web Design sertifikasi)
- scrimba.com (interaktif HTML/CSS kurslari)

**Topluluk**: Stack Overflow, CSS-Tricks, Dev.to, Frontend Mentor, Turkey Frontend Developer topluluklari
