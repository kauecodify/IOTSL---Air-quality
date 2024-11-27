#pip install opencv-python pillow

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import random

def update_status():
    for i, drone in enumerate(drones):
        drone["battery"] = max(0, drone["battery"] - random.randint(1, 5))
        drone["water"] = max(0, drone["water"] - random.randint(1, 10))
        drone_labels[i]["text"] = (f"Drone {i+1}:\n"
                                   f"Bateria: {drone['battery']}%\n"
                                   f"Água: {drone['water']}%\n"
                                   f"Altitude: {drone['altitude']}m")
    root.after(2000, update_status)

def update_video():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (300, 200))
        img = ImageTk.PhotoImage(Image.fromarray(frame))
        video_label.configure(image=img)
        video_label.image = img
    root.after(10, update_video)

root = tk.Tk()
root.title("Monitoramento de Drones")
root.geometry("1000x600")

drones = [{"battery": 100, "water": 100, "altitude": 10} for _ in range(3)]
drone_labels = []

left_frame = ttk.Frame(root, width=200)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

ttk.Label(left_frame, text="Status dos Drones", font=("Arial", 14, "bold")).pack(pady=10)
for i, drone in enumerate(drones):
    label = ttk.Label(left_frame, text="", font=("Arial", 10))
    label.pack(pady=5, anchor="w")
    drone_labels.append(label)

center_frame = ttk.Frame(root)
center_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

map_canvas = tk.Canvas(center_frame, bg="lightblue", width=400, height=400)
map_canvas.pack()
map_canvas.create_oval(180, 180, 220, 220, fill="green", outline="black", width=2)
map_canvas.create_text(200, 250, text="Área de Irrigação", font=("Arial", 12))

right_frame = ttk.Frame(root, width=300)
right_frame.pack(side="right", fill="y", padx=10, pady=10)

ttk.Label(right_frame, text="Câmera ao Vivo", font=("Arial", 14, "bold")).pack(pady=10)
video_label = ttk.Label(right_frame)
video_label.pack(pady=10)

cap = cv2.VideoCapture(0)

update_status()
update_video()

root.mainloop()

cap.release()
