# Repositori Tugas Praktikum Algoritma dan Pemrograman 2026 (LAB-AP-9-2026)

Selamat datang di repositori resmi **LAB-AP-9-2026**!

Repositori ini digunakan sebagai tempat pengumpulan tugas praktikum untuk mata kuliah **Algoritma dan Pemrograman tahun 2026**.

Berikut adalah panduan langkah demi langkah untuk mengumpulkan tugas dengan benar menggunakan **Git dan GitHub**.

## Persiapan Awal (Hanya Dilakukan Sekali)

Sebelum mulai mengerjakan tugas, kamu wajib menghubungkan identitas GitHub-mu dengan Git di laptop.

### 1. Buat Akun GitHub

Jika belum memiliki akun GitHub, silakan daftar melalui [GitHub](https://github.com/).

### 2. Download & Install Git

Unduh dan pasang Git melalui [Git](https://git-scm.com/).

### 3. Konfigurasi Git

Buka Terminal (Linux/macOS) atau Git Bash (Windows).

Jalankan dua perintah berikut. Perintah ini dapat dijalankan di folder mana saja.

```bash
git config --global user.name "Username_GitHub_Kamu"
git config --global user.email "Email_Akun_GitHub_Kamu"
```

Ganti `Username_GitHub_Kamu` dan `Email_Akun_GitHub_Kamu` dengan informasi akun GitHub masing-masing.

---

## Tata Cara Pengumpulan Tugas

### Alur Singkat

```text
Fork → Clone → Buat Branch → Buat Folder → Kerjakan Tugas → Commit → Push → Pull Request
```

### 1. Fork Repositori Ini

Di sudut kanan atas halaman repositori, klik tombol **Fork**.

Proses ini akan membuat salinan repositori `LAB-AP-9-2026` ke dalam akun GitHub pribadimu.

### 2. Clone Repositori

Buka Terminal atau Git Bash, kemudian clone repositori hasil fork yang berada di akun GitHub-mu.

```bash
git clone https://github.com/<USERNAME_KAMU>/LAB-AP-9-2026.git
```

Ganti `<USERNAME_KAMU>` dengan username GitHub masing-masing.

### 3. Buat Branch Sesuai NIM

Masuk ke dalam folder repositori yang baru saja di-clone, kemudian buat branch baru menggunakan NIM masing-masing.

```bash
cd LAB-AP-9-2026
git checkout -b H071261xxx
```

Ganti `H071261xxx` dengan NIM masing-masing.

### 4. Buat Struktur Folder Tugas

Buat folder utama menggunakan NIM, kemudian buat folder khusus untuk praktikum ke-n.

Contoh untuk Praktikum 1:

```bash
mkdir H071261xxx
cd H071261xxx
mkdir Praktikum-1
cd Praktikum-1
```

Struktur folder yang dihasilkan:

```text
LAB-AP-9-2026/
└── H071261xxx/
    └── Praktikum-1/
```

### 5. Kerjakan Tugas

Buat dan simpan file kode di dalam folder `Praktikum-1`.

#### Aturan Penamaan File

Format nama file:

```text
TP<n>__<NIM>.py
```

Contoh:

```text
TP1_H071261xxx.py
```

Format tersebut digunakan apabila dalam satu Tugas Praktikum hanya terdapat satu soal atau satu file program.

Jika dalam satu Tugas Praktikum terdapat beberapa soal yang harus dikerjakan secara terpisah, tambahkan nomor soal setelah nomor praktikum:

```text
TP<n>_<noSoal>_<NIM>.py
```

Contoh:

```text
TP2_1_H071261xxx.py
TP2_2_H071261xxx.py
TP2_3_H071261xxx.py
```

Keterangan:

* `TP1` = Tugas Praktikum 1
* `TP2` = Tugas Praktikum 2
* `1`, `2`, `3` = Nomor soal
* `H071261xxx` = NIM praktikan

Contoh struktur folder:

```text
H071261xxx/
├── Praktikum-1/
│   └── TP1_H071261xxx.py
│
└── Praktikum-2/
    ├── TP2_1_H071261xxx.py
    ├── TP2_2_H071261xxx.py
    └── TP2_3_H071261xxx.py
```

Gunakan format tanpa nomor soal jika tugas hanya terdiri dari satu file. Gunakan format dengan nomor soal jika terdapat beberapa soal yang dikerjakan dalam file terpisah.

### 6. Simpan Perubahan ke Git

Setelah kode selesai dan berjalan dengan baik, tambahkan file ke staging area Git menggunakan `git add`, kemudian lakukan commit.

Ada dua cara untuk menambahkan file:

#### Menambahkan satu file secara spesifik

```bash
git add TP1_1_H071261xxx.py
```

#### Menambahkan semua file dalam folder

Jika ingin menambahkan seluruh perubahan:

```bash
git add .
```

Kemudian cek status file:

```bash
git status
```

Pastikan file yang ingin dikirim sudah masuk ke staging area.

Setelah itu, lakukan commit dengan pesan yang jelas:

```bash
git commit -m "Menambahkan jawaban Tugas Praktikum 1 nomor 1"
```

### 7. Push ke GitHub

Kirim branch yang sudah di-commit dari laptop ke repositori GitHub hasil fork.

```bash
git push -u origin H071261xxx
```

Pastikan `H071261xxx` diganti dengan nama branch sesuai NIM masing-masing.

### 8. Buat Pull Request (PR)

Setelah melakukan push, buka kembali repositori hasil fork di GitHub.

Biasanya akan muncul notifikasi **Compare & pull request**.

Klik tombol tersebut untuk membuat **Pull Request** dari branch NIM-mu menuju repositori utama `LAB-AP-9-2026`.

Pull Request akan digunakan oleh asisten untuk memeriksa dan menilai tugas yang telah dikumpulkan.

---

## Struktur Repository

Setiap praktikan wajib mengikuti struktur folder berikut:

```text
LAB-AP-9-2026/
│
├── H071261xxx/
│   │
│   ├── Praktikum-1/
│   │   ├── TP1_1_H071261xxx.py
│   │   ├── TP1_2_H071261xxx.py
│   │   └── ...
│   │
│   ├── Praktikum-2/
│   │   ├── TP2_1_H071261xxx.py
│   │   ├── TP2_2_H071261xxx.py
│   │   └── ...
│   │
│   └── ...
│
└── README.md
```

---

## Tips untuk Praktikan

### Hindari Spasi pada Nama File dan Folder

Jangan menggunakan spasi dalam nama file atau folder.

Salah:

```text
Tugas 1.py
```

Benar:

```text
Tugas_1.py
```

Kamu juga dapat menggunakan tanda hubung (`-`) jika diperlukan.

### Cek Sebelum Commit

Sebelum melakukan commit, selalu jalankan:

```bash
git status
```

Pastikan hanya file yang diperlukan yang akan dikirim.

Hindari mengirim file atau folder yang tidak diperlukan seperti:

```text
.DS_Store
__pycache__/
*.pyc
```

### Pastikan Program Berjalan

Sebelum melakukan `git add`, `commit`, dan `push`, pastikan kode sudah diuji dan dapat dijalankan dengan baik.

---

## Ringkasan Perintah Git

Jika sudah memahami seluruh alurnya, proses pengumpulan tugas secara singkat adalah:

```bash
# Clone repositori hasil fork
git clone https://github.com/<USERNAME_KAMU>/LAB-AP-9-2026.git

# Masuk ke folder repository
cd LAB-AP-9-2026

# Buat branch sesuai NIM
git checkout -b H071261xxx

# Buat folder tugas
mkdir H071261xxx
cd H071261xxx
mkdir Praktikum-1
cd Praktikum-1

# Kerjakan tugas, kemudian tambahkan file
git add TP1_1_H071261xxx.py

# Cek perubahan
git status

# Commit
git commit -m "Menambahkan jawaban Tugas Praktikum 1 nomor 1"

# Push ke GitHub
git push -u origin H071261xxx
```

Setelah itu, buka GitHub dan buat **Pull Request** menuju repositori utama.
