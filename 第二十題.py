a=int(input("組數為:"))
for i in range(a):
    a1,a2=map(int,input(f"第{i+1}組").split(" "))
    print(f"第{i+1}組應收費用{(a1*250)+(a2*175)}元")