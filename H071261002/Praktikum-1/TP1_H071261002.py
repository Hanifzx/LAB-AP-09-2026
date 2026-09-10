# Laporan Penjualan "Kopi Senja"
# Data yang diketahui
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]
 
# 1. Hitung subtotal masing-masing minuman
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]
 
# 2. Masukkan subtotal ke dalam list
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]
 
# 3. Menghitung total seluruh pendapatan dan pendapatan bersih
BIAYA_OPERASIONAL = 15000
total_seluruh = sum(subtotal_pendapatan)
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL
 
# 4. Menghitung jumlah barang terjual dan target
jumlah_barang_terjual = sum(jumlah)
target_tercapai = total_seluruh > 200000 and jumlah_barang_terjual > 10
 
# Tampilan Akhir
print(" LAPORAN PENJUALAN KOPI SENJA ")
for i in range(len(menu)):
    print(f"{menu[i]:12}: Rp{harga[i]:,} x {jumlah[i]} = Rp{subtotal_pendapatan[i]:,}")
 
print("-----------------------------------------")
print(f"Total Pendapatan Kotor : Rp{total_seluruh:,}")
print(f"Biaya Operasional      : Rp{BIAYA_OPERASIONAL:,}")
print(f"Pendapatan Bersih      : Rp{pendapatan_bersih:,}")
print("-----------------------------------------")
print(f"Jumlah Barang Terjual  : {jumlah_barang_terjual}")
print(f"Target Tercapai        : {target_tercapai}")