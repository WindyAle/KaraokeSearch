drinkDic = { "Coke":1500, "Trevi":1200, "Fanta":1000, "Coffee":800 }
drinkList = list(drinkDic)

print("\n===== Vending Machine =====")
money = int(input("Please input money: "))
print("Your entered", money)

while money >= min(drinkDic.values()):
    print("\nSelect drink")
    print("====================")
    for i, name in enumerate(drinkList):
        print(i+1, name+":", drinkDic[drinkList[i]])
    print("====================")

    pick = int(input("\nChoose one: "))
    print(drinkList[pick-1], "selected")

    money - drinkDic[drinkList[pick-1]]
    print("\n", money, "remained")

print("Thank you to use")