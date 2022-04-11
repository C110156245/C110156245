def prime(x):
    for i in range(2,x):
        if x%i ==0:
            return False
    return True

list_=[]
num = input("請輸入數字")
for i in range(len(num)):
    for h in range(i,len(num)):
        key = int(num[i:h+1])
        if prime(key):list_.append(key)
print(f"最大質數{max(list_)}")if len(list_) > 0 else "No prime found"

