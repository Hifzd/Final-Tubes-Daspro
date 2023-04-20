from primitives import pjglist, konso, idfind, insert
import global_dat

def bangun(tipe, builder, data) :
    global global_dat
    import random

    kemungkinan = [1,2,3,4,5]
    perluair = random.choice(kemungkinan)
    perlupasir = random.choice(kemungkinan)
    perlubatu = random.choice(kemungkinan)

    if tipe == 'single':
        if perluair <= int(global_dat.bahan_bangunan[3][2]) and perlubatu <= int(global_dat.bahan_bangunan[2][2]) and perlupasir <= int(global_dat.bahan_bangunan[1][2]) :
            global_dat.bahan_bangunan[1][2] = int(global_dat.bahan_bangunan[1][2]) - perlupasir
            global_dat.bahan_bangunan[2][2] = int(global_dat.bahan_bangunan[2][2]) - perlubatu
            global_dat.bahan_bangunan[3][2] = int(global_dat.bahan_bangunan[3][2]) - perluair
            newCandi = [idfind(global_dat.candi),builder,perlupasir,perlubatu,perluair]

            kurang = 100-pjglist(global_dat.candi)+1
            print("Candi berhasil dibangun")

            if kurang > 0:
                print("Sisa candi yang perlu dibangun: "+str(kurang))
                idbangun = idfind(global_dat.candi)
                global_dat.candi = insert(global_dat.candi, newCandi, idbangun)
            else:
                print('Sisa candi yang perlu dibangun: 0')
        else :
            print("Bahan tidak mencukupi")
            print('Candi tidak bisa dibangun!')
    
    else: #ketika melakukan batch
        newCandi = [idfind(data),builder,perlupasir,perlubatu,perluair]
        return newCandi