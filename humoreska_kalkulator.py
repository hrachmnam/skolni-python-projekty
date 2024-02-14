#variables
print("prvni číslo: ")
a = input()
print("druhé číslo: ")
b = input()
print("""vyber operátor: 
(Plus/Mínus)""")
#humoresky
c = input()
print(str(c) + "? nebo jak to bylo?")
#počítání
d = input()
if c == d:
    if d == "P":
        print(int(a)+int(b))
    elif d == "M":
        print(int(a)-int(b))
    else:
        print("error :)")
else:
    print("error :)")
