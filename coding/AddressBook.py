#通讯录的类
class AddressBook:
	''' '''
	def __init__(self,ab_item={}):
		if type(ab_item) != type({}):
			raise TypeError('这里需要一个字典作为参数')
		else:
			self.ab_item = ab_item
	
	def __add_ab(self,name,phone):
		'''添加的公用方法'''
		if type(name) != type('') and type(phone) != type([]):
			raise TypeError('参数类型错误')
		else:
			if not name in self.ab_item:
				self.ab_item[name] = phone
			else:
				for p in phone:
					self.ab_item[name].append(p)
			return
	
	def add_one(self,name,phone):
		'''添加一条数据'''
		if type(name) != type('') and type(phone) != type(''):
			raise TypeError('这里需要字符串作为参数')
		else:
			self.__add_ab(name,phone)
			
	def add_many(self,add_ab):
		'''添加多条数据'''
		if type(add_ab) != type({}):
			raise TypeError('这里需要一个字典作为参数')
		else:
			for add_ab_item in add_ab.keys():
				self.__add_ab(add_ab_item,add_ab[add_ab_item])
			return
	
	def	query_by_name(self,name):
		'''根据名称查询号码'''
		if type(name) != type(''):
			raise TypeError('参数有误')
		else:
			if not name in self.ab_item:
				return None
			else:
				return self.ab_item[name]
	
	def update_ab_item(self,name,phone,new_phone):
		'''根据名称，号码修改记录'''
		if type(name) != type('') and type(phone) != type(''):
			raise TypeError('参数有误')
		else:
			if not name in self.ab_item:
				return None
			else:
				if not phone in self.ab_item[name]:
					return None
				else:
					self.ab_item[name][self.ab_item[name].index(phone)] = new_phone
	
	def delete_ab_item(self,name):
		'''根据名称删除一条记录'''
		if type(name) != type(''):
			raise TypeError('参数有误')
		else:
			if not name in self.ab_item:
				return None
			else:
				self.ab_item.pop(name)
		
a = AddressBook({})
a.add_one('d',['123'])
a.add_many({'a':['123'],'d':['456']})
print(a.ab_item)
a.update_ab_item('a','123','789')
print(a.query_by_name('d'))
print(a.ab_item)
a.delete_ab_item('d')
print(a.ab_item)