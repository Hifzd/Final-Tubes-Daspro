import F12
import F13
import F16
import argparse
import commands
import global_dat

# Menggunakan module argarse untuk memanfaatkan argumen tambahan dari terminal
parser = argparse.ArgumentParser()
parser.add_argument("folder", default='', nargs='?')
args = parser.parse_args()
# Menginterpretasikan argumen tambahan sebagai nama folder dari database yang akan digunakan

# Memeriksa apakah argumen tambahan dari user valid
isFoldr_exist = F13.valid(args.folder)

# Jika masukan valid dan folder ada, maka database akan diisi oleh data dari file dalam folder tersebut
if isFoldr_exist:
    F13.load_data(args.folder)

# Menjalankan blok program lainnya bila valid
while isFoldr_exist:
    # Menerima masukan yang akan digunakan untuk memilih fitur/subprogram yang ingin dijalankan
    masukan = input(">>> ")

    # User yang menginput exit dan ayamberkokok (bila user Roro) akan mengakibatkan program berhenti
    if masukan == 'exit':
        F16.ext()
        break
    elif masukan == 'ayamberkokok' and global_dat.current_user[0] == 'Roro':
        F12.ayamberkokok()
        break

    # Masukan akan diarahkan oleh modul commands untuk menjalankan fitur yang sesuai
    else:
        commands.run(masukan)
        print()