#產生一個隨機整數1~100
#讓使用者重複輸入數字去猜
#猜對的話 印出"終於猜對了"
#猜錯的話要告訴 他比答案大/小

import random
r = random.randint(1, 100)
n = 0 #猜第幾次
while True :
	g = input('終極密碼數字多少?')
	g = int(g)
	if g == r :
		print('真狗屎運,竟然猜對了')
		break
	elif g < r :
		print('比答案小')
	elif g > r :
		print('比答案大')
	n = n + 1
	print('這是你猜', n, '次 小嫩逼' )





