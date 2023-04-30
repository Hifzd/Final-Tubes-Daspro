from primitives import pjglist, hitungjin, popp
import global_dat

def hapusjin() :
    # SPESIFIKASI
    # Akan menghilangkan jin dari data users dan juga menghapus data kontribusinya dalam data candi

    # KAMUS
    # bnykjin : int
    # usrn : str
    # YorN : char
    # i,j : int

    # ALGORITMA
    global global_dat
    # Memeriksa apakah user sesuai
    if global_dat.current_user[2] != 'bandung_bondowoso':
        print('Hanya bondowoso yang dapat melenyapkan para jin!')

    else:
        # Menghitung banyaknya jin dari semua tipe dalam database users
        bnykjin = hitungjin(global_dat.users, 'all')
        if bnykjin == 0 : # Belum terdapat jin
            print("Tidak ada jin yang bisa dihilangkan")
        else : # bnykjin > 0 
            usrn = input('Masukkan usrn jin : ')
            # Memeriksa apakah username dari jin yang dihilangkan ada pada database users
            for i in range(pjglist(global_dat.users)):
                if global_dat.users[i][0] == usrn:
                    break
            # Ketika username sudah ada pada database, for loop akan berhenti pada indeks username tersebut
            # Menyebabkan usrn == global_dat.users[i][0] berlaku kecuali bila belum terdapat username tersebut
            if global_dat.users[i][0] != usrn:
                print("Tidak ada jin yang memiliki nama itu")
                            
            else :  # global_dat.users[i][0] == usrn
                YorN = input("Apakah kamu ingin menghapus jin "+usrn+" ? (Y/N) ")
                if YorN == "Y" :
                    # Data dari jin yang dipilih dihilangkan dari database users
                    global_dat.users = popp(global_dat.users, global_dat.users[i])
                    
                    # Riwayat dari candi yang dibangun oleh jin yang sama akan dihilangkan dari database candi
                    # While loop digunakan karena banyak baris database candi dapat berubah seiring pengulangan
                    j = 0
                    while j < pjglist(global_dat.candi):    
                        if global_dat.candi[j][1] == usrn:
                            # Penghapusan data candi yang dibangun oleh jin dengan username <usrn>
                            global_dat.candi = popp(global_dat.candi, global_dat.candi[j])
                        j += 1