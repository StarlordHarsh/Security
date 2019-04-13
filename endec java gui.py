file = open("M:\My code here\EnDec Projec\myfile.txt", "r")
s=file.read()
s1 = ""
for k in s:
    if 65 <= ord(k) <= 90 or 97 <= ord(k) <= 122:
        s1 += (chr(90 - (ord(k) - 65))) if k.isupper() else chr(122 - (ord(k) - 97))
    else:
        s1 += k
print(s1)

