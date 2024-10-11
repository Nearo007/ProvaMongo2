from pymongo import MongoClient
import json

# Conexão com MongoDB Atlas
client = MongoClient('mongodb+srv://Nearo:leandroDB@cluster0.kcsg9.mongodb.net/')

# Seleção do banco de dados e coleções
db = client['GerenciarSkills']
collectionFuncionarios = db['funcionarios']

# Carregar o arquivo JSON corretamente
with open('data/funcionarios.json', 'r', encoding='utf-8') as arquivo_json:
    documents = json.load(arquivo_json)

# Criar uma lista para armazenar os documentos formatados
documentsFuncionariosDict = []

# Iterar sobre cada funcionário no JSON
for funcionario in documents:
    # Adicionar os campos necessários para cada funcionário
    funcionario_dict = {
        '_id': funcionario['ID'],  # Usando 'ID' do JSON como _id no MongoDB
        'Nome_Funcionario': funcionario['Nome_Funcionario'],
        'Cargo': funcionario['Cargo'],
        'Departamento_ID': funcionario['Departamento_ID']
    }
    # Adicionar o dicionário à lista
    documentsFuncionariosDict.append(funcionario_dict)

# Inserir os documentos na coleção
collectionFuncionarios.insert_many(documentsFuncionariosDict)

print("Funcionários inseridos com sucesso!")




"""collectionDepartamentos.insert_many(documents)
collectionHabilidades.insert_many(documents)
collectionFuncionariosHabilidades.insert_many(documents)
collectionCertificacoes.insert_many(documents)
collectionProjetos.insert_many(documents)"""