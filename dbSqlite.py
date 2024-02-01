from datetime import datetime
import sqlite3

db_name="tracker_gps.db"
tb_marker_log="registros_log"   
tb_vehicle_log="vehicles_log"

def create_database():
    conn = sqlite3.connect(db_name)
    conn.close()

def exists_database():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+tb_marker_log+"'")
    table_exists = cursor.fetchone() is not None
    conn.close()
    return table_exists

def create_table():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE "+tb_marker_log+"  (id_marker INTEGER PRIMARY KEY AUTOINCREMENT,marker_info TEXT,date_register DATE,read INTEGER DEFAULT 0)")
    cursor.execute("CREATE TABLE "+tb_vehicle_log+" (unique_id_vehicle TEXT,vehicle_info TEXT,date_marker DATE)")
    conn.commit()
    conn.close()

def save_marker(texto, fecha):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO "+tb_marker_log+" (marker_info, date_register) VALUES (?, ?)", (texto, fecha))
    conn.commit()
    conn.close()
async def save_marker_async(texto, fecha):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO "+tb_marker_log+" (marker_info, date_register) VALUES (?, ?)", (texto, fecha))
    conn.commit()
    conn.close()



def get_markers_no_read():
    fecha=datetime.now()
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM "+tb_marker_log+" WHERE read=0")
    markers = cursor.fetchall()
    conn.close()
    return markers

def update_marker_read(id_marker):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("UPDATE "+tb_marker_log+" SET read=1 WHERE id_marker="+str(id_marker))
    conn.commit()
    conn.close()
    
    
def update_marker_read_not_all():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("UPDATE "+tb_marker_log+" SET read=0")
    conn.commit()
    conn.close()
    
    



def registro_db():
    if(exists_database()==False):
        create_database()
        create_table()



def insert_tb_vehicle_log(unique_id_vehicle:str,vehicle_info:str,date_marker:str):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO "+tb_vehicle_log+" (unique_id_vehicle,vehicle_info,date_marker) VALUES (?,?,?)",(unique_id_vehicle,vehicle_info,date_marker))
    conn.commit()
    conn.close()
    
    
def get_tb_vehicle_log_range_date(date1:str,date2:str):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM "+tb_vehicle_log+" WHERE date_marker BETWEEN '"+date1+"' AND '"+date2+"'")
    markers = cursor.fetchall()
    conn.close()
    return markers  


