# Go (Golang) Bilgi Referansi

## Genel Bakis
Go, Google tarafindan 2009'da Robert Griesemer, Rob Pike ve Ken Thompson tarafindan olusturulmustur. Basitlik, hiz ve olceklenebilirlik odaklidir. Mikroservisler, bulut uygulamalari (Docker, Kubernetes), CLI araclari ve ag programlama icin idealdir.

## Temel Syntax

```go
package main
import "fmt"

func main() {
    yas := 25
    isim := "Ali"

    merhaba := func(kisi string) string {
        return fmt.Sprintf("Merhaba, %s!", kisi)
    }

    if yas >= 18 { fmt.Println("Yetiskin") } else { fmt.Println("Cocuk") }

    for i := 0; i < 5; i++ { fmt.Println(i) }

    meyveler := []string{"elma", "armut"}
    meyveler = append(meyveler, "muz")
}
```

## Yaygin Patternler

- **Error handling**: `if err != nil { return err }` (try-catch yok)
- **Goroutine/Channel**: `go func()`, `ch := make(chan int)`
- **Interface**: `type Arayuz interface { ... }` (implicit implementasyon)
- **Struct method**: Metotlar struct disinda tanimlanir
- **Package organizasyonu**: Kucuk, odakli paketler
- **Context**: Zaman asimi ve iptal mekanizmasi

## Onemli Kutuphaneler

- **net/http**: HTTP sunucu/istemci
- **gorilla/mux**: HTTP router
- **GORM**: ORM
- **cobra**: CLI uygulamalari
- **viper**: Konfigurasyon yonetimi
- **testify**: Test frameworku
- **logrus/zap**: Loglama
- **gin/echo**: Web frameworkleri

## Yaygin Hatalar

- `defer` sirasini yanlis anlamak (LIFO)
- Channel deadlock yapmak
- `_` kullanmadan import/disisken birakmak (derleme hatasi)
- Pointer vs value receiver karistirmak
- `nil` map/e slice'a yazi yazmak
- Global degisken kullanmak (bagimliligi artirir)
