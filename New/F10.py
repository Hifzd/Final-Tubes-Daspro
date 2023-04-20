from primitives import pjglist
import global_dat

def laporancandi():
    global global_dat
    print('> Total Candi: ', pjglist(global_dat.candi)-1)
    print('> Total Pasir yang digunakan:', jmlhbahan(global_dat.candi, 'pasir'))
    print('> Total Batu yang digunakan :', jmlhbahan(global_dat.candi, 'batu'))
    print('> Total Air yang digunakan  :', jmlhbahan(global_dat.candi, 'air'))
    print('> ID Candi Termahal:', MinMax(global_dat.candi, 'max'))
    print('> ID Candi Termurah:', MinMax(global_dat.candi, 'min'))

def MinMax(lis, M):
    index = '-'
    if pjglist(lis) > 1:
        if M == 'min':
            TitikEkstrim = 200000
            for i in range(1,pjglist(lis)):
            # keterangan : lis[i][2] pasir, lis[i][3] batu, lis[i][4] air
                harga = int(lis[i][2])*10000 + int(lis[i][3])*15000 + int(lis[i][4])*7500
                if harga < TitikEkstrim:
                    TitikEkstrim = harga
                    index = lis[i][0]
        if M == 'max':
            TitikEkstrim = 0
            for i in range(1,pjglist(lis)):
            # keterangan : lis[i][2] pasir, lis[i][3] batu, lis[i][4] air
                harga = int(lis[i][2])*10000 + int(lis[i][3])*15000 + int(lis[i][4])*7500
                if harga > TitikEkstrim:
                    TitikEkstrim = harga
                    index = lis[i][0]
            
        return f'{index} (Rp. {format(TitikEkstrim, ".d")})'
    else:
        return index

def jmlhbahan(lis, bahan):
    count = 0
    if bahan == 'pasir':
        n = 2
    elif bahan == 'batu':
        n = 3
    elif bahan == 'air':
        n = 4
    if pjglist(lis) > 1:
        for i in range(1, pjglist(lis)):
            count += int(lis[i][n])
    return count
