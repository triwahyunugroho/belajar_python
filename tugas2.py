while True:
    angka = input("masukkan angka : ")
    try:
        angka = int(angka)
        if angka <= 0:
            print("program selesai")
            break

        list_ganjil = []
        list_genap = []

        cek_angka = 1

        while cek_angka <= angka:
            # operator % (modulo, sisa hasil bagi)
            if cek_angka % 2 == 0:
                list_genap.append(cek_angka)
            else:
                list_ganjil.append(cek_angka)
            cek_angka = cek_angka+1

        print("bilangan ganjil dari 1 sampai", angka, "adalah", list_ganjil)
        print("bilangan genap dari 1 sampai", angka, "adalah", list_genap)

    except Exception:
        print("angka tidak valid")