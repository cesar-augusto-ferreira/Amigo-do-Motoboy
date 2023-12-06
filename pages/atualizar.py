import flet as ft
from functions.bancoLogin import BancoDados

class Atualizar:
        
    nomeTF = ft.TextField(
        label="Nome",
        hint_text= "Digite seu nome",
        text_style= ft.TextStyle(
            color= ft.colors.BLUE,
        )
    )

    emailTF = ft.TextField(
        label="E-mail",
        hint_text= "Digite seu e-mail",
        keyboard_type= "EMAIL",
        text_style= ft.TextStyle(
            color= ft.colors.BLUE,
        )
    )

    senha1TF = ft.TextField(
        label="senha",
        hint_text= "Digite sua senha",
        password= True,
        can_reveal_password=True,
        text_style= ft.TextStyle(
            color= ft.colors.BLUE,
        )
    )

    senha2TF = ft.TextField(
        label="senha",
        hint_text= "Repita a sua senha",
        password= True,
        can_reveal_password=True,
        text_style= ft.TextStyle(
            color= ft.colors.BLUE,
        )
    )

    def atualizarC():
        email = Atualizar.emailTF.value
        nome = Atualizar.nomeTF.value
        senha1 = Atualizar.senha1TF.value
        senha2 = Atualizar.senha2TF.value
        if senha1 == senha2:
            autenticado = BancoDados.atualizarBD(email, nome, senha1)
        if autenticado:
            return True
        else:
            return False
   
       


    

    