import sys
total = []

print("--------------------------")
print("KASIR BSI")
print("-------------------------------")

def daftar_barang():
    print(" No | Nama Barang | Harga")
    print("-------------------------------")
    print(" 1  | rinso       | 23000")
    print(" 2  | beras       | 65000")
    print(" 3  | tepung      | 19000")
    print(" 4  | whiskas     | 17000")
    print(" 5  | minyak      | 29000")
    print("-------------------------------")
    kode = int(input("Masukkan angka depan barang  : "))
    if kode == 1:
        nama = 'rinso'
        jumlah1 = int(input("Masukkan jumlah barang : "))
        total1 = 23000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        nama2 = 'beras'
        jumlah2 = int(input("Masukkan jumlah barang : "))
        total2 = 65000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        nama3 = 'tepung'
        jumlah3 = int(input("Masukkan jumlah barang : "))
        total3 = 19000 * jumlah3 
        total.append(total3)
        tanya()
    elif kode == 4:
        nama4 = 'whiskas'
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 17000 * jumlah4
        print('makanan kucing merk',nama4)
        total.append(total4)
        tanya()
    elif kode == 5:
        nama5 = 'minyak'
        jumlah5 = int(input("Masukkan jumlah barang : "))
        total5 = 29000 * jumlah5  
        print(nama5,'goreng 2 liter')
        total.append(nama)
        tanya()
    return

def tanya():
    print("\n-------------------------------")
    tanya = input("Ingin tambah barang? [y/t] : ")
    print("-------------------------------")
    if tanya == "y":
        daftar_barang()
    elif tanya == "t":
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")

def akhir():
    for harga in total:
        print("SubTotal         : ", sum(total))
        diskon = 0
        a = sum(total)
        if a > 500000:
            diskon = a * 8/100
        elif a > 300000:
            diskon = a * 5/100
        elif a > 200000:
            diskon = a * 3/100
        elif a > 100000:
            diskon = a * 1/100
        else:
            diskon = 0
        print("Potongan Harga   : ", diskon)
        totalakhir = a - diskon
        print('jenis barang     : ', daftar_barang)
        print("Total            : ", totalakhir)
        print("-------------------------------")
        bayar = int(input("Bayar            :  "))
        kembalian = bayar - totalakhir
        print("Kembalian        : ", kembalian)
        print("-------------------------------")
        print("          Terima Kasih         ")
        print("-------------------------------")

daftar_barang()