import flet as ft
from functions.bancoLogin import BancoDados


class Deletar:

    emailTF= ft.TextField(
        label= "E-mail",
        hint_text= "Digite seu e-mail",
        text_style= ft.TextStyle(
            color= ft.colors.BLUE,
        )
    )

    def excluir(): 
        email = Deletar.emailTF.value
        autenticado = BancoDados.deletarC(email)

        if autenticado:
            return True
        else:
            return False

    