menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

BIAYA_OPERASIONAL = 15000
total_seluruh = (sub_kopi + sub_matcha + sub_americano)
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

jumlah_barang = jumlah[0] + jumlah[1] + jumlah[2]
target_tercapai = (total_seluruh > 200000) and (jumlah_barang > 10)

print("== Laporan Penjualan Kopi Senja ==")
print("Subtotal Kopi Susu      :", sub_kopi)
print("Subtotal Matcha Latte   :", sub_matcha)
print("Subtotal Americano      :", sub_americano)
print("Jumlah Barang Terjual   :", jumlah_barang)
print("----------------------------------")
print("Total Pendapatan        :", total_seluruh)
print("Biaya Operasional       :", BIAYA_OPERASIONAL)
print("----------------------------------")
print("Pendapatan Bersih       :", pendapatan_bersih)
print("Target Tercapai         :", target_tercapai)
