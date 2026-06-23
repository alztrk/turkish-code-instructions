# SQL Bilgi Referansi

## Genel Bakis

SQL (Structured Query Language), 1970'lerde IBM'de Edgar Codd'un relasyonel veritabani modeli uzerine gelistirilmistir. Ilk olarak SEQUEL (Structured English Query Language) adiyla anilmis, sonra SQL olarak kisaaltilmistir. 1986'da ANSI, 1987'de ISO standardi haline gelmistir.

SQL veritabanlarini yonetmek, sorgulamak ve manipule etmek icin kullanilan bildirimsel (declarative) bir dildir. MySQL, PostgreSQL, SQLite, Microsoft SQL Server, Oracle Database, MariaDB gibi bircok veritabani yonetim sistemi (DBMS) SQL kullanir. Her DBMS ufak farkliliklar icerse de temel SQL standarttir. SQL gunumuzde veri analizi, raporlama, web uygulamalari, kurumsal sistemler ve buyuk veri platformlarinda temel yapi tasidir.

## Temel Syntax

```sql
-- --- Veritabani Olusturma ---
CREATE DATABASE okul;
USE okul;

-- --- Tablo Olusturma ---
CREATE TABLE ogrenciler (
    id INT PRIMARY KEY AUTO_INCREMENT,
    okul_no VARCHAR(20) UNIQUE NOT NULL,
    ad VARCHAR(100) NOT NULL,
    soyad VARCHAR(100) NOT NULL,
    yas INT CHECK (yas > 0 AND yas < 150),
    bolum_id INT,
    kayit_tarihi DATE DEFAULT CURRENT_DATE,
    not_ortalamasi DECIMAL(3,2) DEFAULT 0.00,
    aktif BOOLEAN DEFAULT true
);

-- --- Veri Ekleme (INSERT) ---
INSERT INTO ogrenciler (okul_no, ad, soyad, yas, bolum_id)
VALUES ('2024001', 'Ali', 'Yilmaz', 20, 1);

INSERT INTO ogrenciler (okul_no, ad, soyad, yas, bolum_id) VALUES
('2024002', 'Ayse', 'Demir', 21, 2),
('2024003', 'Mehmet', 'Celik', 19, 1);

-- --- Tablo Iliski (Foreign Key) ---
CREATE TABLE bolumler (
    id INT PRIMARY KEY AUTO_INCREMENT,
    bolum_adi VARCHAR(100) NOT NULL,
    fakulte_id INT
);

ALTER TABLE ogrenciler
ADD FOREIGN KEY (bolum_id) REFERENCES bolumler(id);

-- --- Temel Sorgulama (SELECT) ---
SELECT * FROM ogrenciler;
SELECT ad, soyad FROM ogrenciler;
SELECT DISTINCT bolum_id FROM ogrenciler;

-- --- Kosullu Sorgu (WHERE) ---
SELECT * FROM ogrenciler WHERE yas > 18;
SELECT * FROM ogrenciler WHERE ad LIKE 'A%';
SELECT * FROM ogrenciler WHERE yas BETWEEN 18 AND 25;
SELECT * FROM ogrenciler WHERE bolum_id IN (1, 2, 3);
SELECT * FROM ogrenciler WHERE ad IS NOT NULL;

-- --- Mantiksal Operatorler ---
SELECT * FROM ogrenciler
WHERE yas > 18 AND bolum_id = 1;

SELECT * FROM ogrenciler
WHERE yas < 20 OR not_ortalamasi > 3.0;

SELECT * FROM ogrenciler
WHERE NOT aktif = false;

-- --- Siralama (ORDER BY) ---
SELECT * FROM ogrenciler ORDER BY yas DESC;
SELECT * FROM ogrenciler ORDER BY soyad ASC, ad ASC;

-- --- Sinirlama (LIMIT/OFFSET) ---
SELECT * FROM ogrenciler LIMIT 10;
SELECT * FROM ogrenciler LIMIT 10 OFFSET 20;  -- sayfalama

-- --- Gruplama (GROUP BY) ---
SELECT bolum_id, COUNT(*) AS ogrenci_sayisi
FROM ogrenciler
GROUP BY bolum_id;

SELECT bolum_id, AVG(yas) AS ortalama_yas, MAX(yas), MIN(yas)
FROM ogrenciler
GROUP BY bolum_id;

-- GROUP BY + HAVING (kosul)
SELECT bolum_id, COUNT(*) AS sayi
FROM ogrenciler
GROUP BY bolum_id
HAVING COUNT(*) > 5;

-- --- JOIN (Tablo Birlestirme) ---
-- INNER JOIN
SELECT o.ad, o.soyad, b.bolum_adi
FROM ogrenciler o
INNER JOIN bolumler b ON o.bolum_id = b.id;

-- LEFT JOIN
SELECT o.ad, b.bolum_adi
FROM ogrenciler o
LEFT JOIN bolumler b ON o.bolum_id = b.id;

-- RIGHT JOIN
SELECT o.ad, b.bolum_adi
FROM ogrenciler o
RIGHT JOIN bolumler b ON o.bolum_id = b.id;

-- Coklu JOIN
SELECT o.ad, b.bolum_adi, f.fakulte_adi
FROM ogrenciler o
JOIN bolumler b ON o.bolum_id = b.id
JOIN fakulteler f ON b.fakulte_id = f.id;

-- --- Alt Sorgu (Subquery) ---
SELECT ad, yas FROM ogrenciler
WHERE yas > (SELECT AVG(yas) FROM ogrenciler);

SELECT ad, soyad FROM ogrenciler
WHERE bolum_id IN (
    SELECT id FROM bolumler WHERE bolum_adi LIKE 'Bilg%'
);

-- EXISTS
SELECT b.bolum_adi FROM bolumler b
WHERE EXISTS (
    SELECT 1 FROM ogrenciler o WHERE o.bolum_id = b.id
);

-- --- CTE (Common Table Expression / WITH) ---
WITH yasli_ogrenciler AS (
    SELECT ad, yas, bolum_id
    FROM ogrenciler
    WHERE yas > 22
)
SELECT y.ad, b.bolum_adi
FROM yasli_ogrenciler y
JOIN bolumler b ON y.bolum_id = b.id;

-- --- Guncelleme (UPDATE) ---
UPDATE ogrenciler
SET ad = 'Veli', soyad = 'Kara'
WHERE id = 1;

-- --- Silme (DELETE) ---
DELETE FROM ogrenciler WHERE id = 1;
DELETE FROM ogrenciler;  -- tabloyu bosalt

-- --- Transaction ---
START TRANSACTION;
UPDATE hesaplar SET bakiye = bakiye - 100 WHERE id = 1;
UPDATE hesaplar SET bakiye = bakiye + 100 WHERE id = 2;
COMMIT;  -- veya ROLLBACK;

-- --- Index Olusturma ---
CREATE INDEX idx_ogrenci_ad ON ogrenciler(ad, soyad);
CREATE UNIQUE INDEX idx_okul_no ON ogrenciler(okul_no);

-- --- View ---
CREATE VIEW ogrenci_bolum_view AS
SELECT o.ad, o.soyad, o.yas, b.bolum_adi
FROM ogrenciler o
JOIN bolumler b ON o.bolum_id = b.id;

-- --- Union ---
SELECT ad FROM ogrenciler
UNION
SELECT ad FROM ogretmenler;

-- --- String Fonksiyonlari ---
SELECT CONCAT(ad, ' ', soyad) AS tam_ad FROM ogrenciler;
SELECT UPPER(ad), LOWER(soyad) FROM ogrenciler;
SELECT LENGTH(ad) FROM ogrenciler;
SELECT SUBSTRING(ad, 1, 3) FROM ogrenciler;

-- --- Tarih Fonksiyonlari ---
SELECT CURRENT_DATE, CURRENT_TIMESTAMP;
SELECT DATE_ADD(kayit_tarihi, INTERVAL 1 YEAR) FROM ogrenciler;
SELECT DATEDIFF(CURRENT_DATE, kayit_tarihi) FROM ogrenciler;

-- --- Aritmetik Fonksiyonlar ---
SELECT COUNT(*), SUM(yas), AVG(yas), MAX(yas), MIN(yas) FROM ogrenciler;
SELECT ROUND(not_ortalamasi, 1) FROM ogrenciler;
```

## Yaygin Patternler

1. **JOIN Cesitleri**: INNER, LEFT, RIGHT, FULL OUTER, CROSS JOIN ile tablo birlestirme
2. **GROUP BY + HAVING**: Gruplama ve gruplar uzerinde kosul
   `SELECT bolum, COUNT(*) FROM ogrenciler GROUP BY bolum HAVING COUNT(*) > 5`
3. **Subquery**: `WHERE ... IN (SELECT ...)` veya `FROM (SELECT ...) AS tmp` ile ic ice sorgu
4. **CTE (WITH)**: Karmasik sorgulari dizi halinde okunabilir yapma
5. **Indexing**: `CREATE INDEX idx_ad ON ogrenciler(ad)` ile sorgu hizlandirma
6. **Transaction**: `BEGIN ... COMMIT/ROLLBACK` ile atomik islem
7. **Pagination**: `LIMIT ? OFFSET ?` veya keyset pagination (`WHERE id > ? LIMIT ?`)
8. **Soft Delete**: `deleted_at` alani ile mantiksal silme
9. **Audit Trail**: `created_at`, `updated_at` alanlari ile degisiklik takibi
10. **JSON Sorgulama**: PostgreSQL/MariaDB'de JSON veri tipinde sorgu
11. **Full-Text Search**: `MATCH ... AGAINST` ile metin arama (MySQL) / `tsvector` (PostgreSQL)
12. **Materialized View**: Ozet sorgularinin onceden hesaplanmasi

```sql
-- Keyset Pagination (buyuk verilerde LIMIT/OFFSET'ten hizli)
SELECT * FROM ogrenciler
WHERE id > 1000
ORDER BY id
LIMIT 20;

-- Soft Delete
UPDATE ogrenciler SET deleted_at = NOW() WHERE id = 1;
SELECT * FROM ogrenciler WHERE deleted_at IS NULL;

-- JSON sorgulama (PostgreSQL)
SELECT * FROM urunler WHERE veri->>'renk' = 'kirmizi';

-- Full-Text Search (MySQL)
SELECT * FROM makaleler
WHERE MATCH(baslik, icerik) AGAINST('programlama' IN BOOLEAN MODE);
```

## Onemli Veritabanlari / Araclar

1. **PostgreSQL**: ACID uyumlu, gelismis JSON/JSONB, full-text search, custom type, extensions
   `SELECT * FROM pg_stat_activity;`
2. **MySQL / MariaDB**: Populer web veritabani (LAMP stack), replikasyon, InnoDB
3. **SQLite**: Embedded, serverless, hafif (mobil, IoT, test)
4. **Microsoft SQL Server (MSSQL)**: Kurumsal, T-SQL, SQL Server Management Studio
5. **Oracle Database**: Kurumsal, PL/SQL, RAC (Real Application Clusters)
6. **MongoDB**: NoSQL dokuman tabanli (SQL degil ama sorgu benzer)
7. **Redis**: In-memory veri yapisi sunucusu (cache, session)
8. **Elasticsearch**: Metin arama ve analitik motoru
9. **DuckDB**: Embedded OLAP veritabani (veri analizi)
10. **SQLAlchemy**: Python ORM
    `session.query(User).filter(User.age > 18).all()`
11. **Prisma**: TypeScript/Node.js ORM
12. **Hibernate / JPA**: Java ORM
13. **Alembic (Python)**: Veritabani migration aracı
14. **Flyway (Java)**: Migration aracı
15. **DBeaver / DataGrip / pgAdmin**: GUI veritabani yonetim araclari
16. **Redis Insight**: Redis GUI

```sql
-- PostgreSQL full-text search
CREATE INDEX idx_makale_arama ON makaleler USING GIN(to_tsvector('turkish', baslik || ' ' || icerik));
SELECT * FROM makaleler WHERE to_tsvector('turkish', baslik) @@ to_tsquery('turkish', 'programlama & dil');

-- SQLAlchemy (Python)
from sqlalchemy import create_engine, text
engine = create_engine('postgresql://user:pass@localhost/veritabani')
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM ogrenciler WHERE yas > :yas"), {"yas": 18})
```

## Yaygin Hatalar

1. **`SELECT *` kullanmak**: Gereksiz sutun cekmek, ag trafigi ve bellek tuketimi, index kullanimini engeller
2. **Index eklememek**: Tablo full scan yavas sorgu, `EXPLAIN ANALYZE` ile kontrol edilmeli
3. **SQL Injection**: Kullanici girdisini direkt sorguya eklemek
   ```sql
   -- Yanlis (guvenlik zaafi)
   "SELECT * FROM kullanicilar WHERE ad = '" + kullaniciAdi + "'"
   -- Dogru
   SELECT * FROM kullanicilar WHERE ad = ?;  -- parameterized query
   ```
4. **`NULL` karsilastirmalarinda `= NULL` kullanmak**: `= NULL` her zaman false, `IS NULL` kullanilmali
5. **N+1 sorgu problemi**: Iliski icin her kayit icin ayri sorgu -> JOIN ile cozulur
6. **Transaction yonetimini unutmak**: Islem yarida kalirsa tutarsiz veri
7. **Implicit type conversion**: `SELECT * FROM tablo WHERE id = '123'` (varchar ile int kiyas)
8. **Buyuk tablolarda DISTINCT**: Benzersiz deger sayisi fazlaysa cok yavas
9. **`HAVING` yerine `WHERE` kullanmamak**: WHERE gruplamadan once filtreler, HAVING gruplamadan sonra
10. **Cascade delete/silinmez (referans kaybi)**: Foreign key cascade ayarlarini unutmak
11. **Parallel sorgu sorunlari**: Deadlock riski (transaction siralamasi onemli)
12. **Backup almamak**: Veritabani yedegi olmamasi felaket senaryosu

## Performans Ipuclari

1. **Index kullanmak**: WHERE, JOIN, ORDER BY sorgularini hizlandirir
   ```sql
   CREATE INDEX idx_ogrenci_yas ON ogrenciler(yas);
   CREATE INDEX idx_bolum ON ogrenciler(bolum_id, yas);  -- composite index
   ```

2. **`EXPLAIN ANALYZE` ile sorgu analizi**: Hangi index kullaniliyor, kac satir taranıyor gorulebilir
3. **Partitioning**: Buyuk tablolari tarih/aralik bazinda bolme
4. **Covering index**: Sadece index uzerinden sorguyu cozme (index-only scan)
5. **Connection Pool**: `pgbouncer`, `HikariCP` ile veritabani baglantisi yonetimi
6. **Batch INSERT**: Tek tek ekleme yerine toplu ekleme
7. **Vacuum / Analyze (PostgreSQL)**: Silinen satirlari temizleme, istatistik guncelleme

```sql
-- EXPLAIN ANALYZE ile sorgu plani
EXPLAIN ANALYZE SELECT * FROM ogrenciler WHERE yas > 18;

-- Batch INSERT (1000 satir tek seferde)
INSERT INTO ogrenciler (okul_no, ad, soyad)
SELECT '2024' || generate_series, 'Ogrenci', 'Test'
FROM generate_series(1, 1000);
```

## Ekosistem

**Veritabani Yonetim Sistemleri**:
- Acik Kaynak: PostgreSQL, MySQL, MariaDB, SQLite, CockroachDB
- Ticari: Oracle, MSSQL, IBM DB2
- Bulut: Amazon RDS/Aurora, Google Cloud SQL, Azure SQL

**ORM'ler**: SQLAlchemy (Python), Prisma (TS/JS), Hibernate (Java), Sequelize (Node.js), Entity Framework (.NET), Diesel (Rust), GORM (Go)

**Migration**: Alembic (Python), Flyway (Java), Liquibase, Prisma Migrate, Goose (Go)

**GUI Araclari**: DBeaver, DataGrip, pgAdmin, MySQL Workbench, TablePlus, HeidiSQL

**Test**: pgTAP, tSQLt

**Monitoring**: pg_stat_statements, pgBadger, MySQL Performance Schema, Grafana + Prometheus

**Bulut Veritabani**: Amazon RDS, Google Cloud Spanner, Azure Cosmos DB, Supabase (PostgreSQL), PlanetScale (MySQL)

## Kaynaklar

**Resmi Dokuman**: postgresql.org/docs, dev.mysql.com/doc, sqlite.org/docs

**Kitaplar**:
- Learning SQL (Alan Beaulieu)
- SQL in 10 Minutes, Sams Teach Yourself (Ben Forta)
- High Performance MySQL
- The Art of PostgreSQL
- SQL Antipatterns (Bill Karwin)

**Web Siteleri**:
- w3schools.com/sql
- sqlbolt.com (interaktif)
- pgexercises.com (PostgreSQL egzersiz)
- leetcode.com (SQL problemleri)

**Interaktif Ogrenme**:
- sqlzoo.net
- hackerrank.com (SQL becerileri)
- stratascratch.com (gercek interview sorulari)
- codecademy.com (SQL kursu)

**Topluluk**: reddit.com/r/SQL, reddit.com/r/PostgreSQL, Stack Overflow SQL etiketi, PostgreSQL Turkey, MySQL Turkey
