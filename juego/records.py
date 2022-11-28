
import sqlite3 as sql


def createDB():
    conn = sql.connect("records.db")
    conn.commit()
    conn.close()


def createTable():
    conn = sql.connect("records.db")
    cursor = conn.cursor()
    cursor.execute(
        """ CREATE TABLE records (
            name text,
            score integer

            
       )"""
   )
    conn.commit()
    conn.close()


def insertRow(nombre, score):
    conn = sql.connect("records.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO records VALUES ('{nombre}', {score} )"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def readRows(score):
    conn = sql.connect("records.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM nombre ORDER BY ¨{score} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    print(datos)
    conn.close()
    print(datos)
    return(str(datos[0][0])) +' '+ (str(datos[0][1]))

def readRows2(field):
    conn = sql.connect("records.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM nombre ORDER BY ¨{field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    print(datos)
    conn.close()
    print(datos)
    return(str(datos[1][0])) +' '+ (str(datos[1][1]))


def readRows3(field):
    conn = sql.connect("records.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM nombre ORDER BY ¨{field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    print(datos)
    conn.close()
    print(datos)
    return(str(datos[2][0])) +' '+ (str(datos[2][1]))


def readRows4(field):
    conn = sql.connect("records.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM nombre ORDER BY ¨{field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    print(datos)
    conn.close()
    print(datos)
    return(str(datos[3][0])) +' '+ (str(datos[3][1]))

def readRows5(field):
    conn = sql.connect("records.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM nombre ORDER BY ¨{field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    print(datos)
    conn.close()
    print(datos)
    return(str(datos[4][0])) +' '+ (str(datos[4][1]))


def insertRow2(recordsList):
    conn = sql.connect("records.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO records VALUES (?, ?)"
    cursor.execute(instruccion, recordsList)
    conn.commit()
    conn.close()


def readOrdered(field):
    conn = sql.connect("records.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM records ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)


def deleteRow():
    conn = sql.connect("records.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM records WHERE name BETWEEN 5 AND 20"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()

def updateFields():
    conn = sql.connect("records.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE * FROM jugadores DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()

#if __name__ == "__main__":
    #createDB()
    #createTable()
    #--
    #insertRow("nombre", str("score"))
    #readOrdered()
    #deleteRow()

