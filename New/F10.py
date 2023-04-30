from primitives import pjglist
import global_dat

def laporancandi():
    # SPESIFIKASI
    # Menampilkan informasi informasi yang diinginkan dengan memberi parameter yang sesuai pada fungsi-fungsi

    # KAMUS
    # Tidak ada variabel lokal

    # ALGORITMA
    global global_dat
    # Memastikan apakah user sesuai
    if global_dat.current_user[2] != 'bandung_bondowoso':
        print('Laporan Candi hanya dapat diakses oleh akun Bandung Bondowoso.')
    else:
        print('> Total Candi: ', pjglist(global_dat.candi)-1)
        print('> Total Pasir yang digunakan:', jmlhbahan(global_dat.candi, 'pasir'))
        print('> Total Batu yang digunakan :', jmlhbahan(global_dat.candi, 'batu'))
        print('> Total Air yang digunakan  :', jmlhbahan(global_dat.candi, 'air'))
        print('> ID Candi Termahal:', MinMax(global_dat.candi, 'max'))
        print('> ID Candi Termurah:', MinMax(global_dat.candi, 'min'))        

def MinMax(lis, M):
    # SPESIFIKASI
    # Mencari harga candi termahal dan termurah (tergantung dari aprameter yang diberikan)

    # KAMUS LOKAL
    # IdCandi : char (initial state) or int
    # lis : array of array (akan diisi database candi)
    # M : str
    # Titik Ekstrim : int (menyimpan harga tertinggi atau terendah)
    # harga : int

    IdCandi = '-'
    # Memeriksa apakah sudah terdapat candi yang dibangun
    if pjglist(lis) == 1: # Database candi hanya berisi judul
        return IdCandi
    else:
        if M == 'min':
            # Jika dicari nilai terkecil, maka TitikEkstrim diinisialisasi dengan nilai yang besar
            TitikEkstrim = 200000
            for i in range(1,pjglist(lis)):
            # keterangan : lis[i][2] pasir, lis[i][3] batu, lis[i][4] air
                harga = int(lis[i][2])*10000 + int(lis[i][3])*15000 + int(lis[i][4])*7500
                if harga < TitikEkstrim:
                    TitikEkstrim = harga
                    IdCandi = lis[i][0]
                    
        if M == 'max':
            # Jika dicari nilai terkecil, maka TitikEkstrim diinisialisasi dengan nilai yang kecil
            TitikEkstrim = 0
            for i in range(1,pjglist(lis)):
            # keterangan : lis[i][2] pasir, lis[i][3] batu, lis[i][4] air
                harga = int(lis[i][2])*10000 + int(lis[i][3])*15000 + int(lis[i][4])*7500
                if harga > TitikEkstrim:
                    TitikEkstrim = harga
                    IdCandi = lis[i][0]

        # Setelah loop dijalankan, akan didapat id candi termahal/termurah
        # Fungsi ini kan mengembalikan id disertai hargai dengan harganya diformat ribuan terpisah oleh koma    
        return f'{IdCandi} (Rp. {format(TitikEkstrim, ",d").replace(",", ".")})'

def jmlhbahan(lis, bahan):
    # SPESIFIKASI 
    # Menghitung jumlah bahan yang diinginkan melalui database candi

    # KAMUS LOKAL
    # count : int
    # n : int (merujuk pada indeks kolom dalam database lis (candi))
    # bahan : str
    # lis : array of array (berisi database candi)

    # ALGORITMA
    count = 0
    if bahan == 'pasir':
        n = 2
    elif bahan == 'batu':
        n = 3
    elif bahan == 'air':
        n = 4
    if pjglist(lis) > 1:
        for i in range(1, pjglist(lis)):
            count += int(lis[i][n])
    return count
