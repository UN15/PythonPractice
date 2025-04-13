total_s = 12345
t = str(total_s//3600)
last_s = total_s%3600
m = str(last_s//60)
s = str(last_s%60)

print(str(total_s)+"초는 "+t+"시간 "+m+"분 "+s+"초입니다.")