# SQL Bilgi Referansi

## Genel Bakis
SQL (Structured Query Language), 1970'lerde IBM'de gelistirilmis, veritabanlarini yonetmek icin kullanilan bir dildir. Veri sorgulama, ekleme, guncelleme ve silme (CRUD) islemleri icin standarttir. MySQL, PostgreSQL, SQLite, MSSQL gibi bircok veritabani SQL kullanir.

## Temel Syntax

```sql
CREATE TABLE ogrenciler (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ad VARCHAR(100) NOT NULL,
    yas INT CHECK (yas > 0)
);

INSERT INTO ogrenciler (ad, yas) VALUES ('Ali', 20);

SELECT ad, yas FROM ogrenciler WHERE yas > 18 ORDER BY yas DESC LIMIT 10;

UPDATE ogrenciler SET ad = 'Veli' WHERE id = 1;

DELETE FROM ogrenciler WHERE id = 1;

SELECT o.ad, d.bolum_adi FROM ogrenciler o JOIN bolumler d ON o.bolum_id = d.id;
```

## Yaygin Patternler

- **JOIN**: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`
- **GROUP BY + HAVING**: `SELECT bolum, COUNT(*) FROM ogrenciler GROUP BY bolum HAVING COUNT(*) > 5`
- **Subquery**: Ic ice sorgular
- **Indexing**: `CREATE INDEX idx_ad ON ogrenciler(ad);`
- **Transaction**: `BEGIN TRANSACTION ... COMMIT/ROLLBACK`
- **CTE (WITH)**: `WITH gecici AS (SELECT ...) SELECT ... FROM gecici`

## Onemli Kutuphaneler/Moduller

- **PostgreSQL**: ACID uyumlu, gelismis ozellikler
- **MySQL/MariaDB**: Populer web veritabani
- **SQLite**: Hafif, embedded veritabani
- **MSSQL**: Microsoft'un veritabani cozumu
- **ORM'ler**: SQLAlchemy (Python), Prisma (TS), Hibernate (Java)
- **Migration araclari**: Alembic, Flyway, Liquibase

## Yaygin Hatalar

- `SELECT *` kullanmak (gereksiz sutun)
- Index eklememek (yavas sorgu)
- SQL injection (parametreli sorgu kullanmamak)
- `NULL` karsilastirmalarinda `= NULL` yapmak (`IS NULL` kullanilmali)
- N+1 sorgu problemi (JOIN ile cozulur)
- Transaction yonetimini unutmak
