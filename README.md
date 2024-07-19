# Cleaning Data - Dokumentasi Belajar Python

Ini adalah dokumentasi dari hasil belajar `dimasbajuri` jika ada kesalahan, error, atau bug mohon hubungi pemilik akun (masih belajar h3h3)

## Persiapan

Install pandas untuk memulai
```
pip install pandas
```
Pada file Python, import module pandas
```
import pandas as pd
```
Pada dokumentasi kali ini saya menggunakan bad_data.csv sebagai contoh

## Konten

Visualisasi Data:

| Name           | Age    | Date of Birth | Email                    | Score |
|----------------|--------|---------------|--------------------------|-------|
| John Doe       | 28     | 1995-05-12    | johndoe@example.com      | 85    |
| Jane Smith     |        | 1987-08-23    | janesmith@example        | 95    |
| Alice Johnson  | 45     | 1978-07-01    | alice.johnson@example.com| NaN   |
| Bob Brown      | 23     | 1999/12/31    | bob.brown@example.com    | 75    |
| Charlie Davis  | thirty | 1993-04-21    | charlie.davis@example.com| 88    |
| Eve Adams      | 40     | 1983-11-02    | eve.adams@example.com    | 65    |
| John Doe       | 28     | 1995-05-12    | johndoe@example.com      | 85    |
| Mia Lee        | 35     | 1989-13-15    | mia.lee@example.com      | 92    |
| Chris Green    | 38     | 1985-10-10    | chris.green@example.com  | 90    |
| Mark White     | NaN    | 1980-06-20    | mark.white@example.com   | NaN   |

Pada sebuah data terkadang terdapat data yang buruk (Bad Data), berikut kriterianya:
1. Empty Cells (Nilai kosong)
    + Nilai yang hilang atau kosong bisa terjadi karena berbagai alasan, seperti kesalahan input data atau data yang tidak tersedia.
    + Contoh: Kolom Age (baris ke 2 dan 10) dan Score (baris ke 3 dan 10)
2. Data in Wrong Format (Format data yang salah)
    + Data yang seharusnya berada dalam format tertentu, namun tersimpan dalam format yang berbeda.
    + Contoh: Kolom Date of Birth (baris ke 3 dan 8) dan Age (Baris ke 2)
3. Wrong Data (Data yang salah)
    + Data yang secara jelas tidak benar atau tidak masuk akal.
    + Contoh: Kolom Age (baris ke 5)
4. Duplicates (Duplikasi)
    + Baris yang sama muncul lebih dari satu kali dalam dataset.
    + Contoh: Kolom Name (Baris ke 1 dan 7)

Untuk membersikannya ada beberapa cara yang dapat dilakukan:

### 1. Mengganti Nilai Kosong

#### a. Mengisi dengan Nilai Tertentu
Mengisi nilai yang kosong dengan nilai median, mean, atau modus atau nilai sesuka hati. Pengisian data menggunakan method `fillna`  
Berikut contoh mengisi data dengan sesuka hati:
```
data_csv["Age"] = data_csv["Age"].fillna(30)
data_csv["Score"] = data_csv["Score"].fillna(30)
```
Berikut contoh mengisi data dengan mean, median, modus:
```
data_csv["Age"] = data_csv["Age"].fillna(data_csv["Age"].mean())
data_csv["Score"] = data_csv["Score"].fillna(data_csv["Age"].Median())
```
#### b. Mengisi dengan Metode Forward Fill atau Backward Fill
Metode ini menggunakan nilai sebelumnya atau berikutnya dalam kolom untuk mengisi nilai kosong. dengan method `ffill` atau `bfill`
```
data_csv["Age"] = data_csv["Age"].ffill()
data_csv["Score"] = data_csv["Score"].bfill()
```

### 2. Mengganti Format Data yang Salah (Data in Wrong Format)

Bla bla bla... Kita lanjut nanti kalo udah nggak males