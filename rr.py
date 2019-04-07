import random
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
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
print(color.UNDERLINE + st[9:])
