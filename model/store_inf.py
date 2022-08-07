import pymysql

def fetch_from_store_inf(dbname, table):
   conn = pymysql.connect(
      host = 'localhost', 
      user = 'doanpython',
      database = dbname
   )
   curr = conn.cursor()
   curr.execute('select * from {}'.format(table))
   data = curr.fetchall()
   data_json = []
   rows_header = [x[0] for x in curr.description]
   for item in data:
      data_json.append(dict(zip(rows_header, item)))
   # https://stackoverflow.com/questions/43796423/python-converting-mysql-query-result-to-json
   conn.close()
   return data_json


