import sqlite3
def __init__db(cursor):
    sql="""CREATE TABLE IF NOT EXISTS standard(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        external_id INTEGER,
        athlete_id,
        name TEXT,
        distance FLOAT,
        date TEXT)"""
    cursor.execute(sql)
class Connection:
    def __init__(self,connection) -> None:
        self.connection=connection
        self.cursor=connection.cursor()
    def add_activity(self,id:int,athlete_id:int,name:str,distance:float,date:str):
        if self.check_if_exists(id)==None:
            sql="""INSERT INTO standard(external_id,athlete_id,name,distance,date) VALUES(?,?,?,?,?)"""
            self.cursor.execute(sql,(id,athlete_id,name,distance,date))
    def check_if_exists(self,external_id:int):
        self.cursor.execute("SELECT id FROM standard WHERE external_id=?",(external_id,))
        return self.cursor.fetchone()
        
if __name__=='__main__':
    with sqlite3.connect("database.db")as connection:
        cursor=connection.cursor()
        connect=Connection(connection)
        connect.check_if_exists(111)
        
