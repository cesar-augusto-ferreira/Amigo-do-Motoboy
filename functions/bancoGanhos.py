import pyodbc


class BancoGanhos ():

    def add_ganhos(email, data, valor):

        conn = pyodbc.connect("Driver={SQL Server};Server=NoteCésar;Database=AppGanhos;")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pessoa WHERE email=? ", (email))

        resultado = cursor.fetchone()

        if resultado is not None:
            create = f"""INSERT INTO ganhos VALUES ('{email}', '{data}', {valor})"""
            cursor.execute(create)
                
            cursor.commit()
            conn.close()
            return True
        else:
            conn.close()
            return False
        
