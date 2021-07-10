# 產生隨機整數1~100 (不要印出來)
# 讓使用者重複輸入猜數字
# 猜對印出"猜對了!"
# 猜錯要提示比答案大/小

import random
r_num = random.randint(1,100)
time = 0

while True:
	print('請猜數字：')
	print(r_num)
	num = input()

	try:	#判斷使用者是否輸入整數
		int(num)
		num = int(num)
		
		if r_num == num:
			time +=1
			print('猜對了!!!', '總共猜了', time, '次')
			break
		
		elif r_num < num and num <= 100 and num > 0:
			print('再小一點', '目前猜了', time, '次')
			time += 1
		
		elif r_num > num and num <= 100 and num > 0:
			print('再大一點', '目前猜了', time, '次')
			time += 1
		
		else:
			print('您輸入的數字超過區間範圍，請輸入1-100區間內正整數')

	except ValueError:
		print('您輸入為非數字或含有小數點，請輸入1-100區間內正整數')
