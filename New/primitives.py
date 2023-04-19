def splitter (opfile, pemisah):
    if len(opfile) == 0:
        return []

    else:
        pemisah1 = '\n'
        pemisah2 = ';' or ','
        count = 1
        for chr in opfile:
            if chr == pemisah:
                count += 1
        
        baris = ["" for i in range(count)]
        i = 0

        for chr in opfile:
            if chr == pemisah:
                i+=1
            else:
                baris[i] += chr

        if pemisah == pemisah1:
            return [splitter(baris[i], ';') for i in range(len(baris))]
        else:
            return baris

def pjglist(lis):
    listring = str(lis)
    count = 0
    if len(listring) == 2:
        return 0
    else:
        if listring[1] == '[':
            for i in range(1,len(listring)):
                if listring[i] == '[':
                    count += 1
            return count
        else:
            for i in range(1,len(listring)):
                petik = 0
                if listring[i] == "'":
                    if petik == 1:
                        petik = 0
                    else:
                        petik = 1
                if listring[i] == ',' and petik == 0:
                    count += 1
            return count + 1

def konso(lis, value):
    newlis = [0 for i in range(pjglist(lis)+1)]
    for i in range(pjglist(lis)):
        newlis[i] = lis[i]
    newlis[pjglist(lis)] = value        
    return newlis

def hitungjin(data, golongan):
    count = 0
    glg = golongan
    if golongan == 'all':
        for i in range(pjglist(data)):
            if data[i][2] == 'jin_pengumpul' or data[i][2] == 'jin_pembangun':
                count+=1
    else: 
        for i in range(pjglist(data)):
            if data[i][2] == golongan:
                count+=1
    return count

def popp(lis,value):
    newlis = [0 for i in range(pjglist(lis)-1)]
    j = 0
    for i in range(pjglist(lis)):
        if lis[i] != value:
            newlis[j] = lis[i]
            j+=1
    return newlis