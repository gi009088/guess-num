# 產生隨機整數1~100 (不要印出來)
# 讓使用者重複輸入猜數字
# 猜對印出"猜對了!"
# 猜錯要提示比答案大/小

while True:
	print('1. 玩猜數字')
	print('2. 離開')
	mod = input()

	if mod == '2':	#離開
		print()
		print('掰掰~')
		break

	elif mod == '1':	#開始遊戲程式

		import random
		import string
		u_min = input('請輸入猜數字的最小值：')
		u_max = input('請輸入猜數字的最大值：')
		
		try:	#判斷使用者輸入的最大最小直是否為整數
			int(u_min) and int(u_max)
			u_min = int(u_min)
			u_max = int(u_max)

			r_num = random.randint(u_min,u_max)		#產生隨機數
			count = 0 		#累計使用者猜了幾次

			while True:
				print('請猜', u_min, '-', u_max, '區間內的數字')

				if count > 5:	#猜超過十次出現放棄文字
					print('放棄看答案請輸入Q')
				if count > 5 and count < 11:
					print('~真的不放棄?!你很有毅力!!~')
				if count == 11:
					print('國父革命11次才成功,加油!!')
				if count > 11 and count < 20:
					print('國父革命11次成功,你試了', count, '次')
				if count == 20:
					print('頒給你毅力獎盃~<3')

				print()
				num = input('我猜...')	

				if num.title() == 'Q' and count > 10:	#放次本局直接看答案
					print('答案為：', r_num, '你輸了!!!')
					print('總共猜了', count, '次')
					if count >= 20:
						print('不過你有毅力獎盃')
					break
				elif num.title() == 'Q' and count <= 10: #小於10次內不可放棄遊戲
					print('小於10次放棄遊戲，將不顯示答案')
					print('掰掰~')
					print()
					print()
					break


				try:	#判斷使用者是否輸入整數
					int(num)
					num = int(num)
		
					if r_num == num:
						count +=1
						print('猜對了!!!', '總共猜了', count, '次')
						if count >= 21:
							print('毅力成功王')
						print()
						break
					elif r_num < num and num <= u_max and num >= u_min:
						count += 1
						u_max = num
						print('再小一點', '目前猜了', count, '次')
						print()
					elif r_num > num and num <= u_max and num >= u_min:
						count += 1
						u_min = num
						print('再大一點', '目前猜了', count, '次')
						print()
					else:
						print('您輸入的數字超過區間範圍，請輸入', u_min, '-', u_max, '區間內整數')
						print()

				except ValueError:
					print('您輸入為非指定文字或含有小數點，請輸入', u_min, '-', u_max, '區間內整數')
					print()
		
		except ValueError:
			print()
			print('請輸入正確的區間數字或離開')
			print()
