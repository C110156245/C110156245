list1=[]
sum=0
a=input("檢測字串(end結束):")
b=input("檢測的單一字元")
for i in a:
    list1.append(i)
for i1 in range(len(list1)):
    if b == list1[i1]:
        sum +=1
    elif b == "end":
        break
print(f"字元{b}出現次數為{sum}")
