#函数实例
def add_num(a,b=10):
	'''两个数字相加  '''
	if str(type(a)) == "<class 'int'>" and str(type(b)) == "<class 'int'>" :
		return a + b
	else:
		return None
		
addResult = add_num(1)
if addResult != None:
	print(addResult)
else:
	print('参数类型错误')

print(add_num.__doc__)


