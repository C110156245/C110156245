a=int(input("輸入度數:"))

if a <= 120:
    print(f"Summer months{a*2.10}")
    print(f"Not summer months{a*2.10}")
elif a > 120 and a <=330:
    print(f"Summer months{(120*2.10)+(a-120)*3.02}")
    print(f"Not summer months{(120*2.10)+(a-120)*2.68}")
elif a > 330 and a <=500:
    print(f"Summer months{(120*2.10)+(330-120)*3.02+(a-330)*4.39}")
    print(f"Not summer months{(120*2.10)+(330-120)*2.68+(a-330)*3.61}")
elif a > 500 and a <=700:
    print(f"Summer months{(120*2.10)+(330-120)*3.02+(500-330)*4.39+(a-500)*4.97}")
    print(f"Not summer months{(120*2.10)+(330-120)*2.68+(500-330)*3.61+(a-500)*4.01}")
elif a>700:
    print(f"Summer months{(120*2.10)+(330-120)*3.02+(500-330)*4.39+(700-500)*4.97+(a-700)*5.63}")
    print(f"Not summer months{(120*2.10)+(330-120)*2.68+(500-330)*3.61+(700-500)*4.01+(a-700)*4.50}")
    