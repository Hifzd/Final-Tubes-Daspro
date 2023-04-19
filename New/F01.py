from primitives import pjglist
import global_dat

def login():
    global global_dat
    if global_dat.current_user[0] == '':
        inpusr = input("Username : ")
        pwd = input("Password : ")
        print()
        for i in range(pjglist(global_dat.users)):                 #loop akan mengecek apakah inputan username dari user terdapat pada list "username"
            if global_dat.users[i][0] == inpusr:                   #jika terdapat username yang terdaftar pada list, maka loop akan diberhentikan
                global_dat.current_user[0] = inpusr
                break            
        if global_dat.current_user[0] == "":                           #jika username belum terdaftar pada list "username"
            print("Username tidak terdaftar")
        elif pwd != global_dat.users[i][1]:                 
            print("Password salah!")
            global_dat.current_user[0] = ""                            #jika password salah, maka username pengguna di reset (dianggap belum login kembali)
            global_dat.current_user[1] = ""
        else:
            #data username dan rolenya akan di simpan sebagai pengguna yang sedang login dalam sesi ini
            global_dat.current_user[0] = inpusr
            global_dat.current_user[1] = pwd
            global_dat.current_user[2] = global_dat.users[i][2]
            print(f"Selamat datang, {inpusr}!")
            print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    else:
        print('Login gagal')
        print(f'Anda telah login dengan username {global_dat.current_user[0]}, silahkan lakukan “logout” sebelum melakukan login kembali.')