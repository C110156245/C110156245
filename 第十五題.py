a=str(input("輸入一組四位數字為:"))
list_str=[]
list_int=[]
list_str1=[]
for i in a:
    list_str.append(i)
for n in range(len(list_str)):
    list_int.append(int(list_str[n]))
for h in range(len(list_int)):
    list_int[h]=(list_int[h]+7)%10
a1=list_int[0]
a2=list_int[1] 
a3=list_int[2] 
a4=list_int[3] 

list_int[0] = a3
list_int[2] = a1
list_int[1] = a4
list_int[3] = a2
for b in list_int:
    list_str1.append(str(b))
strA="".join(list_str1)
print(f"輸出加密後的數字為{strA}")
