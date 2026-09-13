menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

total_barang = sum(jumlah)
total_seluruh = sum(subtotal_pendapatan)

BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

target_tercapai = total_seluruh > 200000 and total_barang > 10

print("total seluruh :", total_seluruh)
print("pendapatan_bersih :", pendapatan_bersih)
print("target_tercapai :", target_tercapai)