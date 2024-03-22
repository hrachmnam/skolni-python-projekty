print("Dobrý den")
print("Tento program určí vaše BMI(body mass index)")
print("*" * 44)
print("zadejte vaši výšku v cm")
height_in_cm = int(input())
print("zadejte vaši hmotnost v kg")
weight = int(input())
height_in_m = (height_in_cm / 100)
bmi = round((weight / (height_in_m * height_in_m)) , 2)
print("vaše bmi je: " + str(bmi))
if bmi <= 16.5:
    print("máte těžkou podvýživu")
elif bmi > 16.5 and bmi < 18.5:
    print("máte podváhu")
elif bmi > 18.5 and bmi < 25:
    print("máte ideální (zdravou) váhu")
elif bmi > 25 and bmi < 30:
    print("máte nadváhu")
elif bmi > 30 and bmi < 35:
    print("máte obezitu prvního stupně")
elif bmi > 35 and bmi < 40:
    print("máte obezitu druhého stupně")
elif bmi > 40:
    print("máte obezitu třetího stupně (též morbidní obezitu)")
else:
    print("ERROR")
