print("1.feladat")
for i in range(40,60,5):
    print(i)

print("2.feladat")
for i in range(200,0,-40):
    print(i,end=" ")

print("3.feladat")
import random
k=[]
menyi=int(input("Mennyi szám legyen eg sorban? "))
for i in range(30):
    x=random.randint(-10,10)
    print(f"{x:2}",end=" ")
    k.append(x)
    if i%menyi==menyi-1:
        print()

print("4.feladat")
n=0
nu=0
for i in range(30):
    if k[i]<0:
        n+=1
    if k[i]==0:
        nu+=1
print(f"{n} db negatív szám van a listában.")
print(f" {nu} db mulla van a listában.")


print("5.feladat")
d=[]
for i in range(50):
    d.append(random.randint(2,12))
for i in range(50):
    print(f"{d[i]:2.0f}",end=" ")
    if i%10==9:
        print()

print("6.feladat")
szam=0
while szam<2 or szam>12:
    szam=int(input("Kérek egy számot (2-től 12-ig): "))
    if szam<2 or szam>12:
        print("Nem jó a szám!")


print("7.feladat")
db=0
for i in range(50):
    if d[i]==szam:
        db+=1
print(f"A listában {db} db {szam}-os van.")