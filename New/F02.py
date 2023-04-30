import global_dat

def logout():
    # SPRESIFIKASI
    # Akan memeriksa apakah user sudah login, bila iya, maka nilai current_user yang- 
    # menyimpan data user yang telah login di reset(menjadi kosong)

    # KKAMUS LOKAL
    # tidak terdapat variabel lokal

    # ALGORITMA
    global global_dat
    if global_dat.current_user[0] == '':
        print("Logout gagal")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else:
        print("Berhasil logout")
        global_dat.current_user[0], global_dat.current_user[1], global_dat.current_user[2] = '','',''