from tkinter import Tk
from tkinter import Button

class Button_cus(Button):
   def __init__(self, parent, **kwargs):
      kwargs['font'] = ('Times New Roman', 14)
      kwargs['foreground'] = 'black'
      kwargs['background'] = 'white'
      super().__init__(parent, **kwargs)
   pass

def render_lobby_ui():
   lobbyui = Lobby_ui()
   lobbyui_fr = lobbyui.build(1024, 576 , 150, 75)
   lobbyui.renderFrame(lobbyui_fr)
   lobbyui.mainloop(lobbyui_fr)
   return

class Lobby_ui():
   def __init__(self):
      self.title = 'Đại sảnh'
   
   def build(self, width, height, xaxis, yaxis):
      lobby_frame = Tk()
      lobby_frame.title(self.title)
      lobby_frame.configure(bg='white')
      temp = str(width) + 'x' + str(height) + '+' + str(xaxis) + '+' +  str(yaxis)
      lobby_frame.geometry(temp)
      return lobby_frame
   
   def renderFrame(self, lobby_frame):
      # background photoimage here
      
      global button_store
      button_store = Button_cus(lobby_frame, text = "Store information management")
      button_store.place(x=100, y=100)
      
      global button_staff
      button_staff = Button_cus(lobby_frame, text = "Staff information management")
      button_staff.place(x=100, y=150)
      
      global button_drink
      button_drink = Button_cus(lobby_frame, text = "Drink information management")
      button_drink.place(x=100, y=200)
      
      global button_table
      button_table = Button_cus(lobby_frame, text = "Table information management")
      button_table.place(x=100, y=250)
      
      global button_request_form
      button_request_form = Button_cus(lobby_frame, text = "Request for drink")
      button_request_form.place(x=100, y=300)
      
      global button_bill
      button_bill = Button_cus(lobby_frame, text = "Bill printing management")
      button_bill.place(x=100, y=350)
      
      global label_copyright
      
      
      return
   
   def mainloop(self, lobby_frame):
      lobby_frame.mainloop()