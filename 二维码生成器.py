from tkinter import *
import qrcode
from tkinter import messagebox
#导入库，没有请安装或使用exe版



class Application(Frame):                      #面向对象编写图形化界面
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
    def createWidget(self):
        self.label01 = Label(self,text = "你想要创建的内容：")
        self.label01.pack()
        v1 = StringVar()                                            #创建输入的文本框
        self.entry01 = Entry(self,textvariable=v1)
        self.entry01.pack()
        v1.set("")

        self.label02 = Label(self, text="文件名:")
        self.label02.pack()
        v1 = StringVar()
        self.entry02 = Entry(self, textvariable=v1)
        self.entry02.pack()
        v1.set("")

        self.btn01 = Button(self,text = "生成",command=self.login).pack()             #创建生成按钮


    def login(self):
        img = qrcode.make(self.entry01.get())
        img.save(self.entry02.get()+".png")                                 #当按下按钮后生成二维码并保存
        print("生成内容："+self.entry01.get())
        print("文件名:"+self.entry02.get())
        messagebox.showinfo("二维码生成器","生成可能会出现延迟，请稍等")


root = Tk()
root.geometry("400x200+200+300")                                               #创建文本框并运行Application
root.title("二维码生成器")
app = Application(master = root)


root.mainloop()

