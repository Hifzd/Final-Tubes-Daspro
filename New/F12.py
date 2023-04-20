from primitives import pjglist
import global_dat
import time

def ayamberkokok():
    global global_dat
    print('Kukuruyuk.. Kukuruyuk..')
    print()
    time.sleep(2)
    jmlhCandi = pjglist(global_dat.candi) - 1
    print(f'Jumlah candi : {jmlhCandi}')
    time.sleep(2)
    if jmlhCandi < 100:
        print('Selamat, Roro Jonggrang memenangkan permainan!')
        print()
        print('*Bandung Bondowoso angry noise*')
        print('Roro Jonggrang dikutuk menjadi candi')
    else:
        print('Yah, Bandung Bondowoso memenangkan permainan!')
    
