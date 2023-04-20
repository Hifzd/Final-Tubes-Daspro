from primitives import splitter
import os
import global_dat

def valid(folder):
    save_folder = 'save'
    if os.path.isdir(os.path.join(save_folder,folder)) and folder != '':
        print('''Loading...

Selamat datang di program “Manajerial Candi”
Silahkan ketik login dan masukkan username Anda''')
        return True
        
    else:
        if folder == "":
            print('''Tidak ada nama folder yang diberikan!

Usage: python main.py <nama_folder>''')
        else :
            print(f'Folder "{folder}" tidak ditemukan.')
        return False

def load(folder, csv):
    save_folder = 'save'
    path = os.path.join(save_folder, folder)
    file_path = os.path.join(path, str(csv))
    dat = open(f'{file_path}', 'r')
    matrix = splitter(dat.read(), '\n')
    return matrix

def load_data(folder):
  global_dat.users = load(folder, 'user.csv')
  global_dat.candi = load(folder, 'candi.csv')
  global_dat.bahan_bangunan = load(folder, 'bahan_bangunan.csv')