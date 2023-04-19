from primitives import pjglist, konso
import global_dat

def bangun() :
    global global_dat
    import random
    print(pjglist(global_dat.candi))
    kemungkinan = [1,2,3,4,5]
    perluair = random.choice(kemungkinan)
    perlupasir = random.choice(kemungkinan)
    perlubatu = random.choice(kemungkinan)

    if perluair <= int(global_dat.bahan_bangunan[3][2]) and perlubatu <= int(global_dat.bahan_bangunan[2][2]) and perlupasir <= int(global_dat.bahan_bangunan[1][2]) :
        global_dat.bahan_bangunan[1][2] = int(global_dat.bahan_bangunan[1][2]) - perlupasir
        global_dat.bahan_bangunan[2][2] = int(global_dat.bahan_bangunan[2][2]) - perlubatu
        global_dat.bahan_bangunan[3][2] = int(global_dat.bahan_bangunan[3][2]) - perluair
        newCandi = [pjglist(global_dat.candi),global_dat.current_user[0],perlupasir,perlubatu,perluair]
        global_dat.candi = konso(global_dat.candi, newCandi)

        print("Candi berhasil dibangun")

        print("Sisa yang perlu dibangun: "+str(100-pjglist(global_dat.candi)))
    else :
        print("Bahan tidak mencukupi")