from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Janela principal
janela = Tk()
janela.title("Cadastro de cliente")
janela.geometry("700x400")

####Notbook (abas)

abas = ttk.Notebook(janela)
abas.pack(fill="both", expand=True)

#aba01 - Cadastro
aba1 = Frame(abas)
abas.add(aba1, text="Cadastro")

#aba02 - Tabela
aba2 = Frame(abas)
abas.add(aba2, text="Clientes cadastrados")

#Função cadastrar
def cadastrar():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    cidade = entry_cidade.get()
    
    if nome == "" or telefone == "" or email == "" or cidade == "":
        messagebox.showwarning("ERRO", "Preencha todos os campos!")
    else:
        tabela.insert("", END, values=(nome, telefone, email, cidade))
        
        entry_nome.delete(0,END)
        entry_telefone.delete(0,END)
        entry_email.delete(0,END)
        entry_cidade.delete(0,END)

        messagebox.showinfo("Sucesso", "Cliente cadastrado")

### Aba Cadastro
Label(aba1, text="Nome").pack(pady=5)
entry_nome = Entry(aba1, width=40)
entry_nome.pack()


Label(aba1, text="Telefone").pack(pady=5)
entry_telefone = Entry(aba1, width=40)
entry_telefone.pack()

Label(aba1, text="Email").pack(pady=5)
entry_email = Entry(aba1, width=40)
entry_email.pack()

Label(aba1, text="Cidade").pack(pady=5)
entry_cidade = Entry(aba1, width=40)
entry_cidade.pack()


Button(
    aba1,
    text="Cadastro",
    bg="green",
    fg="white",
    width=20,
    command=cadastrar
).pack(pady=20)

###aba tabela
colunas = ("Nome", "Telefone", "Email", "Cidade")

tabela=ttk.Treeview(
    aba2,
    columns=colunas,
    show="headings"
)

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=150)

tabela.pack(fill="both", expand=True, pady=20)






janela.mainloop()
