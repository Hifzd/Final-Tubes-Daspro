from primitives import pjglist
import global_dat
import time

def ayamberkokok():
    # SPESIFIKASI
    # Akan menyebabkan selesainay program dan menampilkan pemenang permainan 

    # KAMUS LOKAL
    # jmlhCandi : int

    # ALGORITMA
    global global_dat
    print('Kukuruyuk.. Kukuruyuk..')
    print()
    time.sleep(2)

    jmlhCandi = pjglist(global_dat.candi) - 1
    # JmlhCandi dikurangi 1 karena database/matriks candi berisi 1 baris judul
    print(f'Jumlah candi : {jmlhCandi}')
    time.sleep(2)

    # Bondowoso akan menang ketika candi sudah 100, sedangkan Roro akan menang jika kurang dari itu
    if jmlhCandi < 100:
        print('Selamat, Roro Jonggrang memenangkan permainan!')
        print()
        time.sleep(1)
        print('*Bandung Bondowoso angry noise*')
        print('Roro Jonggrang dikutuk menjadi candi')
    else:
        print()
        print('Yah, Bandung Bondowoso memenangkan permainan!')