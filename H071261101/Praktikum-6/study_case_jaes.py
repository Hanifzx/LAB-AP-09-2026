waktu = ("Senin", "23:00")
tersangka = {"Andi", "Budi", "Citra"}
tersangka.add("Dina")
tersangka.remove("Budi")
bukti_TKP = {"Rambut", "Jejak Sepatu", "Kacamata"}
barang_dina = {"Buku", "Jejak Sepatu", "Pena"}
bersalah = bukti_TKP.intersection(barang_dina)
status_akhir = {"Andi":"Aman","Citra":"Aman", "Dina":"Buron"}
status_akhir["Dina"] = "tertangkap"

print("Jam Kejadian:", waktu[1])
print("Daftar tersangka baru:", tersangka)
print("Bukti yang memberatkan Dina:", bersalah)
print("Status Akhir:", status_akhir)