print("zadejte dělenec")
a = int(input())
print("zadejte dělitel")
b = int(input())
if (a == 0 or b == 0):
    print("ERROR")
else:
    c = round(a/b,5)
    print("podíl je: " + str(c))
