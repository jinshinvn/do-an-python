from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
import time
import threading
import json
import hashlib

def getUsernameAndLogin(event=None):
    username = entryLogin.get() 
    password = entryPassword.get()
    passwordHashed = hashlib.sha256(password.encode()).hexdigest()
    with open('userData.json', encoding='utf8') as userDataJsonFile:
        tempDict = json.load(userDataJsonFile)
    if (tempDict.get(username)==passwordHashed):
        messagebox.showwarning(title=None, message = 'Login thành công.')
    else:
        labelImgNotify.place(x=725, y=2.5)
        th_popUpWrongCredentialsLogin()
    return

def popUpWrongCredentialsLogin():
    time.sleep(2)
    labelImgNotify.place_forget()
    return

def th_popUpWrongCredentialsLogin():
    thread = threading.Thread(target=popUpWrongCredentialsLogin)
    thread.start()
    return

class loginUI():
    def __init__(self, width, height, xaxis, yaxis):
        global loginFrame
        loginFrame = Tk()
        loginFrame.title('Đăng nhập cùng chúng tôi')
        loginFrame.iconbitmap('login.ico')
        loginFrame.configure(bg='white')
        self.width = width
        self.height = height
        self.xaxis = xaxis
        self.yaxis = yaxis

    def renderFrame(self):
        temp = str(self.width) + 'x' + str(self.height) + '+' + str(self.xaxis) + '+' +  str(self.yaxis)
        loginFrame.geometry(temp)

        imgIllus = PhotoImage(file = './img/undraw1.png')
        labelIllus = Label(loginFrame, image = imgIllus, bg='white')
        labelIllus.place(x=100, y=100)

        labelTitle = Label(
            loginFrame, 
            text = "ĐĂNG NHẬP", 
            font= ('Times New Roman', 24), 
            foreground= "blue3",
            bg='white'
        )
        labelTitle.place(x=675, y=90)

        emailPassEntryWidth = 30
        emailPassEntryHeight = 35

        labelLogin = Label(
            loginFrame, 
            text = "Email: ", 
            font= ('Times New Roman', 14), 
            foreground= "black",
            bg = 'white'
        )
        labelLogin.place(x=625, y=150)
        
        global entryLogin
        entryLogin = Entry(
            loginFrame, 
            borderwidth=2,
            font= ('Times New Roman', 14), 
            width=emailPassEntryWidth,

        )
        entryLogin.place(x=625, y=200, height=emailPassEntryHeight)
            
        labelPassword = Label(
            loginFrame, 
            text = "Mật khẩu: ", 
            font= ('Times New Roman', 14),
            foreground= "black",
            bg = 'white',
        )
        labelPassword.place(x=625, y=250)
        
        global entryPassword
        entryPassword = Entry(
            loginFrame, 
            show = '*', 
            borderwidth=2,
            font= ('Times New Roman', 14), 
            width=emailPassEntryWidth
        )
        entryPassword.place(x=625, y=300, height=emailPassEntryHeight)

        rememberMe = Checkbutton(
            loginFrame, 
            text='Lưu phiên đăng nhập',
            bg='white'
        )
        rememberMe.place(x=690, y=430)
        
        imgLoginBut = PhotoImage(file = './img/login.png')
        labelLoginBut = Label(loginFrame, image = imgLoginBut, bg='white')
        labelLoginBut.bind('<Button-1>', getUsernameAndLogin)
        bindedBut = Button(loginFrame, image=imgLoginBut, command=getUsernameAndLogin)
        labelLoginBut.place(x=665, y=370)

        # i don't know why it ran perfectly
        # Source: https://stackoverflow.com/questions/40658728/clickable-images-for-python
        
        global img
        global labelImgNotify
        img = PhotoImage(file = './img/vnwronglogin.png')
        labelImgNotify = Label(loginFrame, image = img, bg='white')

        loginFrame.mainloop()

myLoginUI = loginUI(1024, 576 , 150, 75)
myLoginUI.renderFrame()