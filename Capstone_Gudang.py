#Ini adalah perintah untuk mengimpor pustaka tabulate yang akan digunakan untuk menyajikan data inventaris dalam bentuk tabel.
import tabulate as tb

# Inisialisasi dictionary untuk menyimpan data inventaris yang berisi beberapa dictionary yang merepresentasikan data inventaris, masing-masing memiliki informasi tentang nama barang, jumlah, dan harga.
inventaris_gudang = [
    {'Nama': 'Alat K3', 'Jumlah': 50, 'Harga': 100000},
    {'Nama': 'APAR', 'Jumlah': 20, 'Harga': 500000},
    {'Nama': 'Lanyard', 'Jumlah': 30, 'Harga': 25000},
    {'Nama': 'Helmet Safety', 'Jumlah': 40, 'Harga': 75000},
    {'Nama': 'Safety Glasses', 'Jumlah': 35, 'Harga': 35000},
    {'Nama': 'Ear Plugs', 'Jumlah': 25, 'Harga': 15000},
    {'Nama': 'Gloves', 'Jumlah': 60, 'Harga': 20000},
    {'Nama': 'Safety Shoes', 'Jumlah': 45, 'Harga': 120000},
    {'Nama': 'Reflective Vest', 'Jumlah': 30, 'Harga': 45000},
    {'Nama': 'Safety Harness', 'Jumlah': 15, 'Harga': 95000}
]
# Fungsi ini untuk membuat item baru dalam inventaris dengan memasukkan nama, jumlah, dan harga barang.
# Meminta pengguna untuk memasukkan nama barang melalui fungsi input() dan menyimpannya dalam variabel nama_barang.
# While True:: Memulai loop tak terbatas untuk memvalidasi input jumlah barang.
# try-except digunakan untuk menangani kemungkinan kesalahan saat pengguna memasukkan jumlah barang.
# int(input("Masukkan jumlah barang: ")) mencoba untuk mengonversi input pengguna menjadi tipe data integer. Jika berhasil, nilai akan disimpan dalam variabel jumlah_barang.
# if isinstance(jumlah_barang, int): memeriksa apakah jumlah_barang adalah integer. Jika ya, loop akan dihentikan dengan break.
# Jika pengguna memasukkan sesuatu yang bukan integer, cetak 'Masukkan Angka!' akan ditampilkan dan pengguna diminta untuk memasukkan nilai yang valid.

def create_item():
    nama_barang = input("Masukkan nama barang: ")
    while True:
        try:
            jumlah_barang = int(input("Masukkan jumlah barang: "))
            if isinstance(jumlah_barang,int):
                break
            else:
                print('Masukkan Angka!')
                
        except: print('Masukkan Angka!')

    while True:
        try:
            harga_barang = int(input("Masukkan harga barang: "))
            if isinstance(harga_barang,int):
                break
            else:
                print('Masukkan Angka!')
                
        except: print('Masukkan Angka!')
    

    item_baru = {
        'Nama': nama_barang,
        'Jumlah': jumlah_barang,
        'Harga': harga_barang
    }
# Ini adalah perintah pada saat item baru telah ditambahkan akan masuk ke urutan terakhir dan print "Item berhasil ditambahkan ke inventaris."
    inventaris_gudang.append(item_baru)
    print("Item berhasil ditambahkan ke inventaris.")

# Perintah return ini agar kembali ke inventaris_gudang
    return inventaris_gudang

# Fungsi ini untuk menghapus item dari inventaris berdasarkan nama barang
def delete_item():
    nama_barang = input("Masukkan nama barang yang ingin dihapus: ")

# Ini adalah perintah setelah kita masukkan nama barang berarti Nama, Jumlah, Harga barang akan dihapus. Dan print "berhasil dihapus dari inventaris"
    for item in inventaris_gudang:
        if item['Nama'] == nama_barang:
            inventaris_gudang.remove(item)
            print(f"Barang dengan nama '{nama_barang}' berhasil dihapus dari inventaris.")

# Perintah return ini agar kembali ke inventaris_gudang
            return inventaris_gudang

 # Ini adalah perintah ketika nama barang yang kita masukkan tidak ada di tabel
    print(f"Tidak ada barang dengan nama '{nama_barang}' dalam inventaris.")

# Fungsi untuk memperbarui jumlah atau harga barang dalam inventaris berdasarkan nama barang yang dimasukkan
def update_item():
    nama_barang = input("Masukkan nama barang yang ingin diperbarui: ")

# Ini adalah loop yang akan melakukan iterasi melalui setiap item (barang) dalam inventaris_gudang.
    for item in inventaris_gudang:

# Setiap item dalam inventaris_gudang dicek apakah memiliki atribut 'Nama' yang sama dengan nama_barang yang ingin diperbarui.
# Jika ada barang dengan nama yang sesuai, maka program akan meminta pengguna untuk memilih atribut mana yang ingin diperbarui dengan menampilkan pesan berikut:
# 1.Jumlah Barang : 
# 2.Harga Barang : 
# Kemudian, program akan meminta pengguna untuk memasukkan pilihan (1 atau 2) menggunakan int(input("Masukkan pilihan (1/2): ")).

        if item['Nama'] == nama_barang:
            print("Pilih atribut yang ingin diperbarui:")
            print("1. Jumlah Barang")
            print("2. Harga Barang")
            pilihan = int(input("Masukkan pilihan (1/2): "))

# Jika pilihan == 1, program akan meminta pengguna untuk memasukkan jumlah barang baru menggunakan jumlah_barang = int(input("Masukkan jumlah barang baru: ")). Kemudian, nilai Jumlah dari item tersebut dalam inventaris akan diperbarui.
# Jika pilihan == 2, program akan meminta pengguna untuk memasukkan harga barang baru menggunakan harga_barang = float(input("Masukkan harga barang baru: ")). Kemudian, nilai Harga dari item tersebut dalam inventaris akan diperbarui.
# Jika pengguna memasukkan pilihan lain selain 1 atau 2, program akan mencetak pesan "Pilihan tidak valid."
# Setelah atribut barang berhasil diperbarui, program akan mengembalikan inventaris_gudang, yang kemudian dapat menyimpan perubahan yang telah dilakukan.
# Jika tidak ada barang dengan nama yang sesuai dengan nama_barang di dalam inventaris, program akan mecetak pesan "Tidak ada barang dengan nama '{nama_barang}' dalam inventaris."
            
            if pilihan == 1:
                jumlah_barang = int(input("Masukkan jumlah barang baru: "))
                item['Jumlah'] = jumlah_barang
                print("Jumlah barang berhasil diperbarui.")
            elif pilihan == 2:
                harga_barang = float(input("Masukkan harga barang baru: "))
                item['Harga'] = harga_barang
                print("Harga barang berhasil diperbarui.")
            else:
                print("Pilihan tidak valid.")
            return inventaris_gudang
        
    print(f"Tidak ada barang dengan nama '{nama_barang}' dalam inventaris.")

# Fungsi ini bertujuan untuk menampilkan seluruh inventaris gudang dalam bentuk tabel menggunakan tabulate.
# Selanjutnya, dilakukan pengecekan dengan if not inventaris_gudang: untuk memeriksa apakah inventaris_gudang kosong atau tidak. Jika kosong, akan mencetak pesan "Inventaris kosong.". Ini memberi tahu pengguna bahwa tidak ada barang dalam inventaris jika kondisinya kosong.
# Jika inventaris_gudang tidak kosong, maka akan dilakukan pengolahan untuk menampilkan isi inventaris dalam bentuk tabel.
# Variabel headers adalah sebuah list yang berisi header atau judul kolom-kolom yang akan ditampilkan dalam tabel. Di sini, terdapat empat judul kolom: "No.", "Nama Barang", "Jumlah Barang", dan "Harga Barang".
# Variabel rows digunakan untuk menampung data dari setiap barang dalam bentuk list yang akan ditambahkan ke tabel.
# Dilakukan iterasi melalui setiap item dalam inventaris_gudang menggunakan for idx, item in enumerate(inventaris_gudang, start=1):
# Enumerate() digunakan untuk menghasilkan indeks (idx) dan item dalam list inventaris_gudang. Indeks dimulai dari 1 (start=1).
# Setiap barang (item) yang ditemukan dalam inventaris_gudang akan ditambahkan ke rows dalam bentuk list yang berisi nomor urut (idx), nama barang (item['Nama']), jumlah barang (item['Jumlah']), dan harga barang (item['Harga']).
# Akhirnya, menggunakan fungsi tabulate() untuk mencetak tabel dengan memanfaatkan data yang telah disiapkan dalam rows dan menggunakan headers sebagai judul kolom. 
# tablefmt='grid' digunakan untuk menentukan format tabel yang diinginkan, dalam hal ini menggunakan format grid.

def display_inventory():
    print("Inventaris Gudang:")
    if not inventaris_gudang:
        print("Inventaris kosong.")
    else:
        headers = ["No.", "Nama Barang", "Jumlah Barang", "Harga Barang"]
        rows = []

        for idx, item in enumerate(inventaris_gudang, start=1):
            rows.append([idx, item['Nama'], item['Jumlah'], item['Harga']])

        print(tb.tabulate(rows, headers=headers, tablefmt='grid'))

# Fungsi ini bertujuan untuk menampilkan menu opsi kepada pengguna dan meminta mereka untuk memilih opsi ya4ng diinginkan.

def get_user_choice():
    while True:
        try:
            print("\n===== PT ELEKTRIKA MITRA USAHA =====")
            print("1. Tambah Item")
            print("2. Hapus Item")
            print("3. Perbarui Item")
            print("4. Tampilkan Inventaris")
            print("5. Keluar")

            choice = int(input("Masukkan pilihan (1/2/3/4/5): "))
            
# Menggunakan struktur if-elif-else untuk mengevaluasi pilihan yang dimasukkan pengguna.
# Jika pengguna memilih 1, fungsi create_item() akan dipanggil.
# Jika pengguna memilih 2, fungsi delete_item() akan dipanggil.
# Jika pengguna memilih 3, fungsi update_item() akan dipanggil.
# Jika pengguna memilih 4, fungsi delete_item() akan dipanggil.
# Jika pengguna memilih 5, program akan mencetak 'Terima Kasih' dan loop akan dihentikan dengan break.
# Jika pengguna memasukkan angka diluar rentang 1-5, pesan 'Mohon Masukkan Angka 1-5' akan ditampilkan.
# except: print('Terjadi error.'): Menggunakan blok except untuk menangani kesalahan yang mungkin terjadi selama eksekusi program,
# mencetak pesan 'Terjadi error.' jika terjadi kesalahan.

            if choice == 1:
                create_item()

            elif choice ==2:
                delete_item()

            elif choice ==3:
                update_item()

            elif choice ==4:
                display_inventory()

            elif choice ==5:
                print('Terima Kasih')
                break

            else:
                print('Mohon Masukkan Angka 1-5')


        except: print('Terjadi error.')

# Fungsi program yang menggunakan loop While untuk menjalankan fungsi sesuai dengan pilihan. 
# Fungsi main() adalah fungsi utama yang akan dijalankan. 
# Ini adalah tempat di mana program akan berjalan dalam lopping tak terbatas sampai pengguna memilih untuk keluar (memilih opsi 'Keluar').
# Di dalam loop while True:, pertama-tama, program akan memanggil fungsi get_user_choice() untuk mendapatkan pilihan.
def main():
    while True:
        choice = get_user_choice()

# Jika choice == '1', program akan memanggil fungsi create_item() yang seharusnya bertanggung jawab untuk menambahkan item ke inventaris.
# Jika choice == '2', program akan memanggil fungsi delete_item() yang seharusnya bertanggung jawab untuk menghapus item dari inventaris.
# Jika choice == '3', program akan memanggil fungsi update_item() yang seharusnya bertanggung jawab untuk memperbarui item dalam inventaris.
# Jika choice == '4', program akan memanggil fungsi display_inventory() yang akan menampilkan inventaris gudang.
# Jika choice == '5', program akan mencetak pesan "Terima kasih!" dan keluar dari loop while menggunakan pernyataan break, sehingga mengakhiri program.

        if choice == '1':
            create_item()
        elif choice == '2':
            delete_item()
        elif choice == '3':
            update_item()
        elif choice == '4':
            display_inventory()
        elif choice == '5':
            print("Terima kasih!")
            break

# if __name__ == "__main__": digunakan untuk memastikan bahwa main() hanya dijalankan jika file ini dieksekusi langsung
# (bukan diimpor sebagai modul dari file lain). 

if __name__ == "__main__":
    main()