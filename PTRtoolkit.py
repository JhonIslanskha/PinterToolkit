import os

def menu():

    print(""" 
██▓███   ██▓ ███▄    █ ▄▄▄█████▓▓█████  ██▀███     ▄▄▄█████▓ ▒█████   ▒█████   ██▓     ██ ▄█▀ ██▓▄▄▄█████▓
▓██░  ██▒▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒     ██▄█▒ ▓██▒▓  ██▒ ▓▒
▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ▓███▄░ ▒██▒▒ ▓██░ ▒░
▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄     ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    ▓██ █▄ ░██░░ ▓██▓ ░ 
▒██▒ ░  ░░██░▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██▒ █▄░██░  ▒██▒ ░ 
▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▒ ▓▒░▓    ▒ ░░   
░▒ ░      ▒ ░░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒ ▒░ ▒ ░    ░    
░░        ▒ ░   ░   ░ ░   ░         ░     ░░   ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░ ░░ ░  ▒ ░  ░      
          ░           ░             ░  ░   ░                     ░ ░      ░ ░      ░  ░░  ░    ░           
========================================
Created By Jh0n 1sl4nskh4_404

Blog: http://jalansawa.blogspot.co.id

Facebook: https://goo.gl/5aAUfm
Ver: 2.0
----
ONLY FOR TERMUX!
----
==========================================
00. MASTER LINUX INDONESIA
------------------------------------------
1. Install Nmap 
2. Install Hydra
3. Install SQLMap
4. Install Metasploit
5. Install ngrok
6. Install Kali Nethunter
7. Install angryFuzzer
8. Install Red_Hawk
9. Install Weeman
10. Install IPGeoLocation
11. Install Cupp
12. Instagram Bruteforcer (instahack)
13. Twitter Bruteforcer   (TwitterSniper)
14. Install Ubuntu
15. Install Fedora
16. Install viSQL
17. Install Hash-Buster
18. Install D-TECT
19. Install routersploit
20. Install Arch
21. XSStrike
22. Brutespray
23. commixproject
24. ReconDog
25. onioff
26. hakkuframework
------------------------------------------
99. Exit
==========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "00":
        print("================================")
        print("This will install: nmap, hydra, sqlmap, metasploit, ngrok, angryFuzzer, red_hawk, weeman, IPGeoLocation, cupp, instahack, TwitterSniper, Hash-Buster, D-TECT, routersploit and viSQL with one click.")
        print("----------------")
        hm = input("[?] Apakah Anda ingin melanjutkan? (y/n): ")
        print("================================")
        if hm == "y":
            print("========================================================")
            print("[+] Silakan Menunggu Proses Instalasi Program Selesai...")
            print("[+] Ini akan memakan waktu lama.                        ")
            print("========================================================")
            os.system("pkg update")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y python2")
            os.system("pkg install -y wget")
            os.sysetm("pkg install -y nmap")
            os.system("plg install -y hydra ")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg install wget")
            os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
            os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
            os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
            os.system("cd /data/data/com.termux/files/home && bundle install")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
            os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
            os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home && pip2 install requests")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y php")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y python2")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
            os.system("cd /data/data/com.termux/files/home && cd weeman")
            os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
            os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
            os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y nano")
            os.system("pip install requests")
            os.system("pip install beautifulsoup4")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pip install mechanicalsoup")
            os.system("pkg install -y nano")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            os.system("pkg update -y")
			os.system("pkg install -y git")
			os.system("pkg install -y python2")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sdrausty/TermuxArch
			os.system("cd /data/data/com.termux/files/home && cd Arch")
			os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/XSStrike.git
			os.system("cd /data/data/com.termux/files/home && cd XSStrike")
			os.system("pip2 install -r requirements.txt")
			os.system("pkg update -y")
			os.system("pkg install -y git")
			os.system("pkg install -y python2")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/x90skysn3k/brutespray.git
			os.system("cd /data/data/com.termux/files/home && cd brutespray.py
			os.system("pkg install python2")
			os.system("pkg install git")
			os.system("cd /data/data/com.termux/files/home && git clonehttps://github.com/commixproject/commix.git")
            os.system("cd /data/data/com.termux/files/home && cd commix")
			os.system("pip2 install -r requirements.txt")
			os.system("pkg install python2")
			os.system("pkg install git")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/ReconDog)
            os.system("cd /data/data/com.termux/files/home && cd ReconDog")
			os.system("chmod +x dog.py")
			os.system("pkg install python2")
			os.system("pkg install git")
			os.system("pkg install tor")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/k4m4/onioff.git
            os.system("cd /data/data/com.termux/files/home && cd onioff")
			pip2 install -r requirements.txt 
			os.system("pkg install python")
			os.system("pkg install git")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/4shadoww/hakkuframework")
            os.system("cd /data/data/com.termux/files/home && cd hakkuframework")
			os.system("chmod +x hakku")
		    os.system("clear")
            print("========================================")
            print("[+] semuanya berhasil dipasang:)        ")
            print("[+] Happy Hacking <3                    ")
            print("========================================")
        else:
            rmenu = input("[?] Back to Menu? (y/n): ")
            if rmenu == "y":
                menu()
            else:
                break
    if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] nmap installed successfully :)  ")
        print("[+] Ketik 'nmap' untuk memulai.     ")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y hydra")
        os.system("cd /data/data/com.termux/files/home")
        print("==================================== ")
        print("[+] hydra installed successfully :)    ")
        print("[+] Ketik 'hydra' untuk memulai.       ")
        print("==================================== ")
        rmenu = input("[?] Back to Menu? (y/n) ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap installed successfully :) ")
        print("[+] Buka sqlmap dan ketik 'python2 sqlmap.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "4":
        os.system("pkg install -y wget")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Metasploit installed successfully :)")
        print("[+] Ketik 'msfconsole' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "5":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ngrok installed successfully :)")
        print("[+] Masuk ke ngrok folder dan ketik './ngrok http 80' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "6":
        os.system("pkg update -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
        os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Nethunter installed successfully :)")
        print("[+] Buka folder Nethunter-In-Termux dan ketik './kalinethunter' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "7":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
        os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
        os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home && pip2 install requests")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] angryFuzzer installed successfully :)")
        print("[+] Pergi ke folder angryFuzzer dan ketik 'python2 angryFuzzer.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "8":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] RED_HAWK installed successfully :)")
        print("[+] Buka folder RED_HAWK dan ketik 'php rhawk.php' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "9":
        os.system("pkg update -y")
        os.system("pkg install -y python2")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
        os.system("cd /data/data/com.termux/files/home && cd weeman")
        os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] weeman installed successfully :)")
        print("[+] Pergi ke weeman folder dan ketik 'python2 weeman.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "10":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
        os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
        os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] IPGeoLocation installed successfully :)")
        print("[+] Buka map IPGeoLocation dan ketik 'python ipgeolocation.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "11":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
        print("====================================")
        print("[+] Cupp installed successfully :)")
        print("[+] Pergi ke folder cupp dan ketik 'python cupp3.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "12":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
        print("====================================")
        print("[+] Instahack installed successfully :)")
        print("[+] Buka folder instahack dan ketik 'python hackinsta.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "13":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pip install mechanicalsoup")
        os.system("pkg install -y nano")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
        print("====================================")
        print("[+] TwitterSniper installed successfully :)")
        print("[+] Pergi ke TwitterSniper folder dan ketik 'python TwitterSniper.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "14":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print("====================================")
        print("[+] Ubuntu installed successfully :)")
        print("[+] Buka folder termux-ubuntu dan ketik './start.sh' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "15":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y wget")
        os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
        print("====================================")
        print("[+] Fedora installed successfully :)")
        print("[+] Ketik 'sh termux-fedora.sh f26_arm64' atau 'sh termux-fedora.sh f26_arm' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "16":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
        print("====================================")
        print("[+] viSQL installed successfully :)")
        print("[+] Buka folder viSQL dan ketik 'python2 viSQL.py --help' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "17":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
        print("====================================")
        print("[+] Hash-Buster installed successfully :)")
        print("[+] Pergi ke folder Hash-Buster dan ketik 'python2 hash.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "18":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
        print("====================================")
        print("[+] Hash-Buster installed successfully :)")
        print("[+] Pergi ke folder D-TECT dan ketik 'python2 d-tect.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
		elif what == "19":	
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            print("====================================")
            print("[+] routersploit installed successfully :)")
            print("[+] Pergi ke folder routersploit dan ketik 'python2 rsf.py' untuk memulai.")
            print("====================================")
            rmenu = input("[?] Back to Menu? (y/n): ")
            if rmenu == "y":
                menu()
		else:
            break
		elif what == "20":	
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sdrausty/TermuxArch")
            os.system("cd /data/data/com.termux/files/home && ./TermuxArch/stupTermuxArch.sh")
            os.system("pip2 install -r requirements.txt")
            print("====================================")
            print("[+] Arch installed successfully :)")
            print("[+] Pergi ke folder Arch dan ketik './arch/startArch' untuk memulai.")
            print("====================================")
            rmenu = input("[?] Back to Menu? (y/n): ")	
		    if rmenu == "y":
                menu()
		else:
            break
		elif what == "21":	
			os.system("pkg install python2")
			os.system("pkg install git")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/XSStrike.git")
            os.system("cd /data/data/com.termux/files/home && cd XSStrike")
			os.system("pip2 install -r requirements.txt")
			print("====================================")
            print("[+] XSStrike installed successfully :)")
            print("[+] Pergi ke folder XSStrike dan ketik 'python2 xxstrike' untuk memulai.")
            print("====================================")
			rmenu = input("[?] Back to Menu? (y/n): ")	
		    if rmenu == "y":
                menu()		
		else:
            break
		elif what == "22":
			os.system("pkg install python2")
			os.system("pkg install git")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/x90skysn3k/brutespray.git")
            os.system("cd /data/data/com.termux/files/home && cd brutespray")
			os.system("pip2 install -r requirements.txt")
			print("====================================")
            print("[+] brutespray installed successfully :)")
            print("[+] Pergi ke folder brutespray dan ketik 'python2 brutespray.py' untuk memulai.")
            print("====================================")
			rmenu = input("[?] Back to Menu? (y/n): ")	
		    if rmenu == "y":
                menu()	
		else:
            break
		elif what == "23":
			os.system("pkg install python2")
			os.system("pkg install git")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/commixproject/commix.git")
            os.system("cd /data/data/com.termux/files/home && cd commix")
			os.system("pip2 install -r requirements.txt")
			print("====================================")
            print("[+] commixproject installed successfully :)")
            print("[+] Pergi ke folder commix dan ketik 'python2 commix.py' untuk memulai.")
            print("====================================")
			rmenu = input("[?] Back to Menu? (y/n): ")	
		    if rmenu == "y":
                menu()		
		else:
            break
		elif what == "24":
			os.system("pkg install python2")
			os.system("pkg install git")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/ReconDog")
            os.system("cd /data/data/com.termux/files/home && cd ReconDog")
			os.system("chmod +x dog.py")
			print("====================================")
            print("[+] commixproject installed successfully :)")
            print("[+] Pergi ke folder ReconDog dan ketik 'python2 dog.py' untuk memulai.")
            print("====================================")
			rmenu = input("[?] Back to Menu? (y/n): ")	
		    if rmenu == "y":
                menu()			
		else:
            break
		elif what == "25":
			os.system("pkg install python2")
			os.system("pkg install git")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/k4m4/onioff.git")
            os.system("cd /data/data/com.termux/files/home && cd onioff")
			os.system("chmod +x dog.py")
			print("====================================")
            print("[+] commixproject installed successfully :)")
            print("[+] Pergi ke folder onioff dan ketik 'python2 onioff.py url ' untuk memulai.")
            print("====================================")
			rmenu = input("[?] Back to Menu? (y/n): ")	
		    if rmenu == "y":
                menu()				
		else:
            break
		elif what == "26":
			os.system("pkg install python2")
			os.system("pkg install git")
			os.system("cd /data/data/com.termux/files/home && git clone https://github.com/4shadoww/hakkuframework")
            os.system("cd /data/data/com.termux/files/home && cd hakkuframework")
			os.system("chmod +x hakku")
			print("====================================")
            print("[+] commixproject installed successfully :)")
            print("[+] Pergi ke folder hakkuframework dan ketik 'python hakku ' untuk memulai.")
            print("====================================")
			rmenu = input("[?] Back to Menu? (y/n): ")	
		    if rmenu == "y":
                menu()				
		else:
             break
    elif what == "99":
        print("Bye.")
        break
