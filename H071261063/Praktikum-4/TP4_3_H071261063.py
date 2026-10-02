def PM(detik):
    if detik == 0:
        print("Luncurkan!")
    else:
        print(detik)
        PM(detik - 1)

while True:
    try:
        angka = int(input("Masukkan angka awal hitung mundur: "))
        if angka >= 0:
            break
        else:
            print("Input tidak valid, angka tidak boleh negatif")
            continue
    except:
        print("Input tidak valid, angka tidak boleh negatif")
PM(angka)