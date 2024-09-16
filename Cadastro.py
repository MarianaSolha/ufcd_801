# Importa a classe ArquivoCSV do módulo ArquivoCSV para manipulação de arquivos CSV
from ArquivoCSV import ArquivoCSV
# Importa a classe Log do módulo Log para registar eventos no log
from Log import Log  

class Cadastro:
    
    def __init__(self):
        # Inicializa o objeto Cadastro com um objeto ArquivoCSV para manipulação do arquivo de cadastro e um objeto Log para registo de eventos
        self.arquivoCSVCadastro = ArquivoCSV("cadastroUsuarios.csv")
        self.log = Log()  # Instância da classe Log para registo de eventos
        
    #Valida e cadastra o usuário
    def validar_cadastro(self):
        
        while True:
            # Valida o email e a senha inseridos pelo usuário
            emailValido = self.validar_email()
            senhaValida = self.validar_senha()
            
            # Verifica se o email e a senha são válidos
            if emailValido and senhaValida:
                # Verifica se o email já está cadastrado
                if not self.verificar_email_cadastrado(emailValido):
                    # Salva os dados de cadastro (email e senha) no arquivo CSV
                    self.arquivoCSVCadastro.salvar_dados([emailValido, senhaValida])
                    print("Cadastro realizado com sucesso.")
                    # Regista o evento de cadastro no log
                    self.log.log_cadastro(emailValido)  
                    break
                else:
                    print("Email já cadastrado.")
            else:
                print("Email ou senha inválidos.")
                
    #Valida o email inserido
    def validar_email(self):
        
        while True:
            email = input("Insira um email (entre 8 e 12 caracteres e @): ")
            if '@' in email and 8 <= len(email.split('@')[0]) <= 12:
                return email
            else:
                print("Email inválido. Verifique se ele possui '@' e tem entre 8 e 12 caracteres.")
    #Valida a senha inserida
    def validar_senha(self):
        
        while True:
            senha = input("Insira sua senha (Mínimo 6 caracteres): ")
            if len(senha) >= 6:
                return senha
            else:
                print("Senha inválida. Deve ter pelo menos 6 caracteres.")

    #Verifica se o email já está cadastrado
    def verificar_email_cadastrado(self, email):

        dados = self.arquivoCSVCadastro.ler_dados()
        for linha in dados:
            if linha[0] == email:
                return True
        return False
    
    #Mostra os usuários cadastrados
    def mostrar_usuarios_cadastrados(self):
        
        dados = self.arquivoCSVCadastro.ler_dados()
        if not dados:
            print("Nenhum usuário cadastrado.")
        else:
            print("Usuários cadastrados:")
            for linha in dados:
                print("Email:", linha[0])
