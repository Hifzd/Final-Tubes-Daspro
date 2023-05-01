from primitives import pjglist, konso, hitungjin
import global_dat

def jinless100(users, golongan):
    # SPESIFIKASI
    # Akan menghitung jumlah jin dari semua golongan dan mengoutput boolean-
    # bernilai True jika jumlah jin kurang dari 100 atau False jika tidak

    # KAMUS LOKAL
    # count : int

    # Algoritma
    count = hitungjin(users, golongan)
    #fungsi primitif hitungjin akan menghitung jumlah jin dengan golongan tertentu dalam matriks users
    if count < 100:
        return True
    else:
        print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
        return False

def summonjin():
    # SPESIFIKASI
    # Berfungsi untuk menambahkan jin ke dalam data users dengan data-data (password dan role) yang diinginkan

    # KAMUS LOKAL
    # val   : bool
    # jenis : int
    # usrjin,pwdjin,rolejin : str
    # jinbaru : array

    # ALGORITMA
    global global_dat
    # Memeriksa apakah user sesuai
    if global_dat.current_user[2] != 'bandung_bondowoso':
        print('Hanya Bondowoso yang dapat memanggil para jin!')
        
    else:
        # Memeriksa apakah jumlah jin masih kurang dari 100 dan menyimpan nilai True or Falsenya ke dalam val
        val = jinless100(global_dat.users, 'all')
        if val:
            print('Jenis jin yang dapat dipanggil:')
            print(' (1) Pengumpul - Bertugas mengumpulkan bahan bangunan')
            print(' (2) Pembangun - Bertugas membangun candi\n')

            # Akan dilakukan 3 while loop yang akan selalu berjalan hingga input user sesuai, hingga pada-
            # akhirnya didapat data lengkap mengenai jin yang ingin ditambahkan

            # Pemilihan jenis jin
            while True:
                jenis = int(input('Masukkan nomor jenis jin yang ingin dipanggil: '))
                print()
                if jenis == 1 or jenis == 2 :
                    print('Memilih jin', end=" ")
                    if jenis == 1 :
                        rolejin = "jin_pengumpul"
                        print('"Pengumpul".')
                    else:
                        rolejin = "jin_pembangun"
                        print('"Pembangun".')
                    break
                else:
                    print(f'Tidak ada jenis jin bernomor "{jenis}"!\n')

            # Pemberian username jin baru
            while True:
                usrnjin = input('Masukkan username jin : ')
                # Memeriksa apakah username jin baru sudah ada pada database users
                for i in range(pjglist(global_dat.users)):
                    if usrnjin == global_dat.users[i][0]:
                        print(f'Username "{usrnjin}" sudah diambil!\n')
                        break
                # Ketika username sudah ada pada database, while loop akan berhenti pada indeks username tersebut
                # Menyebabkan usrnjin == global_dat.users[i][0] berlaku kecuali bila belum terdapat username tersebut
                if usrnjin != global_dat.users[i][0]:
                    break

            #Pemberian password jin baru
            while True:
                pwdjin = input('Masukkan password jin : ')
                print()

                # Pemeriksaan apakah panjang password sudah sesuai kriteria
                if len(pwdjin) < 5 or len(pwdjin) > 25:
                    print('Password panjangnya harus 5-25 karakter!\n')
                else:
                    break
            print('Mengumpulkan sesajen...')
            print('Menyerahkan sesajen...')
            print('Membacakan mantra...')
            print()
            # Dibuat sebuah array yang berisi username, password, dan role jin baru
            jinbaru = [usrnjin, pwdjin, rolejin]
            print(f'Jin {usrnjin} berhasil dipanggil')
            # Data dari jin baru tersebut akan ditambahkan ke dalam database users
            global_dat.users = konso(global_dat.users, jinbaru)