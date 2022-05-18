from array import*
a=[["123","TOM","DTGD"],["456","Cat","CSIE"],["789","Nana","ASIE"],["321","Lim","DBA"],["654","Won","FDD"]]
b=input("輸入查詢學號為")
for i in range(5):
    if (a[i][0]) == b:
        print(f"學生資料為:{a[i][0]} {a[i][1]} {a[i][2]}")