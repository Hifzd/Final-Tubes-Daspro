from primitives import pjglist, popp
import global_dat

def hancurkancandi() :
    # SPESIFIKASI
    # Menghancurkan candi dengan menghapus candi dari database

    # KAMUS LOKAL
    # Id : str
    # Found : bool
    # YorN : char

    # ALGORITMA
    global global_dat
    # Memeriksa apakah pengguna sudah sesuai
    if global_dat.current_user[2] != 'roro_jonggrang':
        print('Hanya Roro Jonggrang yang dapat menghancurkan candi!')

    else:
        Id = input("Masukkan ID candi: ")
        Found = False # Mulanya dianggap tidak ada candi dengan id = Id
        print()
        
        # Pencarian candi ber-id = Id dalam database candi 
        for i in range(1,pjglist(global_dat.candi)):
            if Id == global_dat.candi[i][0]:
                Found = True
                break
        
        # Bila ada, Found berubah menjadi True
        if Found:
            YorN = input(f'Apakah anda yakin ingin menghancurkan candi ID: {Id} (Y/N)? ')
            print()
            if YorN == 'Y' or 'y':
                global_dat.candi = popp(global_dat.candi, global_dat.candi[i])
                # Candi yang terpilih akan dihilangkan dari database
                # Fungsi popp akan menghilangkan satu baris dalam database
            print('Candi berhasil dihancurkan.')

        else : # Tidak terdapat candi ber-id = Id
            print("Tidak ada candi dengan ID tersebut")

