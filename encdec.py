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


from os import system, name, path
import progressbar
from getpass import getpass
import sys
import time
import uuid
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import random
import time


def bashenc():
    s = input("Enter the message to Encrypt:")
    s1 = ""

    for k in s:
        if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
            s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))
        else:
            s1 += k
    print("Encrypted message is:", s1)


def bashdec():
    s = input("Enter the message to Decrypt:")
    s1 = ""

    for k in s:
        if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
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
    for k in s:
        if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
            j = ord(k) + 13
            s1 += (chr(j if j <= 90 else (j - 26)) if k.isupper() else chr(j if j <= 122 else (j - 26)))
        else:
            s1 += k
    print(s1)


def rotdec():
    s = input("Enter ur string here to Decrypt:")
    li = len(s)
    s1 = ""
    print("Encrypted string is:", end="")
    print("\n")
    for k in s:
        if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
            j = ord(k) - 13
            s1 += (chr(j if j >= 65 else (j + 26)) if k.isupper() else chr(j if j >= 97 else (j + 26)))
        else:
            s1 += k
    print(s1)


def rot22enc():
    s = input("Enter ur string here to Encrypt:")
    s1 = ""
    print("Encrypted string is:", end="")
    print("\n")

    for k in s:
        if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
            j = ord(k) + 22
            s1 += (chr(j if j <= 90 else (j - 26)) if k.isupper() else chr(j if j <= 122 else (j - 26)))
        else:
            s1 += k
    print(s1)


def rot22dec():
    s = input("Enter your string here to Decrypt:")
    s1 = ""
    print("Encrypted string is:", end="")
    print("\n")

    for k in s:
        if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
            j = ord(k) - 22
            s1 += (chr(j if j >= 65 else (j + 26)) if k.isupper() else chr(j if j >= 97 else (j + 26)))
        else:
            s1 += k
    print(s1)


def simenc():
    s = input("Enter the string to encrypt here:")
    print(color.HEADER + "Encrypted string is:" + color.END, end="")

    for k in s:
        if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
            k = ord(k) + 1
            print(chr(k), end="")
        else:
            print(k, end="")


def simdec():
    s = input("Enter the encrypted string here to decrypt it:")
    print(color.HEADER + "Decrypted string is" + color.END, end="")

    for k in s:
        if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
            i = ord(k) - 1
            print(chr(i), end="")
        else:
            print(k, end="")


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
        elif not (65 <= ord(k) <= 90) or not (97 <= ord(k) <= 122):
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
        elif not (65 <= ord(k) <= 90) or not (97 <= ord(k) <= 122):
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


def chkpass(pasw):
    s1 = ""
    for k in pasw:
        if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
            s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))
        else:
            s1 += k


def password():
    while True:
        pasw = input("Enter your new Password:")
        pasw1 = input("Enter your Password again:")
        if pasw == pasw1:
            file = open('pass.txt', 'w')
            s1 = ""
            while len(s1) < 9:
                ran = random.randrange(4)
                if ran == 0:
                    s1 += chr(random.randrange(33, 34))
                elif ran == 1:
                    s1 += chr(random.randrange(48, 58))
                elif ran == 2:
                    s1 += chr(random.randrange(65, 91))
                elif ran == 3:
                    s1 += chr(random.randrange(97, 123))
            for k in pasw:
                if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
                    s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))
                else:
                    s1 += k
            file.write(s1)
            file.close()
            break
        else:
            print("Password did not matched, Enter again")


def mail():
    secsend = time.time()
    fromaddr = "cyberbot1502@gmail.com"
    toaddr = "hj101998@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'OTP'
    otp = ""
    while len(otp) < 6:
        otp += chr(random.randrange(48, 58))
    body = "OTP-" + otp + "\n This otp will expire in 2 mins"
    msg.attach(MIMEText(body, 'plain'))
    attachment = open("README.md", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "Hexadecimalqwertyuiop")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()
    print("OTP Sent Successfully to:", toaddr)
    return otp, secsend


if not path.exists("pass.txt"):
    otp, secsend = mail()
    while True:
        chkOTP = input("Enter the OTP-") if chkOTP == otp and int(time.time() - secsend) < 120:
            password()
            break
        elif int(time.time() - secsend) >= 120:
            print("OTP expired !")
        else:
            print("OTP entered is wrong, Try Again")
else:
    tryc = 3
    while tryc != 0:
        file = open("pass.txt", "r")
        pasw = input("Enter your Password to Continue:")
        s1 = ""
        for k in pasw:
            if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
                s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))
            else:
                s1 += k
        if s1 == file.read()[9:]:
            print("Password Matched")
            break
        else:
            print("Wrong Password")
            tryc -= 1
    if tryc == 0:
        print("A mail has ben snet to your registered email, please enter it to reset your password")
        otp = mail()
        if input("Enter the OTP received") == otp:
            clr()
            password()
        else:
            print("Wrong answer")
            sys.exit(0)

while True:
    clr()
    print("""
              Menu-
              
              1. Atbash Encryption
              2. Rot13
              3. Rot22
              4. Simple Encryption
              5. Caesar Keyed 
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
                clr()
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
                clr()
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
                clr()
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
                clr()
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
                clr()
                break

    elif c == 6:
        password()
