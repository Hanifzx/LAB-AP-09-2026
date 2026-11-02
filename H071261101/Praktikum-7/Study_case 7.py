import os

file_lama = "daftar_tugas.txt"
file_baru = "tugas_selesai.txt"

tugas = input("Masukkan satu tugas baru: ")
with open(file_lama, "w")as f:
    f.write(tugas)
    print("[Sistem] File tugas berhasil dibuat")

extra_tugas = input("Masukkan tugas tambahan: ")
with open(file_lama, "a")as f:
    f.write(f"\n{extra_tugas}")
    print("[Sistem] Tugas berhasil ditambahkan")

with open(file_lama, "r")as f:
    data = f.read()
    print(data)

with open(file_lama, "r")as f:
    words = f.read()
    print(words[0:10])

os.rename(file_lama, file_baru)
print(f"nama file berhasil diubah menjadi {file_baru}")

hapus = input("Apakah anda ingin menghapus file? (y/n): ")
if hapus == "y":
    os.remove(file_baru)
    print("File berhasil dihapus")
else:
    print("File tidak dihapus")