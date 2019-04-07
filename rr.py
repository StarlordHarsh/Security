import random

st = ""
while len(st) < 9:
    ran = random.randrange(4)
    if ran == 0:
        st += chr(random.randrange(33, 34))
        print(ran, "", st)
    elif ran == 1:
        st += chr(random.randrange(48, 58))
        print(ran, "", st)
    elif ran == 2:
        st += chr(random.randrange(65, 91))
        print(ran, "", st)
    elif ran == 3:
        st += chr(random.randrange(97, 123))
        print(ran, "", st)
st+="ywod"
print(st[9:])
