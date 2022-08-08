DB_NAME = 'coffee-store-py'

from view.login import render_login_ui
from view.lobby import render_lobby_ui
from view.table_manage import render_table_manage_ui
from model.store_inf import fetch_from_store_inf

def fetch_from_db():
   temp = []
   table_name = ['store', 'staff', 'seat', 'drink', 'request_form', 'bill', 'detail_bill']
   for item in table_name:
      data = fetch_from_store_inf(DB_NAME, item)
      temp.append(data)
   return temp

render_table_manage_ui()


