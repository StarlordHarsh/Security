
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
from os import system, name, path
import progressbar
import sys
import time
#from tqdm import tqdm

def bashenc():
    s = input("Enter the message to Encrypt:")
    s1 = ""

    for k in s:
        if ord(k)==32:
            s1+=" "
        else:
            s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))
    print("Encrypted message is:", s1)

def bashdec():
    s = input("Enter the message to Decrypt:")
    s1 = ""
    for k in s:
        if ord(k) == 32:
            s1 += " "
        else:
            s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))
    print("Decrypted message is:", s1)

def rotenc():
    s = input("Enter ur string here to Encrypt:")
    li = len(s)
    s1 = ""
    print("Encrypted string is:", end="")
    print("\n")

    for i in s:
        if ord(i) == 32:
            s1 += " "
        else:
            j = ord(i) + 13
            s1 += (chr(j if j <= 90 else (j - 26)) if i.isupper() else chr(j if j <= 122 else (j - 26)))
    print(s1)

def rotdec():
    s = input("Enter ur string here to Decrypt:")
    li = len(s)
    s1 = ""
    print("Encrypted string is:", end="")
    print("\n")

    for i in s:
        if ord(i) == 32:
            s1 += " "
        else:
            j = ord(i) - 13
            s1 += (chr(j if j >= 65 else (j + 26)) if i.isupper() else chr(j if j >= 97 else (j + 26)))
    print(s1)

def rot22enc():
    s = input("Enter ur string here to Encrypt:")
    li = len(s)
    s1=""
    print("Encrypted string is:", end="")
    print("\n")

    for i in s:
        if ord(i) == 32:
            s1 += " "
        else:
            j = ord(i)+22
            s1 += (chr(j if j<=90 else (j-26)) if i.isupper() else chr(j if j<=122 else (j-26)))
    print(s1)

def rot22dec():
    s = input("Enter ur string here to Decrypt:")
    li = len(s)
    s1 = ""
    print("Encrypted string is:", end="")
    print("\n")

    for i in s:
        if ord(i) == 32:
            s1 += " "
        else:
            j = ord(i) - 22
            s1 += (chr(j if j >= 65 else (j + 26)) if i.isupper() else chr(j if j >= 97 else (j + 26)))
    print(s1)

def simenc():
    s = input("Enter the string to encrypt here:")
    print(color.HEADER + "Encrypted string is:" + color.END, end="")

    for i in s:
        if ord(i)==32:
            print(" ",end="")
        else:
            k = ord(i)+1
            print(chr(k), end="")

def simdec():
    s = input("Enter the encrypted string here to decrypt it:")
    print(color.HEADER + "Decrypted string is" + color.END, end="")

    for i in s:
        if ord(i)==32:
            print(" ", end="")
        else:
            k = ord(i)-1
            print(chr(k), end="")

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
        elif n > k:
            print(n, end="")
        elif ord(n) == 32:
            print(' ', end="")

def cdec():
    t = input("Enter the string to Decrypt:")
    k = input("Enter the key you used earlier during Encryption:")
    for j in t:
        if j > k:
            print(j, end="")
        elif j < k:
            j = chr(ord(j) + 1)
            print(j, end="")
        elif j == k:
            print('a', end="")
        elif j == ' ':
            print(' ', end="")

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
if (path.exists("ans.txt")==True):
    print("""
                  Enter your password to conitnue:""")
    pasw=input()
    file = open('pass.txt', 'w')
    file.write(pasw)
    file.close()
#if (path.exists("ans.txt")):


while True:
    #os.stat("ans").st_size == 0:
    #file = open('ans.txt', 'w')

    print("""
              Menu-
              
              1. Atbash Encryption
              2. Rot13
              3. Rot22
              4. Simple Encryption(add 1)
              5. caesar(with ur key) where ! denotes a single space 
              0. Exit The program 
                                              """)
    c = int(input("Your Choice-"))
    if c == 0:
        delay_print(color.WARNING + "Thanks for using me!" + color.END)
        delay_print(color.FAIL + "Leave a Reply on cyberbot1502@gmail.com" + color.END)
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

