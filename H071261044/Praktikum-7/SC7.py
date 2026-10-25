#Mencatat tugas baru
#Menambahkan tugas lain
#Mengecek daftar
##Menghapus tugas

import os

print("--- BUAT DAFTAR TUGAS ---")
with open("daftar_tugas.txt", "w") as file:
    tugas = input("Masukkan nama tugas: ")
    file.write(tugas + "\n")
print("[Sistem] Tugas berhasil disimpan!")

print("--- TUGAS TAMBAHAN LAIN --- ")
with open("daftar_tugas.txt", "w") as file:
    tambahan = input("Masukkan tugas tambahan: ")
    file.write(tambahan + "\n")
print("[Sistem] Tugas berhasil ditambahkan! ")

print(" --- DAFTAR KESELURUHAN TUGAS ---")
with open("daftar_tugas.txt", "r") as file:
    tugas = file.read()
    print(tugas)

print(" --- 10 karakter pertama --- ")
print(tugas[:11])

print("--- PENYELESAIAN TUGAS ---")
filename = "daftar_tugas.txt"
new_filename = "tugas_selesai.txt"
os.rename(filename, new_filename)
print("[Sistem] Nama file berhasil diubah menjadi", new_filename)
hapus = input("[Sistem] Konfirmasi hapus file? (y): ")
if hapus.lower() == "y":
    os.remove(filename)
    print("File tugas telah dihapus. Selamat beristirahat!")
else:
    print("Input hapus tidak Valid!")


