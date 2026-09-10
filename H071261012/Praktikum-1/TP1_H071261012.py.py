# ===== Laporan Penjualan "Kopi Senja" ===== 

# Data awal
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# 1. Subtotal untuk masing-masing produk
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]
var = harga [2] * jumlah [1]
# 2. Masukkan ketiga subtotal ke dalam satu list
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

# 3. Hitung total seluruh pendapatan dan pendapatan bersih
total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

# 4. Hitung jumlah barang terjual dan cek apakah target tercapai
jumlah_barang_terjual = sum(jumlah)
target_tercapai = total_seluruh > 200000 and jumlah_barang_terjual > 10

# Hasil
print("Subtotal:", subtotal_pendapatan)
print("Pendapatan Bersih:", pendapatan_bersih)
print("Target Tercapai:", target_tercapai)  
print("hasil", var)