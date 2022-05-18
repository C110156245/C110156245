
item = ['國文','英文','微積分','體育','程式設計']
score=[]
a1=int(input('國文:'))
a2=int(input('英文:'))
a3=int(input('微積分:'))
a4=int(input('體育:'))
a5=int(input('程式設計:'))
score.append(a1)
score.append(a2)
score.append(a3)
score.append(a4)
score.append(a5)
avg = (a1+a2+a3+a4+a5)/5
print(f'平均分數:{avg}')
maxscore=(max(score))
minscore=(min(score))
s=score.index(maxscore)
s1=score.index(minscore)
print(f'最高分科目:{item[s]}{maxscore}分')
print(f'最低分科目:{item[s1]}{minscore}分')

