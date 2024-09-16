# Importa o módulo csv para manipulação de arquivos CSV
import csv

class ArquivoCSV:
    
    def __init__(self, nomeArquivo):
        # Inicializa o objeto ArquivoCSV com o nome do arquivo fornecido
        self.nomeArquivo = nomeArquivo
    
    #Lê os dados do arquivo CSV
    def ler_dados(self):
        
        # Abre o arquivo no modo leitura ('r') e usa o módulo csv para ler os dados
        with open(self.nomeArquivo, 'r', newline='') as file:
            # Cria um leitor CSV
            reader = csv.reader(file)
            # Converte os dados lidos em uma lista e retorna
            return list(reader)
        
    #Salva os dados no arquivo CSV
    def salvar_dados(self, dados):
        
        # Abre o arquivo no modo append ('a') para adicionar dados ao final do arquivo
        with open(self.nomeArquivo, 'a', newline='') as file:
            # Cria um escritor CSV
            writer = csv.writer(file)
            # Escreve os dados fornecidos no arquivo CSV
            writer.writerow(dados)
