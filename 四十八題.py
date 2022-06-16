animal = {}
n=int(input("輸入筆數n:"))
for i in range(n):
    key1,value1 = map(str,input(":").split(" "))
    animal[key1] = value1
a=input("輸入欲查詢單字:")
if a in animal:
    print(f"{a}中文意思為{animal.get(a)}")
else:
    print("無")