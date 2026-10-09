def countdown(detik):
    print(detik)
    if detik == 0:
        print("Luncurkan!")
        return
    countdown(detik - 1)

while True:
    try:
        angka = int(input("Masukkan angka awal hitung mundur: "))
        if angka < 0:
            print("Input tidak valid, angka tidak boleh negatif")
            continue
        else:
            break
            
    except:
        print("Input tidak valid, angka tidak boleh negatif")
countdown(angka)