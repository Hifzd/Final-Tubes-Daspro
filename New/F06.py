from primitives import pjglist, idfind, insert
import global_dat

def bangun(tipe, builder, data) :
    # SPESIFIKASI
    # Membangun sebuah candi dan mencari bahan bahan yang diperlukan

    # KAMUS LOKAL
    # kemungkinan : array
    # perluair, perlupasir, perlubatu : int
    # tipe : string
    # builder : string (pada command 'bangun' berisi role dari user, sedangkan ketika dipanggil batchbangun, akan berisi username jin)
    # data : array of array (hanya digunakan ketika fungsi ini dipanggil oleh batchbangun)

    global global_dat
    import random

    # Menentukan banyak bahan yang diperlukan
    kemungkinan = [1,2,3,4,5]
    perluair = random.choice(kemungkinan)
    perlupasir = random.choice(kemungkinan)
    perlubatu = random.choice(kemungkinan)

    # Memeriksa apakah fungsi digunakan untuk command 'bangun' (membangun 1 candi oleh jin pembangun)
    if tipe == 'single':
        # Memeriksa apakah role sesuai
        if builder != 'jin_pembangun':
            print('Hanya jin pembangun yang dapat memabangun candi!')
            
        else:
            # Meriksa apakah bahan yang tersedia mencukupi kebutuhan pembangunan candi
            stock = global_dat.bahan_bangunan
            # Keterangan: baris 0 berupa judul, baris 1 data pasir, baris 2 data batu,  baris 3 data pasir
            # kolom 0 nama bahan, kolom 1 deskripsi, kolom 2 jumlah bahan
            if perluair <= int(stock[3][2]) and perlubatu <= int(stock[2][2]) and perlupasir <= int(stock[1][2]) :
                # Mengupdate jumlah tiap bahan dalam database bahan_bangunan
                global_dat.bahan_bangunan[1][2] = int(stock[1][2]) - perlupasir
                global_dat.bahan_bangunan[2][2] = int(stock[2][2]) - perlubatu
                global_dat.bahan_bangunan[3][2] = int(stock[3][2]) - perluair
                # Dibuat sebuah array berisi data dari candi yang akan dibuat
                newCandi = [idfind(global_dat.candi),builder,perlupasir,perlubatu,perluair]

                # Memeriksa jumlah candi yang telah dibangun
                kurang = 101-pjglist(global_dat.candi)
                print("Candi berhasil dibangun.")

                if kurang > 0: # Candi kurang dari 100
                    # Mencari id terendah yang belum ada
                    idbangun = idfind(global_dat.candi)
                    # Memasukkan data candi terbaru ke baris idbangun ke dalam database candi
                    global_dat.candi = insert(global_dat.candi, newCandi, idbangun)
                    print("Sisa candi yang perlu dibangun: ",kurang-1)
                else: # Sudah terdapat 100 candi
                    print('Sisa candi yang perlu dibangun: 0.')
                    # tidak ada candi baru yang dimasukkan ke dalam database candi

            else : # Bahan kurang mencukupi
                print("Bahan tidak mencukupi")
                print('Candi tidak bisa dibangun!')
    
    else: #ketika melakukan batch
        # Membuat array data candi yang 'ingin' dibangun
        newCandi = [idfind(data),builder,perlupasir,perlubatu,perluair]
        # candi-candi individual belum tentu dapat dibangun saat batch,
        # sehingga data candi tidak langsung dimasukkan ke database candi
        return newCandi

# Keterangan fungsi primitif:
# Idfind(a) : mencari indeks terkecil dari candi yang belum ada pada database a (candi)
# insert(a,b) : memasukkan data b ke baris b dalam database a (dapat meggeser data baris setelahnya)