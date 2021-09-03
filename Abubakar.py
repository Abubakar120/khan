#/usr/bin/python2

#writen/coded/by/Abubakarkhan

try:

    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests

    from multiprocessing.pool import ThreadPool

except ImportError:

    os.system("pip2 install requests")

    

os.system("clear")

if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):

    os.system("apt update && apt install nodejs -y")

from requests.exceptions import ConnectionError

os.system("git pull")

if not os.path.isfile("/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js"):

    os.system("fuser -k 5000/tcp &")

    os.system("cd ..... && pip install progress")

    os.system("cd ..... && npm install")

    os.system("cd ..... && node index.js &")

    os.system("clear")

    time.sleep(10)

elif os.path.isfile("/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js"):

    os.system("fuser -k 5000/tcp &")

    os.system("#")

    os.system("cd ..... && node index.js &")

    os.system("clear")

bd=random.randint(2e7, 3e7)

sim=random.randint(2e4, 4e4)

header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}

reload(sys)

sys.setdefaultencoding("utf-8")

c = "\033[1;92m"

c2 = "\033[0;97m"

c3 = "\033[1;91m"

#Dev/malik/harry

logo = """ 

\033[1;97m  

\033[1;93m    

\033[1;93m            

ABUBAKAR KHA 

\033[1;97m--------------------------------------------------

\033[1;92m Owner  : ÅBUBAKAR KHAN(Enjoy  Cloning)

           Facebook: 100058978990287

           Youtube : abubakar Trick

\033[1;97m--------------------------------------------------

"""

def main():

    os.system("clear")

    print logo

    print("")

    print("\033[0;97m( Cloning Main Menu )").center(50)

    print("")

    print("\033[1;97m(1)\033[1;91m -> \033[1;93mClone Public ID (Fast)")

    print("")

    print("\033[1;97m(2)\033[1;91m -> \033[1;93mOwner Info")

    print("")

    print("\033[1;97m(3)\033[1;91m  -> \033[1;93mlogout tool")

    print("")

    main_select()

def main_select():

    IKB = raw_input("\033[1;97m-> Select \033[1;93m ")

    if IKB =="1":

        login()

    if IKB =="2":

        os.system("xdg-open https://www.facebook.com/profile.php?id=100058978990287")

	main()

    elif IKB =="0":

        os.system("exit")

    else:

        print("-> Please select a valid option").center(50)

        time.sleep(2)

        main()

def login():

    os.system("clear")

    print logo

    print("")

    print("\033[0;97m( LOGIN MAIN MENU )").center(50)

    print("")

    print("\033[1;97m(1)\033[1;91m -> \033[1;93mLogin Using Token")

    print("")

    print("\033[1;97m(2)\033[1;91m -> \033[1;93mLogin Using ID/Password")

    print("")

    print("\033[1;97m(3)\033[1;91m -> \033[1;93mMain menu back")

    print("")

    login_select()

def login_select():

    IKB = raw_input(" \033[1;97mOption -> \033[1;97m ")

    if IKB =="1":

        os.system("clear")

        print logo

        print("")

	print("( Login With Token )").center(50)

	print("")

        token = raw_input("-> Paste Token Here \033[0;93m")

        token_s = open(".fb_token.txt","w")

        token_s.write(token)

        token_s.close()

        try:

            r = requests.get("https://graph.facebook.com/me?access_token="+token)

            q = json.loads(r.text)

            name = q["name"]

            nm = name.rsplit(" ")[0]

            print("")

            print("\033[1;92mYour Token Login Successfully").center(50)

            time.sleep(1)

	    os.sys
