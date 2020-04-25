#請受試者 「自行輸入數字範圍」
#讓使用者重複輸入數字去猜
#猜對的話 印出"終於猜對了"
#猜錯的話要告訴 他比答案大/小

import random
start = input('請決定數值範圍之下限')
end = input('請決定數值範圍之上限')
start = int(start)
end = int(end)
r = random.randint(start, end)
n = 0 #猜第幾次
while True :
	n +=  1 # n = n+1
	g = input('終極密碼數字多少?')
	g = int(g)
	if g == r :
		print('真狗屎運,竟然猜對了')
		print('智障嗎 第', n, '次才猜對' )
		break
	elif g < r :
		print('比答案小')
	elif g > r :
		print('比答案大')
	print('這是你猜', n, '次 小嫩逼' )





