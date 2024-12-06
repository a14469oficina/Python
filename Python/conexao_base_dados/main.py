import sqlite3
import hashlib

def create_conn():
    connection = sqlite3.connect("user.db")
    cursor = connection.cursor()
    #Crear Tabela
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL 
        )"""
    )
    #Unique é unico
    connection.commit()#só quando queremos alterar ou inserir ou apagar alguma coisa
    connection.close()
#Receber a password e retorna-la encriptada
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


#verificar se a password que eu digitei é igual a password encriptada que esta na base de dados
def verify_pasword(stored_password,password):
    return stored_password == hash_password(password)

def insert_user(nome,username,senha,mail):
    connection = sqlite3.connect("user.db")
    cursor = connection.cursor()
    senha_encriptada = hash_password(senha)

    try:
        cursor.execute(
            """
              INSERT INTO users(nome,username,password,email)
              VALUES(?,?,?,?)
            """,
            (nome,username,senha_encriptada,mail)
        )
        connection.commit()
        print("Utilizador inserido com sucesso")
    except sqlite3.IntegrityError as e:
        print(f"Erro ao inserir o utilizador: {e}")
    finally:
        connection.close()

def list_users():
    connection = sqlite3.connect("user.db")
    cursor = connection.cursor()
    cursor.execute("SELECT id,nome,username,password,email FROM users")
    users = cursor.fetchall()

    for user in users:
        print(user)

    connection.close()

def find_by_username(username):
    connection = sqlite3.connect("user.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id,nome,username,email,password FROM users WHERE username =?"
    )
    user= cursor.fetchone()

    if user: #se o utilizador existir
        print("Utilizador encontrado")
        print(user[:4])#Mostra informações do utilizador sem a senha
        return user
    else:
        print("Utilizador não encontrado")
        return None
    
    connection.close()

def authenticate_user(username,password):
    user = find_by_username(username)
    if user:
        stored_password = user[4]
        if verify_pasword(stored_password,password):
            print("Autenticação bem sucedida")
        else:
            print("Autenticação falhou! Utilizador/Password incorretas")
    
if __name__ == "__main__":
    #Criar a base de dados e a tabela
    create_conn()