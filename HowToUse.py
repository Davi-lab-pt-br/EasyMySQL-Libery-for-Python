from EasyMySQL import *

# Criando a conexão
connect = Conectar()

# Criando o cursor
cursor = CURSOR()

# Comando SQL
command = 'INSERT INTO bdyoutube.vendas_dois (nome, valor) VALUES ("coco", 2)'

# Executando o comando
cursor.execute_command(command)

# Lembre-se de commit se necessário
cursor.connexion.commit()
