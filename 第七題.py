import math

a,b=map(int,(input("輸入月租費形式及通話時間為:").split(",")))
if str(a) == "186":
    if (b*0.09) / 186 <= 2:
        print(f"通話費為:{math.ceil((b*0.09)*0.9)}")
    elif (b*0.09) / 186 > 2:
        print(f"通話費為:{math.ceil((b*0.09)*0.8)}")
elif str(a) =="386":
    if (b*0.08) / 186 <= 2:
        print(f"通話費為:{math.ceil((b*0.08)*0.8)}")
    elif (b*0.08) / 186 > 2:
        print(f"通話費為:{math.ceil((b*0.08)*0.7)}")

elif str(a) =="586":
    if (b*0.07) / 186 <= 2:
        print(f"通話費為:{math.ceil((b*0.07)*0.7)}")
    elif (b*0.07) / 186 > 2:
        print(f"通話費為:{math.ceil((b*0.07)*0.6)}")

elif str(a) =="986":
    if (b*0.06) / 186 <= 2:
        print(f"通話費為:{math.ceil((b*0.06)*0.6)}")
    elif (b*0.06) / 186 > 2:
        print(f"通話費為:{math.ceil((b*0.06)*0.5)}")