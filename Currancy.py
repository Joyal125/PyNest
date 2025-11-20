amount = int(input("Enter amount: "))
denom = int(input("Enter denomination: "))

match denom:
    case 100:
        print("100 :", amount // 100)
    case 50:
        print("50 :", amount // 50)
    case 20:
        print("20 :", amount // 20)
    case 10:
        print("10 :", amount // 10)
    case 5:
        print("5 :", amount // 5)
    case 2:
        print("2 :", amount // 2)
    case 1:
        print("1 :", amount // 1)
    case _:
        print("Invalid denomination")
