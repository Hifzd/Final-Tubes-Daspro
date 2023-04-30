from F14 import save

def ext():
    # SPESIFIKASI
    # Memberi pilihan menyimpan program sebelum program diakhiri

    # KAMUS
    # YorN : char

    # ALGORITMA
    while True: # While loop tidak akan berhenti hingga input user valid
        YorN = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')
        if YorN == 'Y' or YorN == 'y':
            # Akan dilakukan penyimpanan data dengan menjalankan prosedut save
            save()
            break
        elif YorN == 'N' or YorN =='n':
            break
        else:
            print('Masukan tidak valid')