const fs = require('fs');
const entries = [];

function E(instr, code, lang) {
    entries.push({
        instruction: instr,
        response: code.trim(),
        language: lang,
        category: 'project',
        type: 'manual',
        format: 'project'
    });
}

// ========================= PYTHON (150 entries) =========================

E("Basit bir not defteri uygulamasi yap. Kullanici not ekleyebilmeli, silebilmeli ve listeleyebilmeli.",
  "class NotDefteri:\n    def __init__(self):\n        self.notlar = []\n    def not_ekle(self, baslik, icerik):\n        self.notlar.append({'id': len(self.notlar)+1, 'baslik': baslik, 'icerik': icerik})\n        print(f\"'{baslik}' baslikli not eklendi.\")\n    def not_sil(self, not_id):\n        for n in self.notlar:\n            if n['id'] == not_id:\n                self.notlar.remove(n)\n                print(f\"{not_id} numarali not silindi.\")\n                return\n        print('Not bulunamadi.')\n    def not_listele(self):\n        if not self.notlar: print('Henuz not yok.'); return\n        for n in self.notlar:\n            print(f\"[{n['id']}] {n['baslik']}: {n['icerik'][:30]}...\")\n    def not_ara(self, kelime):\n        return [n for n in self.notlar if kelime.lower() in n['baslik'].lower()]\nnd = NotDefteri()\nnd.not_ekle('Alisveris', 'Marketten sut, ekmek, yumurta alinacak')\nnd.not_ekle('Is', 'Proje teslimi 15 Mart')\nnd.not_listele()\nnd.not_sil(1)\nnd.not_listele()",
  "python");

E("JSON dosyasina kaydeden bir not defteri yap. Notlar kalici olarak saklansin.",
  "import json, os\nclass NotDefteriJSON:\n    def __init__(self, dosya='notlar.json'):\n        self.dosya = dosya\n        self.notlar = self.yukle()\n    def yukle(self):\n        try:\n            with open(self.dosya, 'r', encoding='utf-8') as f: return json.load(f)\n        except: return []\n    def kaydet(self):\n        with open(self.dosya, 'w', encoding='utf-8') as f:\n            json.dump(self.notlar, f, ensure_ascii=False, indent=2)\n    def ekle(self, baslik, icerik):\n        self.notlar.append({'id': len(self.notlar)+1, 'baslik': baslik, 'icerik': icerik})\n        self.kaydet()\n    def sil(self, not_id):\n        self.notlar = [n for n in self.notlar if n['id'] != not_id]\n        self.kaydet()\n    def listele(self):\n        if not self.notlar: print('Bos'); return\n        for n in self.notlar: print(f\"[{n['id']}] {n['baslik']}\")\nnd = NotDefteriJSON()\nnd.ekle('Python ogren', 'Decorator konusunu calis')\nnd.ekle('Kitap oku', 'Temiz Kod kitabi')\nnd.listele()",
  "python");

E("Not defterine renk kodlariyla kategorize etme ozelligi ekle.",
  "class KategoriliNot:\n    def __init__(self):\n        self.notlar = []\n    def ekle(self, baslik, icerik, kategori='Genel', renk='#fff'):\n        self.notlar.append({'baslik': baslik, 'icerik': icerik, 'kategori': kategori, 'renk': renk})\n    def kategoriye_gore(self, kategori):\n        return [n for n in self.notlar if n['kategori'] == kategori]\n    def tumunu_listele(self):\n        for n in self.notlar:\n            print(f\"[{n['kategori']}] {n['baslik']} - Renk: {n['renk']}\")\n    def kategorileri_getir(self):\n        return list(set(n['kategori'] for n in self.notlar))\nnd = KategoriliNot()\nnd.ekle('Sunum hazirla', 'Slaytlar', 'Is', '#ff6b6b')\nnd.ekle('Spor yap', '30 dk kosu', 'Saglik', '#51cf66')\nnd.tumunu_listele()",
  "python");

E("Not defterine arama ve filtreleme ekle.",
  "class NotArama:\n    def __init__(self):\n        self.notlar = []\n    def ekle(self, baslik, icerik):\n        self.notlar.append({'baslik': baslik, 'icerik': icerik})\n    def ara(self, sorgu):\n        sorgu = sorgu.lower()\n        return [n for n in self.notlar if sorgu in n['baslik'].lower() or sorgu in n['icerik'].lower()]\n    def filtrele(self, kw):\n        sonuc = self.ara(kw)\n        for n in sonuc:\n            print(f\"{n['baslik']}: {n['icerik'][:50]}\")\n        print(f\"{len(sonuc)} sonuc bulundu.\")\nn = NotArama()\nn.ekle('Python Proje', 'Bir not defteri uygulamasi')\nn.ekle('Django Ogren', 'Web framework hakkinda')\nn.ekle('Proje Plan', 'Proje takvimi')\nn.filtrele('Proje')",
  "python");

E("Not defterine oncelik seviyesi ekle. Notlar yuksek, orta, dusuk oncelikli olabilsin.",
  "class OncelikliNot:\n    ONCELIK = {'yuksek': 3, 'orta': 2, 'dusuk': 1}\n    def __init__(self):\n        self.notlar = []\n    def ekle(self, baslik, icerik, oncelik='orta'):\n        self.notlar.append({'baslik': baslik, 'icerik': icerik, 'oncelik': oncelik, 'puan': self.ONCELIK[oncelik]})\n    def sirali_listele(self):\n        sirali = sorted(self.notlar, key=lambda n: n['puan'], reverse=True)\n        for n in sirali:\n            icon = {'yuksek': '!!!', 'orta': '!!', 'dusuk': '!'}[n['oncelik']]\n            print(f\"{icon} [{n['oncelik'].upper()}] {n['baslik']}\")\n    def oncelige_gore_getir(self, seviye):\n        return [n for n in self.notlar if n['oncelik'] == seviye]\nnd = OncelikliNot()\nnd.ekle('Proje teslim', 'Cuma gunu', 'yuksek')\nnd.ekle('Kitap oku', 'Hafta sonu', 'dusuk')\nnd.sirali_listele()",
  "python");

// More entries will be generated by the script
