# C++ Bilgi Referansi

## Genel Bakis

C++, Bjarne Stroustrup tarafindan 1979'da Bell Laboratuvarlari'nda "C with Classes" olarak baslatilmis, 1985'te ilk ticari surumu yayinlanmistir. C diline nesne yonelimli programlama, generic programlama (template'ler) ve ozel fonksiyonlar eklenerek olusturulmustur. 1998'de ilk ISO standardi (C++98) yayinlanmis, ardindan C++11, C++14, C++17, C++20 ve C++23 ile dil surekli evrilmistir.

C++ yuksek performansli uygulamalar, oyun gelistirme (Unreal Engine), gomulu sistemler, isletim sistemleri (Windows, Linux cekirdek bilesenleri), gercek zamanli sistemler, finansal sistemler ve tarayicilar (Chrome, Firefox) gibi performans kritik alanlarda kullanilir. Dogrudan bellek yonetimi (pointer, reference), sifir maliyetli soyutlama (zero-cost abstraction) ve donanim seviyesinde kontrol imkani sunar. Hem procedural hem OOP hem de generic programlama paradigmalarini destekler.

## Temel Syntax

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
#include <map>
#include <fstream>

// --- Degiskenler ve Veri Tipleri ---
int main() {
    std::string isim = "Ali";
    int yas = 25;
    double pi = 3.14159;
    bool aktif = true;
    char harf = 'A';
    unsigned int pozitif = 100;
    long long buyuk = 1'000'000'000LL;

    // --- String Islemleri ---
    std::string mesaj = "Merhaba, " + isim + "!";
    std::cout << mesaj.length() << std::endl;
    std::transform(mesaj.begin(), mesaj.end(), mesaj.begin(), ::toupper);

    // --- Diziler ve Vektor ---
    int dizi[5] = {1, 2, 3, 4, 5};
    std::vector<int> sayilar = {1, 2, 3};
    sayilar.push_back(4);
    sayilar.pop_back();

    // --- Map (Sozluk) ---
    std::map<std::string, int> yaslar;
    yaslar["Ali"] = 25;
    yaslar["Veli"] = 30;

    // --- Kosullar ---
    if (yas >= 18) {
        std::cout << "Yetiskin" << std::endl;
    } else if (yas > 12) {
        std::cout << "Ergen" << std::endl;
    } else {
        std::cout << "Cocuk" << std::endl;
    }

    // Ternary
    std::string durum = (yas >= 18) ? "Yetiskin" : "Cocuk";

    // Switch
    switch (yas) {
        case 18: std::cout << "18" << std::endl; break;
        default: std::cout << "Diger" << std::endl;
    }

    // --- Donguler ---
    for (int i = 0; i < 5; i++) {
        std::cout << i << std::endl;
    }

    for (int sayi : sayilar) {          // range-based for
        std::cout << sayi << std::endl;
    }

    int i = 0;
    while (i < 5) { std::cout << i++ << std::endl; }

    // --- Fonksiyonlar ---
    auto topla = [](int a, int b) -> int { return a + b; };
    std::cout << topla(3, 4) << std::endl;

    // Lambda ile capture
    int faktor = 2;
    auto katla = [faktor](int x) { return x * faktor; };

    // --- Sinif (OOP) ---
    class Hayvan {
    protected:
        std::string ad;
    public:
        Hayvan(const std::string& ad) : ad(ad) {}
        virtual std::string sesCikar() const = 0;  // pure virtual
        virtual ~Hayvan() = default;               // virtual destructor
    };

    class Kopek : public Hayvan {
    private:
        std::string cins;
    public:
        Kopek(const std::string& ad, const std::string& cins)
            : Hayvan(ad), cins(cins) {}
        std::string sesCikar() const override {
            return "Hav hav!";
        }
    };

    // --- Smart Pointers ---
    auto ptr = std::make_unique<Kopek>("Karabas", "Kangal");
    auto shared = std::make_shared<Hayvan>("Tekir");

    // --- STL Algoritmalari ---
    std::vector<int> v = {5, 3, 1, 4, 2};
    std::sort(v.begin(), v.end());
    auto it = std::find(v.begin(), v.end(), 3);
    std::reverse(v.begin(), v.end());

    // --- Hata Yakalama ---
    try {
        if (yas == 0) throw std::runtime_error("Sifir yas!");
        std::cout << "Yas: " << yas << std::endl;
    } catch (const std::runtime_error& e) {
        std::cerr << "Runtime hata: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Genel hata: " << e.what() << std::endl;
    }

    // --- Dosya Islemleri ---
    std::ofstream dosya("ornek.txt");
    if (dosya.is_open()) {
        dosya << "Merhaba dosya" << std::endl;
        dosya.close();
    }

    // --- Move Semantics ---
    std::vector<int> kaynak = {1, 2, 3};
    std::vector<int> hedef = std::move(kaynak);  // kaynak bosalir

    return 0;
}
```

## Yaygin Patternler

1. **RAII (Resource Acquisition Is Initialization)**: Kaynak alimi sinif constructor'inda, temizlik destructor'da
2. **Smart Pointers**: `unique_ptr` (tek sahip), `shared_ptr` (paylasimli), `weak_ptr` (circular reference cozumu)
3. **STL Algoritmalari**: `sort`, `find`, `transform`, `accumulate`, `copy`
4. **Move Semantics**: `std::move` ile gereksiz kopyalamalari onleme
5. **Lambda**: `[capture](params) { body }` ile inline anonim fonksiyon
6. **Const Correctness**: Olabilecek her yerde `const` kullanmak
7. **PIMPL Idiom (Pointer to Implementation)**: Arayuzu implementasyondan ayirma
8. **CRTP (Curiously Recurring Template Pattern)**: Template ile statik polimorfizm
9. **SFINAE**: Template overload cozumu (C++20'de concepts ile degisti)
10. **Rule of Five/Five**: Custom destructor, copy-constructor, copy-assignment, move-constructor, move-assignment
11. **Type Traits**: `std::is_integral<T>`, `std::enable_if` ile tip ozellikleri
12. **Policy-Based Design**: Template parametresi ile davranis belirleme

```cpp
// RAII ornegi
class KaynakYoneticisi {
    int* kaynak;
public:
    KaynakYoneticisi() : kaynak(new int[100]) {}
    ~KaynakYoneticisi() { delete[] kaynak; }
    // Copy/move operasyonlari da eklenmeli
};

// CRTP Pattern
template <typename Derived>
class HayvanTemel {
public:
    void seslen() {
        static_cast<Derived*>(this)->sesCikar();
    }
};
class Kedi : public HayvanTemel<Kedi> {
public:
    void sesCikar() { std::cout << "Miyav" << std::endl; }
};
```

## Onemli Kutuphaneler

1. **STL (Standard Template Library)**: Container (vector, map, set), iterator, algoritma, functor
2. **Boost**: Kapsamli, peer-reviewed C++ kutuphaneleri (asio, filesystem, spirit, smart_ptr'nin atasi)
3. **Qt (Qt6)**: GUI frameworku (cross-platform, sinyal-slot mekanizmasi)
   `QPushButton buton("Tikla"); QObject::connect(&buton, &QPushButton::clicked, ...)`
4. **OpenCV**: Bilgisayarli goru ve goruntu isleme
5. **OpenGL / Vulkan**: 3D grafik API (oyun, simulasyon)
6. **Catch2 / Google Test**: Unit test frameworkleri
7. **nlohmann/json**: JSON isleme
   `json j = {{"ad", "Ali"}, {"yas", 25}};`
8. **POCO**: Ag (http, ftp), XML, veritabani uygulamalari
9. **fmt**: Modern string formatlama (C++20'de std::format olarak)
   `fmt::format("Merhaba {}! Yas: {}", isim, yas);`
10. **spdlog**: Hizli loglama kutuphanesi
11. **Asio (veya Boost.Asio)**: Ag ve asenkron I/O
12. **Crypto++ / OpenSSL**: Kriptografik islemler
13. **Eigen**: Lineer cebir kutuphanesi (makine ogrenmesi, robotik)
14. **TBB (Intel oneAPI TBB)**: Paralel programlama
15. **wxWidgets**: Cross-platform GUI frameworku
16. **SFML / SDL**: Oyun ve multimedya gelistirme
17. **Protobuf / FlatBuffers**: Serilestirme
18. **abseil**: Google'in C++ standart kutuphane eklentileri

```cpp
// fmt ornegi
#include <fmt/core.h>
std::string mesaj = fmt::format("{} yas: {}", "Ali", 25);

// nlohmann/json ornegi
#include <nlohmann/json.hpp>
using json = nlohmann::json;
json kullanici = {{"ad", "Ali"}, {"aktif", true}};
std::cout << kullanici.dump(4) << std::endl;  // guzel yazdir
```

## Yaygin Hatalar

1. **Pointer aritmetigi ile bellek hatalari**: Dizi siniri asimi (out-of-bounds) -> `std::vector` kullan
2. **`new`/`delete` manuel yonetimi**: Smart pointer kullanmamak bellek sizintisina yol acar
   ```cpp
   // Yanlis
   int* ptr = new int(5);
   // delete ptr;  // unutulursa leak
   // Dogru
   auto ptr = std::make_unique<int>(5);
   ```
3. **Dangling pointer**: Silinmis (delete edilmis) bellege erismek -> UB (undefined behavior)
4. **Buffer overflow**: `char dizi[10]; strcpy(dizi, "cok uzun metin");` -> `std::string` kullan
5. **`virtual` destructor unutmak**: Polymorphic base sinifta ~destructor virtual degilse kaynak sizintisi
6. **Include guard eksikligi**: `#pragma once` veya `#ifndef HEADER_H` kullanilmali
7. **Exception safety**: Kaynak alinmisken exception firlatilirsa RAII cozer
8. **Reference vs pointer karistirmak**: Reference yeniden baglanamaz, pointer baglanabilir
9. **Const correctness**: `const` metod icinde sinif degiskenini degistirmek
10. **Implicit conversion**: `explicit` constructor kullanmamak istenmeyen donusumlere yol acar
11. **Uninitialized variable**: `int x; std::cout << x;` -> undefined behavior
12. **Macro kullanimi**: `#define MAX 100` -> `constexpr int MAX = 100;` tercih edilmeli
13. **Iterator invalidation**: Vektor yeniden boyutlandirilirken iterator gecersizlesir

## Performans Ipuclari

1. **Move semantics kullanmak**: Kopyalamadan kacinmak icin `std::move` ve move constructor
   ```cpp
   std::vector<int> buyukVeri(1000000);
   std::vector<int> hedef = std::move(buyukVeri);  // O(1)
   ```

2. **Reserve kullanmak**: Vektor kapasitesini onceden ayirmak (`reserve`)
   ```cpp
   std::vector<int> v;
   v.reserve(1000);  // birden fazla reallocation'u onler
   for (int i = 0; i < 1000; i++) v.push_back(i);
   ```

3. **Pass by reference**: Buyuk nesneleri `const T&` ile gecmek (kopyalamayi onleme)
4. **Small Object Optimization**: Small string vs heap allocation (SSO)
5. **`std::thread` vs `std::async`**: Task-based (async) thread-based'e tercih edilir
6. **Cache locality**: Vector (bitisik bellek) vs list (daginik) erisim hizi
7. **Constexpr / Consteval**: Derleme zamani hesaplamalari (C++17/C++20)
8. **RVO/NRVO**: Return value optimization dogal olarak compile edilmeli

```cpp
// constexpr compile-time hesaplama
constexpr int faktoriyel(int n) {
    return n <= 1 ? 1 : n * faktoriyel(n - 1);
}
constexpr int sonuc = faktoriyel(5); // compile time
```

## Ekosistem

**Derleyiciler**: GCC (G++), Clang (LLVM), MSVC (Visual Studio), Intel C++, MinGW

**Build Sistemleri**: CMake (standart), Bazel, Meson, Ninja, Make, MSBuild

**Paket Yoneticileri**: vcpkg (Microsoft), Conan, Hunter, CPM

**IDE**: Visual Studio, CLion (JetBrains), Qt Creator, VS Code + C++ extension, Code::Blocks

**Test**: Google Test, Catch2, Boost.Test, doctest

**Static/Lint**: Clang-Tidy, Cppcheck, PVS-Studio, Clang Static Analyzer

**Formatlama**: clang-format, Artistic Style

**Profiler**: Valgrind (Linux), perf, VTune (Intel), Very Sleepy (Windows)

**Dokumantasyon**: Doxygen, Sphinx + Breathe

**Standard**: C++98, C++11, C++14, C++17, C++20, C++23 (en guncel)

## Kaynaklar

**Resmi Dokuman**: isocpp.org, en.cppreference.com (Turkiye'den w/cpp)

**Kitaplar**:
- The C++ Programming Language (Bjarne Stroustrup - yaratici)
- Effective Modern C++ (Scott Meyers)
- C++ Primer (Stanley Lippman)
- A Tour of C++ (Bjarne Stroustrup)
- Clean C++ (Stephan Roth)

**Web Siteleri**:
- learncpp.com - Kapsamli ucretsiz C++ egitimi
- cppreference.com - En kapsamli C++ referans
- isocpp.org - Standart C++ sitesi
- hackingcpp.com - Gorsel C++ egitimi

**Interaktif Ogrenme**:
- exercism.org/tracks/cpp
- codewars.com
- leetcode.com
- codeforces.com (Algoritma yarismalari)

**Topluluk**: reddit.com/r/cpp, isocpp.org/forums, CppCon (yillik konferans), C++ User Groups, Stack Overflow
