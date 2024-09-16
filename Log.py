# Importa a classe ArquivoCSV do módulo ArquivoCSV para manipulação de arquivos CSV
from ArquivoCSV import ArquivoCSV
# Importa o módulo time para manipulação de data e hora
import time

class Log:
    
    def __init__(self):
        # Inicializa o objeto Log com um objeto ArquivoCSV para manipulação do arquivo de log
        self.arquivoCSVLog = ArquivoCSV('log.csv')
        
    #Regista a entrada de um usuário
    def log_entrada(self, usuario):
        
        # Cria a mensagem de log para entrada do usuário
        mensagem = "Usuário " + usuario + " entrou no sistema."
        # Chama o método para registar a mensagem no arquivo de log
        self.registar_log(mensagem)
        
    #Regista a saída de um usuário
    def log_saida(self, usuario):
        
        # Cria a mensagem de log para saída do usuário
        mensagem = "Usuário " + usuario + " saiu do sistema."
        # Chama o método para registar a mensagem no arquivo de log
        self.registar_log(mensagem)

    #Regista o login de um usuário
    def log_login(self, usuario):
        
        # Cria a mensagem de log para login do usuário
        mensagem = "Usuário " + usuario + " realizou login."
        # Chama o método para registar a mensagem no arquivo de log
        self.registar_log(mensagem)

    #Regista o cadastro de um usuário
    def log_cadastro(self, usuario):
        
        # Cria a mensagem de log para cadastro do usuário
        mensagem = "Usuário " + usuario + " foi cadastrado."
        # Chama o método para registar a mensagem no arquivo de log
        self.registar_log(mensagem)
        
    #Registra uma mensagem no arquivo de log
    def registar_log(self, mensagem):
        
        # Obtém a data e hora atual
        data_hora = time.strftime('%Y-%m-%d %H:%M:%S')
        # Salva a mensagem de log junto com a data/hora no arquivo de log
        self.arquivoCSVLog.salvar_dados([data_hora, mensagem])
        
    #Mostra o conteúdo do arquivo de log
    def mostrar_log(self):
  
        # Lê os dados do arquivo de log
        dados = self.arquivoCSVLog.ler_dados()
        # Verifica se há registos no log
        if not dados:
            # Se não houver registos, exibe uma mensagem informando
            print("Nenhum registo no log.")
        else:
            # Se houver registos, exibe cada registo no log com a data/hora e a mensagem
            print("Registos no log:")
            for linha in dados:
                print("Data/Hora:", linha[0], "- Mensagem:", linha[1])
