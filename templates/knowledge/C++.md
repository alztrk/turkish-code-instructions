# C++ Bilgi Referansi

## Genel Bakis
C++, Bjarne Stroustrup tarafindan 1985'te C diline nesne yonelimli programlama eklenerek olusturulmustur. Yuksek performansli uygulamalar, oyun gelistirme (Unreal Engine), gomulu sistemler ve isletim sistemlerinde kullanilir. Dogrudan bellekle calisma imkani saglar.

## Temel Syntax

```cpp
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::string isim = "Ali"; int yas = 25;
    bool aktif = true;

    auto merhaba = [](std::string kisi) {
        return "Merhaba, " + kisi + "!";
    };

    if (yas >= 18) std::cout << "Yetiskin" << std::endl;

    for (int i = 0; i < 5; i++) std::cout << i << std::endl;

    std::vector<std::string> meyveler = {"elma", "armut"};
    meyveler.push_back("muz");
}
```

## Yaygin Patternler

- **RAII**: Kaynak yonetimi (constructor/destructor)
- **Smart Pointers**: `unique_ptr`, `shared_ptr`, `weak_ptr`
- **STL Algoritmalari**: `sort`, `find`, `transform`
- **Move Semantics**: `std::move`, rvalue referanslari
- **Lambda**: `[capture](params) { body }`
- **Const Correctness**: Mumkunse `const` kullanmak

## Onemli Kutuphaneler

- **STL (Standard Template Library)**: Container, iterator, algoritma
- **Boost**: Genis kapsamli yardimci kutuphane
- **Qt**: GUI frameworku
- **OpenCV**: Goruntu isleme
- **Catch2/Google Test**: Test frameworkleri
- **POCO**: Ag ve sunucu uygulamalari
- **nlohmann/json**: JSON isleme

## Yaygin Hatalar

- Pointer aritmetigi ile bellek hatalari
- `new`/`delete` manuel yonetimi (smart pointer kullanmamak)
- Dangling pointer (silinmis bellege erisim)
- Buffer overflow (dizi sinirlari)
- `virtual` destructor unutmak (kalitimda)
- Include guard eksikligi (`#pragma once`)
