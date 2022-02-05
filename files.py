from encodings import utf_8


def read():
    numbers = []
    with open("./files/numbers.txt","r",encoding="utf_8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)
def write():
    names = ['sdsds','trtrt','eret']
    with open("./files/names.txt","w",encoding="utf_8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
def append():
    names = ['okokok','gdgdgdgd','opfkfkdk']
    with open("./files/names.txt","a",encoding="utf_8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
def run():
    append()
if __name__ == '__main__':
    run()