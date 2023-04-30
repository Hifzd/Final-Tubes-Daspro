from primitives import pjglist
import global_dat

def login():
    # SPRESIFIKASI
    # Memeriksa pengguna saat ini, bila belum login, maka akan-
    # menerima input data login dari user dan memvalidasinya

    # KAMUS LOKAL
    # inpusr : str
    # pwd    : str
    # valid  : bool
    # i, Id  : int

    # ALGORITMA
    global global_dat
    if global_dat.current_user[0] != '':
        print('Login gagal')
        print(f'Anda telah login dengan username {global_dat.current_user[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.')
        
    else:
        inpusr = input("Username : ")
        pwd = input("Password : ")
        valid = False
        print()
        # Pencarian username pada matriks user di kolom 0 (kolom yag berisi nama pengguna)
        for i in range(pjglist(global_dat.users)):     
            if global_dat.users[i][0] == inpusr:
                valid = True
                Id = i
                break 
                # Bila terdapat username yang sama dalam matriks, maka-
                # inpusr dianggap valid dan Id (indeks) barisnya disimpan

        if not(valid):
            print("Username tidak terdaftar")

        # Program akan melihat apakah pwd sesuai dengan password user (kolom 1) pada baris dengan indeks "Id"
        elif pwd != global_dat.users[Id][1]:                 
            print("Password salah!")

        else:
            #Ketika semua valid, data username dan rolenya akan di simpan sebagai pengguna yang sedang login dalam sesi ini
            #Data pemain ini akan disimpan dalam list 'current_user'
            global_dat.current_user[0] = inpusr
            global_dat.current_user[1] = pwd
            global_dat.current_user[2] = global_dat.users[i][2]
            print(f"Selamat datang, {inpusr}!")
            print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')