from fake_useragent import UserAgent
import requests

def find_xss(target):
    ua=UserAgent()
    header = {'User-Agent': str(ua.random)}
    attack_type = input("Type attack POST OR GET ? (p/g) : ")
    # GET REQUEST
    if attack_type == "g":
        try:
            site = target
            req = requests.get(site);
            print("url is alive" + "\n")
        except:
            print("url does't respond ")

        try:
            payload_file = 'data/xsspayload.txt'
            payload_open = open(payload_file, "r")
        except FileNotFoundError:
            print(
                "your file " + payload_file + " is not found, try again !")
        print("Attacking is in process\n")
        time.sleep(1)

        payload_open = open(payload_file, "r")
        for payload in payload_open:
            if payload in requests.get(site + payload, headers=header).text:
                print("XSS  DETECTED: " + requests.get(site + payload, headers=header).target)
            else:
                print("NO RESULTS FOR : " + payload)
    else:
        print("Unknown answer please enter g or p")