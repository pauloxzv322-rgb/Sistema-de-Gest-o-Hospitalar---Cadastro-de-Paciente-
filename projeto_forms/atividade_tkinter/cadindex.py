from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Janela principal
janela = Tk()
janela.title("Sistema de Gestão Hospitalar - Cadastro de Paciente")
janela.geometry("800x600")

#### Notebook (abas)
abas = ttk.Notebook(janela)
abas.pack(fill="both", expand=True)

# aba01 - Cadastro do Paciente
aba1 = Frame(abas)
abas.add(aba1, text="Cadastro do Paciente")

# aba02 - Pacientes Cadastrados
aba2 = Frame(abas)
abas.add(aba2, text="Pacientes Cadastrados")

# Função cadastrar
def cadastrar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    nascimento = entry_nascimento.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    convenio = entry_convenio.get()
    emergencia = entry_emergencia.get()
    
    # Validação de campos obrigatórios
    if not (nome and cpf and nascimento and telefone and email and convenio and emergencia):
        messagebox.showwarning("ERRO", "Preencha todos os campos obrigatórios!")
    else:
        # Insere na Treeview da Aba 2
        tabela.insert("", END, values=(nome, cpf, nascimento, telefone, email, convenio, emergencia))
        
        # Limpa os campos após o cadastro
        entry_nome.delete(0, END)
        entry_cpf.delete(0, END)
        entry_nascimento.delete(0, END)
        entry_telefone.delete(0, END)
        entry_email.delete(0, END)
        entry_convenio.delete(0, END)
        entry_emergencia.delete(0, END)

        messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")

### Aba 1 - Cadastro do Paciente
# Usando um Frame central para organizar melhor os campos
container = Frame(aba1)
container.pack(pady=10)

Label(container, text="Nome Completo").pack(pady=2)
entry_nome = Entry(container, width=50)
entry_nome.pack()

Label(container, text="CPF").pack(pady=2)
entry_cpf = Entry(container, width=50)
entry_cpf.pack()

Label(container, text="Data de Nascimento").pack(pady=2)
entry_nascimento = Entry(container, width=50)
entry_nascimento.pack()

Label(container, text="Telefone").pack(pady=2)
entry_telefone = Entry(container, width=50)
entry_telefone.pack()

Label(container, text="Email").pack(pady=2)
entry_email = Entry(container, width=50)
entry_email.pack()

Label(container, text="Convênio / SUS").pack(pady=2)
entry_convenio = Entry(container, width=50)
entry_convenio.pack()

Label(container, text="Contato de Emergência").pack(pady=2)
entry_emergencia = Entry(container, width=50)
entry_emergencia.pack()

Button(
    aba1,
    text="Salvar Cadastro",
    bg="#2e7d32",
    fg="white",
    width=25,
    font=("Arial", 10, "bold"),
    command=cadastrar
).pack(pady=20)

### Aba 2 - Tabela de Pacientes
colunas = ("Nome", "CPF", "Nascimento", "Telefone", "Email", "Convênio", "Emergência")

# Barra de rolagem para a tabela
scroll_y = Scrollbar(aba2)
scroll_y.pack(side=RIGHT, fill=Y)

tabela = ttk.Treeview(
    aba2,
    columns=colunas,
    show="headings",
    yscrollcommand=scroll_y.set
)

scroll_y.config(command=tabela.yview)

# Configuração dos cabeçalhos e largura das colunas
for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=110, anchor=CENTER)

tabela.pack(fill="both", expand=True, padx=10, pady=10)

janela.mainloop()