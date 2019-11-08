#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @name: Bipiti - Basic Information Gathering and Security Scanner
# @author:   hakkitoklu

class usage:
    def banner(self):
        x = "_" * 55
        print(x)
        print("""

  _______ __ _______ __ _______ __ 
 |   _   |__|   _   |__|       |__|
 |.  1   |  |.  1   |  |.|   | |  |
 |.  _   |__|.  ____|__`-|.  |-|__|
 |:  1    \ |:  |        |:  |     
 |::.. .  / |::.|        |::.|     
 `-------'  `---'        `---'     


Basic Information Gathering and Security Scanner
            HAKKI TOKLU

""")
        print(x)

    def basic(self, _exit_=True):
        self.banner()
        print("Usage :\n")
        print("    portscanner   |  Port Scan                   (e.g: --action portscanner --url 192.168.1.1)")
        print("    whois         |  Whois Query                 (e.g: --action whois --url http://www.site.com)")
        print("    mail          |  Mail Parse                  (e.g: --action mail --url http://www.site.com)")
        print("    links         |  Link Parse Query            (e.g: --action links --url http://www.site.com)")
        print("    certificate   |  SSL Certificate Information (e.g: --action certificate --url http://www.site.com)")
        print(
            "    sql           |  SQL Injection               (e.g: --action sql --url http://www.site.com/abc/?id=2)")
        print(
            "    xss           |  XSS Scan                    (e.g: --action xss --url https://www.site.com/abc/abc?query=1)")
        print("\n\n\n")

