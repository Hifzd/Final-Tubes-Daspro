from F14 import save

def ext():
    YorN = 'a'
    while True:
        YorN = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')
        if YorN == 'Y' or YorN == 'y':
            save()
            break
        elif YorN == 'N' or YorN =='n':
            break