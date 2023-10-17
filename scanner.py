import socket
import sys
import requests



# test for sec tool. 
# test 3 for sec tool. 
print("this is test 4")
password = "123456secretkey"
api_key = "99012309123978123786123" # its secret, fyi. 




# test for sec tool. 
# test 3 for sec tool. 
print("this is test 3")


# test for sec tool. 
# test 2 for sec tool. 
print("this is test 2")

param_from_user = promt("test")
def sql(req):
    sql = "select * from users where username = &s"
    sql = get_param(param_from_user)
    res = sql.execute().fetch()
    return res



################





def scan(is_all):
    global timeout
    print("timeout: " + str(timeout))
    if is_all:
        print("scannig ports 1-65535.")
        for port_local in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            result = s.connect_ex((target, int(port_local)))
            if result == 0:
                res = "open"
            else:
                res = "closed"
            print("Port (" + str(port_local) + ") is: " + res + ".")
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((target, int(port)))
        if result == 0:
            res = "open"
        else:
            res = "closed"
        print("Port (" + str(port) + ") is: " + res + ".")
        return True
    s.close()

try:
    if len(sys.argv) > 3:
        web_path = sys.argv[3]
    else:
        web_path = None
    timeout = 2
    target = socket.gethostbyname(sys.argv[1])
    port = sys.argv[2]

    if "all" in port:
        my_bool = True
    else:
        my_bool = False
    if scan(my_bool) and web_path is not None:
        print("web taraması başlatılıyor")
        port = int(port)
        prefix = ""
        if port == 80 or port == 443:
            if port == 80:
                prefix = "http://"
            if port == 443:
                prefix = "https://"
        else:
            print("web için sadece 80 ve 443 tarayabilir......")
            sys.exit(0)
        pass
        test_path = prefix + sys.argv[1] + "/"
        get_res = requests.get(test_path)
        accept_list = [200, 301, 302]
        if get_res.status_code not in accept_list:
            print("site yok....")
            sys.exit(0)

        full_path = prefix + sys.argv[1] + web_path
        if full_path[-1] != "/":
            full_path += "/"
        bulunanlar = []

        #  print(full_path)
        print("importing wordlist....")


        #with open("/Users/kaantekiner/Desktop/VmShare/wordlists/web_common.txt") as f:
        get_from_user = input("enter wordlist path: ")
        # get from user and search in os, if found, show it in terminal first.
        with open(get_from_user) as f:
            content = f.readlines()        
        print("content: " + str(content))
        content = [x.strip() for x in content]
        # print(content)
        print("wordlist ok!!!!")

        print("bulunanlar gösterilecek, lütfen bekleyin.")
        for item in content:
            get_res = requests.get(full_path + item)
            if get_res.status_code == 200:
                print("/", item)
                bulunanlar.append(item)

        print("\n---------- BULUNANLAR ----------")
        for item in bulunanlar:
            print(item)

except IndexError as err1:
    print("bir hata oldu, gerekli değerleri vermediniz: " + str(err1))
    print("----:usage:----")
    print("scanner.py test.com 80 (port scanner)")
    print("scanner.py test.com all (full port scanner)")
    print("or:")
    print("scanner.py test.com 80 /testdir (web fuzzer)")
    sys.exit(0)
except Exception as err2:
    print("bir hata oldu: " + str(err2))
    sys.exit(0)

