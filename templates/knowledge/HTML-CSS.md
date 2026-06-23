# HTML-CSS Bilgi Referansi

## Genel Bakis
HTML (1991, Tim Berners-Lee), web sayfalarinin yapisini tanimlayan isaretleme dilidir. CSS (1996) ise sayfalari gorsel bicimlendiren stiller dilidir. Birlikte web'in temelini olustururlar.

## Temel Syntax

```html
<!DOCTYPE html>
<html lang="tr">
<head><meta charset="UTF-8"><title>Baslik</title></head>
<body>
    <header><h1>Merhaba</h1></header>
    <main>
        <section>
            <p>Bu bir <strong>paragraf</strong>tir.</p>
            <ul><li>Madde 1</li><li>Madde 2</li></ul>
        </section>
    </main>
    <footer>&copy; 2026</footer>
</body>
</html>
```

```css
body { font-family: Arial; margin: 0; padding: 20px; }
.container { max-width: 960px; margin: 0 auto; }
.flex { display: flex; justify-content: center; gap: 1rem; }
.grid { display: grid; grid-template-columns: 1fr 2fr; gap: 1rem; }
@media (max-width: 768px) { .grid { grid-template-columns: 1fr; } }
```

## Yaygin Patternler

- **Semantik HTML**: `header`, `main`, `nav`, `section` etiketleri
- **BEM**: `block__element--modifier` sinif adlandirma
- **Responsive**: Mobile-first, media queries
- **Modern Layout**: Flexbox ve Grid (float kullanma)
- **CSS Variables**: `:root { --renk: #333; }`

## Onemli Kutuphaneler/Frameworkler

- **Bootstrap/Tailwind**: CSS frameworkleri
- **Sass/SCSS**: CSS preprocessor
- **Styled Components / CSS Modules**: Bilesen CSS
- **Font Awesome / Material Icons**: Ikon setleri
- **Animate.css / GSAP**: Animasyon

## Yaygin Hatalar

- `div` asirisi (semantik etiket kullanilmali)
- Inline CSS (bakim zorlasir)
- `!important` asirisi (specificity sorunu)
- `alt` metni unutmak (erisilebilirlik)
- `px` kullanimi (`rem`/`em` tercih edilmeli)
- Cross-browser testi yapmamak
