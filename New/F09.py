from primitives import hitungjin
import global_dat

def laporanjin():
    global global_dat

    print('> Total Jin:', hitungjin(global_dat.users, 'all'))
    print('> Total Jin Pengumpul:', hitungjin(global_dat.users, 'jin_pengumpul'))
    print('> Total Jin Pembangun:', hitungjin(global_dat.users, 'jin_pembangun'))
    print('> Jin Terajin :')
    print('> Jin Termalas:')
    print('> Jumlah Pasir:', global_dat.bahan_bangunan[1][2],'unit')
    print('> Jumlah Batu :', global_dat.bahan_bangunan[2][2],'unit')
    print('> Jumlah Air  :', global_dat.bahan_bangunan[3][2],'unit')