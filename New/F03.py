from primitives import pjglist, konso, hitungjin
import global_dat

def jinless100(users, golongan):
    count = hitungjin(users, golongan)
    if count <= 6:
        return True
    elif count > 6:
        print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
        return False

def summonjin():
    global global_dat
    val = jinless100(global_dat.users, 'all')
    if val:
        print('Jenis jin yang dapat dipanggil:')
        print(' (1) Pengumpul - Bertugas mengumpulkan bahan bangunan')
        print(' (2) Pembangun - Bertugas membangun candi')
        print()
        while True:
            jenis = int(input('Masukkan nomor jenis jin yang ingin dipanggil: '))
            print()
            if jenis == 1 or jenis == 2 :
                print('Memilih jin', end=" ")
                if jenis == 1 :
                    rolejin = "jin_pengumpul"
                    print('"Pengumpul".')
                else:
                    rolejin = "jin_pembangun"
                    print('"Pembangun".')
                break
            else:
                print(f'Tidak ada jenis jin bernomor "{jenis}"!')
        print()
        while True:
            usrnjin = input('Masukkan username jin : ')
            for i in range(pjglist(global_dat.users)):
                if usrnjin == global_dat.users[i][0]:
                    print(f'Username "{usrnjin}" sudah diambil!')
                    print()
                    break
            if usrnjin != global_dat.users[i][0]:
                break
        while True:
            pwdjin = input('Masukkan password jin : ')
            print()
            if len(pwdjin) < 5 or len(pwdjin) > 25:
                print('Password panjangnya harus 5-25 karakter!')
                print()
            else:
                break
        print('Mengumpulkan sesajen...')
        print('Menyerahkan sesajen...')
        print('Membacakan mantra...')
        print()
        jinbaru = [usrnjin, pwdjin, rolejin]
        print(f'Jin {usrnjin} berhasil dipanggil')
        global_dat.users = konso(global_dat.users, jinbaru)