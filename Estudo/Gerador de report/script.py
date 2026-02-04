#!/usr/bin/env python3
import csv
import os

os.system("cls" if os.name=="nt" else"clear")
def read_employees(csv_file_location):
    """
    Objetivo: Abrir o CSV e transformá-lo numa lista de dicionários.
    """
    # 1. Registamos um "dialeto". O 'skipinitialspace=True' remove espaços 
    # que existam após a vírgula (ex: "Nome, Departamento" vira "Departamento" e não " Departamento").
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    
    # 2. Respondendo à tua pergunta: Usamos o 'with' para abrir o ficheiro. 
    # Ao contrário do open() sozinho, o 'with' garante que o ficheiro FECHA automaticamente 
    # assim que o bloco terminar, mesmo que ocorra um erro.
    with open(csv_file_location, 'r', encoding='utf-8') as f:
        # O DictReader utiliza a primeira linha (cabeçalho) como chaves do dicionário.
        employee_file = csv.DictReader(f, dialect='empDialect')
        
        employee_list = []
        for data in employee_file:
            # 3. Para que serve o dict(data)? 
            # O DictReader devolve um objeto especial (OrderedDict). Ao usar dict(data), 
            # convertemos esse objeto num dicionário padrão do Python para ser mais fácil de usar depois.
            employee_list.append(dict(data))
            
    return employee_list

def process_data(employee_list):
    """
    Objetivo: Contar quantos funcionários existem em cada departamento.
    """
    # Criamos uma lista para guardar apenas os nomes dos departamentos.
    department_list = []
    for employee_data in employee_list:
        # Acedemos à chave 'Department' de cada dicionário na lista.
        department_list.append(employee_data['Department'])
    
    department_data = {}
    # O set(department_list) remove nomes repetidos. Se "Sales" aparece 3 vezes, 
    # o set transforma-o em apenas 1 para não contarmos o mesmo setor várias vezes.
    for department_name in set(department_list):
        # Aqui, contamos quantas vezes esse nome aparece na lista original e guardamos no dicionário.
        department_data[department_name] = department_list.count(department_name)
        
    return department_data

def write_report(dictionary, report_file):
    """
    Objetivo: Criar o ficheiro de texto final com o relatório.
    """
    # Abrimos o ficheiro em modo 'w' (escrita). Se já existir, ele será substituído.
    with open(report_file, "w") as f:
        # O sorted() garante que os departamentos apareçam por ordem alfabética (A-Z).
        for k in sorted(dictionary):
            # 4. Explicando melhor a escrita: f.write(str(k) + ':' + str(dictionary[k]) + '\n')
            # k = a chave (Nome do Departamento, ex: "Sales")
            # dictionary[k] = o valor associado à chave (Quantidade, ex: 3)
            # O str() garante que números sejam tratados como texto para podermos "colar" tudo.
            # O '\n' é essencial: ele diz ao computador para saltar para a linha seguinte.
            """ f.write(str(k) + ':' + str(dictionary[k]) + '\n') """
            f.write(f"{k}: {dictionary[k]}\n")

# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    # Estas linhas garantem que o script procure o ficheiro na mesma pasta onde o script está guardado,
    # evitando o erro de "Ficheiro não encontrado" que viste no terminal.
    diretorio_do_script = os.path.dirname(__file__)
    caminho_csv = os.path.join(diretorio_do_script, 'employees.csv')
    caminho_report = os.path.join(diretorio_do_script, 'report.txt')

    try:
        # Passo 1: Ler o CSV e criar a lista
        lista_de_dados = read_employees(caminho_csv)
        
        # Passo 2: Processar essa lista para contar os departamentos
        contagem_final = process_data(lista_de_dados)
        
        # Passo 3: Gravar os resultados no ficheiro report.txt
        write_report(contagem_final, caminho_report)
        
        print(f"✔ Sucesso! Relatório gerado em: {caminho_report}")
        
    except FileNotFoundError:
        print(f"❌ Erro: Não encontrei o ficheiro '{caminho_csv}' na pasta correta.")