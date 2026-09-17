# CONDITIONAL STATEMENT I

level_pedas = int(input("Masukkan persentase: "))

if level_pedas >= 0 and level_pedas <= 10:
    print("Level Aman")
elif level_pedas >= 11 and level_pedas <= 40:
    print("Level Sedang")
elif level_pedas >= 41 and level_pedas <= 70:
    print("Level Pedas")
elif level_pedas > 70 and level_pedas <= 100:
    print("Level Ekstrem")
else:
    print("invalid")

