import requests

def find_sql(target):
    sqlFile = open("data/sqlpayload.txt", "r")
    sqlPayload = sqlFile.readlines()
    sqlFile.close()
    if "=" in target:
        d = str(target).find('=')
        for i in sqlPayload:
            try:
                i = i.split("\n")[0]
                text = str(target[0:d + 1]) + str(i)
                result = requests.get(text)
                if int(result.status_code) == 200:
                    print("[VULNERABLE]Sqli paylaod: ", str(i))
                    print("[VULNERABLE]Sqli URL: ", text)
                else:
                    print("[NOT VULNERABLE]Sqli paylaod: ", str(i))
                    print("[NOT VULNERABLE]Sqli URL: ", text)
            except:
                pass
    else:
        print("[-]Sqli isn't available")