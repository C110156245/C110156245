month,day=map(int,input("輸入月及日:").split(" "))
if month == 1:
    if day >=21 and day<=31:
        print("水瓶座")
    elif day<21 and day>0:
        print("摩羯座")
elif month == 2:
    if day >=1 and day<=18:
        print("水瓶座")
    elif day>18 and day<=28:
        print("雙魚座")
elif month == 3:
    if day >=1 and day<=20:
        print("雙魚座")
    elif day>20 and day<=31:
        print("牡羊座")
elif month == 4:
    if day >=1 and day<=20:
        print("牡羊座")
    elif day>20 and day<=30:
        print("金牛座")
elif month == 5:
    if day >=1 and day<=21:
        print("金牛座")
    elif day>21 and day<=31:
        print("雙子座")
elif month == 6:
    if day >=1 and day<=21:
        print("雙子座")
    elif day>21 and day<=30:
        print("巨蟹座")
elif month == 7:
    if day >=1 and day<=22:
        print("巨蟹座")
    elif day>22 and day<=31:
        print("獅子座")
elif month == 8:
    if day >=1 and day<=23:
        print("獅子座")
    elif day>23 and day<=31:
        print("處女座")
elif month == 9:
    if day >=1 and day<=23:
        print("處女座")
    elif day>23 and day<=30:
        print("天秤座")
elif month == 10:
    if day >=1 and day<=23:
        print("天秤座")
    elif day>23 and day<=31:
        print("天蠍座")
elif month == 11:
    if day >=1 and day<=22:
        print("雙子座")
    elif day>22 and day<=30:
        print("射手座")
elif month == 12:
    if day >=1 and day<=21:
        print("射手座")
    elif day>21 and day<=31:
        print("魔羯座")