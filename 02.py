import tkinter

w = 280
h = 480
processH = 120
resultH = 60
btnW = 70
btnH = 60

root = tkinter.Tk()
root.minsize(w, h);
root.title('我的计算器')

process = tkinter.StringVar()
process.set('')
result = tkinter.StringVar()
result.set(0)

labelProcess = tkinter.Label(root, font = ('微软雅黑', 20), bg = '#ff0000', bd = '9', fg = '#00ffff', anchor = 'se', textvariable = process)
labelProcess.place(width = w, height = processH)
labelResult = tkinter.Label(root, font = ('微软雅黑', 30), bg = '#00ff00', bd = '9', fg = '#0000ff', anchor = 'se', textvariable = result)
labelResult.place(y = processH, width = w, height = resultH)

btn7 = tkinter.Button(root, text = '7', font = ('微软雅黑', 20), fg = '#000000', bd = 0.5, command = lambda : clickNum('7'))
btn7.place(x = 0, y = processH + resultH + btnH, width = btnW, height = btnH)

root.mainloop()
