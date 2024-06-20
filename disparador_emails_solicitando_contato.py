import pandas as pd
import automacao_emails_solicitando_contato as auto_email
import time
from datetime import datetime, timedelta

# Função para simular o envio de email
def enviar_emails(emails):
    resultados = []
    resultado_email = auto_email.interagir_automacao(emails)
    for email in emails:
        resultados.append(resultado_email)
    return resultados

# Carregar o arquivo CSV com o separador ';'
df = pd.read_csv('[insira o caminho do arquivo base com extensão .csv]', sep=';')

# Função principal para processar os emails em lotes de 10
def processar_emails(df):
    while True:
        # Verificar quantos emails com status "sem disparo" existem
        emails_com_erro_count = df[(df['status'] != 'enviado') & (df['status'] != 'sem disparo')].shape[0]
        emails_enviados_count = df[df['status'] == 'enviado'].shape[0]
        emails_pendentes_count = df[df['status'] == 'sem disparo'].shape[0]
        print("========================================================================================")
        print(f"Horário de verificação: [{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}]")
        print(f"Emails enviados: {emails_enviados_count}")
        print(f"Emails pendentes: {emails_pendentes_count}")
        print(f"Emails com status de erro: {emails_com_erro_count}")
        print("========================================================================================")
        
        if emails_pendentes_count == 0:
            print(f"[{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] Todos os emails foram processados.")
            break
        
        # Selecionar os primeiros 10 emails com status "sem disparo"
        emails_pendentes = df[df['status'] == 'sem disparo'].head(300)
        email_list = emails_pendentes['email'].tolist()
        
        # Enviar a lista de emails e obter os resultados
        resultados = enviar_emails(email_list)
        
        # Atualizar o DataFrame com os novos status
        for index, resultado in zip(emails_pendentes.index, resultados):
            df.at[index, 'status'] = resultado

        # Salvar as atualizações no arquivo CSV
        df.to_csv('[insira o caminho de destino do arquivo com extensão .csv]', sep=';', index=False)

# Executar o processamento dos emails
processar_emails(df)