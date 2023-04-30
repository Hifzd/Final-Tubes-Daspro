from primitives import hitungjin, pjglist, konso
import global_dat

def pembuat_candi():
    # SPESIFIKASI
    # Mencari jin pembangun yang ada pada database candi
    # Mengembalikan matriks yang berisi 1 kolom username para jin dan 1 kolom jumlah candi yang dibangun olehnya

    # KAMUS
    # i, j, count : int
    # builder : array of array (kolom 0 berisi nama jin, kolom 1 jumlah candi yang dibangun olehnya)
    # unique : boolean

    # ALGORITMA 
    global global_dat
    builder = []
    # Menambahkan jin pembangun melalui database candi (memeriksa kolom pembangun candi)
    for i in range(1,pjglist(global_dat.candi)):
        unique = True
        if pjglist(builder) > 0:
            # Memeriksa apakah username sudah terdapat pada matriks builder
            for j in range(pjglist(builder)):
                if builder[j][0] == global_dat.candi[i][1]:
                    unique = False
        if unique:
            # Jin dimasukkan ke dalam matriks builder dan diinisialisasi jumlah candi terbangunnya 0
            builder = konso(builder,[global_dat.candi[i][1], 0])

    # Menambahkan jin melalui data jin
    for i in range(pjglist(global_dat.users)):
        if global_dat.users[2] == 'jin_pembangun':
            unique = True
            for j in range(pjglist(builder)):
                # Memeriksa apakah username sudah terdapat pada matriks builder
                if builder[j][0] == global_dat[i][0]:
                    unique = False
            if unique:
                # Jin dimasukkan ke dalam matriks builder dan diinisialisasi jumlah candi terbangunnya 0
                builder = konso(builder,[global_dat.users[i][0], 0])

    for i in range(pjglist(builder)):
        count = 0
        # Menghitung banyaknya candi yang dibangun oleh jin yang terdaftar dalam matriks builder
        for j in range(1,pjglist(global_dat.candi)):
            if builder[i][0] == global_dat.candi[j][1]:
                count += 1
        builder[i][1] = count
        # Memasukkan jumlah candi yang dibangun oleh builder[i][0]
    return (builder)
    # Mengembalikan sebuah matriks yang berisi data pembangun candi dan jumlah candi yang dibangun

def RankJin(adj):
    # SPESIFIKASI
    # Menentukan jin terajin atau termalas (ditentukan oleh 'adj') dari para jin pembangun dan-
    # data candi yang terbangun (mengantisipasi jika ada jin yang berubah role)

    # KAMUS
    # selected_jin : str
    # data_pembuat : array of array (kolom 0 berisi nama jin, kolom 1 jumlah candi yang dibangun olehnya)
    # MinMax : int (Menyimpan data jumlah candi yang terbangun)
    #          (menyimpan nilai terbesar jika adj 'Rajin', nilai terkecil jika adj 'Malas')
    # adj : str

    # ALGORITMA
    # Inisialisasi variabel
    selected_jin = '-'
    data_pembuat = pembuat_candi()

    if pjglist(data_pembuat) > 0: # Memvalidasi apakah sudah ada jin pembangun & candi
        data_pembuat = pembuat_candi()
        # Jin yang paling awal dijadikan jin yang terpilih
        selected_jin, MinMax = data_pembuat[0][0], data_pembuat[0][1]

        # Mengupdate jin yang terpilih melalui 2 parameter:
        # kerajinan dan leksikografis calon jin terpilih dibanding jin yang terpilih sebelumnya
        #  
        for i in range(pjglist(data_pembuat)):
            if adj == 'Rajin' and data_pembuat[i][1] >= MinMax and data_pembuat[i][0] < selected_jin:
                # jika yang diminta jin terajin, dicari kontribusi terbesar lalu leksikografis terendah
                selected_jin = data_pembuat[i][0]
            elif adj == 'Malas' and data_pembuat[i][1] <= MinMax and data_pembuat[i][0] > selected_jin:
                # jika yang diminta jin termalas, dicari kontribusi terkecil lalu leksikografis terendah
                selected_jin = data_pembuat[i][0]

    return selected_jin

def laporanjin():
    # SPESIFIKASI
    # Mengeluarkan tampilan informasi yang terkait dengan jin

    # KAMUS LOKAL
    # Tidak ada variabel lokal

    # Algoritma
    global global_dat
    # Memastikan apakah user sesuai
    if global_dat.current_user[2] != 'bandung_bondowoso':
        print('Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.')

    else:
        # Menampilkan informasi dengan memanggil fungsi fungsi dengan parameter yang
        print('> Total Jin:', hitungjin(global_dat.users, 'all'))
        print('> Total Jin Pengumpul:', hitungjin(global_dat.users, 'jin_pengumpul'))
        print('> Total Jin Pembangun:', hitungjin(global_dat.users, 'jin_pembangun'))
        print('> Jin Terajin :', RankJin('Rajin'))
        print('> Jin Termalas:', RankJin('Malas'))
        print('> Jumlah Pasir:', global_dat.bahan_bangunan[1][2],'unit')
        print('> Jumlah Batu :', global_dat.bahan_bangunan[2][2],'unit')
        print('> Jumlah Air  :', global_dat.bahan_bangunan[3][2],'unit')