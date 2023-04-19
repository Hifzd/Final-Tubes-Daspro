from primitives import pjglist, hitungjin, popp
import global_dat

def hapusjin() :
    global global_dat
    bnykjin = hitungjin(global_dat.users, 'all')
    if bnykjin == 0 :
        print("Tidak ada jin yang bisa dihilangkan")
    else :
        username = input('Masukkan username jin : ')
        for i in range(pjglist(global_dat.users)):
            if global_dat.users[i][0] == username:
                break
            
        if global_dat.users[i][0] == username:
            YorN = input("Apakah kamu ingin menghapus jin "+username+" ? (Y/N) ")
            if YorN == "Y" :
                global_dat.users = popp(global_dat.users, global_dat.users[i])

        else :
            print("Tidak ada jin yang memiliki nama itu")