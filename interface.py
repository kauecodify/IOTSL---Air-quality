import tkinter as tk
from tkinter import Label, Button, Frame
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import numpy as np

def simular_dados():
    return {
        "temperatura": round(random.uniform(20, 35), 1),
        "umidade": round(random.uniform(30, 70), 1),
        "pm2_5": round(random.uniform(0, 100), 1)
    }

def avaliar_qualidade_ar(pm2_5):
    if pm2_5 <= 12:
        return "Bom", "green"
    elif 12 < pm2_5 <= 35:
        return "Moderado", "yellow"
    elif 35 < pm2_5 <= 55:
        return "Ruim", "orange"
    else:
        return "Muito Ruim", "red"

def atualizar_dados():
    if not monitorando:
        return

    dados = simular_dados()
    temperatura, umidade, pm2_5 = dados.values()
    status, cor = avaliar_qualidade_ar(pm2_5)

    label_temperatura.config(text=f"Temperatura: {temperatura} °C")
    label_umidade.config(text=f"Umidade: {umidade} %")
    label_pm2_5.config(text=f"PM2.5: {pm2_5} µg/m³")
    label_status.config(text=f"Qualidade do Ar: {status}", bg=cor)

    atualizar_grafico(pm2_5, cor)
    root.after(3000, atualizar_dados)

def atualizar_grafico(pm2_5, cor):
    ax.clear()
    x = np.linspace(0, 10, 500)
    y = np.sin(x * 2 * np.pi) * (pm2_5 / 100)
    ax.plot(x, y, color=cor, linewidth=2, label=f"PM2.5: {pm2_5} µg/m³")
    ax.set_title("Representação Senoidal da Qualidade do Ar")
    ax.set_xlabel("Tempo")
    ax.set_ylabel("Amplitude")
    ax.legend()
    canvas_grafico.draw()

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

root = tk.Tk()
root.title("Monitoramento Avançado - Qualidade do Ar")
root.geometry("800x600")
root.configure(bg="#f5f5f5")

monitorando = False

titulo = Label(root, text="Monitoramento Avançado - Qualidade do Ar", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333")
titulo.pack(pady=10)

label_status_operacao = Label(root, text="Parado", font=("Arial", 14, "bold"), bg="#f5f5f5", fg="red")
label_status_operacao.pack(pady=5)

frame_dados = Frame(root, bg="white", bd=2, relief="solid")
frame_dados.pack(pady=10, padx=10, fill="x")

label_temperatura = Label(frame_dados, text="Temperatura: -- °C", font=("Arial", 14), bg="white", anchor="w")
label_temperatura.pack(fill="x", padx=10, pady=5)

label_umidade = Label(frame_dados, text="Umidade: -- %", font=("Arial", 14), bg="white", anchor="w")
label_umidade.pack(fill="x", padx=10, pady=5)

label_pm2_5 = Label(frame_dados, text="PM2.5: -- µg/m³", font=("Arial", 14), bg="white", anchor="w")
label_pm2_5.pack(fill="x", padx=10, pady=5)

label_status = Label(frame_dados, text="Qualidade do Ar: --", font=("Arial", 16, "bold"), bg="gray", fg="white")
label_status.pack(fill="x", padx=10, pady=20)

fig = Figure(figsize=(6, 3), dpi=100)
ax = fig.add_subplot(111)
canvas_grafico = FigureCanvasTkAgg(fig, root)
canvas_grafico.get_tk_widget().pack(pady=10)

frame_botoes = Frame(root, bg="#f5f5f5")
frame_botoes.pack(pady=20)

btn_start = Button(frame_botoes, text="Start", font=("Arial", 12), bg="blue", fg="white", command=iniciar_monitoramento)
btn_start.grid(row=0, column=0, padx=10)

btn_parar = Button(frame_botoes, text="Stop", font=("Arial", 12), bg="red", fg="white", command=parar_monitoramento)
btn_parar.grid(row=0, column=1, padx=10)

root.mainloop()
