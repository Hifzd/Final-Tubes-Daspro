def idfind(lis):
    for i in range(len(lis)):
        if i != 0:
            if int(lis[i][0]) > i:
                break
    else:
        # executed if the loop completes without a break statement
        return len(lis)
    return i
    
def insert(lis, value, ind):
    newlis = []
    inserted = False
    for i in range(len(lis)):
        if i == ind:
            newlis = konso(newlis, value)
            inserted = True
        newlis = konso(newlis, lis[i])
    if not inserted:
        newlis = konso(newlis, value)
    return newlis

def konso(lis, value):
    newlis = [0 for i in range(len(lis)+1)]
    for i in range(len(lis)):
        newlis[i] = lis[i]
    newlis[len(lis)] = value
    return newlis

a = [['0', 'adwa', 'adwawd'], [1, 'awd', 'fawawf'], ['4', 'tes', 'tis'], ['5', 'blabla', 'aniw']]

for i in range(7):
    b = idfind(a)
    a = insert(a, [b, 'AAAAAA', 'BBBBB'], b)

print(a)