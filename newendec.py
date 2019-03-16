import os, random, string,getpass

length = 13
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
ran= ''.join(random.choice(chars) for i in range(length))



def prnt():
    print("""                      

                                     1.encrypt the text
                                     2.Decrypt the text



                                                                                           """)
def bar():
    progress = progressbar.ProgressBar()
    for i in progress(range(12)):
        time.sleep(0.1)
k = ''
import os
import progressbar
import sys
import time

os.system(r"D:\cartoon.exe")
print("Just For Security Purpose Answer a Question")
print("\n\n")

def Pet():
    print("Default Pet name is:NULL", "Please change this to your pet name for security Purpose!")
    petn = getpass.getpass(prompt='What is your pet name>>')
    li = len(petn)
    p = None
    while li != 0:
        j = open(r"ans.txt", "w")
        j.write('1')
        j.close()
        while p != 0:
            for i in petn:
                j = ord(i)
                a=petn.index(i)
                if (i.strip()):
                    if j >= 97 and j <= 109 or j >= 65 and j <= 77:
                        j = j + 13
                        p = open(r"ans.txt", "a")
                        p.write(chr(j))
                        li = li - 1
                        p=0

                    elif j >= 110 and j <= 122 or j >= 78 and j <= 90:
                        j = j - 13
                        p = open(r"ans.txt", "a")
                        p.write(chr(j))
                        li = li - 1
                        p=0

                    elif j == 32:
                        p = open(r"ans.txt", "a")
                        p.write(chr(j))
                        li = li - 1
                        p=0
                else:
                    print("can't leave this field blank!")
                    time.sleep(4)
                    p = 1
                    sys.exit(0)

    c = open(r"ans.txt")
    x = c.readlines()
    c.close()
    g = open(r"ans.txt", "r+")
    for line in x:
        g.write(line[1:])
        g.truncate()

h = open(r"ans.txt", "r")
if (os.path.getsize(r"ans.txt") == 1):
    Pet()

else:
    print("As u have completed the Security Question So proceeding further!")
    time.sleep(4)
    os.system("cls")

x = int(input("enter 0 to set ur new password and 1 to continue with the old one:"))
cho = None
if x == 1:
    count = 0
    #pas = input("Enter ur password to continue..")
    pas = getpass.getpass(prompt='Enter Your Password here>')
    d = open(r"passw.txt", "r")
    f=d.read()
    d.close()
    li = len(f)
    while li != 0:
        str = ""
        f = open(r"passw.txt", "r")
        t = f.read()
        for i in t:
            j = ord(i)
            if j >= 119 and j <= 122 or j >= 87 and j <= 90:
                j = j - 22
                str = str + chr(j)
                li = li - 1

            elif j >= 97 and j <= 118 or j >= 65 and j <= 86:
                j = j + 4
                str = str + chr(j)
                li = li - 1

            elif j == 32:
                str = str + chr(32)
                li = li - 1

            elif j >= 48 and j <= 57:
                str = str + chr(j)
                li = li - 1

    if pas==str:
        print("Password verified successfuly...")
        os.system("cls")
        count = 1

    elif pas!=str:
        print("Wrong Password!", "If forget ur password then change it in next run!Thank You!")
        time.sleep(5)
        li=0
        sys.exit(0)

s = open(r"passw.txt", "r")
u = s.read()
l = len(u)

if x == 0:
    if l == 1:
        n = open(r"passw.txt", "w")
        n.write(ran)
        n.close()
        f=open(r"passw.txt","r")
        g=f.read()
        print("Default Password is:",g, " change this to your password,for security reasons you know very well!")
        pasn = getpass.getpass(prompt='Enter Your new Password here>>>')
        print("Please note down this password becuase u need this for login purpose")
        li = len(pasn)
        p = open(r"passw.txt")
        x = p.readlines()
        p.close()
        g = open(r"passw.txt", "r+")
        i=list(pasn)
        u=i.index(i[0])
        for line in x:
            g.write(line[1:u])
            g.truncate()
        while li != 0:
            for i in pasn:
                j = ord(i)
                if j >= 97 and j <= 100 or j >= 65 and j <= 68:
                    j = j + 22
                    f = open(r"passw.txt", "a")
                    f.write(chr(j))
                    f.close()
                    li = li - 1

                elif j >= 101 and j <= 122 or j >= 69 and j <= 90:
                    j = j - 4
                    n = open(r"passw.txt", "a")
                    n.write(chr(j))
                    n.close()
                    li = li - 1

                elif j == 32:
                    d = open(r"passw.txt", "a")
                    d.write(chr(j))
                    d.close()
                    li = li - 1

                elif j >= 48 and j <= 57:
                    s = open(r"passw.txt", "a")
                    s.write(chr(j))
                    s.close()
                    li = li - 1

        '''p = open(r"passw.txt")
        x = p.readlines()
        p.close()
        g = open(r"passw.txt", "r+")
        for line in x:
            g.write(line[1:])
            g.truncate()'''

        time.sleep(2)
        print("Please Restart the tool now...")

        time.sleep(3)
        sys.exit(0)
        count = 0

    else:
        q = int(input("Forget Password??, No problem enter 1 here to set a new password:"))
        if q == 1:
            a =getpass.getpass(prompt='Enter Your Pet name to verify it is u>>>>')
            b = open(r"ans.txt", "r")
            v = b.read()
            os.system("cls")
            li=len(v)
            while li != 0:
                str=""
                for i in v:
                    j = ord(i)
                    if j >= 97 and j <= 109 or j >= 65 and j <= 77:
                        j = j + 13
                        str=str+chr(j)
                        li = li - 1
                    elif j >= 110 and j <= 122 or j >= 78 and j <= 90:
                        j = j - 13
                        str=str+chr(j)
                        li = li - 1

                    elif j == 32:
                        str=str+chr(j)
                        li = li - 1

            time.sleep(10)
            print("Verifying from database")
            bar()

            if str == a:
                print("You are Verified....")
                j = open(r"passw.txt", "w")
                j.write('1')
                j.close()
                p = open(r"passw.txt", "a")
                pasnn=getpass.getpass(prompt='Enter Your new password>>>>')
                li = len(pasnn)
                while li != 0:
                    for i in pasnn:
                        j = ord(i)
                        if j >= 97 and j <= 100 or j >= 65 and j <= 68:
                            j = j + 22
                            f = open(r"passw.txt", "a")
                            f.write(chr(j))
                            f.close()
                            li = li - 1

                        elif j >= 101 and j <= 122 or j >= 69 and j <= 90:
                            j = j - 4
                            n = open(r"passw.txt", "a")
                            n.write(chr(j))
                            n.close()
                            li = li - 1

                        elif j == 32:
                            d = open(r"passw.txt", "a")
                            d.write(chr(j))
                            d.close()
                            li = li - 1

                        elif j >= 48 and j <= 57:
                            s = open(r"passw.txt", "a")
                            s.write(chr(j))
                            s.close()
                            li = li - 1

                p = open(r"passw.txt")
                x = p.readlines()
                p.close()
                g = open(r"passw.txt", "r+")
                for line in x:
                    g.write(line[1:])
                    g.truncate()

                print("Changing the password")
                bar()
                time.sleep(3)
                print("Password Changed Successfuly,Restart the app to use it")
                time.sleep(3)
                sys.exit(0)

            else:
                print("Security Check Failed!!Exiting,Try again")
                time.sleep(3)
                sys.exit(0)

        count = 0

def bashenc():
    delay_print("Atbash encryption method ready to launch!")
    s = ""
    S = ''
    print("\n")
    s = input("Enter ur message here to encrypt:")
    t = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
         'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
         'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L','P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G','U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A', '@': '@', ' ': ' ', '.': '.', 'a': 'z', 'b': 'y',
         'c': 'x', 'd': 'w', 'e': 'v',':':':','f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q','k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
         'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g','u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a','?':'?','!':'!','+':'+','*':'*','/':'/','#':'#','$':'$','%':'%','^':'^','&':'&','(':'(',')':')'
        ,'~':'~','`':'`','>':'>','<':'<','0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','_':'_','-':'-','"':'"','{':'{','}':'}','[':'[',']':']'

                      }
    for k in s:
        if k != ' ':
            S += t[k]

        else:
            S += ' '

    delay_print("Encrypted messsage is:")
    time.sleep(4)
    print(S)


def bashdec():
    S = ''
    s = input("Enter the message to decrypt:")
    t = {'Z': 'A', 'Y': 'B', 'X': 'C', 'W': 'D', 'V': 'E','U': 'F', 'T': 'G', 'S': 'H', 'R': 'I', 'Q': 'J','P': 'K', 'O': 'L', 'N': 'M', 'M': 'N', 'L': 'O',
         'K': 'P', 'J': 'Q', 'I': 'R', 'H': 'S', 'G': 'T',':':':','F': 'U', 'E': 'V', 'D': 'W', 'B': 'Y', 'A': 'Z', '@': '@', ' ': ' ', '.': '.', 'z': 'a', 'y': 'b',
         'w': 'd', 'v': 'e', 'c': 'x','u': 'f', 't': 'g', 's': 'h', 'r': 'i', 'q': 'j','p': 'k', 'o': 'l', 'n': 'm', 'm': 'n', 'l': 'o','k': 'p', 'j': 'q', 'i': 'r', 'h': 's', 'g': 't',
         'f': 'u', 'e': 'v', 'd': 'w', 'x': 'c', 'b': 'y', 'a': 'z','?':'?','!':'!','+':'+','-':'-','*':'*','/':'/','#':'#','$':'$','%':'%','^':'^','&':'&','(':'(',')':')'
        ,'~':'~','`':'`','>':'>','<':'<','0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','_':'_','-':'-','"':'"','{':'{','}':'}','[':'[',']':']'}

    for k in s:
        if k != ' ':
            S += t[k]

        else:
            S += ' '

    print("Decrypted messsage is:")
    time.sleep(4)
    print(S)


def rotenc():
    s = ""
    j = None
    s = input("Enter ur string here to encrypt:")
    li = len(s)
    print("Encrypted string is:", end="")
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if j >= 97 and j <= 109 or j >= 65 and j <= 77:
                j = j + 13
                print(chr(j), end="")
                li = li - 1

            elif j >= 110 and j <= 122 or j >= 78 and j <= 90:
                j = j - 13
                print(chr(j), end="")
                li = li - 1

            elif j == 32:
                print(chr(j), end="")
                li = li - 1

            elif j>=48 and j<57:
                print(chr(j),end="")
                li=li-1

            elif j>=33 and j<=47:
                print(chr(j),end="")
                li=li-1

            elif j>=58 and j<=64:
                print(chr(j),end="")
                li=li-1

            elif j>=91 and j<=96:
                print(chr(j),end="")
                li=li-1

            elif j>=123 and j<=126:
                print(chr(j),end="")
                li=li-1

def rotdec():
    s = ""
    s = input("Enter the encrypted string to decrypt it:")
    li = len(s)
    print("Decrypted string is:", end="")
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if j >= 97 and j <= 109 or j >= 65 and j <= 77:
                j = j + 13
                print(chr(j), end="")
                li = li - 1

            elif j >= 110 and j <= 122 or j >= 78 and j <= 90:
                j = j - 13
                print(chr(j), end="")
                li = li - 1

            elif j == 32:
                print(chr(j), end="")
                li = li - 1

            elif j >= 48 and j < 57:
                print(chr(j), end="")
                li = li - 1

            elif j >= 33 and j <= 47:
                print(chr(j), end="")
                li = li - 1

            elif j >= 58 and j <= 64:
                print(chr(j), end="")
                li = li - 1

            elif j >= 91 and j <= 96:
                print(chr(j), end="")
                li = li - 1

            elif j >= 123 and j <= 126:
                print(chr(j), end="")
                li = li - 1

def rot22enc():
    s = ""
    j = None
    s = input("Enter ur string here to encrypt:")
    li = len(s)
    print("Encrypted string is:", end="")
    print("\n")
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if j >= 97 and j <= 100 or j >= 65 and j <= 68:
                j = j + 22
                print(chr(j), end="")
                li = li - 1

            elif j >= 101 and j <= 122 or j >= 69 and j <= 90:
                j = j - 4
                print(chr(j), end="")
                li = li - 1

            elif j == 32:
                print(" ", end="")
                li = li - 1

            elif j >= 48 and j < 57:
                print(chr(j), end="")
                li = li - 1

            elif j >= 33 and j <= 47:
                print(chr(j), end="")
                li = li - 1

            elif j >= 58 and j <= 64:
                print(chr(j), end="")
                li = li - 1

            elif j >= 91 and j <= 96:
                print(chr(j), end="")
                li = li - 1

            elif j >= 123 and j <= 126:
                print(chr(j), end="")
                li = li - 1

def rot22dec():
    s = ""
    s = input("Enter the encrypted string to decrypt it:")
    li = len(s)
    print("\nDecrypted string is:", end="")
    print("\n")
    time.sleep(4)
    while li != 0:
        for i in s:
            j = ord(i)
            if j >= 119 and j <= 122 or j >= 87 and j <= 90:
                j = j - 22
                print(chr(j), end="")
                li = li - 1

            elif j >= 97 and j <= 118 or j >= 65 and j <= 86:
                j = j + 4
                print(chr(j), end="")
                li = li - 1

            elif j == 32:
                print(" ", end="")
                li = li - 1

            elif j >= 48 and j < 57:
                print(chr(j), end="")
                li = li - 1

            elif j >= 33 and j <= 47:
                print(chr(j), end="")
                li = li - 1

            elif j >= 58 and j <= 64:
                print(chr(j), end="")
                li = li - 1

            elif j >= 91 and j <= 96:
                print(chr(j), end="")
                li = li - 1

            elif j >= 123 and j <= 126:
                print(chr(j), end="")
                li = li - 1

def simenc():
    s = ""
    s = input("Enter the string to encrypt here:")
    li = len(s)
    print("Encrypted string is:", end="")
    print("\n")
    for i in s:
        j = ord(i)
        if j == 32:
            print(chr(j), end="")
            li = li - 1

        elif j >= 48 and j < 57:
            print(chr(j), end="")
            li = li - 1

        elif j >= 33 and j <= 47:
            print(chr(j), end="")
            li = li - 1

        elif j >= 58 and j <= 64:
            print(chr(j), end="")
            li = li - 1

        elif j >= 91 and j <= 96:
            print(chr(j), end="")
            li = li - 1

        elif j >= 123 and j <= 126:
            print(chr(j), end="")
            li = li - 1

        else:
            j = j + 1
            print(chr(j), end="")
            li = li - 1


def simdec():
    s = ""
    s = input("Enter the encrypted string here to decrypt it:")
    li = len(s)
    print("Decrypted string is", end="")
    print("\n")
    for i in s:
        j = ord(i)
        if j == 32:
            print(chr(j), end="")
            li = li - 1

        elif j >= 48 and j < 57:
            print(chr(j), end="")
            li = li - 1

        elif j >= 33 and j <= 47:
            print(chr(j), end="")
            li = li - 1

        elif j >= 58 and j <= 64:
            print(chr(j), end="")
            li = li - 1

        elif j >= 91 and j <= 96:
            print(chr(j), end="")
            li = li - 1

        elif j >= 123 and j <= 126:
            print(chr(j), end="")
            li = li - 1

        else:
            j = j - 1
            print(chr(j), end="")
            li = li - 1


def cenc():
    s = "abcdefghijklmnopqrstuvwxyz"
    print("Current working string is:", s)
    k = input("Input a single word key u want to use for encryption:")
    if len(k) > 1:
        print("App Crashed!Wait for the Update where key will be greater than length 1")
        time.sleep(5)
        sys.exit(0)

    i = ord(k)
    s = s.replace(k, '')
    s = k + s
    print("Now string is:", s)
    t = input("Enter the string to Encrypt here:")
    li = len(t)
    print("Encrypted string is:", end="")
    while li != 0:
        for n in t:
            j = ord(n)
            if j == ord('a'):
                j = i
                print(chr(j), end="")
                li = li - 1

            elif n > 'a' and n <= k:
                j = j - 1
                print(chr(j), end="")
                li = li - 1

            elif n > k:
                print(n, end="")
                li = li - 1

            elif ord(n) == 32:
                print(chr(32), end="")
                li = li - 1

            elif j >= 48 and j < 57:
                print(chr(j), end="")
                li = li - 1

            elif j >= 33 and j <= 47:
                print(chr(j), end="")
                li = li - 1

            elif j >= 58 and j <= 64:
                print(chr(j), end="")
                li = li - 1

            elif j >= 91 and j <= 96:
                print(chr(j), end="")
                li = li - 1

            elif j >= 123 and j <= 126:
                print(chr(j), end="")
                li = li - 1

def cdec():
    h = ""
    c = ''
    s = "abcdefghijklmonpqrstuvwxyz"
    t = input("Enter the Encrypted String to Decrypt it here:")
    k = input("Enter the key you used earlier during encryption:")
    if len(k) > 1:
        print("App Crashed!Wait for the Update where key will be greater than length 1")
        time.sleep(5)
        sys.exit(0)

    s = s.replace(k, '')
    s = k + s
    i = ord(k)
    li = len(t)
    for j in t:
        p = ord(j)
        if j > k:
            print(j, end="")

        elif j < k:
            if j == ' ':
                print(' ', end="")

            else:
                if p>=48 and p<=57:
                    print(chr(p),end="")
                    li=li-1

                elif p >= 33 and p <= 47:
                    print(chr(p), end="")
                    li = li - 1

                elif p >= 58 and p <= 64:
                    print(chr(p), end="")
                    li = li - 1

                elif p >= 91 and p <= 96:
                    print(chr(p), end="")
                    li = li - 1

                elif p >= 123 and p <= 126:
                    print(chr(p), end="")
                    li = li - 1

                else:
                    j = chr(ord(j) + 1)
                    print(j, end="")

        elif j == k:
            print('a', end="")


def delay_print(s):
    for c in s:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.1)


os.system("cls")

if count == 1:
    os.system(r"D:\cartoon.exe")
    choice = None
    delay_print("This Script Can Encrypt Ur Message In a Different Manner So That No Third Person Can Read It!")
    print("\n\n\n")
    choice = int(input("\nEnter 1 to start encryption and decryption process and 0 to exit the program:"))
    if choice == 0:
        delay_print("Thanks for using me!")
        delay_print("Leave a Reply on cyberbot1502@gmail.com")
        time.sleep(3)
        sys.exit(0)

    bar()

    while choice != 0:
        print("""

                   1.Atbash Encryption
                   2.Rot13
                   3.Rot22
                   4.Simple Encryption(add 1)
                   5.caesar(with ur key for only small alphabets)
                   6.Exit The program 

                                               """)

        c = 0
        ch = None
        c = int(input("Please Choose ur encryption Method from the following techniques listed above:"))
        if c == 6:
            delay_print("Thanks for using me!")
            delay_print("Leave a Reply on cyberbot1502@gmail.com")
            time.sleep(3)
            sys.exit(0)

        if c == 1:
            while ch != 0:
                prnt()
                f = int(input("Enter ur choice what to do now:"))
                if f == 1:
                    bashenc()
                if f == 2:
                    bashdec()
                ch = int(input("\nWant to do some more encryption-decryption task on Atbash then enter 2 otherwise 0:"))

        elif c == 2:
            hc = None
            while hc != 0:

                prnt()
                f = int(input("Enter ur choice what to do now:"))
                if f == 1:
                    rotenc()
                if f == 2:
                    rotdec()

                hc = int(input("\nTo do some more task in ROT13 enter 4 otherwise 0:"))
                print("\n")

        elif c == 3:
            cc = None
            while cc != 0:
                prnt()
                f = int(input("Enter ur choice what to do now:"))
                if f == 1:
                    rot22enc()
                if f == 2:
                    rot22dec()

                cc = int(input("\nTo do more task in ROT22 enter 4 otherwise 0:"))
                print("\n")

        elif c == 4:
            g = None
            while g != 0:

                prnt()
                f = int(input("Enter ur choice what to do now:"))
                if f == 1:
                    simenc()

                if f == 2:
                    simdec()

                g = int(input("\nTo do more task in Simple method enter 5 otherwise 0:"))

        elif c == 5:
            i = None
            while i != 0:
                prnt()
                g = int(input("Enter ur choice what to do now:"))
                if g == 1:
                    cenc()
                if g == 2:
                    cdec()

                i = int(input("\nTo do more task in caesor keyed enter 6 otherwise 0:"))
else:

    print("Wrong Password!please change ur password if u forget it in next run")

    time.sleep(4)