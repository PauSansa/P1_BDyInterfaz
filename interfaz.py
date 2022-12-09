import tkinter as tk
from tkinter import *
import datamanager


class Interfaz:
    username = ""
    password = ""

    def crear_interfaz(self):


        def mostrar_tabla():
            window = tk.Tk()
            window.configure(bd=100)
            window.title("Visualizador de Datos")
            rows = datamanager.return_listas()
            for i in range(1, 5):
                window.columnconfigure(i, weight=4)
            for i in range(len(rows)):
                for j in range(len(rows[i])):
                    label = tk.Label(window, text=f"{rows[i][j]}", )
                    label.grid(column=j, row=i)
            window.mainloop()

        def desactiva_pass():
            password_label.grid_forget()
            password_entry.grid_forget()

        def desactiva_user():
            username_label.grid_forget()
            username_entry.grid_forget()

        def activa_user():
            username_label.grid(column=0, row=0, sticky="W")
            username_entry.grid(column=1, row=0, sticky="E")

        def activa_pass():
            password_entry.grid(column=1, row=1, sticky="E")
            password_label.grid(column=0, row=1, sticky="W")

        def accion_rbutton():
            if var_rb.get() == 1:
                # ELIMINAR DATOS
                save_button.configure(text="Elimina", command=accion_button)
                activa_user()
                desactiva_pass()


            elif var_rb.get() == 0:
                # AÑADIR DATOS
                save_button.configure(text="Añade", command=accion_button)
                activa_user()
                activa_pass()

            elif var_rb.get() == 2:
                # VER DATOS
                save_button.configure(text="Mirar Base de Datos", command=accion_button)
                desactiva_user()
                desactiva_pass()


        def accion_button():
            if var_rb.get() == 0:
                # AÑADIR USUARIO
                self.username = username_entry.get()
                self.password = password_entry.get()
                datamanager.anadir_usuario(self.username, self.password)
            elif var_rb.get() == 1:
                # BORRAR USUARIO
                self.username = username_entry.get()
                datamanager.quitar_usuario(self.username)
            elif var_rb.get() == 2:
                mostrar_tabla()

        # Root Configure
        root = tk.Tk()
        root.configure(bd=20)
        root.title("Gestor de Datos")
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
        save_button = tk.Button(root, text="Añade", command=accion_button)
        save_button.grid(column=2, row=2)


        # RadioButton
        var_rb = IntVar()
        anadir_rb = tk.Radiobutton(root, text="Añadir", variable=var_rb, value=0, command=accion_rbutton)
        anadir_rb.grid(column=0, row=3, sticky="W")

        borrar_rb = tk.Radiobutton(root, text="Quitar", variable=var_rb, value=1, command=accion_rbutton)
        borrar_rb.grid(column=1, row=3, sticky="E")

        ver_rb = tk.Radiobutton(root, text="Ver Users", variable=var_rb, value=2, command=accion_rbutton)
        ver_rb.grid(column=2, row=3)

        root.mainloop()
