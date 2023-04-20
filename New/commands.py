import F01
import F02
import F03
import F04
import F05
import F06
import F07
import F08
import F09
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
            F06.bangun('single', global_dat.current_user[0],'')
        else:
            print('Hanya jin pembangun yang bisa membangun candi')

    elif masukan == 'kumpul':
        if global_dat.current_user[2] == 'jin_pengumpul':
            F07.kumpul()
        else:
            print('Hanya jin pembangun yang bisa membangun candi')

    elif masukan == 'batchbangun' or masukan == 'batchkumpul':
        if global_dat.current_user[2] == 'bandung_bondowoso':
            if masukan == 'batchkumpul':
                F08.batchkumpul()
            else:
                F08.batchbangun()
        else:
            print('Hanya sang Bondowoso yang bisa mengerahkan seluruh jin pengumpul/pembangun!')
    
    elif masukan == 'laporanjin':
        if global_dat.current_user[2] == 'bandung_bondowoso':
            F09.laporanjin()
        else:
            print('Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.')