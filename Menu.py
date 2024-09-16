# Importa as classes necessárias do módulo ArquivoCSV, Cadastro, Login e Log
from ArquivoCSV import ArquivoCSV
from Cadastro import Cadastro
from Login import Login
from Log import Log

class Menu:    
    
    def __init__(self):
        # Instancia um objeto ArquivoCSV para manipular o arquivo de cadastro de usuários
        self.arquivoCSVCadastro = ArquivoCSV('cadastroUsuarios.csv')
        # Instancia um objeto ArquivoCSV para manipular o arquivo de registo de log
        self.arquivoCSVLog = ArquivoCSV('log.csv')
    
    
    def mostrar_menu(self):
        # Mostra as opções do menu na tela
        print("Para entrar, digite:")
        print("1. Fazer login")
        print("2. Se não é cadastrado")
        print("3. Mostrar usuários cadastrados")
        print("4. Ver log")
        print("5. Sair")
    
    def opcao_escolhida(self):
        # Instancia um objeto Log para registar eventos no log
        instanciaObjetoLog = Log()  

        # Loop para mostrar o menu continuamente e permitir ao usuário escolher uma opção
        while True:
            # Mostra o menu na tela
            self.mostrar_menu()
            # Solicita ao usuário que escolha uma opção
            opcao = input("Opção: ")
            
            # Verifica qual opção o usuário escolheu e executa a ação correspondente
            if opcao == "1":
                # Instancia um objeto Login para lidar com o processo de login
                instanciaObjetoLogin = Login()
                # Chama o método para validar o login do usuário
                instanciaObjetoLogin.validar_login()
                
            elif opcao == "2":
                # Instancia um objeto Cadastro para lidar com o processo de cadastro de novos usuários
                instanciaObjetoCadastro = Cadastro()
                # Chama o método para validar e cadastrar um novo usuário
                instanciaObjetoCadastro.validar_cadastro()
                
            elif opcao == "3":
                # Instancia um objeto Cadastro para lidar com a exibição dos usuários cadastrados
                instanciaObjetoCadastro = Cadastro()
                # Chama o método para mostrar os usuários cadastrados
                instanciaObjetoCadastro.mostrar_usuarios_cadastrados()
                
            elif opcao == "4":
                # Chama o método para mostrar o log na tela
                instanciaObjetoLog.mostrar_log()
                
            elif opcao == "5":
                # Chama o método para registar a saída do usuário no log
                instanciaObjetoLog.log_saida("usuario") 
                print("Fim")
                break
            
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

# Verifica se o código está sendo executado como o programa principal
if __name__ == "__main__":
    # Instancia um objeto Menu para gerenciar o menu e as opções do programa
    instanciaObjetoMenu = Menu()
    # Chama o método para permitir ao usuário escolher uma opção
    instanciaObjetoMenu.opcao_escolhida()
