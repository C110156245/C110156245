A = input("sA")
B = list(map(str,input("sB").split(" ")))
if A in B:
    print("子字串判斷YES")
else:
    print("子字串判斷NO")