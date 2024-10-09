import customtkinter as ctk
from pynput.keyboard import Controller
import time
from tkinter import messagebox
from threading import Thread
from PIL import Image, ImageTk

keyboard = Controller()
cancelar = False  

def digitar_texto():
    global cancelar
    cancelar = False  
    texto = entrada.get("1.0", "end-1c")
    if not texto.strip():
        messagebox.showwarning("Aviso", "Por favor, digite algum texto.")
        return
    messagebox.showinfo("Aviso", "Daqui 5 segundos, a digitação começará.")
    time.sleep(5) 
    for letra in texto:
        if cancelar:
            messagebox.showinfo("Aviso", "Digitação cancelada.")
            return
        keyboard.press(letra)
        keyboard.release(letra)
        time.sleep(0.025)

def cancelar_digitar():
    global cancelar
    cancelar = True

janela = ctk.CTk()
janela.title("Digite sua Redação Aqui!")
janela.geometry("600x500")
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

try:
    imagem = Image.open("icon.jpg")
    imagem = ImageTk.PhotoImage(imagem)
    label_imagem = ctk.CTkLabel(janela, image=imagem)
    label_imagem.pack(pady=10)
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")

entrada = ctk.CTkTextbox(janela, width=500, height=200)
entrada.pack(pady=20)

botao_iniciar = ctk.CTkButton(janela, text="Iniciar Digitação", command=lambda: Thread(target=digitar_texto).start())
botao_iniciar.pack(pady=10)

botao_cancelar = ctk.CTkButton(janela, text="Cancelar Digitação", command=cancelar_digitar)
botao_cancelar.pack(pady=10)

janela.mainloop()