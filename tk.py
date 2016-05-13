#-*-coding:utf-8-*-
from tkinter import *
import tkinter.messagebox as messagebox

#从Frame派生一个Application类，这是所有Widget的父容器
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput = Entry(self) 
		self.nameInput.pack()
		self.alertButton = Button(self,text='hello',command=self.hello)
		self.alertButton.pack()

	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message','Hello,%s' %name)

#实例化Appication,并启动消息循环
app = Application()     
app.master.title('Hello,World')     #设置窗口标题
app.mainloop()       #主消息循环
