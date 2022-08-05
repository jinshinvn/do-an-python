from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Toplevel
from tkinter import PhotoImage
from tkinter import Entry
from tkinter import PanedWindow
from PIL import Image, ImageTk

class View_control_panel:
   @staticmethod
   def render_sign_up_ui():
      return
   pass

def render_login_ui():
   loginui = Login_ui()
   loginui_fr = loginui.build(1024, 576 , 150, 75)
   loginui.renderFrame(loginui_fr)
   return

email_pass_entry_width = 30
# email_pass_entry_height = 35

# https://stackoverflow.com/questions/60321170/correctly-extend-a-tkinter-widget-using-inheritance
class Label_log(Label):
   def __init__(self, parent, **kwargs):
      kwargs['font'] = ('Times New Roman', 14)
      kwargs['foreground'] = 'black'
      kwargs['background'] = 'white'
      super().__init__(parent, **kwargs)
      
class Label_img(Label):
   def __init__(self, parent, **kwargs):
      kwargs['background'] = 'white'
      super().__init__(parent, **kwargs)      
      
class Label_log_title(Label):
   def __init__(self, parent, **kwargs):
      kwargs['font'] = ('Times New Roman', 24)
      kwargs['foreground'] = 'blue3'
      kwargs['background'] = 'white'
      super().__init__(parent, **kwargs)

class Entry_log(Entry):
   def __init__(self, parent, **kwargs):
      kwargs['font'] = ('Times New Roman', 14)
      kwargs['borderwidth'] = 2
      kwargs['width'] = email_pass_entry_width
      super().__init__(parent, **kwargs)
      
class Entry_pass(Entry):
   def __init__(self, parent, **kwargs):
      kwargs['font'] = ('Times New Roman', 14)
      kwargs['borderwidth'] = 2
      kwargs['show'] = '*'
      kwargs['width'] = email_pass_entry_width
      super().__init__(parent, **kwargs)

class Login_ui():
   def __init__(self):
      self.title = 'Đăng nhập'
      self.logui_icon_dir = 'login.ico'
      self.img_mid_left_dir = './img/undraw1.png'
      self.raw_dn_bg_img_dir = './img/dn.png'
      self.img_log_but_dir = './img/login.png'
      return
   
   def build(self, width, height, xaxis, yaxis):
      login_frame = Tk()
      login_frame.title(self.title)
      login_frame.iconbitmap(self.logui_icon_dir)
      login_frame.configure(bg='white')
      temp = str(width) + 'x' + str(height) + '+' + str(xaxis) + '+' +  str(yaxis)
      login_frame.geometry(temp)
      return login_frame
   
   def renderFrame(self, login_frame):
      def renderLeft(login_frame):
         global img_mid_left
         img_mid_left = PhotoImage(file = self.img_mid_left_dir)
         lbl_img_mid_left = Label_img(login_frame, image = img_mid_left)
         lbl_img_mid_left.place(x=100, y=100)
         return
      renderLeft(login_frame)
      def renderBgRight(login_frame):
         global raw_dn_bg_img
         global dn_fr_img
         raw_dn_bg_img = Image.open(self.raw_dn_bg_img_dir)
         raw_dn_bg_img = raw_dn_bg_img.resize((int(544/1.4), int(629/1.4)), Image.Resampling.LANCZOS)
         dn_fr_img = ImageTk.PhotoImage(raw_dn_bg_img)
         lbl_dn_bg_img = Label_img(login_frame, image = dn_fr_img)
         lbl_dn_bg_img.place(x = 560, y = 40)
         return 
      renderBgRight(login_frame)
      
      def renderLbls(login_frame):
         global lbl_title
         lbl_title = Label_log_title(login_frame, text = "ĐĂNG NHẬP")
         lbl_title.place(x=675, y=90)

         global lbl_log
         lbl_log = Label_log(login_frame, text = "Email: ")
         lbl_log.place(x=625, y=150)
         
         global entry_log
         entry_log = Entry_log(login_frame)
         entry_log.place(x=625, y=200)
         
         global lbl_pass
         lbl_pass = Label_log(login_frame, text = "Mật khẩu: ")
         lbl_pass.place(x=625, y=250)
         
         global entry_pass
         entry_pass = Entry_pass(login_frame)
         entry_pass.place(x=625, y=300)

         global img_log_but
         img_log_but = PhotoImage(file = self.img_log_but_dir)
         lbl_log_but = Label_img(login_frame, image = img_log_but)
         
         # lbl_log_but.bind('<Button-1>', getUsernameAndLogin)
         # bindedBut = Button(login_frame, image=img_log_but, command=getUsernameAndLogin)
         # bindedBut = Button(login_frame, image=img_log_but, command=getUsernameAndLogin)
         
         lbl_log_but.place(x=665, y=370)
         
      renderLbls(login_frame)
      
      # config global to distract garbage collector, don't remove
      # Source: https://stackoverflow.com/questions/40658728/clickable-images-for-python
      
      global img_wrong_log
      global lbl_img_notify
      img_wrong_log = PhotoImage(file = './img/vnwronglogin.png')
      lbl_img_notify = Label_img(login_frame, image = img_wrong_log)

      login_frame.mainloop()

