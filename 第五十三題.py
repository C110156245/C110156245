mail=[]
name1=[]

a=int(input("輸入n值:"))
for a in range(a):
    a1=input("輸入姓名:")
    b1=input("輸入電子郵件:")
    name1.append(a1)
    mail.append(b1)
c = input("請輸入要查詢電子郵件的名字:")
for i in range(len(name1)):
    if name1[i] == c:
        print(f"{name1[i]}得電子郵件是{mail[i]}")