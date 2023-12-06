import flet as ft
from functions.bancoLogin import BancoDados

class Cadastro:
    
       
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

    def criacao_conta():
        email = Cadastro.emailTF.value
        nome = Cadastro.nomeTF.value
        senha1 = Cadastro.senha1TF.value
        senha2 = Cadastro.senha2TF.value
        if senha1 == senha2:
            autenticado = BancoDados.cadastrar(email, nome, senha1)
        if autenticado:
            return True
        else:
            return False
   
       


    

    