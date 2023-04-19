import F13
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
        break
    else:
        commands.run(masukan)
        print()
        print(global_dat.users)