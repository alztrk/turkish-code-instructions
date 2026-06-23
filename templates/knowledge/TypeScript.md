# TypeScript Bilgi Referansi

## Genel Bakis
TypeScript, Microsoft tarafindan 2012'de gelistirilen, JavaScript'e statik tip ekleyen bir dildir. Buyuk olcekteki projelerde tip guvenligi saglar. JavaScript'e derlenir. Angular, React ve NestJS gibi frameworklerde yaygindir.

## Temel Syntax

```typescript
// Tip belirleme
let isim: string = "Ali";
let yas: number = 25;
let aktif: boolean = true;

// Interface
interface Kullanici {
    id: number;
    ad: string;
    eposta?: string; // opsiyonel
}

// Fonksiyon
function merhaba(kisi: Kullanici): string {
    return `Merhaba, ${kisi.ad}!`;
}

// Tip tanimi
type Durum = "aktif" | "pasif" | "beklemede";

// Generic
function ilk<T>(dizi: T[]): T | undefined {
    return dizi[0];
}

// Enum
enum Renk { Kirmizi = "RED", Yesil = "GREEN" }
```

## Yaygin Patternler

- **Utility Types**: `Partial<T>`, `Pick<T,K>`, `Omit<T,K>`, `Readonly<T>`
- **Type Guards**: `typeof`, `instanceof`, custom type guards
- **Discriminated Unions**: Ayrismis birlik tipleri
- **Type Inference**: Mumnkunse tipi inferred birakmak
- `strict: true` kullanmak (tsconfig.json)

## Onemli Kutuphaneler

- **ts-node/lis-ts**: Dogrudan TS calistirma
- **Zod/Yup**: Runtime validation/sema
- **Prisma/TypeORM**: ORM araclari
- **NestJS**: Backend framework
- **ts-jest**: Jest ile TypeScript test
- **ESLint + typescript-eslint**: Statik analiz

## Yaygin Hatalar

- `any` tipini asiri kullanmak (tip guvenligini kaybetmek)
- `null/undefined` kontrolu yapmamak
- `as` keyword'unu asiri kullanmak (tip zorlamasi)
- Type assertion yerine type annotation kullanmamak
- `tsconfig.json` strict modunu acmamak
