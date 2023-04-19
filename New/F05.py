from primitives import pjglist
import global_dat

def ubahjin() :
    global global_dat
    username = input("Masukkan username jin : ")

    for i in range(pjglist(global_dat.users)):
        if global_dat.users[i][0] == username:
            break
    
    if global_dat.users[i][0] == username:
        if global_dat.users[i][2] == "jin_pengumpul" :
            pilihan = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
            if pilihan == "Y" :
                global_dat.users[i][2] = "jin_pembangun"
                
        elif global_dat.users[i][2] == "jin_pembangun" :
            pilihan = input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
            if pilihan == "Y" :
                global_dat.users[i][2] = "jin_pengumpul"

        print(f'Jin {username} telah berhasil diubah')

    else:
        print('Tidak ada jin dengan username tersebut.')