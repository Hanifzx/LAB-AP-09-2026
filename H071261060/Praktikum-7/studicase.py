import os
folder_saat_ini = os.path.dirname(os.path.abspath(__file__))
file_nya = os.path.join(folder_saat_ini, "daftar_tugas.txt")

print("--- BUAT DAFTAR TUGAS ---")
tugas_pertama = input("Masukkan tugas pertama: ")
print("[Sistem] File tugas berhasil dibuat!\n")

with open(file_nya, "w") as a:
    a.write(f"{tugas_pertama}\n")

print("--- TAMBAH TUGAS LAIN ---")
tugas_kedua = input("Masukkan tugas tamabahan: ")
print("[Sistem] Tugas berhasil dibuat!\n")

with open(file_nya, "a") as b:
    b.write(f"{tugas_kedua}\n")

with open(file_nya, "r") as r:
    isi = r.read()
    print("--- DAFTAR KESELURUHAN TUGAS ---\n")
    print(isi + "\n")

with open(file_nya, "r") as p:
    isinya = p.read(10)
    print("--- 10 KARAKTER PERTAMA ---\n")
    print(isinya + "\n")


print("--- PENYELESAIAN TUGAS ---")
os.rename(file_nya, "tugas_selesai.txt")
print("[Sistem] Nama file berhasil diubah menjadi tugas_selesai.txt.")
hapus_file = input("[Sistem] Konfirmasi hapus file? (y): ")
if hapus_file == "y":
    os.remove("tugas_selesai.txt")
    print("[Sistem] File tugas telah dihapus. Selamat beristirahat!")
else:
    print("Selesai")