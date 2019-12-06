# bipiti
*BiPiTi - Basic Information Gathering and Security Scanner*

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) ![Version: v1.0](https://img.shields.io/badge/version-v1.0-blue) 

**Introduction**<br/><br/>
BiPiTi is a basic information gathering tool consist of main infomation gathering scripts and additional basic sql and xss vulnerability scanner scripts.
It is coded for self development and educational purpose. Please do not consider this tool as a professional work. In this repository, my intent is coding tools which I think will improve me, and share these tools.

<br/><br/>
**Features**
- Whois Lookup
- Mail Dump
- Link Crawl
- SSL Certificate Info
- SQL Injection
- XSS
- Port Scanner
- CVE Details Finder related with Port Scanner

<br/><br/>
**Installation**
```
$ git clone https://github.com/hakkitoklu/bipiti.git
$ cd bipiti
$ pip3 install -r requirements.txt 
```

<br/>**Usage**
```
$ python3 bipiti.py -a whois -t https://www.example.com
$ python3 bipiti.py -a maildump -t https://www.example.com
$ python3 bipiti.py -a linkcrawl -t https://www.example.com
$ python3 bipiti.py -a certificate -t https://www.example.com
$ python3 bipiti.py -a sql -t https://www.example.com
$ python3 bipiti.py -a xss -t https://www.example.com
$ python3 bipiti.py -a portscanner -t https://www.example.com
```
