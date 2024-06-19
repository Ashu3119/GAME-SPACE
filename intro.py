from tkinter import *
import subprocess
class Work:
    def __init__(self, win):
        self.id= Label(win, text='Username', font='Helvetica 20',anchor='center',borderwidth=5, relief="groove")
        self.id.place(x=245, y=350, width=150, height=75)
        self.pw = Label(win, text='Password', font='Helvetica 20',anchor='center',borderwidth=5, relief="groove")
        self.pw.place(x=245, y=435, width=150, height=75)
        self.i1=Entry(win,font='Helvetica 20')
        self.i1.place(x=400, y=350, width=200, height=75)
        self.i2=Entry(win)
        self.i2.place(x=400, y=435, width=200, height=75)
        self.b2 = Button(win, text='Submit', activebackground="black", activeforeground="white",font='Helvetica 20',bd='5')
        self.b2.place(x=325, y=550, width=150, height=60)
    def signup(self,username):

window=Tk()
frame = Frame(window, width=720, height=720, )
frame.pack()
frame.place(anchor='center',relx=0.5, rely=0.5)
mywin=Work(window)
window.title('Game Space!')
window.geometry("800x800+200+200")
window.mainloop()