import glob
import os


def add_if_top10(filename, top10 = [["", 0]]):
    size = os.path.getsize(filename)
    if size > min(top10, key= lambda x: x[1])[1]:
        top10.append([filename, size])
        if len(top10) == 11:
            top10.remove(min(top10, key= lambda x: x[1]))

def get_top10_files():
    top10 = [["", 0]]
    root_dir = "/Users/felipemaion/Downloads"
    for filename in glob.iglob(root_dir + '**/*', recursive=True):
        add_if_top10(filename, top10)
    print(*top10, sep="\n")
    return top10

get_top10_files()