DB_NAME = 'coffee-store-py'
TABLE = 'store'

from view.login import render_login_ui
from view.lobby import render_lobby_ui
from model.store_inf import fetch_from_store_inf

# fetch_from_store_inf(DB_NAME, TABLE)
