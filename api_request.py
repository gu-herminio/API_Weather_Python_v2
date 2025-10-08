# Importação das bibliotecas necessárias
import requests
import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
api_key = os.getenv("API_KEY")


def get_weather(city: str,lang: str = "pt"):

    # URL base da API de clima
    link_api = "https://api.weatherapi.com/v1/current.json"


    # Parâmetros que serão enviados na requisição HTTP GET
    parameters = {"key": api_key,
                "q": city,
                "lang" : lang
                }


    # Realiza a requisição GET à API
    response = requests.get(link_api, params = parameters)


    # Se a requisição for bem-sucedida, extrai e imprime os dados
    if response.status_code == 200:
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        localtime = data["location"]["localtime"]

        result = (f"📍 Cidade: {city} \n"
            f"🕒 Hora local: {localtime} \n"
            f"🌡️ Temperatura: {temp}°C \n"
            f"🌤️ Condição: {condition}")
        messagebox.showinfo("Resultado", result)

    else:
        messagebox.showerror("Erro", f"Erro na requisição: {response.status_code} - {response.text}")


#Função para chamar botão 
def on_submit():
    city = city_entry.get()
    if city:
        get_weather(city)
    else: 
        messagebox.showwarning("Atenção", "Por favor, digite o nome da cidade!")

#Criação da janela
root = tk.Tk()
root.title("Consulta de Clima")


#Janela
window_width = 300
window_height = 150
screen_width = root.winfo_screenmmwidth()
screen_height = root.winfo_screenmmheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)



#Entrada de dados sobre cidade
tk.Label(root, text="Digite a cidade: ").pack(pady=5)
city_entry = tk.Entry(root,width=30)
city_entry.pack(pady=5)

#Botão de Consulta
tk.Button(root,text = "Buscar Clima", command=on_submit).pack(pady=10)

#Execução da interface
root.mainloop()

print("test")