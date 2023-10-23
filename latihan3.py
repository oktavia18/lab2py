# input nilai intenger
n = int(input("Masukan nulai n: "))
t = int(input("Masukan nilai t: "))

# cetak nilai variabel
print("variabel n:", n)
print("variabel t:", t)

# cetak hasil operasi kedua variabel dengan format string
print("Hasil penggabungan {1} & {0}: %d".format (n, t) % (n + t))

# konversi nilai variabel
n = int(n)
t = int(t)
print("Hasil penjumlahan {1} + {0}: %d".format(n, t) % (n + t))
print("Hasil pembagian {1} + {0}: %d".format(n, t) % (n / t))