print ("Menghitung Kembalian")

Makanan = int (input("Harga makanan sebesar Rp : "))
Snack = int (input("Harga snack sebesar Rp : "))
Minuman = int (input("Harga minuman sebesar Rp : "))
UangAndi = int(input("Uang yang dibawa Andi adalah Rp : "))

total = (Makanan+Snack+Minuman)
print("Harga totalnya adalah", total)

kembalian = str(UangAndi-total)
utang = str(total-UangAndi)

if total == 10000:
    print ("Uang anda pas! Tidak ada kembalian dan utang :D")
elif total > 10000:
    print ("Uang anda kurang! Anda memiliki utang sebesar Rp" + utang)
else:
    print ("Anda memiliki kembalian sebesar Rp" + kembalian)



