import tkinter as tk
from tkinter import *
import datamanager


class Interfaz:
    username = ""
    password = ""

    def crear_interfaz(self):


        def accion_botton():
            if var_rb.get() == 1:
                save_button.configure(text="Elimina")
                password_entry.grid_forget()
                password_label.grid_forget()
            else:
                print("Estoy en el pass grind")
                save_button.configure(text="Añade")
                password_entry.grid(column=1, row=1, sticky="E")
                password_label.grid(column=0, row=1, sticky="W")



        def guardar_entrys():
            if var_rb.get() == 0:
                self.username = username_entry.get()
                self.password = password_entry.get()
                datamanager.añadir_usuario(self.username, self.password)
            else:
                self.username = username_entry.get()
                datamanager.quitar_usuario(self.username)

        # Root Configure
        root = tk.Tk()
        root.configure(bd=20)
        for i in range(1, 4):
            root.columnconfigure(i, weight=5)


        # Username
        username_label = tk.Label(root, text="Usuario:")
        username_label.grid(column=0, row=0, sticky="W")

        username_entry = tk.Entry(root)
        username_entry.grid(column=1, row=0, sticky="E")


        # Password
        password_label = tk.Label(root, text="Contraseña:")
        password_label.grid(column=0, row=1, sticky="W")

        password_entry = tk.Entry(root)
        password_entry.grid(column=1, row=1, sticky="E")


        # Button
        save_button = tk.Button(root, text="Añade", command=guardar_entrys)
        save_button.grid(column=2, row=2)


        # RadioButton
        var_rb = IntVar()
        anadir_rb = tk.Radiobutton(root, text="Añadir", variable=var_rb, value=0, command=accion_botton)
        anadir_rb.grid(column=0, row=3, sticky="W")

        borrar_rb = tk.Radiobutton(root, text="Quitar", variable=var_rb, value=1, command=accion_botton)
        borrar_rb.grid(column=1, row=3, sticky="E")
        root.mainloop()
