import cmath

a = float(input("zadejte koeficient a: "))
b = float(input("zadejte koeficient b: "))
c = float(input("zadejte koeficient c: "))

diskriminant = (b**2) - (4*a*c)

if diskriminant > 0:
    koren1 = (-b + (diskriminant ** 0.5)) / (2*a)
    koren2 = (-b - (diskriminant ** 0.5)) / (2*a)
    print("kořeny jsou:", koren1, "a", koren2)
elif diskriminant == 0:
    root = -b / (2*a)
    print("kořen:", root)
else:
    koren1 = (-b + cmath.sqrt(diskriminant)) / (2*a)
    koren2 = (-b - cmath.sqrt(diskriminant)) / (2*a)
    print("kořeny jsou komplexní:", koren1, "a", koren2)
