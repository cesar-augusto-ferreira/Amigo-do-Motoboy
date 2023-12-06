import flet as ft

class Inicio:

    fonts= {
        "fontAclonica": "fonts/Aclonica-Regular.ttf"
    }

    def appBarAppInicio(page, ft= ft, label= str):

        appA = ft.AppBar(
            leading_width= 40,
            title= ft.Text(
                label, 
                size= 20,
                font_family= "fontAclonica",
            ),
            center_title= True,
        )
        return appA
 

    texto1 = ft.Text("Bem vindo", size= 25)

    texto2 = ft.Text(" Amigo do Motoboy é um aplicativo que te ajuda a contabilizar as suas"
        " movimentações financeiras diárias, assim você terá mais controle dos seus ganhos e gastos.\n\n")

    botao_cadastrar = ft.ElevatedButton(
        width= 130,
        height= 140,
        style= ft.ButtonStyle(
            shape= ft.RoundedRectangleBorder(radius= 0)      
        ),
        content= ft.Container(
            content= ft.Column(
                alignment= ft.MainAxisAlignment.CENTER,
                controls= [
                    ft.Icon("list", size= 70),
                    ft.Text("Cadastrar", size= 18),
                ],
            ),
        ),
        on_click= texto1
    )    

    botao_recuperar = ft.ElevatedButton(
        width= 130,
        height= 140,
        style= ft.ButtonStyle(
            shape= ft.RoundedRectangleBorder(radius= 0)      
        ),
        content= ft.Container(
            content= ft.Column(
                alignment= ft.MainAxisAlignment.CENTER,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                controls= [
                    ft.Icon("lock", size= 50),
                    ft.Text("Recuperar \n senha", size= 17),
                ],
            ),
        ),
        on_click= texto1
    )  
    botao_entrar = ft.ElevatedButton(
        width= 130,
        height= 140,
        style= ft.ButtonStyle(
            shape= ft.RoundedRectangleBorder(radius= 0)      
        ),
        content= ft.Container(
            content= ft.Column(
                alignment= ft.MainAxisAlignment.CENTER,
                controls= [
                    ft.Icon("login_sharp", size= 60),
                    ft.Text("Entrar", size= 18),
                ],
            ),
        ),
        on_click= texto1
    ) 

