from functools import reduce


def run():
    my_list = [2,2,2,25]
    value_mult = reduce(lambda x, y : x*y,my_list)
    print(value_mult)

if __name__ == '__main__':
    run()