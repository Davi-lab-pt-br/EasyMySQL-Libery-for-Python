from EasyMySQL import *

# Criando a conexão
connect = Connect()

# Criando o cursor
cursor = CURSOR()

# Comando SQL
command = 'INSERT INTO bdyoutube.vendas_dois (name, value) VALUES ("Soda can", $4.50)'

# Running the command
cursor.execute_command(command)

# Remember, the commit is necessary
cursor.Connection.commit()

connect.Connection.close()
cursor.close()
