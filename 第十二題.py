a=list(map(str,input("輸入一整數列為:").split(" ")))
set_a = set(a)
l = list(set_a)
for item in l:
    if a.count(item) >= (len(a)/2):
        print(f"過半元素為{item}")
        break
    else:
        print("過半元素為NO")
        break




a=list(map(str,input("輸入一整數列為:").split(" ")))
for i in a:
    print(i) 