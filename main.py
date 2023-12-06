
import flet as ft
from pages.adicionar import Adicionar
from pages.cadastro import Cadastro
from pages.deletar import Deletar
from pages.home import Home
from pages.sobre import Sobre
from pages.inicio import Inicio
from pages.login import Login
from pages.recuperar import Recuperar
from pages.tempo import Tempo
from pages.atualizar import Atualizar


def main(page: ft.Page):

    def tema(e):
 
        if page.theme_mode == "dark":
            page.theme_mode = "light"
            page.update()
        else:
            page.theme_mode = "dark"
            page.update()  

    page.window_width = 500
    page.window_height = 600
    page.theme_mode = "dark"

    def route_change(route = str):
        page.views.clear()
        page.views.append(
            ft.View(
                "/", 
                controls= [
                    Inicio.appBarAppInicio(page, ft, "Amigo do Motoboy"),
                    ft.Column(
                        spacing = 1,
                        expand= True,
                        controls= [
                            ft.Container(
                                alignment = ft.alignment.center,
                                margin = 2,
                                padding = 50,
                                expand= 2,
                                bgcolor= "Blue",
                                content= ft.Column(   
                                    alignment= ft.alignment.center,                    
                                    controls= [
                                        Inicio.texto1,
                                        Inicio.texto2,
                                    ]
                                ),   
                            ),
                            ft.Container(
                                expand= 1,  
                                content= ft.Row(
                                    controls= [
                                        ft.ElevatedButton(
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
                                            on_click=lambda _: page.go("/cadastro"),
                                        ), 
                                        ft.ElevatedButton(
                                            width= 130,
                                            height= 140,
                                            style= ft.ButtonStyle(
                                                shape= ft.RoundedRectangleBorder(radius= 0)      
                                            ),
                                            content= ft.Container(
                                                content= ft.Column(
                                                    alignment= ft.MainAxisAlignment.CENTER,
                                                    controls= [
                                                        ft.Icon("lock", size= 50),
                                                        ft.Text("Recuperar \n senha", size= 17),
                                                    ],
                                                ),
                                            ),    
                                            on_click=lambda _: page.go("/recuperar"), 
                                        ),       
                                        ft.ElevatedButton(
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
                                            on_click=lambda _: page.go("/login"), 
                                        ),    
                                        
                                    ], 
                                    alignment= ft.MainAxisAlignment.CENTER,                     
                                ), 
                            ),  
                        ],   
                    ), 
                ],   
            ),
        ),
    
        if page.route == "/cadastro":
            page.views.append(  
                ft.View(
                    "/cadastro", 
                    controls= [
                    Inicio.appBarAppInicio(page, ft, "Cadastro"),
                    ft.Column(
                        spacing = 1,
                        expand= True,
                        controls= [
                            ft.Container(
                                alignment = ft.alignment.center,
                                margin = 2,
                                padding = 50,
                                expand= 2,
                                content= ft.Column(
                                    controls= [
                                        Cadastro.nomeTF,
                                        Cadastro.emailTF,
                                        Cadastro.senha1TF,
                                        Cadastro.senha2TF,
                                    ]
                                ),
                            ),
                            ft.Container(
                                expand= 1,  
                                content= ft.Row(
                                    controls= [
                                        ft.ElevatedButton(
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
                                            on_click=lambda _: page.go("/login") if Cadastro.criacao_conta() == True else page.go("/inicio") ,
                                        ),    
                                    ], 
                                    alignment= ft.MainAxisAlignment.CENTER,                     
                                ), 
                            ),  
                        ],   
                    ), 
                ], 
                ),   
            ),
        
        if page.route == "/recuperar":
            page.views.append(  
                ft.View(
                    "/recuperar", 
                    controls= [
                    Inicio.appBarAppInicio(page, ft, "Recuperar a senha"),
                    ft.Column(
                        spacing = 1,
                        expand= True,
                        controls= [
                            ft.Container(
                                alignment = ft.alignment.center,
                                margin = 2,
                                padding = 50,
                                expand= 2,
                                content= ft.Column(
                                    controls= [
                                        Recuperar.nome,
                                        Recuperar.email,                                     
                                    ]
                                ),
                            ),
                            ft.Container(
                                expand= 1,  
                                content= ft.Row(
                                    controls= [
                                        ft.ElevatedButton(
                                            width= 130,
                                            height= 140,
                                            style= ft.ButtonStyle(
                                                shape= ft.RoundedRectangleBorder(radius= 0)      
                                            ),
                                            content= ft.Container(
                                                content= ft.Column(
                                                    alignment= ft.MainAxisAlignment.CENTER,
                                                    controls= [
                                                        ft.Icon("lock", size= 60),
                                                        ft.Text("Recuperar \n senha", size= 17),
                                                    ],
                                                ),
                                            ),    
                                             on_click=lambda _: page.go("/recuperar2") if Recuperar.verificar_email() == True else page.go("/inicio") ,
                                        ),    
                                    ], 
                                    alignment= ft.MainAxisAlignment.CENTER,                     
                                ), 
                            ),  
                        ],   
                    ), 
                ], 
                ),   
            ),
        
        if page.route == "/recuperar2":
            page.views.clear()
            page.views.append(  
                ft.View(
                    "/recuperar2", 
                    controls= [
                    Inicio.appBarAppInicio(page, ft, "Recuperar a senha"),
                    ft.Column(
                        spacing = 1,
                        expand= True,
                        controls= [
                            ft.Container(
                                alignment = ft.alignment.center,
                                margin = 2,
                                padding = 50,
                                expand= 2,
                                content= ft.Column(
                                    controls= [
                                        ft.Text("Sua senha será enviada para seu e-mail", size= 25)                                     
                                    ]
                                ),
                            ),
                            ft.Container(
                                expand= 1,  
                                content= ft.Row(
                                    controls= [
                                        ft.ElevatedButton(
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
                                                        ft.Text("Fazer /nLogin", size= 17),
                                                    ],
                                                ),
                                            ),    
                                            on_click=lambda _: page.go("/login"),
                                        ),    
                                    ], 
                                    alignment= ft.MainAxisAlignment.CENTER,                     
                                ), 
                            ),  
                        ],   
                    ), 
                ], 
                ),   
            ),
        
        if page.route == "/login":
            page.views.append(  
                ft.View(
                    "/login", 
                    controls= [
                    Inicio.appBarAppInicio(page, ft, "Login"),
                    ft.Column(
                        spacing = 1,
                        expand= True,
                        controls= [
                            ft.Container(
                                alignment = ft.alignment.center,
                                margin = 2,
                                padding = 50,
                                expand= 2,
                                content= ft.Column(
                                    controls= [
                                        Login.emailTF,
                                        Login.senhaTF,                                   
                                    ]
                                ),
                            ),
                            ft.Container(
                                expand= 1,  
                                content= ft.Row(
                                    controls= [
                                        ft.ElevatedButton(
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
                                                        ft.Text("Login", size= 18),
                                                    ],
                                                ),
                                            ),    
                                            on_click= lambda _: page.go("/home") if Login.autenticacao() == True else (page.go("/")),
                                        ),    
                                        
                                    ], 
                                    alignment= ft.MainAxisAlignment.CENTER,                     
                                ), 
                            ),  
                        ],   
                    ), 
                ], 
                ),   
            ),
        if page.route == "/home":
            page.views.clear()
            page.views.append(  
                ft.View(
                    "/home", 
                    controls= [
                        ft.AppBar(
                            leading_width= 40,
                            title= ft.Text(
                                "Home", 
                                size= 20,
                                font_family= "fontAclonica"
                            ),
                            center_title= True,
                            actions= [
                                ft.IconButton(ft.icons.PLUS_ONE, on_click= lambda _: page.go('/add')),
                                ft.IconButton(ft.icons.HOME, on_click= lambda _: page.go('/home')),
                                ft.IconButton(ft.icons.AC_UNIT_ROUNDED, on_click= lambda _: page.go('/tempo')),
                                ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click= lambda _: page.go('/config')),
                                ft.PopupMenuButton(
                                    items=[
                                        ft.PopupMenuItem(
                                            content= ft.Row(
                                                controls= [
                                                    ft.Icon(ft.icons.PERSON_2_OUTLINED),
                                                    ft.TextButton(
                                                        text= "Sobre",
                                                        on_click= lambda _: page.go("/sobre"),  
                                                    ),
                                                ]
                                            ),
                                        ),    
                                    ],
                                ),
                            ]
                        ),
                        ft.Container(
                            margin = 50,
                            content= ft.Column(
                                controls= [
                                    Home.texto1,
                                    Home.texto2,
                                    ft.Text("\n"),
                                    Home.texto3,
                                    Home.texto4,
                                    ft.Text("\n"),
                                    Home.texto5,
                                    Home.texto6,
                                    ft.Text("\n"),
                                    Home.texto7,
                                    Home.texto8,  
                                ], 
                            ),                 
                        ), 
                     
                    ],   
                ),      
            )
        
        if page.route == "/tempo":
            page.views.append(  
                ft.View(
                    "/tempo", 
                    controls= [
                        ft.AppBar(
                            leading_width= 40,
                            title= ft.Text(
                                "Tempo", 
                                size= 20,
                                font_family= "fontAclonica",
                            ),
                            center_title= True,
                            actions= [
                                ft.IconButton(ft.icons.PLUS_ONE, on_click= lambda _: page.go('/add')),
                                ft.IconButton(ft.icons.HOME, on_click= lambda _: page.go('/home')),
                                ft.IconButton(ft.icons.AC_UNIT_ROUNDED, on_click= lambda _: page.go('/tempo')),
                                ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click= lambda _: page.go('/config')),
                                ft.PopupMenuButton(
                                    items=[
                                        ft.PopupMenuItem(
                                            content= ft.Row(
                                                controls= [
                                                    ft.Icon(ft.icons.PERSON_2_OUTLINED),
                                                    ft.TextButton(
                                                        text= "Sobre",
                                                        on_click= lambda _: page.go("/sobre"),  
                                                    ),
                                                ]
                                            ),
                                        ),    
                                    ],
                                ),
                            ]
                        ),
                        ft.Container(
                            expand= 1,  
                            content= ft.Column(
                                spacing = 1,
                                expand= True, 
                                alignment= ft.MainAxisAlignment.CENTER,
                                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                controls= [
                                    Tempo.texto1,
                                    Tempo.texto2,
                                    Tempo.texto3,
                                    Tempo.texto4,
                                    Tempo.texto5,
                                    Tempo.texto6,
                                    Tempo.texto7,
                                    Tempo.texto8,
                                    Tempo.texto9,      
                                ],                           
                            ), 
                        ),   
                    ],   
                ),     
            )

        if page.route == "/config":
            page.views.append(  
                ft.View(
                    "/config", 
                    controls= [
                        ft.AppBar(
                            leading_width= 40,
                            title= ft.Text(
                                "Configurações", 
                                size= 20,
                                font_family= "fontAclonica"
                            ),
                            center_title= True,
                            actions= [
                                ft.IconButton(ft.icons.PLUS_ONE, on_click= lambda _: page.go('/add')),
                                ft.IconButton(ft.icons.HOME, on_click= lambda _: page.go('/home')),
                                ft.IconButton(ft.icons.AC_UNIT_ROUNDED, on_click= lambda _: page.go('/tempo')),
                                ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click= lambda _: page.go('/config')),
                                ft.PopupMenuButton(
                                    items=[
                                        ft.PopupMenuItem(
                                            content= ft.Row(
                                                controls= [
                                                    ft.Icon(ft.icons.PERSON_2_OUTLINED),
                                                    ft.TextButton(
                                                        text= "Sobre",
                                                        on_click= lambda _: page.go("/sobre"),  
                                                    ),
                                                ]
                                            ),
                                        ),    
                                    ],
                                ),
                            ]
                        ),
                        ft.Container(
                            padding = 70,
                            content= ft.Column(
                                controls= [
                                    ft.Row(
                                        controls= [
                                            ft.Text(""),
                                            ft.TextButton(
                                                "Light / Dark mode",
                                                icon= ft.icons.WB_SUNNY_OUTLINED,
                                                on_click= tema    
                                            ),
                                        ],
                                    ),
                                    ft.Text("\n"),
                                    ft.Row(
                                        controls= [
                                            ft.TextButton(
                                                "Sair", 
                                                icon= ft.icons.CLOSE,
                                                icon_color= "red",
                                                on_click= lambda _: page.go("/inicio"),
                                            ),
                                        ],
                                    ),
                                    ft.Text("\n"),
                                    ft.Row(
                                        controls= [        
                                            ft.Icon(ft.icons.PERSON_2_OUTLINED),
                                            ft.TextButton(
                                                text= "Atualizar",
                                                on_click= lambda _: page.go("/atualizar"),  
                                            ),
                                        ]
                                    ),
                                    ft.Text("\n"),
                                    ft.Row(
                                        controls= [        
                                            ft.Icon(ft.icons.PERSON_2_OUTLINED),
                                            ft.TextButton(
                                                text= "Excluir",
                                                on_click= lambda _: page.go("/excluir"),  
                                            ),
                                        ]
                                    )   
                                ],  
                            ), 
                        ),    
                    ], 
                ),
            ),  

        if page.route == "/sobre":
            page.views.append(  
                ft.View(
                    "/sobre", 
                    controls= [
                        ft.AppBar(
                            leading_width= 40,
                            title= ft.Text(
                                "Sobre", 
                                size= 20,
                                font_family= "fontAclonica"
                            ),
                            center_title= True,
                            actions= [
                                ft.IconButton(ft.icons.PLUS_ONE, on_click= lambda _: page.go('/add')),
                                ft.IconButton(ft.icons.HOME, on_click= lambda _: page.go('/home')),
                                ft.IconButton(ft.icons.AC_UNIT_ROUNDED, on_click= lambda _: page.go('/tempo')),
                                ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click= lambda _: page.go('/config')),
                                ft.PopupMenuButton(
                                    items=[
                                        ft.PopupMenuItem(
                                            content= ft.Row(
                                                controls= [
                                                    ft.Icon(ft.icons.PERSON_2_OUTLINED),
                                                    ft.TextButton(
                                                        text= "Sobre",
                                                        on_click= lambda _: page.go("/sobre"),  
                                                    ),
                                                ]
                                            ),
                                        ),    
                                    ],
                                ),
                            ]
                        ),
                        ft.Container(
                            padding = 70,
                            content= ft.Column(
                                alignment= "center",
                                controls= [
                                    Sobre.texto1,
                                    ft.Text("\n"),
                                    Sobre.texto2,
                                    ft.Text("\n"),
                                    Sobre.texto3,
                                    ft.Text("\n"),   
                                ],    
                            ), 
                        ),    
                    ], 
                ),
            ),
        
        if page.route == "/atualizar":
            page.views.append(  
                ft.View(
                    "/atualizar", 
                    controls= [
                    ft.AppBar(
                            leading_width= 40,
                            title= ft.Text(
                                "Atualizar", 
                                size= 20,
                                font_family= "fontAclonica"
                            ),
                            center_title= True,
                            actions= [
                                ft.IconButton(ft.icons.PLUS_ONE, on_click= lambda _: page.go('/add')),
                                ft.IconButton(ft.icons.HOME, on_click= lambda _: page.go('/home')),
                                ft.IconButton(ft.icons.AC_UNIT_ROUNDED, on_click= lambda _: page.go('/tempo')),
                                ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click= lambda _: page.go('/config')),
                                ft.PopupMenuButton(
                                    items=[
                                        ft.PopupMenuItem(
                                            content= ft.Row(
                                                controls= [
                                                    ft.Icon(ft.icons.PERSON_2_OUTLINED),
                                                    ft.TextButton(
                                                        text= "Sobre",
                                                        on_click= lambda _: page.go("/sobre"),  
                                                    ),
                                                ]
                                            ),
                                        ),    
                                    ],
                                ),
                            ]
                        ),
                    ft.Column(
                        spacing = 1,
                        expand= True,
                        controls= [
                            ft.Container(
                                alignment = ft.alignment.center,
                                margin = 2,
                                padding = 50,
                                expand= 2,
                                content= ft.Column(
                                    controls= [
                                        Atualizar.nomeTF,
                                        Atualizar.emailTF,
                                        Atualizar.senha1TF,
                                        Atualizar.senha2TF,                                     
                                    ]
                                ),
                            ),
                            ft.Container(
                                expand= 1,  
                                content= ft.Row(
                                    controls= [
                                        ft.ElevatedButton(
                                            width= 130,
                                            height= 140,
                                            style= ft.ButtonStyle(
                                                shape= ft.RoundedRectangleBorder(radius= 0)      
                                            ),
                                            content= ft.Container(
                                                content= ft.Column(
                                                    alignment= ft.MainAxisAlignment.CENTER,
                                                    controls= [
                                                        ft.Icon("lock", size= 60),
                                                        ft.Text("Recuperar \n senha", size= 17),
                                                    ],
                                                ),
                                            ),    
                                            on_click=lambda _: page.go("/home") if Atualizar.atualizarC() == True else page.go("/atualizar") ,
                                        ),    
                                    ], 
                                    alignment= ft.MainAxisAlignment.CENTER,                     
                                ), 
                            ),  
                        ],   
                    ), 
                ], 
                ),   
            ),
        
        if page.route == "/add":
            page.views.append(  
                ft.View(
                    "/add", 
                    controls= [
                    ft.AppBar(
                            leading_width= 40,
                            title= ft.Text(
                                "Adicionar ganhos",
                                size= 20,
                                font_family= "fontAclonica"
                            ),
                            center_title= True,
                            actions= [
                                ft.IconButton(ft.icons.PLUS_ONE, on_click= lambda _: page.go('/add')),
                                ft.IconButton(ft.icons.HOME, on_click= lambda _: page.go('/home')),
                                ft.IconButton(ft.icons.AC_UNIT_ROUNDED, on_click= lambda _: page.go('/tempo')),
                                ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click= lambda _: page.go('/config')),
                                ft.PopupMenuButton(
                                    items=[
                                        ft.PopupMenuItem(
                                            content= ft.Row(
                                                controls= [
                                                    ft.Icon(ft.icons.PERSON_2_OUTLINED),
                                                    ft.TextButton(
                                                        text= "Sobre",
                                                        on_click= lambda _: page.go("/sobre"),  
                                                    ),
                                                ]
                                            ),
                                        ),    
                                    ],
                                ),
                            ]
                        ),
                    ft.Column(
                        spacing = 1,
                        expand= False,
                        controls= [
                            ft.Container(
                                alignment = ft.alignment.center,
                                margin = 2,
                                padding = 50,
                                expand= 2,
                                content= ft.Column(
                                    controls= [
                                        Adicionar.texto1,
                                        Adicionar.valor1,
                                        Adicionar.texto2,
                                        Adicionar.valor2,
                                        Adicionar.texto3,
                                        Adicionar.valor3,                                      
                                    ]
                                ),
                            ),
                            ft.Container(
                                expand= 1,  
                                content= ft.Row(
                                    controls= [
                                        ft.ElevatedButton(
                                            width= 130,
                                            height= 140,
                                            style= ft.ButtonStyle(
                                                shape= ft.RoundedRectangleBorder(radius= 0)      
                                            ),
                                            content= ft.Container(
                                                content= ft.Column(
                                                    alignment= ft.MainAxisAlignment.CENTER,
                                                    controls= [
                                                        ft.Icon("plus_one", size= 60),
                                                        ft.Text("Adicionar \n ganhos", size= 17),
                                                    ],
                                                ),
                                            ),    
                                            on_click=lambda _: page.go("/home") if Adicionar.addGanhos() == True else page.go("/add") ,
                                        ),    
                                        
                                    ], 
                             
                                ), 
                            ),  
                        ],   
                    ), 
                ], 
                ),   
            ),

        if page.route == "/excluir":
            page.views.append(  
                ft.View(
                    "/excluir", 
                    controls= [
                    Inicio.appBarAppInicio(page, ft, "Excluir a conta"),
                    ft.Column(
                        spacing = 1,
                        expand= True,
                        controls= [
                            ft.Container(
                                alignment = ft.alignment.center,
                                margin = 2,
                                padding = 50,
                                expand= 2,
                                content= ft.Column(
                                    controls= [
                                        
                                        ft.Text("Sua conta será excluida", size= 25),
                                        Deletar.emailTF                                  
                                    ]
                                ),
                            ),
                            ft.Container(
                                expand= 1,  
                                content= ft.Row(
                                    controls= [
                                        ft.ElevatedButton(
                                            width= 130,
                                            height= 140,
                                            style= ft.ButtonStyle(
                                                shape= ft.RoundedRectangleBorder(radius= 0)      
                                            ),
                                            content= ft.Container(
                                                content= ft.Column(
                                                    alignment= ft.MainAxisAlignment.CENTER,
                                                    controls= [
                                                        ft.Icon("lock", size= 60),
                                                        ft.Text("Excluir \n conta", size= 17),
                                                    ],
                                                ),
                                            ),    
                                            on_click=lambda _: page.go("/inicio") if Deletar.excluir() == True else page.go("/home"),
                                        ),    
                                        
                                    ], 
                                    alignment= ft.MainAxisAlignment.CENTER,                     
                                ), 
                            ),  
                        ],   
                    ), 
                ], 
                ),   
            ),
      
        
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)    

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    


ft.app(target=main)




