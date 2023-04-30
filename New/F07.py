import global_dat

def kumpul() :
    # SPESIFIKASI
    # Menentukan jumlah bahan yang didapat dan memasukkannya ke dalam database
    # Hanya berfungsi untuk command 'kumpul' dari jin pengumpul (tidak akan dipanggil oleh batchkumpul)

    # KAMUS LOKAL
    # dapatpasir, dapatbatu, dapatair : int (1-5)

    # ALGORITMA
    global global_dat

    # Memeriksa apakah role user sesuai
    if global_dat.current_user[2] == 'jin_pengumpul':
        # Menentukan jumlah bahan yang terkumpul
        dapatpasir = gather()
        dapatbatu = gather()
        dapatair = gather()
        
        # Memperbaharui jumlah bahan ada database bahan bangunan dengan keterangan:
        # baris 0 judul, baris 1 data pasir, baris 2 data batu,  baris 3 data pasir
        # kolom 0 nama bahan, kolom 1 deskripsi, kolom 2 jumlah bahan
        global_dat.bahan_bangunan[1][2] = int(global_dat.bahan_bangunan[1][2])+dapatpasir
        global_dat.bahan_bangunan[2][2] = int(global_dat.bahan_bangunan[2][2])+dapatbatu
        global_dat.bahan_bangunan[3][2] = int(global_dat.bahan_bangunan[3][2])+dapatair
        print("Jin menemukan "+str(dapatpasir)+" pasir, "+str(dapatbatu)+" batu, dan "+str(dapatair)+" air.")

    else: 
        print('Hanya jin pengumpul yang dapat mengumpulkan bahan!')

def gather():
    # SPESIFIKASI
    # Menentukan jumlah bahan yang diperlukan, 
    # library random akan memilih 1 anggota dari sebuah arrah secara acak

    # KAMUS LOKAL
    # kemungkinan : array of int

    # ALGORITMA
    import random
    kemungkinan = [1,2,3,4,5]
    return random.choice(kemungkinan)