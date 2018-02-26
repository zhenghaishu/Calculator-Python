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

	
root.mainloop()