import F01
import F02
import F03
import F04
import F05
import global_dat

def run(masukan):
    if masukan == 'login':
        F01.login()

    elif masukan == 'logout':
        F02.logout()

    elif masukan == 'summonjin':
        if global_dat.current_user[2] == 'bandung_bondowoso':
            F03.summonjin()
        else:
            print('Hanya Bondowoso yang bisa memanggil para jin!')

    elif masukan == 'hapusjin':
        if global_dat.current_user[2] == 'bandung_bondowoso':
            F04.hapusjin()
        else:
            print('Hanya Bondowoso yang bisa melenyapkan para jin!')

    elif masukan == 'ubahjin':
        if global_dat.current_user[2] == 'bandung_bondowoso':
            F05.ubahjin()
        else:
            print('Hanya Bondowoso yang bisa merubah para jin!')

    elif masukan == 'bangun':
        if global_dat.current_user[2] == 'jin_pembangun':
            F06.bangun()
        else:
            print('Hanya jin pembangun yang bisa membangun candi')