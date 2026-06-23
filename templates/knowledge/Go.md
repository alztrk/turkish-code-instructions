# Go (Golang) Bilgi Referansi

## Genel Bakis

Go (Golang), Google tarafindan Robert Griesemer, Rob Pike ve Ken Thompson tarafindan 2007'de gelistirilmeye baslanmis, 2009'da acik kaynak olarak yayinlanmistir. C++ karmasikligina ve Java'nin agirligina alternatif olarak basit, hizli ve olceklenebilir bir dil ihtiyacindan dogmustur. 2012'de 1.0 surumu kararli hale gelmistir.

Go gunumuzde mikroservis mimarileri, bulut tabanli uygulamalar, konteyner teknolojileri (Docker, Kubernetes dogrudan Go ile yazilmistir), CLI araclari, ag programlama ve DevOps araclarinda lider dildir. Basit syntax'i, hizli derlemesi, dahili concurrency modeli (goroutine, channel) ve kolay deploy edilebilen tek binary ciktisi ile bilinir. Google, Uber, Twitch, Dropbox gibi sirketler Go kullanmaktadir.

## Temel Syntax

```go
package main

import (
    "fmt"
    "strings"
    "errors"
    "time"
)

// --- Degiskenler ---
func main() {
    var isim string = "Ali"       // acik tip
    var yas = 25                  // tip cikarimi
    maas := 5000.50               // kisa tanim (en yaygin)
    var aktif bool                // false (zero value)

    // Coklu degisken
    var x, y int = 10, 20
    ad, soyad := "Ali", "Yilmaz"

    // --- Sabit ---
    const PI = 3.14159
    const (
        DurumAktif = "aktif"
        DurumPasif = "pasif"
    )

    // --- String Islemleri ---
    mesaj := "Merhaba, " + isim + "!"
    fmt.Println(len(mesaj))
    fmt.Println(strings.ToUpper(mesaj))
    fmt.Println(strings.Contains(mesaj, "Ali"))

    // --- Diziler ve Slice ---
    var dizi [3]int = [3]int{1, 2, 3}    // sabit uzunluk
    slice := []int{1, 2, 3}              // dinamik
    slice = append(slice, 4, 5)
    fmt.Println(slice[0])                // 1

    // Slice dilimleme
    altSlice := slice[1:3]               // {2, 3}

    // --- Map ---
    yaslar := make(map[string]int)
    yaslar["Ali"] = 25
    yaslar["Veli"] = 30
    fmt.Println(yaslar["Ali"])           // 25

    deger, varMi := yaslar["Ayse"]       , kontrol
    if !varMi {
        fmt.Println("Bulunamadi")
    }

    // --- Kosul ---
    if yas >= 18 {
        fmt.Println("Yetiskin")
    } else if yas > 12 {
        fmt.Println("Ergen")
    } else {
        fmt.Println("Cocuk")
    }

    // Statement ile if
    if sayi := 10; sayi > 5 {
        fmt.Println("Buyuk")
    }

    // --- Donguler (sadece for) ---
    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }

    // while benzeri
    sayac := 0
    for sayac < 5 {
        fmt.Println(sayac)
        sayac++
    }

    // Sonsuz dongu
    // for { }

    // range ile
    meyveler := []string{"elma", "armut", "muz"}
    for index, meyve := range meyveler {
        fmt.Printf("%d: %s\n", index, meyve)
    }

    for anahtar, deger := range yaslar {
        fmt.Printf("%s: %d\n", anahtar, deger)
    }

    // --- Fonksiyonlar ---
    sonuc := topla(3, 4)
    fmt.Println(sonuc)

    // Coklu donus degeri
    bolum, kalan := bol(10, 3)
    fmt.Printf("Bolum: %d, Kalan: %d\n", bolum, kalan)

    // --- Struct ve Metod ---
    kisi := Kisi{Ad: "Ali", Yas: 25}
    fmt.Println(kisi.SelamVer())

    // --- Interface ---
    var hayvan Hayvan
    hayvan = Kopek{Ad: "Karabas"}
    fmt.Println(hayvan.SesCikar())

    // --- Hata Yönetimi ---
    sonuc2, err := tehlikeliIslem(0)
    if err != nil {
        fmt.Println("Hata:", err)
    } else {
        fmt.Println("Sonuc:", sonuc2)
    }

    // --- Goroutine ve Channel ---
    ch := make(chan string)
    go func() {
        ch <- "Merhaba goroutine!"
    }()
    mesaj2 := <-ch
    fmt.Println(mesaj2)

    // --- defer ---
    defer fmt.Println("Bu en son calisir")
    fmt.Println("Ilk bu calisir")
}

// --- Fonksiyon Tanimlari ---
func topla(a int, b int) int {
    return a + b
}

// Coklu donus
func bol(x, y int) (int, int) {
    return x / y, x % y
}

// Named return
func isimlendirilmis() (sonuc int) {
    sonuc = 42
    return
}

// --- Struct ---
type Kisi struct {
    Ad  string
    Yas int
}

// Metod
func (k Kisi) SelamVer() string {
    return fmt.Sprintf("Merhaba, ben %s!", k.Ad)
}

// Pointer receiver
func (k *Kisi) YasiArtir() {
    k.Yas++
}

// --- Interface ---
type Hayvan interface {
    SesCikar() string
}

type Kopek struct{ Ad string }
func (k Kopek) SesCikar() string { return "Hav hav!" }

type Kedi struct{ Ad string }
func (k Kedi) SesCikar() string { return "Miyav!" }

// --- Hata ---
func tehlikeliIslem(x int) (int, error) {
    if x == 0 {
        return 0, errors.New("sifira bolme hatasi")
    }
    return 100 / x, nil
}
```

## Yaygin Patternler

1. **Error handling (if err != nil)**: Go'da try-catch yoktur, hatalar return degeri olarak donulur
2. **Goroutine/Channel**: `go func()` ile hafif thread'ler, `chan` ile senkronizasyon
3. **Interface (implicit)**: Go'da interface'ler otomatik implemente edilir (duck typing)
4. **Struct method / Pointer receiver**: Metotlar struct disinda eklenir, receiver tipine dikkat
5. **Package organizasyonu**: Kucuk, odakli paketler (internal, pkg, cmd dizin yapisi)
6. **Context**: Zaman asimi ve islem iptali icin `context.Context`
7. **Mutex / Sync**: Paylasilan durum icin `sync.Mutex`, `sync.WaitGroup`
8. **Defer**: Kaynak temizligi, lock acma, dosya kapatma
9. **Factory Function**: `NewXxx()` fonksiyonlari ile struct olusturma
10. **Builder Pattern**: Functional options (variadic config)
11. **Middleware Pattern**: HTTP handler zinciri (logging, auth)
12. **Rate Limiter**: `time.Ticker` veya `golang.org/x/time/rate` ile hiz sinirlama
13. **Singleton**: `sync.Once` ile tek seferlik baslatma

```go
// Context ile zaman asimi
ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
defer cancel()
select {
case <-ctx.Done():
    fmt.Println("Zaman asimi")
case sonuc := <-ch:
    fmt.Println(sonuc)
}

// Worker pool
func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        results <- j * 2
    }
}

// sync.Once singleton
var once sync.Once
var instance *Veritabani
func GetVeritabani() *Veritabani {
    once.Do(func() { instance = &Veritabani{} })
    return instance
}

// Functional options
type Config struct{ Host string; Port int }
type Option func(*Config)
func WithHost(h string) Option { return func(c *Config) { c.Host = h } }
func NewConfig(opts ...Option) *Config {
    cfg := &Config{Host: "localhost", Port: 8080}
    for _, opt := range opts { opt(cfg) }
    return cfg
}
```

## Onemli Kutuphaneler

1. **net/http**: Standart HTTP sunucu/istemci (sunucuda default olarak goroutine kullanir)
   `http.HandleFunc("/", handler); http.ListenAndServe(":8080", nil)`
2. **gorilla/mux**: Guclu HTTP router (path parametreleri, middleware)
3. **gin**: Populer web frameworku (hizli, middleware destegi)
   `r := gin.Default(); r.GET("/", func(c *gin.Context) { c.JSON(200, gin.H{"mesaj": "Merhaba"}) })`
4. **echo**: Hafif web frameworku
5. **chi**: Hafif, composable router
6. **GORM**: Populer ORM
   `db.Where("yas > ?", 18).Find(&kullanicilar)`
7. **sqlx**: Veritabani islemleri (standart library uzerine extension)
8. **cobra**: CLI uygulamalari (Kubernetes, Docker CLI de kullanir)
   `var rootCmd = &cobra.Command{Use: "app", Run: func(cmd *cobra.Command, args []string) {}}`
9. **viper**: Konfigurasyon yonetimi (JSON, YAML, env, flag)
10. **testify**: Test frameworku (assert, mock, suite)
    `assert.Equal(t, 42, sonuc)`
11. **logrus / zap**: Yapisal loglama (zap en hizlisi)
12. **validator**: Struct validation
13. **JWT-go**: JSON Web Token
14. **bcrypt / argon2**: Sifre hashleme
15. **Swaggo / gin-swagger**: API dokuman
16. **gRPC-go**: gRPC frameworku
17. **ent**: Facebook'un ORM'si (code generation)
18. **fx / wire**: Dependency injection (Uber fx, Google wire)
19. **testcontainers-go**: Test icin Docker container yonetimi
20. **migrate / golang-migrate**: Veritabani migration

```go
// gin ornegi
import "github.com/gin-gonic/gin"
func main() {
    r := gin.Default()
    r.GET("/api/merhaba/:isim", func(c *gin.Context) {
        isim := c.Param("isim")
        c.JSON(200, gin.H{"mesaj": "Merhaba " + isim})
    })
    r.Run(":8080")
}

// cobra + viper ornegi
import "github.com/spf13/cobra"
var cfgFile string
var rootCmd = &cobra.Command{
    Use: "uygulama",
    Run: func(cmd *cobra.Command, args []string) {
        viper.SetConfigFile(cfgFile)
        viper.ReadInConfig()
    },
}
```

## Yaygin Hatalar

1. **`defer` sirasini yanlis anlamak**: Defer'ler LIFO (Last In, First Out) calisir
2. **Channel deadlock**: Sadece okuyan veya sadece yazan goroutine beklerken kilitlenme
3. **`_` kullanmadan import/degisken birakmak**: Kullanilmayan import/degisken derleme hatasidir
4. **Pointer vs value receiver karistirmak**: Value receiver kopya ile calisir, degisiklikler kalici olmaz
5. **`nil` map/slice'a yazi yazmak**: Map'in make ile initialize edilmesi gerekir
6. **Global degisken kullanmak**: Fonksiyonel bagimliligi artirir, testi zorlastirir
7. **Loop variable capture (goroutine icinde)**: `for i := range items { go func() { fmt.Println(i) }() }` -> ayni i'yi okur
   ```go
   // Cozum
   for i := range items {
       i := i  // local kopya
       go func() { fmt.Println(i) }()
   }
   ```
8. **`select` icinde default kullanmamak**: Bekleyen channel yoksa bloklanir
9. **Empty struct vs interface**: `interface{}` her tipi alir, gereksiz kullanim performans kaybi
10. **Pointer kullanimi asiri**: Go'da pass-by-value esastir, buyuk struct'lar icin pointer tercih edilir
11. **JSON field tag unutmak**: Kucuk harf field'lar JSON'da gorunmez
12. **`goroutine` leak**: Baslatilan goroutine bitmezse kaynak sizintisi

## Performans Ipuclari

1. **Pool kullanmak**: `sync.Pool` ile gecici nesneleri yeniden kullanma
   ```go
   var bufferPool = sync.Pool{
       New: func() interface{} { return new(bytes.Buffer) },
   }
   buf := bufferPool.Get().(*bytes.Buffer)
   buf.Reset()
   defer bufferPool.Put(buf)
   ```

2. **Slice capacity onceden ayirmak**: `make([]int, 0, 1000)` ile append'lerde reallocation'u azaltma
3. **String builder kullanmak**: `+` ile birlestirme yerine `strings.Builder`
   ```go
   var sb strings.Builder
   for _, s := range kelimeler { sb.WriteString(s) }
   fmt.Println(sb.String())
   ```
4. **Goroutine sayisini sinirlamak**: Worker pool pattern ile kontrolsuz goroutine'den kacinmak
5. **Escape analysis'a dikkat**: Pointer kullanimi heap allocation'a sebep olabilir
6. **Profil ile optimizer**: `pprof` ile CPU ve memory profiling
7. **`interface{}` kullanmamak**: Tip guvenli kod hem hizli hem guvenli

```go
// pprof kullanimi
import _ "net/http/pprof"
func main() {
    go func() { http.ListenAndServe(":6060", nil) }()
    // http://localhost:6060/debug/pprof/
}
```

## Ekosistem

**Frameworkler**: Gin, Echo, Fiber, Chi, Revel, Beego

**CLI Frameworkleri**: Cobra, Urfave/cli

**Veritabani**: GORM, ent, sqlx, pgx (PostgreSQL), go-redis

**Build**: go build (dahili, hizli), Makefile, Mage (Go ile build), Bazel

**Paket Yoneticisi**: Go Modules (dahili, go.mod/go.sum), GOPATH (eski)

**Test**: go test (dahili), testify, GoMock, ginkgo (BDD)

**Linter/Formatter**: gofmt (standart), golangci-lint, staticcheck

**Package Registry**: pkg.go.dev, Go Proxy

**Runtime**: go run, go build ile tek binary

**CI/CD**: GitHub Actions, GitLab CI, Drone CI

**Monitoring**: Prometheus (Go ile yazilmis), OpenTelemetry, expvar

## Kaynaklar

**Resmi Dokuman**: go.dev (tour, doc, blog)

**Turkce Kaynaklar**:
- golang.istihza.com - Kapsamli Turkce Go kaynagi
- go.deu.edu.tr - Dokuz Eylul Unv. Go ders notlari

**Kitaplar**:
- The Go Programming Language (Donovan, Kernighan)
- Go in Action (William Kennedy)
- Concurrency in Go (Katherine Cox-Buday)
- Go Design Patterns

**Web Siteleri**:
- gophercises.com (Go egzersizleri)
- exercism.org/tracks/go
- gotutorial.com
- golangbyexample.com

**Interaktif Ogrenme**:
- tour.golang.org (resmi Go turu)
- gobyexample.com (orneklerle Go)
- codewars.com
- leetcode.com

**Topluluk**: reddit.com/r/golang, Gopher Discord, Go Turkey (Telegram), Stack Overflow, Go Conference/Turkey
