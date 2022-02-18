


import tkinter as tk

def draw():
    print("ddd")

"""
主視窗控制
"""
win = tk.Tk() #建立主視窗
win.title("Rose Beta -1 ")

#視窗大小
win.geometry('1024x768') #主視窗大小 寬*高
#win.minsize(width=400 , height= 400 )
#win.maxsize(width=1024 , height= 768 )
win.resizable(False,False)

#icon
win.iconbitmap("rose-shape.ico")
#背景顏色
win.config(background= "#D55FD1")
#透明度
win.attributes("-alpha" , 0.9)

"""
按鈕
"""
filename = r"D:\Vs code\vscode file\python\gif1.gif"
img1 = tk.PhotoImage(file=filename)

bt1 = tk.Button(text="click")
bt1.config(bg="#929C82")
bt1.config(width= 4 , height= 2 )
bt2 = tk.Button(text="click test ")
bt2.config(image = img1)

bt1.config(command=draw)
bt1.pack()#封裝按鈕
bt2.pack()





win.mainloop() #讓主視窗不關閉