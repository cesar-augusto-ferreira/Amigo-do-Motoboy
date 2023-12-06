import flet as ft
import json as js
import requests
from functions.funcoes import Funcoes

class Tempo:


    API_KEY = "c9948274f47aade634cf5f79f7fd6971"
    cidade = "ribeirão preto"
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperaturaA = requisicao_dic['main']['temp'] - 273.15
    humidade = requisicao_dic['main']['humidity'] 
    temperaturaMax = requisicao_dic['main']['temp_max'] - 273.15

    texto1= ft.Text("Veja o tempo agora\n\n", size= 20)

    texto2= ft.Text("cidade:", size= 20)
    texto3= ft.Text('Ribeirão preto ', size= 20)

    texto4= ft.Text("\n Condições:", size= 20)
    texto5= ft.Text(descricao, size= 20)

    texto6= ft.Text("\n Temperatuta", size= 20)
    texto7= ft.Text(f"{temperaturaA} ºC", size= 20)

    texto8= ft.Text("\n Humidade do ar", size= 20)
    texto9= ft.Text(f"{humidade} %", size= 20)

    

   
      

    




 

