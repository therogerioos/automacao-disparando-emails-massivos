import pandas as pd
import automacao_emails_proatividade_e_quebra as auto_email
from datetime import datetime

# Carregar o arquivo CSV com o separador ';'
df = pd.read_csv('[insira o caminho do arquivo .csv]', sep=';', encoding='latin-1')

num_linhas = df['Acao'].count()

# Assuntos definidos para cada ação
assunto_proatividade = "insira o assunto"
assunto_quebra = "insira o assunto"

# Adicionar a coluna 'status' ao DataFrame, se ainda não existir
if 'status' not in df.columns:
    df['status'] = 'Em Tratamento'

# Looping através de cada linha do DataFrame
for index, row in df.iterrows():
    nome = row['PrimeiroNome']
    email = row['Email1']
    linha_digitavel = row['Linha Digitavel']
    acao = row['Acao']

    disparando = index + 1

    progresso = (disparando/num_linhas) * 100

    if isinstance(progresso, (int, float)):
        print(f"Disparo: {disparando} de {num_linhas} - Progresso: {progresso:.2f}%")
    else:
        print(f"Disparo: {disparando} de {num_linhas}")
    
    if acao == "Proatividade":
        status = auto_email.disparando_email_proatividade(email, nome, linha_digitavel, assunto_proatividade)
    elif acao == "Quebra":
        status = auto_email.disparando_email_quebra(email, nome, linha_digitavel, assunto_quebra)
    else:
        status = "Ação desconhecida"  # Caso a ação não seja reconhecida

    # Atualiza a coluna 'status' da linha atual
    df.loc[index, 'status'] = status

    # Salvar as atualizações no arquivo CSV
    df.to_csv('[insira o caminho de destino do arquivo .csv]', sep=';', index=False)