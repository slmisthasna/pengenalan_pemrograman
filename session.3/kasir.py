
harga: int = 15000
jumlah: int = 3

total: int = harga * jumlah
diskon: float = total * 10 / 100
bayar: float = total - diskon

print("=PROGRAM KASIR=")
print("Harga  : Rp", harga)
print("Jumlah :", jumlah)
print("Total  : Rp", total)
print("Diskon : Rp", diskon)
print("Bayar  : Rp", bayar)