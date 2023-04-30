import F01
import F02
import F03
import F04
import F05
import F06
import F07
import F08
import F09
import F10
import F11
import F14
import F15
import global_dat

def run(masukan):
    # SPESIFIKASI
    # Mengarahkan program ke fitur/subprogram berdasarkan masukan dari masukan user

    # KAMUS LOKAL
    # masukan : str

    # ALGORITMA
    if masukan == 'login':
        F01.login()

    elif masukan == 'logout':
        F02.logout()

    elif masukan == 'summonjin':
        F03.summonjin()

    elif masukan == 'hapusjin':
        F04.hapusjin()

    elif masukan == 'ubahjin':
        F05.ubahjin()

    elif masukan == 'bangun':
        F06.bangun('single', global_dat.current_user[2],'')

    elif masukan == 'kumpul':
        F07.kumpul()

    elif masukan == 'batchbangun':
        F08.batchbangun()
    
    elif masukan == 'batchkumpul':
        F08.batchkumpul()

    elif masukan == 'laporanjin':
        F09.laporanjin()
    
    elif masukan == 'laporancandi':
        F10.laporancandi()

    elif masukan == 'hancurkancandi':
        F11.hancurkancandi()

    elif masukan == 'save':
        F14.save()
    
    elif masukan == 'help':
        F15.help(global_dat.current_user[2])

    else: # bila masukan user belum sesuai
        print('Command tidak ditemukan\nSilahkan ketik "help" untuk melihat command yang bisa digunakan')