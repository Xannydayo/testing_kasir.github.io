class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Toko:
    def __init__(self):
        self.daftar_produk = []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)

    def lihat_daftar_produk(self):
        for i, produk in enumerate(self.daftar_produk, 1):
            print(f"{i}. {produk.nama} - Rp {produk.harga:.2f}")

    def hitung_total(self, keranjang):
        total = 0
        for item in keranjang:
            total += item.harga
        return total

    def cetak_struk(self, keranjang, total):
        print("\n===== Struk Pembelian =====")
        for item in keranjang:
            print(f"{item.nama} - Rp {item.harga:.2f}")
        print("==========================")
        print(f"Total Pembelian: Rp {total:.2f}")
        print("==========================\n")

def main():
    toko = Toko()

    # Menambahkan beberapa produk ke dalam daftar produk
    produk1 = Produk("Buku", 25.0)
    produk2 = Produk("Pensil", 5.0)
    produk3 = Produk("Penggaris", 10.0)

    toko.tambah_produk(produk1)
    toko.tambah_produk(produk2)
    toko.tambah_produk(produk3)

    keranjang = []

    while True:
        print("===== Toko Online =====")
        toko.lihat_daftar_produk()
        print("0. Selesai Belanja")
        print("========================")
        
        pilihan = input("Pilih produk (nomor): ")

        if pilihan == "0":
            break
        elif pilihan.isdigit() and 1 <= int(pilihan) <= len(toko.daftar_produk):
            produk_terpilih = toko.daftar_produk[int(pilihan) - 1]
            keranjang.append(produk_terpilih)
            print(f"{produk_terpilih} telah ditambahkan ke keranjang.")
        else:
            print("Pilihan tidak valid.")

    total_pembelian = toko.hitung_total(keranjang)
    toko.cetak_struk(keranjang, total_pembelian)
    print("Terima kasih telah berbelanja di Toko Online!")

if __name__ == "__main__":
    main()
