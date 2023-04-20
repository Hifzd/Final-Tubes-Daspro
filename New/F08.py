from F06 import bangun
from F07 import gather
from primitives import pjglist, hitungjin, insert, idfind
import global_dat

def batchkumpul() :
    global global_dat
    jumlahair = 0
    jumlahpasir = 0
    jumlahbatu = 0
    count = hitungjin(global_dat.users, 'jin_pengumpul')

    if count > 0:
        for i in range(count) :
            jumlahair += gather()
            jumlahpasir += gather()
            jumlahbatu += gather()
        
        global_dat.bahan_bangunan[1][2] = int(global_dat.bahan_bangunan[1][2])+jumlahpasir
        global_dat.bahan_bangunan[2][2] = int(global_dat.bahan_bangunan[2][2])+jumlahbatu
        global_dat.bahan_bangunan[3][2] = int(global_dat.bahan_bangunan[3][2])+jumlahair
        print("Jin menemukan total "+str(jumlahpasir)+" pasir "+str(jumlahbatu)+" batu "+str(jumlahair)+" air ")

    else:
        print('Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.')

def batchbangun() :
    global global_dat
    count = hitungjin(global_dat.users, 'jin_pembangun')
    if count > 0:
        jinkuli = [0 for i in range(count)]
        j = 0
        data = global_dat.candi

        for i in range(pjglist(global_dat.users)):
            if global_dat.users[i][2] == 'jin_pembangun':
                jinkuli[j] = global_dat.users[i][0]
                j+=1

        newCandis = [0 for i in range(count)]
        for i in range(count):
            newCandis[i] = bangun('batch', jinkuli[i],data)
            data = insert(data, newCandis[i], idfind(data))
            # data adalah rekayasa dari matriks candi bila semua candi berhasil dibangun

        totalBahan = [0 for i in range(count)]
        # keterangan : [0] pasir, [1] batu, [2] air
        for i in range(count):
            totalBahan[0] += int(newCandis[i][2])
            totalBahan[1] += int(newCandis[i][3])
            totalBahan[2] += int(newCandis[i][4])

        print(f'Mengarahkan {count} jin untuk memanbangun candi dengan total bahan:')
        print(f'{totalBahan[0]} pasir, {totalBahan[1]} batu, {totalBahan[2]} air')

        lebihPasir = global_dat.bahan_bangunan[1][2] - totalBahan[0]
        lebihBatu  = global_dat.bahan_bangunan[2][2] - totalBahan[1] 
        lebihAir   = global_dat.bahan_bangunan[3][2] - totalBahan[2]

        if lebihPasir >= 0 and lebihAir >= 0 and lebihBatu >= 0:
            global_dat.candi = data
            global_dat.bahan_bangunan[1][2] = lebihPasir
            global_dat.bahan_bangunan[2][2] = lebihBatu
            global_dat.bahan_bangunan[3][2] = lebihAir
            print(f'Para jin berhasil membangun {pjglist(newCandis)} candi')
            
        else:
            print('Para jin gagal membangun candi karena kekurangan bahan!')
            print('Kurang',end='')
            if lebihPasir < 0:
                print('',abs(lebihPasir), 'pasir', end='')
            if lebihBatu < 0:
                print('',abs(lebihBatu), 'batu', end='')
            if lebihAir < 0:
                print('',abs(lebihAir), 'air', end='')
            print('.')
    else:
        print('Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.')