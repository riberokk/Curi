import os, time

tarefas = {}

def visualizar():
    os.system("cls")
    print("Tarefas:")
    print()
    for chave, dados in tarefas.items():
        print(f"Tarefa {chave}º\nNome: {dados['Tarefa']}\nDescrição: {dados['Descrição']}")
        print()
        time.sleep(0.5)
    os.system("pause")

def criar():
    os.system("cls")
    print("Criar Tarefas:")
    tarefa = input("Insira o nome da tarefa \n---> ")
    descricao = input("Insira a descrição da tarefa \n---> ")
    chave = len(tarefas) + 1
    tarefas[chave] = {"Tarefa": tarefa, "Descrição": descricao}
    os.system("pause")

def editar():
    os.system("cls")
    print("Editar Tarefas")
    for chave, dados in tarefas.items():
        print(f"{chave} - Tarefa: {dados['Tarefa']}")
    alt = int(input("Insira o número da tarefa que deseja alterar \n---> "))
    if alt in tarefas:
        print(f"Você está alterando dados da tarefa: {tarefas[alt]['Tarefa']}")
        alt2 = int(input("Qual dado você deseja editar (1 - Nome, 2 - Descrição)\n---> "))
        if alt2 == 1:
            alt3 = input("Insira o novo nome:\n---> ")
            tarefas[alt]['Tarefa'] = alt3
        elif alt2 == 2:
            alt4 = input("Insira a nova descrição:\n---> ")
            tarefas[alt]['Descrição'] = alt4
    else:
        print("Tarefa não encontrada.")
    os.system("pause")

def excluir():
    os.system("cls" if os.name == "nt" else "clear")
    print("Excluir Tarefas")
    for chave, dados in tarefas.items():
        print(f"{chave} - Tarefa: {dados['Tarefa']}")
    alt = int(input("Insira o número da tarefa que deseja excluir \n---> "))
    
    if alt in tarefas:
        del tarefas[alt]
        print("Tarefa excluída com sucesso.")
    else:
        print("Tarefa não encontrada.")
    os.system("pause")