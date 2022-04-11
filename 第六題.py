from multiprocessing.connection import answer_challenge
from ntpath import join


a=map(str,input("輸入值為:").split(","))
list_=[]
for i in a:
    list_.append(i)
list_int=list(map(int,list_))
a1=sorted(list_int)
a2=list(reversed(a1))
s="".join(map(str,a1))
b="".join(map(str,a2))
ans=int(b)-int(s)
print(f"最大值數列和最小值數列差值為{str(ans)}")