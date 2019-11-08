#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    BiPiTi - Basic Information Gathering and Security Scanner
    Copyright (C) 2019 HAKKI TOKLU

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>."""

"""This app is coded for educational purpose. Please use for good! Otherwise it is not my responsibility."""

try:
    from bs4 import BeautifulSoup
    import re
    import requests
    import whois
    import ssl
    import socket
    import time
    from fake_useragent import UserAgent
    import urllib.request
    from urllib.error import HTTPError, URLError
    import portscan
    from usage import *
    import argparse
except ImportError:
    print("Import Error! Please install requirements")

u=usage()

def main():

    __version__="1.0"
    ap=argparse.ArgumentParser()
    ap.add_argument("--action",required=True,help="Process Name")
    ap.add_argument("--url",required=True,help="Target URL/IP")
    ap.add_argument("--version",action='version',version=__version__)

    args=ap.parse_args()
    url=args.url
    action=args.action
    """action = input("Action :")
    url = input("URL : ")"""

    u.basic()

    if url and action:
        if action != ("portscanner"):
            print(str(url).split("/")[2])
        print("[+]URL:", url, "\n==========================")

        if action == "sql":
            sql(url)

        elif action == "whois":
            whoisQuery(url)


        elif action == "portscanner":
            print("Scaning port on " + str(url))
            portscan.portscanner(url)

        elif action == "xss":
            xss(url)

        elif action == "maildump":
            maildump(url)

        elif action == "linkcrawl":
            linkcrawl(url)

        elif action == "certificate":
            if str(url).split("/")[2]:
                url = str(url).split("/")[2]
            elif str(url).split("/")[3]:
                url = str(url).split("/")[2]

            print(url)
            certificateInformation(url)
        else:
            exit()



def whoisQuery(url):
    query = whois.whois(url)
    print("[+]Domain: ", query.domain)
    print("[+]Update time: ", query.get('updated_date'))
    print("[+]Expiration time: ", query.get('expiration_date'))
    print("[+]Name server: ", query.get('name_servers'))
    print("[+]Email: ", query.get('emails'))

def certificateInformation(url):
    try:
        context = ssl.create_default_context()
        server = context.wrap_socket(socket.socket(), server_hostname=url)
        server.connect((url, 443))
        certificate = server.getpeercert()
        print("[+]Certificate Serial Number: ", certificate.get('serialNumber'))
        print("[+]Certificate SSL Version:", certificate.get('version'))
        print("[+]Certificate:", certificate)
    except:
        pass


def sql(url, dosyaAdi):
    # örnek url  = http://www.patopowerparts.com/detalle-producto.php?id=999999.9
    # örnek url  = https://aagensoc.org/cemeteryRecords.php?cid=114
    # örnek url  = http://kiranbooks.com/magazines/plan_details.php?id=999999.9 (olumsuz)
    sqlFile = open("data/sqlpayload.txt", "r")
    sqlPayload = sqlFile.readlines()
    sqlFile.close()
    if "=" in url:
        d = str(url).find('=')
        for i in sqlPayload:
            try:
                i = i.split("\n")[0]
                text = str(url[0:d + 1]) + str(i)
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


def xss(url):
    ua=UserAgent()
    header = {'User-Agent': str(ua.random)}
    attack_type = input("Type attack POST OR GET ? (p/g) : ")
    # GET REQUEST
    if attack_type == "g":
        try:
            site = url
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
                print("XSS  DETECTED: " + requests.get(site + payload, headers=header).url)
            else:
                print("NO RESULTS FOR : " + payload)
    else:
        print("Unknown answer please enter g or p")


def maildump(url):
    imageExt = ["jpeg", "exif", "tiff", "gif", "bmp", "png", "ppm", "pgm", "pbm", "pnm", "webp", "hdr", "heif",
                "bat",
                "bpg", "cgm", "svg"]
    print("Searching emails... please wait")
    ua = UserAgent()
    print("This operation may take several minutes")
    try:
        count = 0
        listUrl = []
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': ua.random
            })

        try:
            conn = urllib.request.urlopen(req, timeout=5)

        except TimeoutError:
            raise ValueError('Timeout ERROR')

        except (HTTPError, URLError):
            raise ValueError(url + '--- Bad Url...')

        status = conn.getcode()
        contentType = conn.info().get_content_type()

        if (status != 200 or contentType == "audio/mpeg"):
            raise ValueError(url + '--- Bad Url...')

        html = conn.read().decode('utf-8')

        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", html)

        for email in emails:
            if (email not in listUrl and email[-3:] not in imageExt):
                count += 1
                print(str(count) + " - " + email)
                listUrl.append(email)
                print(email)

        soup = BeautifulSoup(html, "lxml")
        links = soup.find_all('a')

        print("They will be analyzed " + str(len(links) + 1) + " Urls...")
        time.sleep(2)

        for tag in links:
            link = tag.get('href', None)
            if link is not None:
                try:
                    if (link[0:4] == 'http'):
                        req = urllib.request.Request(
                            link,
                            data=None,
                            headers={
                                'User-Agent': ua.random
                            })

                        try:
                            f = urllib.request.urlopen(req, timeout=10)

                        except TimeoutError:
                            print(url + "--- Bad Url..")
                            time.sleep(2)
                            pass

                        except (HTTPError, URLError):
                            print(url + "--- Bad Url..")
                            time.sleep(2)
                            pass

                        status = f.getcode()
                        contentType = f.info().get_content_type()

                        if (status != 200 or contentType == "audio/mpeg"):
                            print(url + "--- Bad Url..")
                            time.sleep(2)
                            pass

                        s = f.read().decode('utf-8')

                        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", s)

                        for email in emails:
                            if (email not in listUrl and email[-3:] not in imageExt):
                                count += 1
                                print(email)
                                listUrl.append(email)

                # Sigue si existe algun error
                except Exception:
                    pass

        print("")
        print("***********************")
        print("Finish: " + str(count) + " emails were found")
        print("***********************")


    except KeyboardInterrupt:
        pass

    except Exception as e:
        pass


def linkcrawl(url):
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    tags = soup.find_all('a')
    for tag in tags:
        print(tag.get('href'))


if __name__ == "__main__":
	try:
	    main()
	except KeyboardInterrupt as e:
		exit(print('Exiting...'))