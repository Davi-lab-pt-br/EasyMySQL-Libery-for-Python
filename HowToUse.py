from EasyMySQL import *

# Criando a conexão
connect = Connect()

# Criando o cursor
cursor = CURSOR()

# Comando SQL
command = 'INSERT INTO bdyoutube.vendas_dois (name, value) VALUES ('Soda can', $4.50)'

# Executando o comando
cursor.execute_command(command)

# Lembre-se de commit se necessário
cursor.connexion.commit()
