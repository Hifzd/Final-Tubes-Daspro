import global_dat

def kumpul() :
    global global_dat

    kemungkinan = [1,2,3,4,5]
    dapatpasir = gather()
    dapatbatu = gather()
    dapatair = gather()
    
    global_dat.bahan_bangunan[1][2] = int(global_dat.bahan_bangunan[1][2])+dapatpasir
    global_dat.bahan_bangunan[2][2] = int(global_dat.bahan_bangunan[2][2])+dapatbatu
    global_dat.bahan_bangunan[3][2] = int(global_dat.bahan_bangunan[3][2])+dapatair
    print("Jin menemukan "+str(dapatpasir)+" pasir, "+str(dapatbatu)+" batu, dan "+str(dapatair)+" air.")

def gather():
    import random
    kemungkinan = [1,2,3,4,5]
    return random.choice(kemungkinan)