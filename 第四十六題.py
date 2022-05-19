a = (input("輸入筆數n:"))
o={}
for i in range(4):
    h=(input("獎牌 面數").split())
    o[h[0]]=h[1]
        
print(f"金牌有{o['金']}面")
print(f"銀牌有{o['銀']}面")
print(f"銅牌有{o['銅']}面")
print(f"優牌有{o['優']}面")


