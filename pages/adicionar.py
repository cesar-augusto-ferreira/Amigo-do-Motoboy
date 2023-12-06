import flet as ft
from functions.bancoGanhos import BancoGanhos


class Adicionar():

    texto1 = ft.Text("Digite o email", size= 18)
    valor1 = ft.TextField(
        label="digite o e-mail",
        text_style= ft.TextStyle(
            color= ft.colors.BLUE,
        )
    )

    texto2 = ft.Text("Adicionar ganhos", size= 18)
    valor2 = ft.TextField(
        label="Adicionar o valor",
        text_style= ft.TextStyle(
            color= ft.colors.BLUE,
        )
    )

    texto3 = ft.Text("Data", size= 18)
    valor3 = ft.TextField(
        label="Data",
        text_style= ft.TextStyle(
            color= ft.colors.BLUE,
        )
    )


    def addGanhos():
        email = Adicionar.valor1
        valor = Adicionar.valor2
        data = float(Adicionar.valor)
        
        add = BancoGanhos.add_ganhos(email, data, valor)
        if add is not None:
            return True
        else:
            return False


