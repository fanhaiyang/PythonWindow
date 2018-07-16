from tkinter import *  # __all__=[a,b]
from tkinter import messagebox
import random

# function 注册

# 关闭窗口
def colseWindow():
    messagebox.showinfo(title="警告",message="不许关闭，好好回答")
    return

def closeAll():
    # destory 销毁窗口（父+子窗口）
    window.destroy()

def colseYes():
    #messagebox.showinfo(title="警告",message="好好考虑，好好回答")
    return

def colseNo():
    rand=random.randrange(0,100,5)
    NoHappy(rand)

# 开心
def Yes():
    yes=Toplevel(window)
    yes.title("高兴")
    yes.geometry("250x100+700+300")
    yesLabel=Label(yes,text="高兴就好！我也高兴",font=('微软雅黑',20))

    # 布局定位方式2：包定位 pack
    yesLabel.pack()
    btn1=Button(yes,text="确定",width=10,height=2,command=closeAll)
    btn1.pack()
    yes.protocol("WM_DELETE_WINDOW",colseYes)

# 不开心
def NoHappy(num=0):
    nohappy=Toplevel(window)
    nohappy.title("不开心")
    size="250x100"
    position=size+'+'+str(700+num)+'+300'   #"250x100+700+300"
    print(position)
    nohappy.geometry(position)
    nohappyLabel=Label(nohappy,text="再考虑考虑",font=('微软雅黑',20))
    # 布局定位方式2：包定位 pack
    nohappyLabel.pack()
    btn1=Button(nohappy,text="开心",width=10,height=2,command=nohappy.destroy)
    btn1.pack()
    nohappy.protocol("WM_DELETE_WINDOW",colseNo)


################################

# 注册窗体
window=Tk()

window.title("Hello Baby")
# 窗体定位
window.geometry("510x650+600+200") # width:510  height:680  居左定位：600  居上定位：400
# 窗口位置
#window.geometry("+600+400")

# 点击关闭窗口事件
window.protocol("WM_DELETE_WINDOW",colseWindow)

# 标签控件
label1=Label(window,text="Hello Baby",font=('微软雅黑',15),fg='red')
# 布局 grid 网格布局 
# sticky 对其方式：N S W E 上下左右
# 第一行，第一列
label1.grid(row=0,column=0,sticky=W)

label2=Label(window,text="Are you Happy?",font=('微软雅黑',30))
label2.grid(row=1,column=1,sticky=E)

# 显示图片
photo=PhotoImage(file="./Images/hh.gif")
imageLable=Label(window,image=photo)
# columnspan 列合并
imageLable.grid(row=2,columnspan=2)

# 按钮
btn1=Button(window,text="开心",width=6,height=2,command=Yes)
btn1.grid(row=3,column=0,sticky=W)
btn2=Button(window,text="不开心",command=NoHappy)
btn2.grid(row=3,column=1,sticky=E)

# 窗体展示
window.mainloop()