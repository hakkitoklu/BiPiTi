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
        print("    portscanner   |  Port Scan                   (e.g: -a / --action portscanner --url 192.168.1.1)")
        print("    whois         |  Whois Query                 (e.g: -a / --action whois --url http://www.site.com)")
        print("    maildump      |  Mail Parse                  (e.g: -a / --action mail --url http://www.site.com)")
        print("    linkcrawl     |  Link Parse Query            (e.g: -a / --action links --url http://www.site.com)")
        print("    certificate   |  SSL Certificate Information (e.g: -a / --action certificate --url http://www.site.com)")
        print("    sql           |  SQL Injection               (e.g: -a / --action sql --url http://www.site.com/abc/?id=2)")
        print("    xss           |  XSS Scan                    (e.g: -a / --action xss --url https://www.site.com/abc/abc?query=1)")
        print("\n\n\n")

