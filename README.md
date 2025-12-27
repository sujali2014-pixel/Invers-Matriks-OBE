# Matrix Inversion using Elementary Row Operations (OBE)

Repositori ini berisi skrip Python untuk menghitung **Invers Matriks 3x3** menggunakan metode **Gauss-Jordan Elimination** atau **Operasi Baris Elementer (OBE)**. Skrip ini memanfaatkan library **NumPy** untuk efisiensi komputasi dan memberikan visualisasi langkah demi langkah proses augmentasi matriks.

## 🚀 Fitur Utama

* **Langkah-Demi-Langkah**: Menampilkan setiap perubahan pada matriks augmented  (Tukar baris, Normalisasi, Eliminasi).
* **Efisiensi NumPy**: Menggunakan teknik *vectorized operations* (seperti `np.hstack` dan *row slicing*) untuk memproses baris tanpa banyak loop manual.
* **Penanganan Matriks Singular**: Dilengkapi pengecekan apakah matriks memiliki invers atau tidak (singular).
* **Input Interaktif**: Memudahkan pengguna memasukkan elemen matriks melalui terminal.

## 🛠️ Prasyarat

Pastikan Anda sudah menginstal Python dan library NumPy di lingkungan Anda:

```bash
pip install numpy

```

## 📋 Cara Penggunaan

1. Clone repositori ini atau download file `INVERS OBE.py`.
2. Jalankan skrip melalui terminal/command prompt:
```bash
python "INVERS OBE.py"

```


3. Masukkan elemen-elemen matriks 3x3 sesuai petunjuk di layar.
4. Program akan menampilkan visualisasi setiap langkah hingga hasil akhir ditemukan.

## 💡 Contoh Logika Program

Skrip ini mentransformasi matriks  menjadi  dengan tiga operasi utama:

1. **Swap**: Menukar baris jika elemen pivot bernilai 0.
2. **Scale**: Membagi baris dengan elemen pivot agar menjadi 1 (Utama).
3. **Eliminate**: Mengurangi baris lain agar elemen di kolom yang sama dengan pivot menjadi 0.

```text
Contoh Output Langkah:
--- Langkah 2: Baris 1 dibagi 2.00 ---
--------------------------------------------------
|   1.00    0.50    1.00  |    0.50    0.00    0.00 |
|   0.00    1.00    2.00  |    0.00    1.00    0.00 |
|   1.00    0.00    1.00  |    0.00    0.00    1.00 |
--------------------------------------------------

```

## 📂 Struktur File

* `INVERS OBE.py`: Kode sumber utama menggunakan Python & NumPy.

---

**Catatan**: Skrip ini dikonfigurasi khusus untuk matriks 3x3, namun logika di dalamnya dapat dengan mudah diadaptasi untuk matriks .
