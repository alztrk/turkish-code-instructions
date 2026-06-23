# TypeScript Bilgi Referansi

## Genel Bakis

TypeScript, Microsoft tarafindan Anders Hejlsberg onderliginde 2012 yilinda gelistirilmeye baslanmistir. JavaScript'in super kumesi (superset) olan bu dil, statik tip kontrolu, sinif tabanli nesne yonelim ve modern ECMAScript ozelliklerini JavaScript'e ekler. JavaScript'e derlenerek calisir.

Gunumuzde buyuk olcekli projelerde tip guvenligi ve bakim kolayligi icin standart haline gelmistir. Angular bastan TypeScript ile yazilmistir. React (create-react-app, Next.js), NestJS, Vue 3, ve Svelte gibi populer frameworkler TypeScript'i birinci sinif destekler. VS Code'un kendisi de TypeScript ile yazilmistir. Stack Overflow anketlerinde en sevilen ve en cok kullanilan diller arasinda ust siradadir.

## Temel Syntax

```typescript
// --- Temel Tipler ---
let isim: string = "Ali";
let yas: number = 25;
let aktif: boolean = true;
let bos: null = null;
let tanimsiz: undefined = undefined;
let herhangi: any = "her sey olabilir"; // kacis valfi (kullanma)
let bilinmiyor: unknown = "tip guvenli";
let asla: never;                        // asla olusmayacak (hata fonk)

// --- Dizi ve Tuple ---
let rakamlar: number[] = [1, 2, 3];
let isimler: Array<string> = ["Ali", "Veli"]; // generic syntax
let tuple: [string, number] = ["Ali", 25];     // sabit uzunluk

// --- Enum ---
enum Renk {
    Kirmizi,          // 0
    Yesil = "GREEN",
    Mavi = 2
}
const renk = Renk.Yesil;

// --- Union ve Intersection ---
let kimlik: string | number = "ABC123";  // union
kimlik = 456;

type Calisan = { ad: string; sirket: string };
type Kisi = { ad: string; yas: number };
type CalisanKisi = Calisan & Kisi;       // intersection

// --- Interface ---
interface Kullanici {
    readonly id: number;           // sadece okunur
    ad: string;
    soyad?: string;                // opsiyonel
    eposta?: string;
    readonly kayitTarihi: Date;
}

interface Admin extends Kullanici {
    rol: "admin" | "moderator";
    yetkiler: string[];
}

// --- Type vs Interface ---
type Durum = "aktif" | "pasif" | "beklemede";  // union type
type ID = string | number;

// --- Fonksiyon Tipleri ---
function topla(a: number, b: number): number {
    return a + b;
}

// Opsiyonel ve default parametre
function selamla(isim: string, unvan?: string): string {
    return `Merhaba ${unvan ? unvan + " " : ""}${isim}`;
}

// Arrow function tipi
const carp: (a: number, b: number) => number = (x, y) => x * y;

// Fonksiyon tipi (interface)
interface Matematik {
    (x: number, y: number): number;
}
const bol: Matematik = (x, y) => x / y;

// --- Generic ---
function ilk<T>(dizi: T[]): T | undefined {
    return dizi[0];
}
const sayi = ilk<number>([1, 2, 3]);    // number
const metin = ilk(["a", "b"]);           // type inference

// Generic interface
interface ApiYanit<T> {
    basarili: boolean;
    veri: T;
    hata?: string;
}

// Generic constraint
function uzunluk<T extends { length: number }>(item: T): number {
    return item.length;
}

// --- Class ---
abstract class Hayvan {
    constructor(public ad: string) {}  // shorthand
    abstract sesCikar(): string;
}

class Kopek extends Hayvan {
    constructor(ad: string, public cins: string) {
        super(ad);
    }
    sesCikar(): string {
        return "Hav hav!";
    }
}

// --- Type Guards ---
function yazdir(deger: string | number) {
    if (typeof deger === "string") {
        console.log(deger.toUpperCase());
    } else {
        console.log(deger.toFixed(2));
    }
}

// Custom type guard
function isKullanici(obj: any): obj is Kullanici {
    return obj && typeof obj.ad === "string";
}

// --- Utility Types ---
interface Urundetay {
    id: number;
    ad: string;
    fiyat: number;
    aciklama: string;
}

type Kismi = Partial<Urundetay>;          // hepsi opsiyonel
type SadeceAd = Pick<Urundetay, "ad">;    // sadece ad
type AdVeFiyat = Pick<Urundetay, "ad" | "fiyat">;
type IdHaric = Omit<Urundetay, "id">;     // id haric
type SadeceOku = Readonly<Urundetay>;     // hepsi readonly

// --- Dekorator (experimental) ---
function Log(target: any, propertyKey: string) {
    console.log(`Property: ${propertyKey} okundu`);
}

// --- Module ---
// export const API_URL = "https://api.example.com";
// import { API_URL } from "./config";
// import * as Config from "./config";
```

## Yaygin Patternler

1. **Utility Types**: `Partial<T>`, `Pick<T,K>`, `Omit<T,K>`, `Readonly<T>` ile tip manipülasyonu
2. **Type Guards**: `typeof`, `instanceof`, custom type guard fonksiyonlari ile tip daraltma
3. **Discriminated Unions**: `type Sonuc = { tip: "basarili"; veri: T } | { tip: "hata"; hata: Error }`
4. **Type Inference**: Tipi acikca belirtmeden inferred birakmak (kod temizligi)
5. **`strict: true` kullanmak**: tsconfig.json'da strict mod ile maksimum tip guvenligi
6. **Generic Constraints**: `extends` ile generic tipleri kisitlama
7. **Branded Types**: Nominal tip taklidi icin brand (marka) tipi
8. **Mapped Types**: `{ [K in keyof T]: ... }` ile mevcut tipi donusturme
9. **Template Literal Types**: `type EventName = `on${Capitalize<string>}``
10. **Conditional Types**: `T extends U ? X : Y` tipinde kosullu tipler
11. **Satisfies Operator** (TS 4.9+): Tip kontrolu yapip daraltma
12. **Namespace vs Module**: Eski (namespace) ve yeni (module) organizasyon

```typescript
// Discriminated Union
type Sonuc<T> =
    | { durum: "basarili"; veri: T }
    | { durum: "hata"; hata: string };

function isle(sonuc: Sonuc<number>) {
    if (sonuc.durum === "basarili") {
        console.log(sonuc.veri.toFixed());  // tip daraltildi
    }
}

// Mapped Type
type Optional<T> = { [K in keyof T]?: T[K] };

// Branded Type
type Brand<T, B> = T & { __brand: B };
type TL = Brand<number, "TL">;
type USD = Brand<number, "USD">;
function toplaPara(a: TL, b: TL): TL {
    return (a + b) as TL;
}

// Conditional Type
type IsString<T> = T extends string ? "Evet" : "Hayir";
type Test1 = IsString<"merhaba">;  // "Evet"
type Test2 = IsString<number>;     // "Hayir"
```

## Onemli Kutuphaneler

1. **TypeScript Compiler (tsc)**: TS'yi JS'e derler
2. **ts-node**: Dogrudan TypeScript calistirma (tsx de var)
3. **tsx**: Modern TS icin hizli calistirici (esbuild tabanli)
4. **Zod**: Runtime validation ve type inference
   `const schema = z.object({ ad: z.string() })`
5. **Yup**: Schema validation (Zod'dan eski, daha cok kullanilir)
6. **Prisma**: Modern ORM (auto-generated types)
   `const user = await prisma.user.findUnique({ where: { id } })`
7. **TypeORM**: Decorator tabanli ORM
8. **Drizzle ORM**: SQL benzeri API ile ORM
9. **NestJS**: Dekorator tabanli backend framework
   `@Controller("users") class UserController {}`
10. **ts-jest**: Jest ile TypeScript test
11. **Vitest**: Vite uzerinde test frameworku (TS native)
12. **ESLint + typescript-eslint**: TS icin statik analiz
13. **Prettier**: Kod formatlama
14. **GraphQL Code Generator**: GraphQL'den tip uretme
15. **tRPC**: Tip guvenli API (client-server types shared)
    `const router = t.router({ ... })`
16. **InversifyJS**: Dependency injection container
17. **RxJS**: Reaktif programlama (Observable)
18. **MobX**: State management (decorator tabanli)
19. **Playwright**: Browser test otomasyonu

```typescript
// Zod ornegi
import { z } from "zod";
const KullaniciSchema = z.object({
    ad: z.string().min(2),
    yas: z.number().positive(),
    eposta: z.string().email().optional(),
});
type Kullanici = z.infer<typeof KullaniciSchema>;

// tRPC ornegi
import { initTRPC } from "@trpc/server";
const t = initTRPC.create();
const appRouter = t.router({
    kullaniciGetir: t.procedure
        .input(z.string())
        .query(({ input }) => fetchKullanici(input)),
});
```

## Yaygin Hatalar

1. **`any` tipini asiri kullanmak**: Tip guvenligini tamamen kaybetmek, mumkunse `unknown` tercih edilmeli
2. **`null/undefined` kontrolu yapmamak**: Strict mode'da hata alinir, optional chaining (`?.`) kullanilmali
3. **`as` keyword'unu asiri kullanmak**: Tip zorlamasi (type assertion) tip guvenligini bypass eder
4. **Type assertion yerine type annotation kullanmamak**: `const x: string = y` dogru, `const x = y as string` riskli
5. **`tsconfig.json` strict modunu acmamak**: strict false ile bir cok hata gozden kacar
6. **`@ts-ignore` kullanmak**: Sorunu gizler, `@ts-expect-error` tercih edilmeli
7. **Excess property checking farkinda olmamak**: Interface disi alan eklenince hata
8. **Generic tipleri gereksiz karmasiklastirmak**: Basit cozum varken karmasik generic yazmak
9. **Namespace vs Module karisikligi**: ES6 module sistemi kullanilmali, namespace degil
10. **`.d.ts` dosyalarini yanlis kullanmak**: Sadece tip tanimi icin, kod icin degil
11. **Type-only import kullanmamak**: `import type { Kullanici }` ile runtime yukunu azaltmak
12. **Declaration merging yanlis kullanimi**: Ayni isimde interface/fonksiyon birlestirme

## Performans Ipuclari

1. **`strict` mod kullanmak**: Derleme asamada hatalari yakalar, runtime hatalarini azaltir
2. **`--noEmit` ile kontrol**: Production build haric tip kontrolu icin emisyon yapmadan kullanma
3. **Project References**: Buyuk projelerde monorepo icin referans ile bolumsel derleme
4. **`skipLibCheck: true`**: node_modules tip dosyalarini kontrol etmemek (derleme hizi)
5. **Type-only import kullanmak**: Sadece tip icin import edilen dosyalari runtime'dan cikarma
   `import type { Kullanici } from "./models";`
6. **`incremental: true`**: Sadece degisen dosyalari derleme
7. **Generic overload yerine union kullanmak**: Generic tip inferansi derlemeyi yavaslatabilir

```typescript
// Derleme hizi icin --noEmit
// tsc --noEmit --strict
```

## Ekosistem

**Derleyiciler**: tsc (kendi), esbuild (Go ile yazilmis, cok hizli), swc (Rust), Bun

**Frameworkler (Backend)**: NestJS, AdonisJS, FoalTS, Ts.ED

**Frameworkler (Frontend)**: Angular, Next.js (React), Nuxt 3 (Vue), SvelteKit

**Build Araclari**: Vite, Webpack + ts-loader, Rollup, Turbopack

**Paket Yoneticisi**: npm, yarn, pnpm

**Linter/Formatter**: ESLint + typescript-eslint, Prettier, Rome

**Test**: Jest + ts-jest, Vitest, Cypress, Playwright

**Monorepo**: Turborepo, Nx, Lerna, Rush

**ORM**: Prisma, TypeORM, Drizzle, MikroORM, Kysely

**Validator**: Zod, Yup, Joi (JS), class-validator (NestJS)

## Kaynaklar

**Resmi Dokuman**: typescriptlang.org (Turkish dokumani da var)

**Playground**: typescriptlang.org/play (interaktif deneme)

**Kitaplar**:
- Programming TypeScript (Boris Cherny)
- TypeScript Handbook (resmi)
- Effective TypeScript (Dan Vanderkam)
- Learning TypeScript (Josh Goldberg)

**Web Siteleri**:
- totaltypescript.com
- type-level-typescript.com
- typescript-exercises.vercel.app
- typescripttutorial.net

**Interaktif Ogrenme**:
- exercism.org/tracks/typescript
- codewars.com
- typehero.dev (TypeScript oyunu)
- typescript-challenges (Github)

**Topluluk**: TypeScript subreddit, TypeScript Discord, Stack Overflow, Twitter/X

**Araclar**:
- tsconfig.json bazli proje olusturma: `tsc --init`
- Playground ile hizli deneme
- `npm create vite@latest` ile TS projesi baslatma
