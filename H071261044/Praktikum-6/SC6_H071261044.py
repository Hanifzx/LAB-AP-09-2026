#STUDY CASE
waktu = ("Senin", "23:00")
tersangka = ["Andi", "Budi", "Citra"]
tersangka.remove("Budi")
tersangka.append("Dina")
tersangka_baru = (tersangka)
bukti_tkp = {"Rambut", "Jejak Sepatu", "Kacamata"}
barang_dina = {"Buku", "Jejak Sepatu", "Pena"}
status = {"Andi": "Aman", "Citra": "Aman", "Dina": "Aman"}

print(f"Jam Kejadian: {waktu[1]}")
print(f"Daftar tersangka baru: {tersangka_baru}")
print(f"Bukti yang memberatkan Dina: {bukti_tkp.intersection(barang_dina)}")
print(f"Status Akhir: {status}")