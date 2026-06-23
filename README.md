# 🇹🇷 Turkish Code Instructions

> **Türkçe kod açıklama veri seti** — Turkish instruction-code pairs for LLM fine-tuning.

Bu veri seti, Türkçe instruction'lar ile kod çiftlerinden oluşur. Amacı, Türkçe kod üreten/tanıyan modelleri eğitmek için kullanılabilecek kaliteli bir kaynak sağlamaktır.

## 📊 İstatistikler

| Metrik | Değer |
|---|---|
| Toplam örnek | 531 |
| Format sayısı | 7 |
| Dil sayısı | 10 |
| Boyut | 271 KB (JSONL) |

## 📁 Klasör Yapısı

```
├── output/
│   └── dataset.jsonl          # Birleştirilmiş veri seti
├── submissions/               # Tüm manuel batch'ler (kaynak)
├── templates/                 # Pattern template'leri
│   ├── python.json
│   ├── javascript.json
│   ├── typescript.json
│   ├── java.json
│   ├── cpp.json
│   ├── go.json
│   ├── rust.json
│   ├── sql.json
│   ├── web.json
│   ├── algorithms.json
│   └── knowledge/             # Dil bilgi dosyaları
├── dataset_card.json          # HuggingFace metadata
└── README.md
```

## 🎯 Formatlar

| Format | Açıklama | Adet |
|---|---|---|
| `standard` | Instruction → kod | 341 |
| `bug_fix` | Hatalı kod → düzeltilmiş kod | 40 |
| `advanced` | İleri seviye konular | 40 |
| `project` | Proje bazlı (çok fonksiyonlu) | 30 |
| `cross_lang` | Aynı problem, farklı diller | 30 |
| `code_to_desc` | Kod → Türkçe açıklama | 25 |
| `test` | Test yazma | 25 |
| `knowledge` | Kavram açıklamaları | 20 |

## 🛠 Diller

| Dil | Adet |
|---|---|
| Python | 142 |
| JavaScript | 84 |
| Java | 67 |
| Go | 43 |
| SQL | 43 |
| TypeScript | 42 |
| Web (HTML/CSS) | 32 |
| C++ | 21 |
| Algorithms | 20 |
| Rust | 17 |

## 📝 Kullanım

Bu veri seti özellikle **Türkçe kod üreten modelleri fine-tune etmek** için hazırlanmıştır.

```python
# HuggingFace datasets ile yükleme
from datasets import load_dataset

dataset = load_dataset("json", data_files="output/dataset.jsonl")
print(dataset["train"][0])
```

## 🧠 Veri Türleri

- **Türkçe değişken isimli kodlar**: `toplam`, `sayiListesi`, `kullaniciAdi` gibi
- **Farklı zorluk seviyeleri**: Başlangıçtan ileri seviyeye
- **Gerçek proje senaryoları**: Hesap makinesi, telefon rehberi, yapılacaklar listesi
- **Hata ayıklama**: Hatalı kod + düzeltilmiş kod çiftleri

## 🤝 Katkı

Yeni instruction-code çiftleri eklemek için `submissions/` klasörüne JSON dosyası ekleyin:

```json
{"instruction": "Türkçe instruction", "response": "kod", "language": "python", "category": "manual", "type": "manual"}
```

## 📄 Lisans

MIT
