all =set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
English=set(['John','Mary','Fiona','Claire','Ben','Bill'])
Math = set(['Mary','Fiona','Claire','Eva','Ben'])
EnMaallpass=[]
Manopass=[]
EnManopass=[]
for i in all:
    if i in English and i in Math:
        EnMaallpass.append(i)
    elif i not in Math and i not in English:
        EnManopass.append(i)
    elif i not in Math:
        Manopass.append(i)
print(f"數學英文都及格{EnMaallpass}")
print(f"數學不及格{Manopass}")
print(f"數學英文都不及格{EnManopass}")

    