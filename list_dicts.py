from socket import if_nameindex


def run():
    print("test")
    list = ["wewe",234,"kljkj"]
    dict = {"one":"test01","two":"test02"}
    super_list = [
        {"one":"test01","two":"test02"},
        {"one":"test01","two":"test02"}
    ]
    super_dict = {
        "n01":["wewe",234,"kljkj"],
        "n02":["wewe",234,"kljkj"]
    }
    for key, value in super_dict.items():
        print(key, '-', value)

if __name__ == '__main__':
    run()