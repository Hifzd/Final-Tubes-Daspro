from primitives import pjglist
import global_dat

def ubahjin() :
    # SPESIFIKASI
    # Mengubah role atau tipe dari jin yang diminta

    # KAMUS LOKAL
    # username : str
    # pilihan : chr

    # ALGORITMA
    global global_dat
    # Memeriksa apakah user sesuai
    if global_dat.current_user[2] != 'bandung_bondowoso':
        print('Hanya Bondowoso yang dapat mengganti peran para jin!')
        
    else:
        username = input("Masukkan username jin : ")
        # Memeriksa apakah ada jin dengan username tersebut dalam database users
        for i in range(pjglist(global_dat.users)):
            if global_dat.users[i][0] == username:
                break
        # Ketika username sudah ada pada database, for loop akan berhenti pada indeks username tersebut
        # Menyebabkan usrn == global_dat.users[i][0] berlaku kecuali bila belum terdapat username tersebut
        if global_dat.users[i][0] != username:
            print('Tidak ada jin dengan username tersebut.')

        else:
            # Memeriksa role dari jin yang terpilih dan merubah role ke role sebaliknya
            if global_dat.users[i][2] == "jin_pengumpul" :
                pilihan = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
                if pilihan == "Y" :
                    global_dat.users[i][2] = "jin_pembangun"
                    
            elif global_dat.users[i][2] == "jin_pembangun" :
                pilihan = input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
                if pilihan == "Y" :
                    global_dat.users[i][2] = "jin_pengumpul"

            print(f'Jin {username} telah berhasil diubah')
