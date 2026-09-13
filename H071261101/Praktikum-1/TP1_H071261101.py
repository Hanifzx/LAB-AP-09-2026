# Data penjualan produk
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# Perhitungan subtotal masing-masing item
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

# Penggabungan subtotal 
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

# total P. kotor dan bersih
total_seluruh = sum(subtotal_pendapatan) #pendapatan kotor
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

# Evaluasi pencapaian target penjualan 
total_barang = sum(jumlah)
target_tercapai = total_seluruh > 200000 and total_barang > 10

# output/hasil
print("Subtotal :", subtotal_pendapatan)
print("Pendapatan Bersih :", pendapatan_bersih)
print("Hasil Target :", target_tercapai)