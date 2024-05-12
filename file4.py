"""
conditional if ... elif ... else
"""


saldo = 1000

tarik_tunai = input("Tarik Tunai : ")

try:
    tarik_tunai = int(tarik_tunai)
    print("=================================")
    if tarik_tunai > saldo:
        print("saldo tidak cukup") 
    elif tarik_tunai >= 10:
        print("saldo awal :", saldo)
        print("tarik tunai :", tarik_tunai)
        print("saldo akhir :", saldo-tarik_tunai)
    else:
        print("minimum penarikan 10 $") 
    print("=================================")

except Exception:
    print("angka tidak valid")
