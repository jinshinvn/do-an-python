from tkinter import Tk
from tkinter import Button

def render_table_manage_ui():
   table_manage_ui = Table_manage_ui()
   table_manage_ui_fr = table_manage_ui.build(1024, 576, 150, 75)
   table_manage_ui.renderFrame(table_manage_ui_fr)
   table_manage_ui.mainloop(table_manage_ui_fr)
   return

class Button_cs(Button):
   def __init__(self, parent, **kwargs):
      kwargs['font'] = ('Times New Roman', 14)
      kwargs['borderwidth'] = 1
      kwargs['width'] = 20
      super().__init__(parent, **kwargs)



class Table_manage_ui:
   
   def __init__(self):
      self.title = "Quản lý bàn"
      return
   
   def build(self, width, height, xaxis, yaxis):
      table_manage_frame = Tk()
      table_manage_frame.title(self.title)
      table_manage_frame.configure(bg='white')
      temp = str(width) + 'x' + str(height) + '+' + str(xaxis) + '+' +  str(yaxis)
      table_manage_frame.geometry(temp)
      return table_manage_frame
      
   def renderFrame(self, table_manage_frame):
      def renderLeft(table_manage_frame):
         global add_but
         add_but = Button_cs(table_manage_frame, text= "Add")
         add_but.place(x=50, y= 50)
         global edit_but
         edit_but = Button_cs(table_manage_frame, text= "Edit")
         edit_but.place(x=50, y=100)
         global delete_but
         delete_but = Button_cs(table_manage_frame, text= "Delete")
         delete_but.place(x=50, y=150)
         return
      renderLeft(table_manage_frame)
   def mainloop(self, table_manage_frame):
      table_manage_frame.mainloop()