print('这是一个游戏，开始吧！')
while True:
	age = input('请输入年龄（推出no）: ')
	if age == 'no':
		print('游戏结束')
		break
	try:
		age = int(age)
		if age <= 20:
			print('好年轻啊')
		elif age <= 30:
			print('你是一个青年人')
		elif age <= 40:
			print('人到中年啦')
		else:
			print('老了啊，时光一去不复返啊！')
	except ValueError as error:
		print('输入有误请重新输入！')