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

// Generate Python entries using template approach
function py(template) {
    const { instr, className, methods, testCode } = template;
    let code = `class ${className}:\n    def __init__(self):\n`;
    // Add init
    code += methods.init ? `        ${methods.init}\n` : '        pass\n';
    // Add methods
    for (const [name, body] of Object.entries(methods)) {
        if (name === 'init') continue;
        const [params, ...lines] = body.split('|');
        code += `    def ${name}(${params}):\n`;
        for (const line of lines) {
            code += `        ${line}\n`;
        }
    }
    code += `\n${testCode}`;
    E(instr, code, 'python');
}

// Python entries array
const pyEntries = [
    // Not defteri
    {instr: 'Basit bir not defteri uygulamasi yap.', className: 'NotDefteri', methods: {init: 'self.notlar = []', ekle: 'self, baslik, icerik|self.notlar.append({"id": len(self.notlar)+1, "baslik": baslik, "icerik": icerik})|print(f"Eklendi: {baslik}")', sil: 'self, not_id|self.notlar = [n for n in self.notlar if n["id"] != not_id]|print(f"Silindi: {not_id}")', listele: 'self|if not self.notlar: print("Bos"); return|[print(f"[{n[chr(39)+chr(105)+chr(100)+chr(39)]}] {n[chr(39)+chr(98)+chr(97)+chr(115)+chr(108)+chr(105)+chr(107)+chr(39)]}") for n in self.notlar]'}, testCode: 'nd = NotDefteri()\nnd.ekle("Alisveris", "Market")\nnd.ekle("Is", "Proje")\nnd.listele()'},
];

// Actually let me just build entries programmatically with clean strings
const pyCodes = [
    // Not defteri
    ['Basit bir not defteri uygulamasi yap. Kullanici not ekleyebilmeli, silebilmeli.',
     'class NotDefteri:\n  def __init__(self): self.notlar = []\n  def ekle(self,b,i): self.notlar.append({"id":len(self.notlar)+1,"baslik":b,"icerik":i})\n  def sil(self,i): self.notlar=[n for n in self.notlar if n["id"]!=i]\n  def listele(self):\n    if not self.notlar: print("Bos"); return\n    for n in self.notlar: print(f"[{n[chr(39)+chr(105)+chr(100)+chr(39)]}] {n[chr(39)+chr(98)+chr(97)+chr(115)+chr(108)+chr(105)+chr(107)+chr(39)]}")\nn=NotDefteri()\nn.ekle("A","B"); n.listele()'],

    ['Yapilacaklar listesi uygulamasi yap. Gorev ekle, tamamla, sil.',
     'class Yapilacak:\n  def __init__(self): self.g=[]\n  def ekle(self,b): self.g.append({"id":len(self.g)+1,"b":b,"t":False})\n  def tamamla(self,i):\n    for g in self.g:\n      if g["id"]==i: g["t"]=True; return\n  def sil(self,i): self.g=[g for g in self.g if g["id"]!=i]\n  def listele(self):\n    for g in self.g: print(f"{\"[X]\" if g[\"t\"] else \"[ ]\"} {g[\"b\"]}")\nt=Yapilacak(); t.ekle("M"); t.ekle("P"); t.tamamla(1); t.listele()'],

    ['Hesap makinesi yap. Toplama, cikarma, carpma, bolme.',
     'class Hesap:\n  def __init__(self): self.s=0\n  def t(self,a,b): self.s=a+b; return self.s\n  def c(self,a,b): self.s=a-b; return self.s\n  def p(self,a,b): self.s=a*b; return self.s\n  def b(self,a,b):\n    if b==0: return "Hata"\n    self.s=a/b; return self.s\nh=Hesap()\nprint(h.t(10,5),h.c(10,5),h.p(3,4),h.b(10,2))'],

    ['Telefon rehberi yap. Kisi ekle, sil, ara, listele.',
     'class Rehber:\n  def __init__(self): self.k={}\n  def ekle(self,i,t): self.k[i]=t\n  def sil(self,i): del self.k[i]\n  def ara(self,kw): return {k:v for k,v in self.k.items() if kw.lower() in k.lower()}\n  def listele(self):\n    for i,t in sorted(self.k.items()): print(f"{i}: {t}")\nr=Rehber(); r.ekle("Ahmet","0532"); r.ekle("Ayse","0533"); r.listele()'],

    ['Alisveris sepeti yap. Urun ekle, cikar, toplam hesapla.',
     'class Sepet:\n  def __init__(self): self.u={}\n  def ekle(self,a,f,m=1): self.u[a]=self.u.get(a,{"f":f,"m":0}); self.u[a]["m"]+=m\n  def cikar(self,a,m=1):\n    if a in self.u:\n      if self.u[a]["m"]<=m: del self.u[a]\n      else: self.u[a]["m"]-=m\n  def toplam(self): return sum(v["f"]*v["m"] for v in self.u.values())\n  def listele(self):\n    for a,u in self.u.items(): print(f"{a}: {u[chr(39)+chr(109)+chr(39)]}x{u[chr(39)+chr(102)+chr(39)]}")\ns=Sepet(); s.ekle("E",10,2); s.ekle("S",35,1); s.listele()'],

    ['Sayi tahmin oyunu yap. Bilgisayar 1-100 arasi sayi tutsun.',
     'import random\nclass Tahmin:\n  def __init__(self): self.h=random.randint(1,100); self.d=0\n  def t(self,s):\n    self.d+=1\n    if s==self.h: return f"Bildin! {self.d}"\n    return "Yuksek!" if s<self.h else "Dusuk!"\n  def oyna(self):\n    for i in range(10):\n      s=int(input(f"[{i+1}/10]: ")); print(self.t(s))\n      if s==self.h: return\nTahmin().oyna()'],

    ['Quiz uygulamasi yap. Sorulari listede tut, puan hesapla.',
     'class Quiz:\n  def __init__(self):\n    self.q=[{"s":"Py yaraticisi?","c":0,"s":["Guido","Linus","Bjarne"]}]\n    self.p=0\n  def baslat(self):\n    for q in self.q:\n      print(q["s"])\n      for j,s in enumerate(q["s"],1): print(f" {j}.{s}")\n      if int(input(": "))-1==q["c"]: self.p+=10; print("Dogru!")\n      else: print(f"Yanlis!{q[chr(39)+chr(115)+chr(39)][q[chr(39)+chr(99)+chr(39)]]}")\n    print(f"Puan:{self.p}")\nQuiz().baslat()'],

    ['Sifre yoneticisi yap. Kullanici adi, sifre, URL sakla.',
     'import json\nclass SifreYon:\n  def __init__(self,d="s.json"): self.d=d; self.v=json.load(open(self.d)) if __import__("os").path.exists(self.d) else []\n  def kaydet(self): json.dump(self.v,open(self.d,"w"),indent=2)\n  def ekle(self,s,k,sf): self.v.append({"s":s,"k":k,"sf":sf}); self.kaydet()\n  def getir(self,s): return [v for v in self.v if s in v["s"]]\n  def listele(self): [print(f"{x[chr(39)+chr(115)+chr(39)]}: {x[chr(39)+chr(107)+chr(39)]} ***") for x in self.v]\nsy=SifreYon(); sy.ekle("github","u1","s1"); sy.listele()'],

    ['Ogrenci not sistemi yap. Ogrenci ekle, not gir, ortalama hesapla.',
     'class ON:\n  def __init__(self): self.o={}\n  def ekle(self,n,i): self.o[n]={"i":i,"n":[]}\n  def ne(self,n,d,p): self.o[n]["n"].append({"d":d,"p":p})\n  def ort(self,n): t=self.o[n]["n"]; return sum(x["p"] for x in t)/len(t) if t else 0\n  def list(self):\n    for n,o in self.o.items():\n      r=self.ort(n); print(f"{n}:{o[chr(39)+chr(105)+chr(39)]}-{r:.1f}-{\"GECTI\" if r>=60 else \"KALDI\"}")\no=ON(); o.ekle("101","A"); o.ne("101","M",85); o.list()'],

    ['Film rehberi yap. Film adi, yil, tur, puan bilgilerini tut.',
     'class FR:\n  def __init__(self): self.f=[]\n  def ekle(self,a,y,t,p): self.f.append({"a":a,"y":y,"t":t,"p":p})\n  def ara(self,k): return [f for f in self.f if k.lower() in f["a"].lower()]\n  def en_iyi(self,n=3): return sorted(self.f,key=lambda f:f["p"],reverse=True)[:n]\n  def list(self):\n    for f in sorted(self.f,key=lambda x:x["y"]): print(f"{f[chr(39)+chr(121)+chr(39)]} {f[chr(39)+chr(97)+chr(39)]} {f[chr(39)+chr(116)+chr(39)]} {f[chr(39)+chr(112)+chr(39)]}/10")\nfr=FR(); fr.ekle("EB",1994,"D",9.3); fr.ekle("Inc",2010,"BK",8.8); fr.list()'],

    ['Gelir gider takibi yap. Gelir ve gider ekle, kategori bazli ozet.',
     'class GG:\n  def __init__(self): self.i=[]\n  def gelir(self,m,k): self.i.append({"t":"g","m":m,"k":k})\n  def gider(self,m,k): self.i.append({"t":"d","m":m,"k":k})\n  def bakiye(self): return sum(x["m"] if x["t"]=="g" else -x["m"] for x in self.i)\n  def kat_ozet(self):\n    o={}\n    for x in self.i: o[x["k"]]=o.get(x["k"],0)+(x["m"] if x["t"]=="g" else -x["m"])\n    return o\n  def list(self):\n    for x in self.i: print(f"{\"+\" if x[\"t\"]==\"gelir\" else \"-\"}{x[\"m\"]} [{x[\"k\"]}]")\ng=GG(); g.gelir(5000,"M"); g.gider(1500,"K"); g.list()'],

    ['Kullanici giris sistemi yap. Kayit ol ve giris yap.',
     'import hashlib\nclass KG:\n  def __init__(self): self.k={}\n  def kayit(self,k,s): self.k[k]=hashlib.sha256(s.encode()).hexdigest()\n  def giris(self,k,s): return k in self.k and self.k[k]==hashlib.sha256(s.encode()).hexdigest()\nkg=KG(); kg.kayit("admin","123"); print(kg.giris("admin","123"))'],

    ['Rastgele sifre olusturucu yap. Uzunluk ve karakter turleri secilebilsin.',
     'import random, string\nclass SU:\n  @staticmethod\n  def ol(uz=12,k=True,b=True,r=True,s=True):\n    h=""\n    if k: h+=string.ascii_lowercase\n    if b: h+=string.ascii_uppercase\n    if r: h+=string.digits\n    if s: h+="!@#$%^&*"\n    return "".join(random.choice(h) for _ in range(uz))\nprint(SU.ol(12)); print(SU.ol(16))'],

    ['Dosya duzenleyici yap. Klasordeki dosyalari listele, ara.',
     'import os, datetime\nclass DD:\n  def __init__(self,y="."): self.y=y\n  def list(self,t=None):\n    for d in os.listdir(self.y):\n      if t and not d.endswith(t): continue\n      b=os.path.getsize(os.path.join(self.y,d)); m=os.path.getmtime(os.path.join(self.y,d))\n      print(f"{b} {datetime.datetime.fromtimestamp(m).strftime(\"%d.%m.%Y\")} {d}")\ndd=DD("."); dd.list(".py")'],
];

for (const [instr, code] of pyCodes) {
    E(instr, code, 'python');
}

// Continue with remaining entries using the same pattern...
// I need to reach 150 Python, then do JS, Java, Go, TS, Web

// For now, let's generate what we have and save
const outputPath = 'C:\\Users\\agnes\\Desktop\\projects\\turkish-code-instructions\\submissions\\project_extra.json';
fs.writeFileSync(outputPath, JSON.stringify(entries, null, 2), 'utf8');
console.log(`Generated ${entries.length} entries. Saved to ${outputPath}`);
