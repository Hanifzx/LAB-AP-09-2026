def hitung_subtotal (harga, jumlah, adalah_member=False):
    harga_jumlah = harga*jumlah 
    if adalah_member == True:
        harga_jumlah = harga_jumlah * (1 - 0.10)
    return int(harga_jumlah)

print ("Selamat datang di Kasir Minimarket!")
while True:
    status_member = input("Apakah Anda member? (y/n): ")
    if status_member == "y":
        adalah_member = True
        break
    elif status_member == "n":
        adalah_member = False
        break
    else:
        print("Hanya menerima input y/n")
        continue
       

total_belanja = 0
while True:
    try:
        nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
        if nama_barang == "":
            break

        harga_barang = int(input("Harga barang: "))
        jumlah_barang = int(input("Jumlah barang: "))

        if harga_barang <= 0:
            print("Harga tidak valid")
            continue
        
        subtotal = hitung_subtotal(harga_barang, jumlah_barang, adalah_member)
        print(f"Subtotal {nama_barang}: Rp{subtotal}")  
        total_belanja += subtotal
    
    except:
        print("Input tidak valid")
        continue

print(f"Total belanja: Rp{total_belanja}")

