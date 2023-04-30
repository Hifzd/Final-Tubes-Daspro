from primitives import splitter
import os
import global_dat

def valid(folder):
    # SPESIFIKASI
    # Akan memvalidasi apakah terdapat folder bernama yang diinput user dalam folder save
    # Mengembalikan nilai True jika terdapat folder tersebut

    # KAMUS LOKAL
    # save_folder : str (merujuk pada folder induk dari folder folder csv program)

    # ALGORITMA
    save_folder = 'save' #inisialisasi folder induk

    # Memastikan bahwa folder ada dalam direktori .../save/<nama_folder>
    if os.path.isdir(os.path.join(save_folder,folder)) and folder != '':
        print('Loading...\n\nSelamat datang di program “Manajerial Candi”')
        print('Silahkan ketik login dan masukkan username Anda')
        return True
        
    else: # Tidak terdapat folder dalam direktori yang ditentukan
        if folder == "": # User tidak memberi argumen <nama_folder> dari terminal
            print('Tidak ada nama folder yang diberikan!\nUsage: python main.py <nama_folder>')
        else :
            print(f'Folder "{folder}" tidak ditemukan.')
        return False

def load(folder, csv):
    # SPESIFIKASI
    # Membaca sebuah file csv dari salah satu folder dalam folder save
    # Menghasilkan sebuah dataset berbentuk matriks (array of array) berisi data dari csv

    # KAMUS LOKAL
    # save_folder : str (merujuk pada induk folder save)
    # path : str (merujuk pada direktori folder dataset yang ingin digunakan dalam folder save)
    # filepath : str (merujuk pada direktori dari file csv)
    # dat : file
    # matrix : array of array

    # ALGORITMA
    save_folder = 'save'
    path = os.path.join(save_folder, folder)    # Membuat sebuah string berisi direktori hingga ke save_folder
    file_path = os.path.join(path, str(csv))    # Membuat direktori file csv yang diinginkan
    dat = open(f'{file_path}', 'r')             # Membuka file csv dalam mode read
    matrix = splitter(dat.read(), '\n')         # Mentranslasikan hasil bacaan
    return matrix                               # Mengembalikan hasil bacaan dalam bentuk matriks

def load_data(folder):
    # SPESIFIKASI
    # Mengisi database global dengan data data dari file csv yang terkait

    # KAMUS LOKAL
    # Tidak ada variabel lokal

    # ALGORITMA
    global_dat.users = load(folder, 'user.csv')
    global_dat.candi = load(folder, 'candi.csv')
    global_dat.bahan_bangunan = load(folder, 'bahan_bangunan.csv')