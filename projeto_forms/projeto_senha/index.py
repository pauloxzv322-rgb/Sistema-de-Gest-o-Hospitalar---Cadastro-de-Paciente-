from tkinter import *
from tkinter import messagebox

# Configuração da janela principal (Cliente)
cliente = Tk()
cliente.title("Solicitar senha")
cliente.geometry("400x250")
cliente.configure(bg="lightgreen")

# Variáveis globais
contador = 1
fila = []
senha_atual = StringVar()
senha_atual.set("---")

# --- Janela do Administrador ---
admin = Toplevel(cliente)
admin.title("Admin")
admin.geometry("300x450")
admin.configure(bg="lightgreen")

Label(admin, text="fila de senha", font=("Arial", 14)).pack(pady=10)
lista_admin = Listbox(admin, width=20, height=10)
lista_admin.pack(pady=10)

# --- Janela do Painel (Telão) ---
painel = Toplevel(cliente)
painel.title("Painel de Senha")
painel.geometry("400x300")
painel.configure(bg="lightgreen")

Label(painel, text="Senha Atual", font=("Arial", 20)).pack(pady=20)
Label(
    painel,
    textvariable=senha_atual,
    font=("Arial", 40),
    fg="red",
    bg="white",
    width=10
).pack(pady=20)

# --- Funções de Lógica ---
def solicitar_senha():
    global contador
    senha = f"A{contador:03d}"
    fila.append(senha)
    lista_admin.insert(END, senha)
    messagebox.showinfo("Senha Solicitada", f"Sua senha é: {senha}")
    contador += 1

def chamar_senha():
    if len(fila) == 0:
        messagebox.showwarning("Aviso", "Fila vazia.")
        senha_atual.set("---")
    else:
        # Pega a primeira senha da lista (quem chegou primeiro)
        proxima_senha = fila.pop(0)
        # Remove visualmente da lista do admin
        lista_admin.delete(0)
        # Atualiza o telão vermelho
        senha_atual.set(proxima_senha)

# --- Botões das Janelas ---

# Botão na janela do Cliente
Label(cliente, text="Retirar senha", font=("Arial", 16), bg="lightgreen").pack(pady=20)
Button(cliente, 
       text="Gerar Senha", 
       width=20, 
       command=solicitar_senha, 
       font=("Arial", 14)).pack(pady=10)

# Botão na janela do Admin (Agora com .pack() para aparecer!)
Button(
    admin, 
    text="Chamar Próxima", 
    width=20, 
    command=chamar_senha, 
    font=("Arial", 14),
    bg="white"
).pack(pady=20)

cliente.mainloop()