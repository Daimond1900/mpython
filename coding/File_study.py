#文件操作
import os
import time
def make_text_file(message):
#	if os.path.isfile('text.txt'):
#		print('文件已经存在')
#	else:
		a = open('text.txt','a')
		a.write('''
hello world
say hello
who are you
		''')
		a.close


def read_txt(line):
	if not os.path.isfile('text.txt'):
		print("文件不存在")
	else:
		a = open('text.txt','r')
		txt = a.readlines()[line-1]
		a.close
		return txt
#print(read_txt(4))

def split_fully(path):
	parent,name = os.path.split(path)
	if name == '':
		return (parent,)
	else:
		return split_fully(parent)+(name,)
print(split_fully("C:\\Users\\1900\\Desktop\\mandroid\\MStudyAndroidLib\\app\\libs"))

def list_desktop(path):
	for file_name in os.listdir(path):
		print(os.path.join(path,file_name))
		
list_desktop('C:\\Users\\1900\\Desktop')
print('-'*100)

def print_tree_dir(path):
	for x in os.listdir(path):
		x_path = os.path.join(path,x)
		x_size = os.path.getsize(x_path)/1024
		x_time = time.ctime(os.path.getmtime(x_path))
	
		print("%-32s:%8d KB,modified %s" % (x_path,x_size,x_time))

		if os.path.isdir(x_path):
			print_tree_dir(x_path)
		
print_tree_dir('C:\\Users\\1900\\Desktop\\mpython\\coding')





















