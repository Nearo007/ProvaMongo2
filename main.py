from pymongo import MongoClient
import json

# Conexão com MongoDB Atlas
client = MongoClient('mongodb+srv://Nearo:leandroDB@cluster0.kcsg9.mongodb.net/')

# Seleção do banco de dados e coleções
db = client['GerenciarSkills']
collectionFuncionarios = db['funcionarios']
collectionDepartamentos = db['departamentos']
collectionHabilidades = db['habilidades']
collectionFuncionariosHabilidades = db['funcionarios_habilidades']
collectionCertificacoes = db['certificacoes']
collectionProjetos = db['projetos']

# Carregar o arquivo JSON corretamente
with open('data/funcionarios.json', 'r', encoding='utf-8') as arquivo_json:
    documents = json.load(arquivo_json)

# Criar uma lista para armazenar os documentos formatados
documentsFuncionariosDict = []

# Iterar sobre cada funcionário no JSON
for funcionario in documents:
    # Adicionar os campos necessários para cada funcionário
    funcionario_dict = {
        '_id': funcionario['ID'],
        'Nome_Funcionario': funcionario['Nome_Funcionario'],
        'Cargo': funcionario['Cargo'],
        'Departamento_ID': funcionario['Departamento_ID']
    }
    # Adicionar o dicionário à lista
    documentsFuncionariosDict.append(funcionario_dict)


with open('data/departamentos.json', 'r', encoding='utf-8') as arquivo_json:
    documentsDepartamentos = json.load(arquivo_json)
    
documentsDepartamentosDict = []

for departamento in documentsDepartamentos:
    departamento_dict = {
        '_id': departamento['ID'],
        'Nome_Departamento': departamento['Nome_Departamento']
    }

    documentsDepartamentosDict.append(departamento_dict)

with open('data/habilidades.json', 'r', encoding='utf-8') as arquivo_json:
    documentsHabilidades = json.load(arquivo_json)

documentsHabilidadesDict = []

for habilidade in documentsHabilidades:
    habilidade_dict = {
        '_id': habilidade['ID'],
        'Nome_Habilidade': habilidade['Nome_Habilidade']
    }

    documentsHabilidadesDict.append(habilidade_dict)

with open('data/funcionarios_habilidades.json', 'r', encoding='utf-8') as arquivo_json:
    documentsFuncionariosHabilidades = json.load(arquivo_json)

documentsFuncionariosHabilidadesDict = []

for funcionario_habilidade in documentsFuncionariosHabilidades:
    funcionario_habilidade_dict = {
        'Funcionario_ID': funcionario_habilidade['Funcionario_ID'],
        'Habilidade_ID': funcionario_habilidade['Habilidade_ID'],
        'Nivel': funcionario_habilidade['Nivel']
    }    

    documentsFuncionariosHabilidadesDict.append(funcionario_habilidade_dict)

with open('data/certificacoes.json', 'r', encoding='utf-8') as arquivo_json:
    documentsCertificacoes = json.load(arquivo_json)

documentsCertificacoesDict = []

for certificacao in documentsCertificacoes:
    certificacao_dict = {
        '_id': certificacao['ID'],
        'Nome_Certificacao': certificacao['Nome_Certificacao'],
        'Funcionario_ID': certificacao['Funcionario_ID'],
        'Data_Conclusao': certificacao['Data_Conclusao']
    }

    documentsCertificacoesDict.append(certificacao_dict)

with open('data/projetos.json', 'r', encoding='utf-8') as arquivo_json:
    documentsProjetos = json.load(arquivo_json)

documentsProjetosDict = []

for projeto in documentsProjetos:
    projeto_dict = {
        '_id': projeto['ID'],
        'Nome_Projeto': projeto['Nome_Projeto'],
        'Departamento_ID': projeto['Departamento_ID']
    }

    documentsProjetosDict.append(projeto_dict)

try:
    collectionFuncionarios.insert_many(documentsFuncionariosDict)
    collectionDepartamentos.insert_many(documentsDepartamentosDict)
    collectionHabilidades.insert_many(documentsHabilidadesDict)
    collectionFuncionariosHabilidades.insert_many(documentsFuncionariosHabilidadesDict)
    collectionCertificacoes.insert_many(documentsCertificacoesDict)
    collectionProjetos.insert_many(documentsProjetosDict)

except:
    pass

# Quais são as informações completas sobre o funcionário "Clédson Silva"?
infoUsuario = collectionFuncionarios.find_one({"Nome_Funcionario": "Clédson Silva"})

print("Informações do funcionário 'Clédson Silva':")
print("\n---------------------")
for key, value in infoUsuario.items():

    print(f"{key}: {value}")
print("\n---------------------")

# Quais funcionarios têm nível avançado em alguma habilidade?
advancedSkills = collectionFuncionariosHabilidades.find({"Nivel": "Avançado"})

print("\n---------------------")
for habilidade in advancedSkills:
    # Buscar o funcionário correspondente pelo ID
    funcionario = collectionFuncionarios.find_one({"_id": habilidade['Funcionario_ID']})
    if funcionario:
        # Puxar o nome do funcionário
        nome_funcionario = funcionario['Nome_Funcionario']
        
        # Buscar a habilidade correspondente pelo ID
        habilidade_info = collectionHabilidades.find_one({"_id": habilidade['Habilidade_ID']})
        if habilidade_info:
            nome_habilidade = habilidade_info['Nome_Habilidade']  # Ajuste conforme o nome do campo
        else:
            nome_habilidade = "Habilidade não encontrada"
        
        print(f"Funcionario: {nome_funcionario}")
        print(f"Habilidade: {nome_habilidade}")
        print(f"Nível: {habilidade['Nivel']}")
        print("---------------------")
    else:
        print(f"Funcionário com ID {habilidade['Funcionario_ID']} não encontrado.")

try:
    # Adicionar um funcionário novo respeitando os campos presentes na tabela.
    collectionFuncionarios.insert_one({
        "_id": 4,
        "Nome_Funcionario": "Leonardo Castor",
        "Cargo": "Developer Sênior Python",
        "Departamento_ID": 1
    })

    collectionFuncionariosHabilidades.insert_one({
        "Funcionario_ID": 4,
        "Habilidade_ID": 1,
        "Nivel": "Avançado"
    })

    collectionCertificacoes.insert_one({
        "_id": 4,
        "Nome_Certificacao": "Certificação Python",
        "Funcionario_ID": 4,
        "Data_Conclusao": "2023-10-11"
    })

    collectionProjetos.insert_one({
        "_id": 4,
        "Nome_Projeto": "Projeto de Gerencimento de API REST",
        "Departamento_ID": 1
    })

except:
    pass

# Atualize o valor de um determinado funcionário para uma habilidade específica.
collectionFuncionariosHabilidades.update_one(
    {"Funcionario_ID": 2, "Habilidade_ID": 2},
    {"$set": {"Nivel": "Iniciante"}}
)

print("Funcionário atualizado com sucesso!\n")

todosFuncionarios =collectionFuncionariosHabilidades.find()

for funcionario in todosFuncionarios:
    # Buscar o nome do funcionário pelo ID
    funcionario_info = collectionFuncionarios.find_one({"_id": funcionario['Funcionario_ID']})
    if funcionario_info:
        nome_funcionario = funcionario_info['Nome_Funcionario']
    else:
        nome_funcionario = "Funcionário não encontrado"

    # Buscar o nome da habilidade pelo ID
    habilidade_info = collectionHabilidades.find_one({"_id": funcionario['Habilidade_ID']})
    if habilidade_info:
        nome_habilidade = habilidade_info['Nome_Habilidade']  # Ajuste conforme o nome do campo
    else:
        nome_habilidade = "Habilidade não encontrada"

    # Imprimir os detalhes
    print(f"Funcionário: {nome_funcionario}, Habilidade: {nome_habilidade}, Nível: {funcionario['Nivel']}")