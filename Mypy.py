
from tkinter import *
from tkinter.ttk import *
root = Tk()
root.wm_title("this is first form")
root.geometry('300x200+150+200')
btt=Button(root,text='some thing')
btt.pack()
w1 = Label(root, text='fssg')
w1.pack()
t=Text(root,width=50,height=20)
t.pack()
if __name__ == "__main__":
    root.mainloop()
