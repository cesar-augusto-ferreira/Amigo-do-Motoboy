import pyodbc


class BancoDados:

    def autenticar(email, senha):
        
        # Conecta ao banco de dados.
        conn = pyodbc.connect("Driver={SQL Server};Server=NoteCésar;Database=AppGanhos;")
        cursor = conn.cursor()

        # Realiza a consulta no banco de dados.
        cursor.execute("SELECT * FROM pessoa WHERE email=? AND senha=?", (email, senha))

        # Obtém o resultado da consulta.
        resultado = cursor.fetchone()

        # Fecha a conexão com o banco de dados.
        conn.close()

        # Verifica se o resultado da consulta é válido.
        if resultado is not None:
            return True
        else:
            return False
        

    def cadastrar(email, nome, senha):

        conn = pyodbc.connect("Driver={SQL Server};Server=NoteCésar;Database=AppGanhos;")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pessoa WHERE email=? ", (email))

        resultado = cursor.fetchone()

        if resultado is None:
            create = f"""INSERT INTO pessoa VALUES ('{email}', '{nome}', '{senha}')"""
            cursor.execute(create)
                
            cursor.commit()
            conn.close()
            return True
        else:
            conn.close()
            return False
        

    def recuperar(nome, email):

        conn = pyodbc.connect("Driver={SQL Server};Server=NoteCésar;Database=AppGanhos;")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pessoa WHERE email=? and nome=? ", (email, nome))

        resultado = cursor.fetchone()
        conn.close()

        if resultado is not None:
            return True
        else:
            return False
        


    def atualizarBD(email, nome, senha):

        conn = pyodbc.connect("Driver={SQL Server};Server=NoteCésar;Database=AppGanhos;")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pessoa WHERE email=? ", (email))

        resultado = cursor.fetchone()

        if resultado is not None:
            cursor.execute("UPDATE pessoa SET nome=?, senha=? WHERE email=? ", (nome, senha, email))
                
            cursor.commit()
            conn.close()
            return True
        else:
            conn.close()
            return False    
        


    def deletarC(email):

        conn = pyodbc.connect("Driver={SQL Server};Server=NoteCésar;Database=AppGanhos;")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pessoa WHERE email=? ", (email))

        resultado = cursor.fetchone()

        if resultado is not None:
            cursor.execute("DELETE FROM pessoa WHERE email=? ", (email))

            cursor.commit()
            conn.close()
            return True
        else:
            conn.close()
            return False    




            
       

       

        

        