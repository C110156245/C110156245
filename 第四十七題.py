a = (input("輸入筆數n:"))
p=[]
for i in range(4):
    g=(input("獎牌 面數").split())
    p.append(g)
for t in p:
    print(f"{t[0]}牌有{t[1]}面")