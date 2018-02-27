import tkinter #导入tkinter模块


#定义数值
w = 280			#整个界面的宽度
h = 480			#整个界面的高度
processH = 120	#存放计算过程的Label的高度
resultH = 60	#存放计算结果的Label的高度
btnWidth = 70	#按纽宽度
btnHeight = 60	#按纽高度


#面板设置
root = tkinter.Tk()
root.minsize(w,h)						#面板大小的最小值
root.title('海天一树的计算器')			#面板的标题

process = tkinter.StringVar()           #字符串用于存放计算过程，初始状态为空
process.set('')
result = tkinter.StringVar()			#字符串用于存放计算结果，初始状态为0
result.set(0)                           

#labelProcess用于显示计算过程，labelResult用于显示计算结果
labelProcess = tkinter.Label(root,font = ('微软雅黑',20),bg = '#ff0000',bd ='9',fg = '#828282',anchor = 'se',textvariable = process)
labelProcess.place(width = w,height = processH)
labelResult = tkinter.Label(root,font = ('微软雅黑',30),bg = '#00ff00',bd ='9',fg = 'black',anchor = 'se',textvariable = result)
labelResult.place(y = processH,width = w,height = resultH)

#数字按键
btn7 = tkinter.Button(root,text = '7',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : clickNum('7'))
btn7.place(x = 0,y = processH + resultH + btnHeight,width = btnWidth,height = btnHeight)
btn8 = tkinter.Button(root,text = '8',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : clickNum('8'))
btn8.place(x = btnWidth,y = processH + resultH + btnHeight,width = btnWidth,height = btnHeight)
btn9 = tkinter.Button(root,text = '9',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : clickNum('9'))
btn9.place(x = 2 * btnWidth,y = processH + resultH + btnHeight,width = btnWidth,height = btnHeight)

btn4 = tkinter.Button(root,text = '4',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : clickNum('4'))
btn4.place(x = 0,y = processH + resultH + 2 * btnHeight,width = btnWidth,height = btnHeight)
btn5 = tkinter.Button(root,text = '5',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : clickNum('5'))
btn5.place(x = btnWidth,y = processH + resultH + 2 * btnHeight,width = btnWidth,height = btnHeight)
btn6 = tkinter.Button(root,text = '6',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : clickNum('6'))
btn6.place(x = 2 * btnWidth,y = processH + resultH + 2 * btnHeight,width = btnWidth,height = btnHeight)

btn1 = tkinter.Button(root,text = '1',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : clickNum('1'))
btn1.place(x = 0,y = processH + resultH + 3 * btnHeight,width = btnWidth,height = btnHeight)
btn2 = tkinter.Button(root,text = '2',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : clickNum('2'))
btn2.place(x = btnWidth,y = processH + resultH + 3 * btnHeight,width = btnWidth,height = btnHeight)
btn3 = tkinter.Button(root,text = '3',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : clickNum('3'))
btn3.place(x = 2 * btnWidth,y = processH + resultH + 3 * btnHeight,width = btnWidth,height = btnHeight)
btn0 = tkinter.Button(root,text = '0',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : clickNum('0'))
btn0.place(x = btnWidth,y = processH + resultH + 4 * btnHeight,width = btnWidth,height = btnHeight)

	
root.mainloop()
