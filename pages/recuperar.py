import flet as ft
from functions.bancoLogin import BancoDados

class Recuperar:

    nome = ft.TextField(
        label="Nome",
        hint_text= "Digite seu nome",
        text_style= ft.TextStyle(
            color= ft.colors.BLUE,
        )
    )

    email = ft.TextField(
        label="E-mail",
        hint_text= "Digite seu e-mail",
        text_style= ft.TextStyle(
            color= ft.colors.BLUE,
        )
    )    

    def verificar_email():
        email = Recuperar.email.value
        nome = Recuperar.nome.value

        verCadastro = BancoDados.recuperar(nome, email)

        if verCadastro is not None:
           
            return True
        else:
            return False
        

   
        
        

