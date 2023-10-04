import csv

# Cria uma lista vazia para armazenar os usuários
usuarios = []

# Solicita ao usuário que insira informações e as adiciona à lista
while True:
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    idade = input("Digite a idade do usuário: ")
    email = input("Digite o e-mail do usuário: ")

    usuario = [nome, idade, email]
    usuarios.append(usuario)

# Escreve a lista de usuários em um arquivo CSV
nome_arquivo = "usuarios.csv"

with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escreve o cabeçalho (nomes das colunas)
    escritor_csv.writerow(['Nome', 'Idade', 'E-mail'])
    
    # Escreve os dados dos usuários
    escritor_csv.writerows(usuarios)

print(f'As informações dos usuários foram armazenadas no arquivo {nome_arquivo}.')


import csv

# Nome do arquivo CSV onde os dados estão armazenados
nome_arquivo = "usuarios.csv"

# Lista para armazenar os dados extraídos da planilha
dados_usuarios = []

# Lê os dados do arquivo CSV
with open(nome_arquivo, mode='r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    # Pula a primeira linha (cabeçalho)
    next(leitor_csv)
    
    # Lê os dados dos usuários e os armazena na lista
    for linha in leitor_csv:
        dados_usuarios.append(linha)

# Mostra os dados extraídos
for usuario in dados_usuarios:
    print(usuario)


import csv

# Função para atualizar os dados de um usuário
def atualizar_dados(nome, nova_idade, novo_email):
    for usuario in dados_usuarios:
        if usuario[0] == nome:
            usuario[1] = nova_idade
            usuario[2] = novo_email
            return True
    return False

# Nome do arquivo CSV onde os dados estão armazenados
nome_arquivo = "usuarios.csv"

# Lista para armazenar os dados extraídos da planilha
dados_usuarios = []

# Lê os dados do arquivo CSV
with open(nome_arquivo, mode='r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    # Pula a primeira linha (cabeçalho)
    cabecalho = next(leitor_csv)
    
    # Lê os dados dos usuários e os armazena na lista
    for linha in leitor_csv:
        dados_usuarios.append(linha)

# Mostra os dados extraídos
for usuario in dados_usuarios:
    print(usuario)

# Exemplo de atualização dos dados de um usuário
nome_alterar = input("Digite o nome do usuário que deseja alterar: ")
nova_idade = input("Digite a nova idade: ")
novo_email = input("Digite o novo e-mail: ")

if atualizar_dados(nome_alterar, nova_idade, novo_email):
    print(f'Dados do usuário {nome_alterar} foram atualizados com sucesso.')

    # Salva as alterações no arquivo CSV
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        
        # Escreve o cabeçalho
        escritor_csv.writerow(cabecalho)
        
        # Escreve os dados atualizados
        escritor_csv.writerows(dados_usuarios)
else:
    print(f'Usuário com o nome {nome_alterar} não encontrado.')
