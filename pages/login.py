import flet as ft
from functions.bancoLogin import BancoDados

class Login:

    emailTF= ft.TextField(
        label= "E-mail",
        hint_text= "Digite seu e-mail",
        text_style= ft.TextStyle(
            color= ft.colors.BLUE,
        )
    )
    senhaTF= ft.TextField(
        label= "Senha",
        hint_text= "Digite sua senha",
        password= True,
        can_reveal_password=True,
        text_style= ft.TextStyle(
            color= ft.colors.BLUE,
        )  
    ) 
    def autenticacao(): 
        email = Login.emailTF.value
        senha = Login.senhaTF.value
        autenticado = BancoDados.autenticar(email, senha)

        if autenticado:
            return True
        else:
            return False

    