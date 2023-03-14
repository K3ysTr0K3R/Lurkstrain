#!/bin/python3

import os
import time
import socket
import requests
from colorama import Fore as color
from concurrent.futures import ThreadPoolExecutor

#host = socket.gethostbyname('185.88.180.183')

B = color.BLUE
C = color.CYAN
Y = color.YELLOW
M = color.MAGENTA
R = color.RED
G = color.GREEN

time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

def restarts():
    os.system("python3 wordspread.py")

def banner():
    os.system('clear')
    print(f"{G}")
    print(" /$$       /$$   /$$ /$$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$")
    print("| $$      | $$  | $$| $$__  $$| $$  /$$/ /$$__  $$|__  $$__/| $$__  $$ /$$__  $$|_  $$_/| $$$ | $$")
    print("| $$      | $$  | $$| $$  \ $$| $$ /$$/ | $$  \__/   | $$   | $$  \ $$| $$  \ $$  | $$  | $$$$| $$")
    print("| $$      | $$  | $$| $$$$$$$/| $$$$$/  |  $$$$$$    | $$   | $$$$$$$/| $$$$$$$$  | $$  | $$ $$ $$")
    print("| $$      | $$  | $$| $$__  $$| $$  $$   \____  $$   | $$   | $$__  $$| $$__  $$  | $$  | $$  $$$$")
    print("| $$      | $$  | $$| $$  \ $$| $$\  $$  /$$  \ $$   | $$   | $$  \ $$| $$  | $$  | $$  | $$\  $$$")
    print("| $$$$$$$$|  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/   | $$   | $$  | $$| $$  | $$ /$$$$$$| $$ \  $$")
    print("|________/ \______/ |__/  |__/|__/  \__/ \______/    |__/   |__/  |__/|__/  |__/|______/|__/  \__/")
    print("")
    print(f"{C}[!!!]{C} {B}Coded By: {C}K3ysTr0K3R{B}")
    print(f"{C}[!!!]{C} {B}Instagram: {C}1_k3ystr0k3r_1{B}")
    print(f"{C}[!!!]{C} {B}Github: {C}https://github.com/K3ysTr0K3R/{B}")
    print(f"{C}[!!!]{C} {B}Welcome to {C}Lurkstrain{C}")
    print(f"{C}[!!!]{C} {B}Lurkstrain v{B}1.0{C}")
    print(f"{C}[!!!]{C} {B}Time: {C}{time}{B}")
banner()
option = input(f"""
{B}╔══════════════════════════════════════╗
{B}║ {Y}({G}1{Y}) {C}WordPress-Finder                 {B}║                           
{B}║ {Y}({G}2{Y}) {C}cPanel-Finder                    {B}║                           
{B}║ {Y}({G}3{Y}) {C}phpmyadmin-Finder                {B}║                           
{B}║ {Y}({G}4{Y}) {C}admin-Finder                     {B}║                           
{B}║ {Y}({G}5{Y}) {C}robots.txt-Finder                {B}║                           
{B}║ {Y}({G}6{Y}) {C}sitemap.xml-Finder               {B}║                     
{B}║ {Y}({G}7{Y}) {C}All-In-One-Scanner               {B}║
{B}╚══════════════════════════════════════╝

{Y}({B}!{Y}) {G}Enter your option to scan your target{B}:{R} """)
banner()
print("")
print(f"{Y}({B}!{Y}) {G}Option {R}{option} {G}selected")
if option == "1":
    def wordpress_check(ip_address):
        dot = ip_address.rfind(".")
        IP = ip_address[:dot + 1]
        for i in range(1, 256):
            ip = IP + str(i) 
            url = f"http://{ip}/wp-login.php"
            try:
                response = requests.get(url, timeout=1, allow_redirects=False)
                if response.status_code == 200:
                    print(f"{Y}[{B}+{Y}] {C}WordPress exists{B}:{G}", url)
            except:
                print(f"{Y}[{R}~{Y}] {R}WordPress does not exist on{Y}", ip)
    ip_address = input(f"{Y}({B}!{Y}) {G}Enter IP Address to check for WordPress{B}:{R} ")
    thread_count = int(input(f"{Y}({B}!{Y}) {G}Enter number of threads{B}:{R} "))
    print("")
    print("=================================================")
    print(f"{Y}[{C}*{Y}] {G}Starting scan{B}: {Y}{time}")
    print("=================================================")
    print("")
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.submit(wordpress_check, ip_address)
    print(f"{Y}[{C}*{Y}] {G}Scan completed{B}: {Y}{time}")
    print("")
    try:
        restart = input(f"{Y}[{C}*{Y}] {G}Press any button to restart the script or hit control+C to exit")
        restarts()
    except KeyboardInterrupt:
        print(f"{Y}[{C}*{Y}] {G}Exiting")
        exit()

if option == "2":
    def cpanel_check(ip_address):
        dot = ip_address.rfind(".")
        IP = ip_address[:dot + 1]
        for i in range(1, 256):
            ip = IP + str(i) 
            url = f"http://{ip}/cpanel"
            try:
                response = requests.get(url, timeout=1, allow_redirects=False)
                if response.status_code == 200:
                    print(f"{Y}[{B}+{Y}] {C}cPanel exists{B}:{G}", url)
            except Exception:
                print(f"{Y}[{R}~{Y}] {R}cPanel does not exist on{Y} {ip}")
    ip_address = input(f"{Y}({B}!{Y}) {G}Enter IP Address to check for cPanel{B}:{R} ")
    thread_count = int(input(f"{Y}({B}!{Y}) {G}Enter number of threads{B}:{R} "))
    print(f"{Y}[{C}*{Y}] {G}Starting scan{B}: {Y}{time}")
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.submit(cpanel_check, ip_address)
    print(f"{Y}[{C}*{Y}] {G}Scan completed{B}: {Y}{time}")
    print("")
    try:
        restarts = input(f"{Y}[{C}*{Y}] {G}Press any button to restart the script or hit control+C to exit")
        restart()
    except KeyboardInterrupt:
        print(f"{Y}[{C}*{Y}] {G}Exiting")
        exit()

if option == "3":
    def phpmyadmin_check(ip_address):
        dot = ip_address.rfind(".")
        IP = ip_address[:dot + 1]
        for i in range(1, 256):
            ip = IP + str(i)
            url = f"http://{ip}/phpmyadmin"
            try:
                response = requests.get(url, timeout=1, allow_redirects=False)
                if response.status_code == 200:
                    print(f"{Y}[{B}+{Y}] {C}phpmyadmin exists{B}:{G}", url)
            except Exception:
                print(f"{Y}[{R}~{Y}] {C}phpmyadmin does not exist on{Y} {ip}")
    ip_address = input(f"{Y}({B}!{Y}) {G}Enter IP Address to check for phpmyadmin{B}:{R} ")
    thread_count = int(input(f"{Y}({B}!{Y}) {G}Enter number of threads{B}:{R} "))
    print(f"{Y}[{C}*{Y}] {G}Starting scan{B}: {Y}{time}")
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.submit(phpmyadmin_check, ip_address)
    print(f"{Y}[{C}*{Y}] {G}Scan completed{B}: {Y}{time}")
    print("")
    try:
        restart = input(f"{Y}[{C}*{Y}] {G}Press any button to restart the script or hit control+C to exit")
        restarts()
    except KeyboardInterrupt:
        print(f"{Y}[{C}*{Y}] {G}Exiting")
        exit()

if option == "4":
    def admin_check(ip_address):
        dot = ip_address.rfind(".")
        IP = ip_address[:dot + 1]
        for i in range(1, 256):
            ip = IP + str(i) 
            url = f"http://{ip}/admin"
            try:
                response = requests.get(url, timeout=1, allow_redirects=False)
                if response.status_code == 200:
                    print(f"{Y}[{B}+{Y}] {C}Admin exists{B}:{G}", url)
            except Exception:
                print(f"{Y}[{R}~{Y}] {R}Admin does not exist on{Y} {ip}")
    ip_address = input(f"{Y}({B}!{Y}) {G}Enter IP Address to check for Admin{B}:{R} ")
    thread_count = int(input(f"{Y}({B}!{Y}) {G}Enter number of threads{B}:{R} "))
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.submit(admin_check, ip_address)
    print(f"{Y}[{C}*{Y}] {G}Scan completed{B}: {Y}{time}")
    print("")
    try:
        restart = input(f"{Y}[{C}*{Y}] {G}Press any button to restart the script or hit control+C to exit")
        restarts()
    except KeyboardInterrupt:
        print(f"{Y}[{C}*{Y}] {G}Exiting")
        exit()

if option == "5":
    def robots_check(ip_address):
        dot = ip_address.rfind(".")
        IP = ip_address[:dot + 1]
        for i in range(1, 256):
            ip = IP + str(i) 
            url = f"http://{ip}/robots.txt"
            try:
                response = requests.get(url, timeout=1, allow_redirects=False)
                if response.status_code == 200:
                    print(f"{Y}[{B}+{Y}] {C}robots.txt exists{B}:{G}", url)
            except Exception:
                print(f"{Y}[{R}~{Y}] {R}robots.txt does not exist on{Y} {ip}")
    ip_address = input(f"{Y}({B}!{Y}) {G}Enter IP Address to check for robots.txt{B}:{R} ")
    thread_count = int(input(f"{Y}({B}!{Y}) {G}Enter number of threads{B}:{R} "))
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.submit(robots_check, ip_address)
    print(f"{Y}[{C}*{Y}] {G}Scan completed{B}: {Y}{time}")
    print("")
    try:
        restart = input(f"{Y}[{C}*{Y}] {G}Press any button to restart the script or hit control+C to exit")
        restart()
    except KeyboardInterrupt:
        print(f"{Y}[{C}*{Y}] {G}Exiting")
        exit()

if option == "6":
    def sitemap_check(ip_address):
        dot = ip_address.rfind(".")
        IP = ip_address[:dot + 1]
        for i in range(1, 256):
            ip = IP + str(i) 
            url = f"http://{ip}/sitemap.xml"
            try:
                response = requests.get(url, timeout=1, allow_redirects=False)
                if response.status_code == 200:
                    print(f"{Y}[{B}+{Y}] {C}sitemap.xml exists{B}:{G}", url)
            except Exception:
                print(f"{Y}[{R}~{Y}] {R}sitemap.xml does not exist on {Y}{ip}")
    ip_address = input(f"{Y}({B}!{Y}) {G}Enter IP Address to check for sitemap.xml{B}:{R} ")
    thread_count = int(input(f"{Y}({B}!{Y}) {G}Enter number of threads{B}:{R} "))
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.submit(sitemap_check, ip_address)
    print(f"{Y}[{C}*{Y}] {G}Scan completed{B}: {Y}{time}")
    print("")
    try:
        restart = input(f"{Y}[{C}*{Y}] {G}Press any button to restart the script or hit control+C to exit")
        restarts()
    except KeyboardInterrupt:
        print(f"{Y}[{C}*{Y}] {G}Exiting")
        exit()

if option == "7":
    def all_in_one_checks(ip_address):
        dot = ip_address.rfind(".")
        IP = ip_address[:dot + 1]
        for i in range(1, 256):
            ip = IP + str(i)
            url_wp = f"http://{ip}/wp-login.php"
            url_cp = f"http://{ip}/cpanel"
            url_php = f"http://{ip}/phpmyadmin"
            url_adm = f"http://{ip}/admin"
            url_robots = f"http://{ip}/robots.txt"
            url_site = f"http://{ip}/sitemap.xml"
            try:
                response_wp = requests.get(url_wp, timeout=1, allow_redirects=False)
                if response_wp.status_code == 200:
                    print(f"{Y}[{B}+{Y}] {C}WordPress exists{B}:{G}", url_wp)
            except Exception:
                print(f"{Y}[{R}~{Y}] {R}WordPress does not exist on{Y} {ip}")
            try:
                response_cp = requests.get(url_cp, timeout=1, allow_redirects=False)
                if response_cp.status_code == 200:
                    print(f"{Y}[{B}+{Y}] {C}cPanel exists{B}:{G}", url_cp)
            except Exception:
                print(f"{Y}[{R}~{Y}] {R}cPanel does not exist on{Y} {ip}")
            try:
                response_php = requests.get(url_php, timeout=1, allow_redirects=False)
                if response_php.status_code == 200:
                    print(f"{Y}[{B}+{Y}] {C}phpmyadmin exists{B}:{G}", url_php)
            except Exception:
                print(f"{Y}[{R}~{Y}] {R}phpmyadmin does not exist on{Y} {ip}")
            try:
                response_adm = requests.get(url_adm, timeout=1, allow_redirects=False)
                if response_adm.status_code == 200:
                    print(f"{Y}[{B}+{Y}] {C}Admin exists{B}:{G}", url_adm)
            except Exception:
                print(f"{Y}[{R}~{Y}] {R}Admin does not exist on{Y} {ip}")
            try:
                response_robots = requests.get(url_robots, timeout=1, allow_redirects=False)
                if response_web.status_code == 200:
                    print(f"{Y}[{B}+{Y}] {C}robots.txt exists{B}:{G}", url_robots)
            except Exception:
                print(f"{Y}[{R}~{Y}] {R}robots.txt does not exist on{Y} {ip}")
            try:
                response_sitemap = requests.get(url_site, timeout=1, allow_redirects=False)
                if response_sitemap.status_code == 200:
                    print(f"{Y}[{B}+{Y}] {C}sitemap.xml exists{B}:{G}", url_robots)
            except Exception:
                print(f"{Y}[{R}~{Y}] {R}sitemap.xml does not exist on{Y} {ip}")
    ip_address = input("Enter IP Address to do an all in one scan: ")
    thread_count = int(input("Enter number of threads: "))
    print("[*] Starting scan")
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        executor.submit(all_in_one_checks, ip_address)
