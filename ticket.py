from random import randint,randrange
l = []
while True:
    ticket = f"IRT{randint(100000,999999)}"
    l.append(ticket)
    if len(l) == 10:
        break
print(l)
ele = l[0]
chk = True
for item in l:
    if ele != item:
        chk = False
        break

if (chk == True): print("Equal")
else: print("Not equal") 