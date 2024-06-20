from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime


def disparando_email_proatividade(email_destinatario, nome, linha, assunto):

    try:

        print(f"[{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] Iniciando aplicação - Disparo de Proatividade")

        corpo_email = f"Olá, {nome}!\nTeste:\n{linha}\n\nTeste"

        # Caminho para o chromedriver na mesma pasta do arquivo .py
        driver = webdriver.Chrome()

        driver.get("[insira a aplicação que será aberta]")
        
        print(f"[{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] Sistema foi aberto")

        # Encontra o campo de usuário pelo ID e digita o nome de usuário
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[1]/label/div/div/div/input"))
        )
        
        username_field.send_keys("[insira o usuario]")

        # Encontra o campo de senha pelo ID e digita a senha

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[2]/label/div/div/div/input"))
        )
        password_field.send_keys("[insira a senha]")

        # Opcionalmente, envia o formulário pressionando Enter
        password_field.send_keys(Keys.RETURN)


        print(f"[{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] Logado com sucesso")

        # Espera até que o elemento esteja presente e clicável, até um máximo de 10 segundos
        passo1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[6]/a/div[2]/i"))
        )

        time.sleep(3)

        passo1.click()

        passo2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[1]/div[1]/div[2]/div[3]/button/span[2]/i"))
        )

        # Clica no elemento
        passo2.click()

        passo3 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div"))
        )

        # Clica no elemento
        passo3.click()

        conteudo_assunto = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[3]/div/div/div/div[1]/div[1]/label[2]/div/div/div[2]/input"))
        )
        conteudo_assunto.send_keys(assunto)

        conteudo_email_destinatario = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[3]/div/div/div/div[1]/div[1]/label[3]/div/div/div[2]/div/input"))
        )
        conteudo_email_destinatario.send_keys(email_destinatario)

        conteudo_email_destinatario.send_keys(Keys.ENTER)

        conteudo_disparo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/p[1]"))
        )
        conteudo_disparo.send_keys(corpo_email)

        time.sleep(3)

        passo7 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[3]/div/div/div/div[3]/div/div/button[1]"))
        )

        # Clica no elemento
        passo7.click()

        time.sleep(3)

        # Fecha o navegador
        driver.quit()

        print(f"[{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] Finalizando aplicação - Proatividade do email: {email_destinatario} realizado")

        return "enviado"
    
    except Exception as e:

        return f"Erro: Ocorreu um problema inesperado. {str(e)}"
    

def disparando_email_quebra(email_destinatario, nome, linha, assunto):

    try:

        print(f"[{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] Iniciando aplicação - Disparo de Proatividade")

        corpo_email = f"Olá, {nome}!\nteste:\n{linha}\n\nteste"

        # Caminho para o chromedriver na mesma pasta do arquivo .py
        driver = webdriver.Chrome()

        driver.get("[insira a aplicação que será aberta]")
        
        print(f"[{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] Sistema foi aberto")

        # Encontra o campo de usuário pelo ID e digita o nome de usuário
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[1]/label/div/div/div/input"))
        )
        
        username_field.send_keys("[insira o usuário]")

        # Encontra o campo de senha pelo ID e digita a senha

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[2]/label/div/div/div/input"))
        )
        password_field.send_keys("[insira a senha]")

        # Opcionalmente, envia o formulário pressionando Enter
        password_field.send_keys(Keys.RETURN)


        print(f"[{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] Logado com sucesso")

        # Espera até que o elemento esteja presente e clicável, até um máximo de 10 segundos
        passo1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[6]/a/div[2]/i"))
        )

        time.sleep(3)

        passo1.click()

        passo2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[1]/div[1]/div[2]/div[3]/button/span[2]/i"))
        )

        # Clica no elemento
        passo2.click()

        passo3 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div"))
        )

        # Clica no elemento
        passo3.click()

        conteudo_assunto = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[3]/div/div/div/div[1]/div[1]/label[2]/div/div/div[2]/input"))
        )
        conteudo_assunto.send_keys(assunto)

        conteudo_email_destinatario = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[3]/div/div/div/div[1]/div[1]/label[3]/div/div/div[2]/div/input"))
        )
        conteudo_email_destinatario.send_keys(email_destinatario)

        conteudo_email_destinatario.send_keys(Keys.ENTER)

        conteudo_disparo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/p[1]"))
        )
        conteudo_disparo.send_keys(corpo_email)

        time.sleep(3)

        passo7 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[3]/div/div/div/div[3]/div/div/button[1]"))
        )

        # Clica no elemento
        passo7.click()

        time.sleep(3)

        # Fecha o navegador
        driver.quit()

        print(f"[{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}] Finalizando aplicação - Quebra de acordo do email: {email_destinatario} realizado")

        return "enviado"
    
    except Exception as e:

        return f"Erro: Ocorreu um problema inesperado. {str(e)}"
