import os
import time
import global_dat
from primitives import pjglist

def listToString(lis, delimiter):
    # SPESIFIKASI
    # Menggabungkan tiap anggota lis ke dalam bentuk string yang tiap elemennya dipisahkan oleh delimiter

    # KAMUS
    # newstr : str
    # i : int
    # lis : array
    # delimiter : char

    # ALGORITMA
    newstr = ''
    for i in range(pjglist(lis)):
        # Penambahan elemen list ke-i ke variabel newstr dalam banetuk string
        newstr += str(lis[i])

        # Penambahan delimiter diantara elemen elemen list
        if i != pjglist(lis)-1:
            newstr += delimiter
    
    return newstr

def saveMatriks(matriks, filename, folder):
    # SPESIFIKASI
    # Membuat sebuah file csv dalam folder terpilih dari matriks yang yang telah digunakan dalam program

    # KAMUS LOKAL
    # f : file
    # i : int
    # matriks : array of array (berisi database yang digunakan oleh keseluruhan program)
    # newline : str (merupakan baris yang ingin dituliskan pada file csv)

    # ALGORITMA
    f = open(f'{folder}/{filename}.csv', mode='w') # Pembukaan file csv dalam folder <folder>

    # Penulisan setiap baris dalam matriks ke file csv
    for i in range(pjglist(matriks)):
        # Membuat sebuah list berisi elemen pada baris-i dan akan dipisahkan oleh ;
        newline = listToString(matriks[i], ';')
        
        # Memasukkan newline ke dalam file
        f.write(newline)
        if i != pjglist(matriks) - 1:
            f.write('\n')
    
    f.close()

def save():
    global global_dat
    new_folder = input('Masukkan nama folder: ')
    print()

    print('Saving...')
    time.sleep(1)
    save_folder = 'save'
    WorkingDir = os.getcwd()
    path = os.path.join(str(WorkingDir), save_folder)

# memeriksa apakah parent folder '/save/' sudah ada
    if os.path.isdir(path): # apabila parent folder sudah ada
        if not(os.path.isdir(os.path.join(path, new_folder))): # apabila belum ada folder yang diinput oleh user dalam parent folder save
            print(f'Membuat folder {save_folder}/{new_folder}')
            print()
        
        new_folder_path = os.path.join(path, new_folder)
        os.makedirs(new_folder_path, exist_ok=True)

    else:                   # apabila parent folder belum ada
        print(f'Membuat folder {save_folder} ...')
        os.mkdir(path)
        print(f'Membuat folder {save_folder}/{new_folder}...')
        new_folder_path = os.path.join(path, new_folder)
        os.mkdir(new_folder_path)

    # Mengesave 3 set matriks ke dalam masing masing csv
    saveMatriks(global_dat.users, 'user', new_folder_path)
    saveMatriks(global_dat.candi, 'candi', new_folder_path)
    saveMatriks(global_dat.bahan_bangunan, 'bahan_bangunan', new_folder_path)
    time.sleep(1)
    print(f'Berhasil menyimpan data di folder {save_folder}/{new_folder}')