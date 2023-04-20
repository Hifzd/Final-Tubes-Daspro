from primitives import pjglist, popp
import global_dat

def hancurkancandi() :
    global global_dat
    Id = input("Masukkan ID candi: ")
    Found = False
    print()

    for i in range(pjglist(global_dat.candi)):
        if Id == global_dat.candi[i][0]:
            Found == True
            break

    if Found:
        YorN = input(f'Apakah anda yakin ingin menghancurkan candi ID: {Id} (Y/N)? ')
        print()
        if YorN == 'Y' or 'y':
            global_dat.candi = popp(global_dat.candi, global_dat.candi[i])
        print('Candi berhasil dihancurkan.')

    else :
        print("Tidak ada candi dengan ID tersebut")
    print()