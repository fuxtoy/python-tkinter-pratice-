from cProfile import label
from cgitb import text
from fileinput import close
import tkinter as tk

from click import command




"""
主視窗控制
"""
win = tk.Tk() #建立主視窗
win.title("Rose Beta -1 ")

#視窗大小
#win.geometry('400x200') #主視窗大小 寬*高
"""
讓主視窗center  
"""
window_height = 500
window_width = 900

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
"""
end here 
"""
#win.minsize(width=400 , height= 400 )
#win.maxsize(width=1024 , height= 768 )
win.resizable(False,False)

#icon
win.iconbitmap("rose-shape.ico")
#背景顏色
win.config(background= "#D55FD1")
#透明度
win.attributes("-alpha" , 0.9)



def close(): 
    global img1
    top = tk.Toplevel()
    top.title("new window")
    top.geometry('1024x768')
    top.iconbitmap("rose-shape.ico")
        #背景顏色
    top.config(background= "#D55FD1")
        #透明度
    top.attributes("-alpha" , 0.9)
    filename = r"D:\Vs code\vscode file\python\gif2.gif"
    img1 = tk.PhotoImage(file=filename)
    lb2 = tk.Label(top , image= img1 ).pack()
    lbkidding = tk.Button(top , text = "為什麼不按X X ??? ", font=("Arial", 30) ,command= top.destroy ).pack()

def get():
    tx = en.get()
    if tx == "我喜歡你":
        lb.config(text ="我也是")
    else : 
        lb.config(text = " error ")
        winout = tk.Tk()
        winout.title("錯了拉")
        winout.geometry('400x400')
        winout.resizable(False,False)
        winout.iconbitmap("rose-shape.ico")
        #背景顏色
        winout.config(background= "#D55FD1")
        #透明度
        winout.attributes("-alpha" , 0.9)
        winout.attributes("-topmost" , 0 )
        btde = tk.Button(winout  , text = " 關掉重來 " , font=("Arial", 30))
        btde.config(command= close )
        btde.pack()


        #lb.config(text= tx)


        

lb = tk.Label(bg = "#D55FD1",fg = "white" , text = " enter " , font=("Arial", 25))

lb.pack()
en = tk.Entry()
en.pack(side=tk.TOP)
bt = tk.Button(text = " ok ")
bt.config(width= 4 , height= 1)
bt.config(command= get )
bt.pack(side=tk.TOP)








win.mainloop() #讓主視窗不關閉