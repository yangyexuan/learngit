#-*-coding:utf-8-*-
"""还以为用Python实现堆栈很难，静下心来看大神写的
才发现其实没什么"""

class stack(object):
	
	def __init__(self, stk = []):
		self._stk = stk
	def pop(self):
		if len(self._stk) == 0:
			return "Sorry,stack is empty,can not pop"
		else:
			return self._stk.pop()
	def push(self,element):
		self._stk.append(element)
	def view(self):
		return self._stk

if __name__ == '__main__':
	ss = stack()
	ss.push(1)
	ss.push(2)
	ss.push('a')
	print (ss.pop())
	ss.push('ad')
	print (ss.view())
		