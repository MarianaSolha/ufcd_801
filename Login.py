from ArquivoCSV import ArquivoCSV
from Log import Log

class Login:
    
    def __init__(self):
        # Inicializa o objeto Login com um objeto ArquivoCSV para manipulação do arquivo de cadastro e um objeto Log para registo de eventos
        self.arquivoCSVCadastro = ArquivoCSV('cadastroUsuarios.csv')
        self.log = Log()  # Instância da classe Log para registo de eventos

    #Valida o login do usuário.
    def validar_login(self):
        
        # Solicita ao usuário que insira o email e a senha para login
        email = input("Insira seu email: ")
        senha = input("Insira sua senha: ")
        
        # Lê os dados do arquivo de cadastro
        dados = self.arquivoCSVCadastro.ler_dados()        
        # Itera sobre os dados para verificar se o email e a senha correspondem a algum registo no arquivo de cadastro
        for linha in dados:
            if linha[0] == email and linha[1] == senha:
                print("Login efetuado.")
                # Regista o evento de login no log
                self.log.log_login(email)  
                return
        # Caso não encontre correspondência, exibe mensagem de erro
        print("Email e/ou senha inválidos.")
