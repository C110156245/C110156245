n=int(input("請輸入階層值M:"))
h=0
sum=1
while True:
    h+=1
    sum*=h
    if sum > n:
        print(f"超過M為{n}的最小階層N值為{h}")
        break 