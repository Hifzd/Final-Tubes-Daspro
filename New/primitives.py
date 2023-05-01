def splitter (DataString, pemisah):
    # SPESIFIKASI
    # Membaca keseluruhan file data dari file dalam bentuk string
    # Mengembalikan sebuah dataset yang berbentuk matriks
    # Fungsi ini akan bekerja secara rekursif karena akan memanggil fungsi ini sendiri

    # KAMUS LOKAL
    # DataString    : str (berisi bentuk string dari array yang ingin dipisahkan tiap elemennya)
    # pemisah   : char (mark pemisah antar elemen, akan berganti ketika rekursi)
    # pemisah1, pemisah2 : char (merupakan mark pemisah antar elemen dalam dataset)
    # count, i  : int
    # baris     : array (menyimpan elemen dari database)
    #             mulanya berupa array of string, setelah splitted rekursi menjadi array of array (matriks)

    # ALGORITMA
    if len(DataString) == 0: # Basis rekursi
        return []

    else:
        # pemisah 1 adalah untuk iterasi pertama, yakni memisahkan setiap baris dalam data ke dalam array
        # pemisah 2 untuk rekursi, memisahkan data yang ada dalam setiap baris ke dalam arrah, sehingga terbentuk 'kolom'
        pemisah1 = '\n'
        pemisah2 = ';' or ','
        count = 1
        i = 0
        
        # Menghitung banyaknya jumlah data yang ingin dipisah
        count = 1   # count mulanya sudah bernilai 1 karena jumlah data akan lebih banyak 1 dari pemisahnya
        for huruf in DataString:
            if huruf == pemisah:
                count += 1

        baris = ["" for i in range(count)]

        # Proses pemasukkan data ke dalam array baris
        i = 0
        for huruf in DataString:
            if huruf == pemisah:
                i+=1
            else:
                baris[i] += huruf

        if pemisah == pemisah1: # Rekursi akan dijalankan hanya untuk penggunaan pertama kali, ketika (pemisah adalah enter)
            return [splitter(baris[i], ';' or ',') for i in range(len(baris))]
            # Pemisahan elemen dilakukan lagi
            # string berisi dataset -> data tiap baris dipisah -> data tiap kolom dipisah
        else:
            return baris

def pjglist(lis):
    # SPESIFIKASI
    # Menghitung jumlah elemen dalam sebuah array, jika lis adalah matriks, maka akan dihitung jumlah baris

    # KAMUS LOKAL
    # listring : str (bentunk string dari array)
    # count    : int

    # ALGORITMA
    listring = str(lis)
    count = 0
    if len(listring) == 2: # entuk string dari array yang sebesar 2 hanya berisi bracket [], sehingga data kosong
        return 0
    else:
        if listring[1] == '[': # Pemeriksaan apakah lis adalah yang diukur array atau matriks
            for i in range(1,len(listring)):
                if listring[i] == '[': # Menghitung seberapa banyak array (baris) di dalam array induk (matriks)
                    count += 1
            return count
        else: # Apabila yang dihitung adalah array
            for i in range(1,len(listring)): # Menghitung banyaknya pemisah
                if listring[i] == ',':
                    count += 1
            return count + 1    # Banyak elemen akan lebih banyak 1 dari pemisah

def konso(lis, value):
    # SPESIFIKASI
    # Menambahkan sebuah elemen ke dalam sebuah array

    # KAMUS LOKAL
    # lis : array (dapat juga berupa array of array (matriks))
    # value : dapat berupa apa saja
    # newlis : array (dapat juga berupa array of array)
    # i = int
 
    # ALGORITMA
    newlis = [0 for i in range(pjglist(lis)+1)] # Newlis akan memiliki kapasitas lebih banyak 1 dari lis
    for i in range(pjglist(lis)): # Memasukkan tiap elemen lis ke dalam newlis
        newlis[i] = lis[i]
    newlis[pjglist(lis)] = value # Elemen terujung dari newlis akan diisi oleh elemen yang ingin ditambahkan
    return newlis # Akan dikembalikan array baru yang sudah ditambahkan elemen 'value'

def hitungjin(data, golongan):
    # SPESIFIKASI
    # Menghitung dan mengembalikan jumlah jumlah jenis jin tertentu dalam sebuah database (users)
    
    # KAMUS LOKAL
    # count : int
    # glg : str (digunakan untuk menghitung jenis jin tertentu)
    # data : array of array (berformat/seperti database users)
    #        kolom 0 username, kolom 1 password, kolom 2 role 

    # ALGORITMA
    count = 0
    if golongan == 'all': # Bila yang ingin dihitung adalah semua jin
        for i in range(pjglist(data)):
            if data[i][2] == 'jin_pengumpul' or data[i][2] == 'jin_pembangun':
                count+=1
    else: # Bila ingin menghitung jumlah jin dengan jenis tertentu
        for i in range(pjglist(data)):
            if data[i][2] == golongan:
                count+=1
    return count

def popp(lis,value):
    # SPESIFIKASI
    # Menghilangkan/menghapuskan sebuah data dari sebuah database

    # KAMUS LOKAL
    # newlis : array (dapat juga berupa array of array) (akan menggantikan lis)
    # i,j : int (i merujuk pada indeks array lama, j pada indeks array baru)
    # lis : array (dapat berupa array of array)
    # value : dapat berupa apa saja

    # ALGORITMA
    newlis = [0 for i in range(pjglist(lis)-1)] # Mmebuat array dengan kapasitas lebih sedikit 1
    j = 0
    # Proses pemasukan elemen selain 'value' ke dalam array baru
    for i in range(pjglist(lis)):
        if lis[i] != value:
            newlis[j] = lis[i]
            j+=1
            # j hanya bertambah saat ruang ke-i dalam newlis sudah terisi
    return newlis

def idfind(lis):
    # SPESIFIKASI
    # Mencari id terkecil candi yang belum ada dalam database candi

    # KAMUS LOKAL
    # lis : array of array (akan diisi database candi dimana kolom 1 adalah id) 
    # i : int (akan digunakan untuk menandakan id candi terkecil yang belum ada)

    # ALGORITMA
    for i in range(1,pjglist(lis)): # dimulai dari baris 1 karena baris 0 berisi judul
        if int(lis[i][0]) > i:      # jika id candi pada baris ke-i lebih besar dari i itu sendiri,
            break                   # disimpulkan bahwa ada id yang 'terlewat'
    
    # Fungsi akan menmenbalikan indeks paling terakhir jika tidak terdapat id yang terlewat
    else:
        return pjglist(lis)
    # Fungsi akan mengembalikan id terakhir (terkecil) yang terlewat/belum ada
    return i
    
def insert(lis, value, ind):
    # SPESIFIKASI
    # Memasukkan sebuah data ke dalam sebuah database dalam tempat yang diinginkan
    
    # KAMUS LOKAL
    # newlis : array (berupa array baru yang akan ditambahkan data baru)
    # inserted : bool (menandakan apakah elemen sudah dimasukkan ke dalam array baru)
    # i : int
    # lis : array (database awal)
    # value : data yang indin dimasukkan
    # ind : int (indeks data tersebut dimasukkan)

    # ALGORITMA
    newlis = []
    inserted = False
    for i in range(pjglist(lis)): # Proses memasukkan elemen array lama kepada yang baru
        if i == ind: # Candi baru akan ditambahkan di baris ke-i sesuai dengan Id nya
            newlis = konso(newlis, value)
            inserted = True
        newlis = konso(newlis, lis[i])
    if not inserted: # Bila mencapai akhir tetapi data baru belum dimasukkan, maka data akan ditambahkan di paling akhir
        newlis = konso(newlis, value)
    return newlis