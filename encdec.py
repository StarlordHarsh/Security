class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[93m'
    WARNING = '\033[92m'
    FAIL = '\033[91m'
    # Formatting
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    # End colored text
    END = '\033[0m'


import re
import os
import sys
from os import system, name, path
import progressbar
import sys
import time


def bashenc():
    s = input("Enter the message to Encrypt:")
    s1 = ""

    for k in s:
        if 65 < ord(k) < 90 or 97 < ord(k) < 122:
            s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))
        else:
            s1 += k
    print("Encrypted message is:", s1)


def bashdec():
    s = input("Enter the message to Decrypt:")
    s1 = ""

    for k in s:
        if 65 < ord(k) < 90 or 97 < ord(k) < 122:
            s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))
        else:
            s1 += k
    print("Decrypted message is:", s1)


def rotenc():
    s = input("Enter ur string here to Encrypt:")
    li = len(s)
    s1 = ""
    print("Encrypted string is:", end="")
    print("\n")
    for i in s:
        if 65 < ord(i) < 90 or 97 < ord(i) < 122:
            j = ord(i) + 13
            s1 += (chr(j if j <= 90 else (j - 26)) if i.isupper() else chr(j if j <= 122 else (j - 26)))
        else:
            s1 += i
    print(s1)


def rotdec():
    s = input("Enter ur string here to Decrypt:")
    li = len(s)
    s1 = ""
    print("Encrypted string is:", end="")
    print("\n")
    for i in s:
        if 65 < ord(i) < 90 or 97 < ord(i) < 122:
            j = ord(i) - 13
            s1 += (chr(j if j >= 65 else (j + 26)) if i.isupper() else chr(j if j >= 97 else (j + 26)))
        else:
            s1 += i
    print(s1)


def rot22enc():
    s = input("Enter ur string here to Encrypt:")
    li = len(s)
    s1 = ""
    print("Encrypted string is:", end="")
    print("\n")

    for i in s:
        if 65 < ord(i) < 90 or 97 < ord(i) < 122:
            j = ord(i) + 22
            s1 += (chr(j if j <= 90 else (j - 26)) if i.isupper() else chr(j if j <= 122 else (j - 26)))
        else:
            s1 += i
    print(s1)


def rot22dec():
    s = input("Enter ur string here to Decrypt:")
    li = len(s)
    s1 = ""
    print("Encrypted string is:", end="")
    print("\n")

    for i in s:
        if 65 < ord(i) < 90 or 97 < ord(i) < 122:
            j = ord(i) - 22
            s1 += (chr(j if j >= 65 else (j + 26)) if i.isupper() else chr(j if j >= 97 else (j + 26)))
        else:
            s1 += i
    print(s1)


def simenc():
    s = input("Enter the string to encrypt here:")
    print(color.HEADER + "Encrypted string is:" + color.END, end="")

    for i in s:
        if 65 < ord(i) < 90 or 97 < ord(i) < 122:
            k = ord(i) + 1
            print(chr(k), end="")
        else:
            print(i, end="")


def simdec():
    s = input("Enter the encrypted string here to decrypt it:")
    print(color.HEADER + "Decrypted string is" + color.END, end="")

    for i in s:
        if 65 < ord(i) < 90 or 97 < ord(i) < 122:
            k = ord(i) - 1
            print(chr(k), end="")
        else:
            print(i, end="")


def cenc():
    s = "abcdefghijklmnopqrstuvwxyz"
    print("Current working string is:", s)
    t = input("Enter the string to Encrypt:")
    k = input("Input a single word key you want to use for Encryption:")
    s = s.replace(k, '')
    s = k + s
    print("Now string is:", s)
    print("Encrypted string is:", end="")
    for n in t:
        j = ord(n)
        if n == 'a':
            j = ord(k)
            print(chr(j), end="")
        elif 'a' < n <= k:
            j = j - 1
            print(chr(j), end="")
        elif 'z' > n > k:
            print(n, end="")
        elif not (65 < ord(n) < 90) or not (97 < ord(n) < 122):
            print(n, end="")


def cdec():
    t = input("Enter the string to Decrypt:")
    k = input("Enter the key you used earlier during Encryption:")
    for j in t:
        if 'z' > j > k:
            print(j, end="")
        elif 'a' < j < k:
            j = chr(ord(j) + 1)
            print(j, end="")
        elif j == k:
            print('a', end="")
        elif not (65 < ord(j) < 90) or not (97 < ord(j) < 122):
            print(j, end="")


def delay_print(s):
    for c in s:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(0.1)


def bar():
    progress = progressbar.ProgressBar()
    for __ in progress(range(25)):
        time.sleep(0.1)


print("This Script Can Encrypt Ur Message In a Different Manner So That No Third Person Can Read It !")
print("\n\n\n")


def prnt():
    clr()
    print("""            
              1. Encrypt the text
              2. Decrypt the text
              3. Exit from this method
                                          """)


def clr():
    if name == 'nt':
        _ = system('cls')


def password():
    while True:
        pasw = input("""Enter your new Password:""")
        pasw1 = input("""Enter your Password again:""")
        if pasw == pasw1:
            print("Enter your question for security purposes ")
            fileq = open('ques.txt', 'w')
            fileq.write(input("Question:"))
            filea = open('ans.txt', 'w')
            filea.write(input("Answer:"))
            file = open('pass.txt', 'w')
            s1 = ""
            for k in pasw:
                if 65 < ord(k) < 90 or 97 < ord(k) < 122:
                    s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))
                else:
                    s1 += k
            file.write(s1)
            file.close()
            fileq.close()
            filea.close()
            break
        else:
            print("Password did not matched, Enter again")


if not path.exists("pass.txt"):
    password()  # if (path.exists("ans.txt")):
else:
    file = open("pass.txt", "r")
    pasw = input("""Enter your Password to Continue:""")
    s1 = ""
    for k in pasw:
        if 65 < ord(k) < 90 or 97 < ord(k) < 122:
            s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))
        else:
            s1 += k
    if s1 == file.read():
        print("Password Matched")
    else:
        print("Wrong Password")
        print("Enter 1 to reset the password else 0 to Exit")
        ch = int(input())
        if ch == 1:
            fileq = open('ques.txt', 'r')
            filea = open('ans.txt', 'r')
            fileans = input(fileq.read())
            if fileans == filea.read():
                password()
            else:
                print("Wrong answer")
                sys.exit()
        else:
            sys.exit()

while True:  # os.stat("ans").st_size == 0:#file = open('ans.txt', 'w')
    print("""
              Menu-
              
              1. Atbash Encryption
              2. Rot13
              3. Rot22
              4. Simple Encryption(add 1)
              5. caesar(with ur key) where ! denotes a single space 
              6. Change your Password
              0. Exit The program 
                                              """)
    c = int(input("Your Choice-"))
    if c == 0:
        print(color.WARNING + "Thanks for using me!" + color.END)
        print(color.FAIL + "Leave a Reply on hj101998@gmail.com" + color.END)
        sys.exit(0)

    if c == 1:
        prnt()
        while True:
            f = int(input("Enter your choice-"))
            if f == 1:
                bashenc()
            elif f == 2:
                bashdec()
            elif f == 3:
                break
    elif c == 2:

        while True:
            prnt()
            f = int(input("Enter your choice-"))
            if f == 1:
                rotenc()
            elif f == 2:
                rotdec()
            elif f == 3:
                break

    elif c == 3:

        while True:
            prnt()
            f = int(input("Enter your choice-"))
            if f == 1:
                rot22enc()
            elif f == 2:
                rot22dec()
            elif f == 3:
                break

    elif c == 4:

        while True:
            prnt()
            f = int(input("Enter your choice-"))
            if f == 1:
                simenc()
            elif f == 2:
                simdec()
            elif f == 3:
                break

    elif c == 5:

        while True:
            prnt()
            f = int(input("Enter your choice-"))
            if f == 1:
                cenc()
            elif f == 2:
                cdec()
            elif f == 3:
                break

    elif c==6:
        password()
