# pip install paho-mqtt
import tkinter as tk
from tkinter import Label, Button, Frame
import random
import time
import paho.mqtt.client as mqtt
import threading
import json

# MQTT
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/air_quality_monitor"

# gera dados simulados dos sensores
def simular_dados():
    return {
        "CO2": round(random.uniform(350, 2000), 1),  # ppm
        "PM2_5": round(random.uniform(0, 150), 1),  # µg/m³
        "temperatura": round(random.uniform(15, 40), 1),  # °C
        "umidade": round(random.uniform(20, 90), 1)  # %
    }

# avalia a qualidade do ar com base em PM2.5
def avaliar_qualidade_ar(pm2_5):
    if pm2_5 <= 12:
        return "Bom", "green"
    elif 12 < pm2_5 <= 35:
        return "Moderado", "yellow"
    elif 35 < pm2_5 <= 55:
        return "Ruim", "orange"
    else:
        return "Muito Ruim", "red"

# envia os dados para o broker MQTT
def enviar_mqtt(client, dados):
    mensagem = json.dumps(dados)
    client.publish(TOPIC, mensagem)
    print(f"Enviado para MQTT: {mensagem}")

# interface gráfica atualizada
def atualizar_dados():
    if not monitorando:
        return

    dados = simular_dados()
    co2, pm2_5, temperatura, umidade = dados.values()
    status, cor = avaliar_qualidade_ar(pm2_5)

    label_co2.config(text=f"CO2: {co2} ppm")
    label_pm2_5.config(text=f"PM2.5: {pm2_5} µg/m³")
    label_temperatura.config(text=f"Temperatura: {temperatura} °C")
    label_umidade.config(text=f"Umidade: {umidade} %")
    label_status.config(text=f"Qualidade do Ar: {status}", bg=cor)

    enviar_mqtt(mqtt_client, dados)
    root.after(3000, atualizar_dados)

# monitoramento
def iniciar_monitoramento():
    global monitorando
    monitorando = True
    label_status_operacao.config(text="Monitorando...", fg="green")
    btn_start.config(state="disabled")
    atualizar_dados()

def parar_monitoramento():
    global monitorando
    monitorando = False
    label_status_operacao.config(text="Parado", fg="red")
    btn_start.config(state="normal")

# broker MQTT
def conectar_mqtt():
    client = mqtt.Client()
    client.connect(BROKER, PORT)
    return client

# interface
root = tk.Tk()
root.title("Monitoramento de Qualidade do Ar")
root.geometry("800x500")
root.configure(bg="#f5f5f5")

monitorando = False
mqtt_client = conectar_mqtt()

titulo = Label(root, text="Monitoramento de Qualidade do Ar", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333")
titulo.pack(pady=10)

label_status_operacao = Label(root, text="Parado", font=("Arial", 14, "bold"), bg="#f5f5f5", fg="red")
label_status_operacao.pack(pady=5)

frame_dados = Frame(root, bg="white", bd=2, relief="solid")
frame_dados.pack(pady=10, padx=10, fill="x")

label_co2 = Label(frame_dados, text="CO2: -- ppm", font=("Arial", 14), bg="white", anchor="w")
label_co2.pack(fill="x", padx=10, pady=5)

label_pm2_5 = Label(frame_dados, text="PM2.5: -- µg/m³", font=("Arial", 14), bg="white", anchor="w")
label_pm2_5.pack(fill="x", padx=10, pady=5)

label_temperatura = Label(frame_dados, text="Temperatura: -- °C", font=("Arial", 14), bg="white", anchor="w")
label_temperatura.pack(fill="x", padx=10, pady=5)

label_umidade = Label(frame_dados, text="Umidade: -- %", font=("Arial", 14), bg="white", anchor="w")
label_umidade.pack(fill="x", padx=10, pady=5)

label_status = Label(frame_dados, text="Qualidade do Ar: --", font=("Arial", 16, "bold"), bg="gray", fg="white")
label_status.pack(fill="x", padx=10, pady=20)

frame_botoes = Frame(root, bg="#f5f5f5")
frame_botoes.pack(pady=20)

btn_start = Button(frame_botoes, text="Start", font=("Arial", 12), bg="blue", fg="white", command=iniciar_monitoramento)
btn_start.grid(row=0, column=0, padx=10)

btn_parar = Button(frame_botoes, text="Stop", font=("Arial", 12), bg="red", fg="white", command=parar_monitoramento)
btn_parar.grid(row=0, column=1, padx=10)

root.mainloop()
