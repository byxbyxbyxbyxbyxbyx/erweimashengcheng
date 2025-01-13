from tkinter import *
import qrcode
from tkinter import messagebox
import os


print(''' 
            qqqq     r      r           cccc         ooooo                d    eeeeeee
           q    q     r    r          c             o       o              d   e       e   
           q    q     r rr          c             o           o            d   e eeeeeeee 
             q qq     r             c             o           o        d d d   e      
                q     r               c             o        o      d      d    ee                
                q     r                 ccccc         ooooo           d  d d      eeeeeee        
          
         ''')
class Application(Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
    def createWidget(self):
        self.label01 = Label(self,text = "你想要创建的内容：")
        self.label01.pack()
        v1 = StringVar()
        self.entry01 = Entry(self,textvariable=v1)
        self.entry01.pack()
        v1.set("")

        self.label02 = Label(self, text="文件名:")
        self.label02.pack()
        v1 = StringVar()
        self.entry02 = Entry(self, textvariable=v1)
        self.entry02.pack()
        v1.set("")

        self.btn01 = Button(self,text = "生成",command=self.login).pack()


    def login(self):
        img = qrcode.make(self.entry01.get())
        img.save(self.entry02.get()+".png")
        print("生成内容："+self.entry01.get())
        print("文件名:"+self.entry02.get())
        messagebox.showinfo("二维码生成器","生成可能会出现延迟，请稍等")


root = Tk()
root.geometry("400x200+200+300")
root.title("二维码生成器")
app = Application(master = root)


root.mainloop()

