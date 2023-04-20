import F12
import F13
import F16
import argparse
import commands
import global_dat

parser = argparse.ArgumentParser()
parser.add_argument("folder", default='', nargs='?')
args = parser.parse_args()

isFoldr_exist = F13.valid(args.folder)

if isFoldr_exist:
    F13.load_data(args.folder)

while isFoldr_exist:
    masukan = input(">>> ")
    if masukan == 'exit':
        F16.ext()
        break
    elif masukan == 'ayamberkokok' and global_dat.current_user[0] == 'Roro':
        F13.ayamberkokok()
        break
    else:
        commands.run(masukan)
        print()