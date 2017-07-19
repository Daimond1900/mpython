#类实例
class Fridge:
	''' 
		这是一个冰箱的类，提供两个方法，一个添加一种食物，另一个一次添加多个食物
	'''
	def __init__(self,items={}):
		'''初始化'''
		if type(items) != type({}):
			raise TypeError("这里需要一个字典作为参数")
		self.items = items
		return
		
	def __add_multi(self,food_name,quantity):
		'''向冰箱添加食物'''
		if not food_name in self.items:
			self.items[food_name] = 0
		self.items[food_name] += quantity
	
	def add_one(self,food_name):
		'''添加一种食物的方法'''
		if type(food_name) != type(''):
			raise TypeError("参数类型错误")
		else:
			self.__add_multi(food_name,1)
		return True
	
	def add_many(self,food_dict):
		'''添加多种食物的方法'''
		if type(food_dict) != type({}):
			raise TypeError("参数类型错误")
		else:
			for item in food_dict.keys():
				self.__add_multi(item,food_dict[item])
			return
	
	def has_various(self,foods):
		'''判断冰箱中时候还有某种食物'''
		try:
			for food in foods.keys():
				if self.items[food] < foods[food]:
					return False
				return True
		except KeyError as error:
			return False
	
	def has(self,food_name,quantity=1):
		'''判断'''
		return self.has_various({food_name:quantity})
		
fridg = Fridge({'牛奶':2,'苹果':3})
fridg.add_one('桃子')
fridg.add_many({'牛奶':3,'凉粉':8})
print(fridg.items)
if fridg.has('牛奶',10):
	print('还有牛奶可以拿')
else:
	print('牛奶已经没有了')
