# 🌤️ Python Weather App

A simple Python application that fetches **real-time weather information** for any city using the [WeatherAPI](https://www.weatherapi.com/) and displays it in a **graphical interface with Tkinter**.  
Users can type a city name and get the **current temperature, weather condition, and local time**.

---

## ⚡ Features

- 🌍 Fetch real-time weather data for any city  
- ⏰ Display local time  
- 🌡️ Display temperature in Celsius  
- 🌤️ Show weather condition (e.g., sunny, cloudy, rain)  
- 🖥️ Simple GUI with Tkinter  
- ⚠️ Alerts for errors or missing input using pop-ups

## 🛠️ Requirements

- Python 3.6+  
- Free WeatherAPI account to get an **API Key**  
- Python libraries available on file "Requirements.txt"
  
## 🔑 .env Configuration
Create a .env file in the project root:
```
API_KEY=YOUR_API_KEY_HERE
```
## ⚠️ Make sure .env is added to .gitignore to keep your API Key private:

```
.env
```
## 🚀 How to Run

1 - Clone the repository:

```
  git clone https://github.com/gu-herminio/weather-app.git
  cd weather-app
```
2 - Install dependencies:
```
pip install -r requirements.txt

```
3 - Create .env with your API Key

4 - Run the app:

```
python api_request.py
```

5 - Enter the city name in the window and click "Buscar Clima".

<img width="300" height="179" alt="Captura de tela 2025-10-08 002732" src="https://github.com/user-attachments/assets/f015d667-aea2-4434-b02e-c23054409323" />

---

## ⚠️ Note

This project is intended for **educational purposes only**.  
It is a simple Python application to learn how to use APIs, handle environment variables, and create a GUI with Tkinter.
