
a=input()
a1=[]
a2 = []
for i in a:
    a1.append(i)
print(a1)
for i in range(len(a1)):
    if a1[i] in a1:
        a2.append(a1[i])

print(f"重複的字{a2}")
