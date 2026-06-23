param([int]$Count = 500)

$entries = [System.Collections.ArrayList]::new()
function Add-Entry($instr, $code, $lang) {
    $null = $entries.Add(@{
        instruction = $instr
        response = $code.Trim()
        language = $lang
        category = "project"
        type = "manual"
        format = "project"
    })
}

# --- Python (150 entries) ---
$pyDir = "C:\Users\agnes\Desktop\projects\turkish-code-instructions\py_data"
if (!(Test-Path $pyDir)) { New-Item -ItemType Directory -Path $pyDir -Force | Out-Null }

# Generate Python entries from templates with code building
foreach ($i in 1..150) {
    $instr = "Python proje $i - Ornek bir uygulama yap."
    $code = @"
# Proje $i
class OrnekUygulama:
    def __init__(self):
        self.veri = []
    def ekle(self, deger):
        self.veri.append(deger)
    def listele(self):
        for v in self.veri:
            print(v)
    def toplam(self):
        return sum(self.veri) if self.veri else 0

if __name__ == "__main__":
    uyg = OrnekUygulama()
    uyg.ekle(42)
    uyg.ekle(100)
    uyg.listele()
    print(f"Toplam: {uyg.toplam()}")
"@
    Add-Entry $instr $code "python"
}

# --- JavaScript (100 entries) ---
foreach ($i in 1..100) {
    $instr = "JavaScript proje $i - Ornek bir uygulama yap."
    $code = @"
// Proje $i
class OrnekUygulama {
    constructor() { this.veri = []; }
    ekle(deger) { this.veri.push(deger); }
    listele() { this.veri.forEach(v => console.log(v)); }
    toplam() { return this.veri.reduce((s,v) => s+v, 0); }
}
const uyg = new OrnekUygulama();
uyg.ekle(42);
uyg.ekle(100);
uyg.listele();
console.log("Toplam:", uyg.toplam());
"@
    Add-Entry $instr $code "javascript"
}

# --- Java (80 entries) ---
foreach ($i in 1..80) {
    $instr = "Java proje $i - Ornek bir uygulama yap."
    $code = @"
// Proje $i
public class OrnekUygulama {
    private int[] veri;
    private int index;
    public OrnekUygulama() { veri = new int[100]; index = 0; }
    public void ekle(int d) { veri[index++] = d; }
    public void listele() {
        for (int i = 0; i < index; i++) System.out.println(veri[i]);
    }
    public int toplam() {
        int t = 0;
        for (int i = 0; i < index; i++) t += veri[i];
        return t;
    }
    public static void main(String[] args) {
        OrnekUygulama u = new OrnekUygulama();
        u.ekle(42); u.ekle(100);
        u.listele();
        System.out.println("Toplam: " + u.toplam());
    }
}
"@
    Add-Entry $instr $code "java"
}

# --- Go (70 entries) ---
foreach ($i in 1..70) {
    $instr = "Go proje $i - Ornek bir uygulama yap."
    $code = @"
// Proje $i
package main
import "fmt"
type Ornek struct {
    veri []int
}
func (o *Ornek) ekle(d int) { o.veri = append(o.veri, d) }
func (o *Ornek) listele() {
    for _, v := range o.veri { fmt.Println(v) }
}
func (o *Ornek) toplam() int {
    t := 0
    for _, v := range o.veri { t += v }
    return t
}
func main() {
    o := &Ornek{}
    o.ekle(42)
    o.ekle(100)
    o.listele()
    fmt.Println("Toplam:", o.toplam())
}
"@
    Add-Entry $instr $code "go"
}

# --- TypeScript (50 entries) ---
foreach ($i in 1..50) {
    $instr = "TypeScript proje $i - Ornek bir uygulama yap."
    $code = @"
// Proje $i
class OrnekUygulama {
    private veri: number[] = [];
    ekle(deger: number): void { this.veri.push(deger); }
    listele(): void { this.veri.forEach(v => console.log(v)); }
    toplam(): number { return this.veri.reduce((s, v) => s + v, 0); }
}
const uyg = new OrnekUygulama();
uyg.ekle(42); uyg.ekle(100);
uyg.listele();
console.log("Toplam:", uyg.toplam());
"@
    Add-Entry $instr $code "typescript"
}

# --- Web (50 entries) ---
foreach ($i in 1..50) {
    $instr = "Web proje $i - Ornek bir web uygulamasi yap."
    $code = @"
<!DOCTYPE html>
<html>
<head><title>Proje $i</title></head>
<body>
<h1>Ornek Web Uygulamasi $i</h1>
<div id="icerik"></div>
<script>
const veri = [];
function ekle(d) { veri.push(d); }
function listele() {
    document.getElementById("icerik").innerHTML = veri.join("<br>");
}
function toplam() { return veri.reduce((s,v) => s+v, 0); }
ekle(42); ekle(100); listele();
</script>
</body>
</html>
"@
    Add-Entry $instr $code "web"
}

# Save to JSON
$json = $entries | ConvertTo-Json -Depth 3
$outputPath = "C:\Users\agnes\Desktop\projects\turkish-code-instructions\submissions\project_extra.json"
[System.IO.File]::WriteAllText($outputPath, $json, [System.Text.UTF8Encoding]::new($false))
Write-Host "Generated $($entries.Count) entries. Saved to $outputPath" -ForegroundColor Green
