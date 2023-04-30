from F06 import bangun
from F07 import gather
from primitives import pjglist, hitungjin, insert, idfind
import global_dat

def batchkumpul() :
    # SPESIFIKASI
    # Menentukan jumlah bahan yang akan didapat ketika semua jin pengumpul dikerahkan

    # KAMUS LOKAL
    # jumlahpasir, jumlahair, jumlahbatu : int
    # i,count : int

    # ALGORITMA
    global global_dat
    # Memeriksa apakah role user sesuai
    if global_dat.current_user[2] != 'bandung_bondowoso':
        print('Hanya bondowoso yang dapat mengerahkan seluruh jin pengumpul!')

    else:
        # Inisialisasi jumlah bahan
        jumlahair = 0
        jumlahpasir = 0
        jumlahbatu = 0

        # Mencari banyaknya jin pengumpul dalam database users
        count = hitungjin(global_dat.users, 'jin_pengumpul')

        if count == 0: # belum ada jin pengumpul
            print('Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.')

        else:
            # Akan dilakukan 'proses' pengumpulan bahan sebanyak jumlah jin pengumpul yang ada
            for i in range(count) :
                jumlahair += gather()
                jumlahpasir += gather()
                jumlahbatu += gather()

            # Memperbaharui jumlah tiap bahan dalam database bahan_bangunan dengan keterangan:
            # baris 0 judul, baris 1 data pasir, baris 2 data batu,  baris 3 data pasir
            # kolom 0 nama bahan, kolom 1 deskripsi, kolom 2 jumlah bahan
            global_dat.bahan_bangunan[1][2] = int(global_dat.bahan_bangunan[1][2])+jumlahpasir
            global_dat.bahan_bangunan[2][2] = int(global_dat.bahan_bangunan[2][2])+jumlahbatu
            global_dat.bahan_bangunan[3][2] = int(global_dat.bahan_bangunan[3][2])+jumlahair
            print("Jin menemukan total "+str(jumlahpasir)+" pasir "+str(jumlahbatu)+" batu "+str(jumlahair)+" air ")

def batchbangun() :
    # SPESIFIKASI
    # Menentukan apakah dapat dilakukan pembangunan oleh seluruh jin pembangun, akan menyimpan data candi yang akan dibangun,
    # Akan dimasukkan ke dalam database candi bila pembangunan seluruh candi memungkinkan

    # KAMUS
    # count,i, j : int
    # jinkuli : array (menyimpan username seluruh jin pembangun)
    # data : array of array (menyimpan data users candi sebelum dilakukan batch bangun)
    # newCandis : array of array (menyimpan data candi yang rencananya ingin dibangun)
    # totalBahan : array of int (menyimpan total bahan bangunan dari semua candi dalam newCandis)
    # lebihPasir, lebihAir, lebihBatu : int (hasil pengurangan stok bahan dengan total tiap bahan bahan)

    # ALGORITMA
    global global_dat
    # Memeriksa apakah user sesuai
    if global_dat.current_user[2] != 'bandung_bondowoso':
        print('Hanya bondowoso yang dapat mengerahkan seluruh jin pembangun!')

    else:
        # Menghitung banyaknya jumlah jin pembangun untuk menentukan besar array jinkuli
        count = hitungjin(global_dat.users, 'jin_pembangun')
        if count == 0:
            print('Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.')
            
        else:
            # Inisialisasi variabel
            jinkuli = [0 for i in range(count)]
            j = 0
            data = global_dat.candi

            # Menghitung jumlah jin pembangun dalam database users
            for i in range(pjglist(global_dat.users)):
                if global_dat.users[i][2] == 'jin_pembangun':
                    jinkuli[j] = global_dat.users[i][0]
                    j+=1

            # Membuat array baru yang akan menyimpan data candi yang rencanaya ingin dibangun
            newCandis = [0 for i in range(count)]
            # Mengisi array newCandis dengan data candi candi terbaru
            for i in range(count):
                newCandis[i] = bangun('batch', jinkuli[i],data)

                if pjglist(data) < 101:
                    data = insert(data, newCandis[i], idfind(data))
                # data adalah duplikat dari matriks candi BILA semua candi berhasil dibangun
                # database candi yang sebenarnya belum terupdate

            # Menyimpan data jumlah setiap bahan ke dalam array
            totalBahan = [0 for i in range(3)]
            # keterangan : [0] pasir, [1] batu, [2] air
            for i in range(count):
                totalBahan[0] += int(newCandis[i][2])
                totalBahan[1] += int(newCandis[i][3])
                totalBahan[2] += int(newCandis[i][4])

            print(f'Mengarahkan {count} jin untuk memanbangun candi dengan total bahan:')
            print(f'{totalBahan[0]} pasir, {totalBahan[1]} batu, {totalBahan[2]} air')

            # Memeriksa apakah stok bahan mencukupi pembangunan seluruh candi dalam newCandis
            lebihPasir = int(global_dat.bahan_bangunan[1][2]) - totalBahan[0]
            lebihBatu  = int(global_dat.bahan_bangunan[2][2]) - totalBahan[1] 
            lebihAir   = int(global_dat.bahan_bangunan[3][2]) - totalBahan[2]
            
            # Bahan yang kurang akan mengakibatkan nilai yang negatif
            if lebihPasir >= 0 and lebihAir >= 0 and lebihBatu >= 0:
                # Bila bahan mencukupi, maka pembangunan semua candi dianggap berhasil
                # Matriks data akan dijadikan sebagai database candi yang baru
                global_dat.candi = data
                # Database bahan bangunan akan diupdate dengan sisa bahan
                global_dat.bahan_bangunan[1][2] = lebihPasir
                global_dat.bahan_bangunan[2][2] = lebihBatu
                global_dat.bahan_bangunan[3][2] = lebihAir
                print(f'Para jin berhasil membangun {pjglist(newCandis)} candi')
                
            else:   # Salah satu, beberapa, atau semua bahan kurang mencukupi
                print('Para jin gagal membangun candi karena kekurangan bahan!')
                print('Kurang',end='')
                # Akan ditampilkan bahan bahan yang kurang dan jumlahnya 
                # (bahan yang kurang akan bernilai negatif)
                if lebihPasir < 0:
                    print('',abs(lebihPasir), 'pasir', end='')
                if lebihBatu < 0:
                    print('',abs(lebihBatu), 'batu', end='')
                if lebihAir < 0:
                    print('',abs(lebihAir), 'air', end='')
                print('.')

# Keterangan fungsi primitif:
# Idfind(a) : mencari indeks terkecil dari candi yang belum ada pada database a (candi)
# insert(a,b) : memasukkan data b ke baris b dalam database a (dapat meggeser data baris setelahnya)