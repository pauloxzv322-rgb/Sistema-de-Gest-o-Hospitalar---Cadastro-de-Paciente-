from tkinter import *
from tkinter import messagebox

cliente=Tk()
cliente.title("Solicitar senha")
cliente.geometry("400x200")
cliente.configure(bg="lightgreen")


contador = 1
fila = []
StringVar()
senha_atual = StringVar()
senha_atual.set("---")

admin = Toplevel(cliente)
admin.title("Admin")
admin.geometry("300x350")
admin.configure(bg="lightgreen")

Label(admin, text="fila de senha", font=("Arial", 14)).pack(pady=10)
lista_admin=Listbox(admin, width=20, height=10)
lista_admin.pack(pady=10)

painel = Toplevel(cliente)
painel.title("Painel de Senha")
painel.geometry("400x300")
painel.configure(bg="lightgreen")








cliente.mainloop()