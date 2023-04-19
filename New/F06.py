def bangun(array,role,candi) :
    import random
    from fungsi import lenn 
    kemungkinan = [1,2,3,4,5]
    perluair = random.choice(kemungkinan)
    perlupasir = random.choice(kemungkinan)
    perlubatu = random.choice(kemungkinan)
    if perluair <= array[1][2] and perlubatu <= array[3][2] and perlupasir <= array[2][2] :
        array[1][2] -= perlupasir
        array[2][2] -= perlubatu
        array[3][2] -= perluair
        candi += [[lenn(candi),role,perlupasir,perlubatu,perluair]]
        print("Candi berhasil dibangun")
        print("Sisa yang perlu dibangun: "+str(100-lenn(candi)+1))
    else :
        print("Bahan tidak mencukupi")
    return candi