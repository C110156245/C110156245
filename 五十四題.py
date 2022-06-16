a=float(input("請輸入路段公里數:"))
if a < 1.5:
    print("所需車資為75")
else:
    sum = (a - 1.5)//0.25
    all1 = (sum*5) + 75
    print(f"所需車資為{all1}")
