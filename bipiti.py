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


try:
    from utils import portscan
    from utils import sql
    from utils import xss
    from utils import maildrumper
    from utils import whois
    from utils import linkcrawler
    from utils import certificate
    from usage import *
    import argparse
except ImportError as e:
    print(e)

u=usage()

def main():

    __version__="1.0"
    ap=argparse.ArgumentParser()
    ap.add_argument("-a","--action",required=True,help="Process Name")
    ap.add_argument("-t","--target",required=True,help="Target URL/IP")
    ap.add_argument("-v","--version",action='version',version=__version__)

    args=ap.parse_args()
    target=args.target
    action=args.action

    u.basic()

    if target and action:
        if action != ("portscanner"):
            print(str(target).split("/")[2])
        print("[+]TARGET : ", target, "\n==========================")

        if action == "sql":
            sql.find_sql(target)

        elif action == "whois":
            whois.whoisQuery(target)


        elif action == "portscanner":
            print("Scaning port on " + str(target))
            portscan.portscanner(target)

        elif action == "xss":
            xss.find_xss(target)

        elif action == "maildump":
            maildrumper.dump(target)

        elif action == "linkcrawl":
            linkcrawler.crawl(target)

        elif action == "certificate":
            if str(target).split("/")[2]:
                target = str(target).split("/")[2]
            elif str(target).split("/")[3]:
                target = str(target).split("/")[2]

            print(target)
            certificate.certificateInformation(target)
        else:
            exit()


if __name__ == "__main__":
	try:
	    main()
	except KeyboardInterrupt as e:
		exit(print('Exiting...'))