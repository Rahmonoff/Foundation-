try:
    with open("raqamlar.txt","w") as f:
        f.write("1 2 3 4 5 6 7 8 9 10")
except FileNotFoundError:
    print("Fayl ochishda xatolik")

try:
    with open("raqamlar.txt","r") as f:
        mylist = f.read().split()
        mylist1 = list(map(lambda x: int(x), mylist))
        result = sum(mylist1)
except FileNotFoundError:
    print("Fayl ochishda xatolik")
print(result)    