import tkinter as tk    #importa a biblioteca tkinter
from tkinter import messagebox    #importa a biblioteca messagebox
def hello():    #função que exibe a mensagem
    messagebox.showinfo("Hello", "Hello World")
root = tk.Tk()    #cria a janela
root.title("Hello Edu")    #define o título da janela
root.geometry("200x500")    #define o tamanho da janela
button = tk.Button(root, text="Hello", command=hello)    #cria um botão
button.pack()    #exibe o botão
root.mainloop()    #inicia o loop principal
#https://pt.stackoverflow.com/questions/456727/como-criar-um-app-simples-com-interface-gr%C3%A1fica-em-pythonc