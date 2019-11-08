#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @name: Bipiti - Basic Information Gathering and Security Scanner
# @author:   hakkitoklu

try:
    import nmap, itertools
    import csv
    import pandas as pd
except ImportError:
    print("Import Error! Please install requirements")


def portscanner(ip):
    default_p = "-sC -sV -O"
    s = input("If you want to specify portscan parameters,type Yes or No (y/n) (Default : -sC -sV -O) : ").lower()
    if s == 'yes' or s == 'y':
        a = input("Specify the parameters (Ex. -sC -sV -O) : ")
        parameters = a
    elif s == 'no' or 'n':
        parameters = default_p
    else:
        print("Invalid input")
    print("\nScanning...\n")

    nm = nmap.PortScanner()
    results = nm.scan(ip, arguments=parameters)
    p_list = []
    v_list = []
    for scans in results['scan']:
        for ports in results['scan'][scans]['tcp']:
            p_list.append((results['scan'][scans]['tcp'][ports]['product']).split())
            v_list.append((results['scan'][scans]['tcp'][ports]['version']).replace('-', ' ').split())
            for t in results['scan'][scans]['tcp'][ports]:
                script_list = []
                try:  # script içeriği olmayan bloklardan gelecek hataları yok saymak için
                    for scripts in results['scan'][scans]['tcp'][ports]['script']:
                        script_list.append(scripts + ":" + "    " + results['scan'][scans]['tcp'][ports]['script'][
                            scripts])  # script başlıkları
                except:
                    pass

    print_output(results)

    find_cve(p_list, v_list)


def find_cve(p_list, v_list):
    # Versiyonu 3.X gibi olanları 3.0-3.9 olarak genişletiyoruz
    for v in v_list:
        if v:
            for vv in v:
                if vv and vv.find('X') != -1:  # Eğer versiyon içerisinde X varsa
                    tmp = vv
                    for i in range(0, 10):
                        vv = tmp
                        vv = vv.replace("X", str(i))
                        v.append(vv)

    tmp_data = []
    # Veri tabanından CVElerin çekilmesi
    with open('cve.csv') as file:
        readcsv = csv.reader(file, delimiter=',')
        for row in readcsv:
            tmp_data.append(row)

    get_data = []

    # Port ve versiyon girdilerine uygun CVElerin alınması
    for i in range(len(p_list)):
        if p_list[i] and v_list[i]:
            for p, v in itertools.zip_longest(p_list[i], v_list[i]):
                p = p_list[i][0]
                if p_list[i][0] is None or v_list[i][0] is None:
                    pass
                elif v is None:
                    v = v_list[i][0]
                    v_list[i].append(v)
                for line in tmp_data:
                    if line[8].find(p) != -1 and line[8].find(v) != -1:
                        get_data.append(line)

    cve_data = []
    # Tekrar eden CVE girdilerini siliyoruz
    for elem in get_data:
        if elem not in cve_data:
            cve_data.append(elem)

    sk = input("\n\n" + str(len(cve_data)) + " possible CVE Details found! Do you want to review? (y/n)").lower()
    if sk == 'y':
        print_cve_output(cve_data)

def print_output(results):
    for scans in results['scan']:
        for ports in results['scan'][scans]['tcp']:
            for t in results['scan'][scans]['tcp'][ports]:
                script_list = []
                try:  # script içeriği olmayan bloklardan gelecek hataları yok saymak için
                    for scripts in results['scan'][scans]['tcp'][ports]['script']:
                        script_list.append(scripts + ":" + "    " + results['scan'][scans]['tcp'][ports]['script'][
                            scripts])  # script başlıkları
                except:
                    pass

            print(str(ports) + ' ' + results['scan'][scans]['tcp'][ports]['state'] + "/" +
                  results['scan'][scans]['tcp'][ports]['name'] + " " + results['scan'][scans]['tcp'][ports][
                      'product'] + "  " + results['scan'][scans]['tcp'][ports]['version'] + " ".join(
                '\n' + i for i in script_list))
        try:
            print("OS : " + results['scan'][scans]['osmatch'][0]['name'])
        except:
            pass
def print_cve_output(output):
    # Çıktı ayarları
    df = pd.DataFrame(output)
    df.rename(
        columns={'cveid': 'CVEID', 'cweid': 'CWEID', 'vul_type': 'Vulnerability Type', 'p_date': 'Publish Date',
                 'u_date': 'Update Date', 'score': 'Score', 'access': 'Access', 'info': 'INFO'}, inplace=True)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_colwidth', 100)
    print(df)