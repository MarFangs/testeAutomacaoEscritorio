import selenium
import time
import os
import datetime
### Adicionar no futuro classe para colocar info de login e privar as informações
acessoUser = "Marceloeduardo"
acessoSenha = "prazo"
elementosPaginaRelatorio = []
ontem = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%d/%m/%Y")

### Topico a se debater: Colocar um menu para selecionar o tipo de relatório ou puxar tudo de uma vez só?

def relatorioAuto():
    print('iniciando automação')
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.edge.service import Service
    ### separando linhas de uso ###
    service = Service(r"D:\PASSAR PARA PENDRIVE\TESTE PYTHON\webdriver\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.maximize_window()
    driver.get("https://ribeiroandrade.elawio.com.br/main")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Email"))).send_keys(acessoUser)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Senha"))).send_keys(acessoSenha)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-bricky.pull-right").click()
    ### Acessar Modulo de Relatório, Prazos###
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID ,"linkModuloRelatorio")))
    driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "linkModuloRelatorio"))
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    trocaAba = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[href="#tab_6"]')))
    driver.execute_script("arguments[0].click();", trocaAba)
    botaoGerarRelatorio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.tab-pane.active button.btn.btn-danger')))
    driver.execute_script("arguments[0].click();", botaoGerarRelatorio)
    driver.find_element(By.ID, "buttonMarcaDesmarcaColunas").click() # clica para desmarcar todas as colunas
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'CheckCol_NPC')))
    driver.find_element(By.NAME, 'CheckCol_NPC').click() # clica para marcar a coluna de interesse (repetir de acordo com id)
    statusPrazoDD = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'select[name="status"] + div button')))
    driver.execute_script("arguments[0].click();", statusPrazoDD)
    prazoDDConcluido = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[value-"3|Concluido"]')))
    driver.execute_script("arguments[0].click();", prazoDDConcluido)
    driver.find_element(By.NAME, "body").click()
    


    #campoData = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "dataHoraPreenchimento")))
    #campoData.clear()
    #campoData.send_keys(ontem + " - " + ontem) # coloca o filtro de data para o dia anterior
    #driver.find_element(By.XPATH, '//button[text()="Apply"]').click()

    time.sleep(900000) # deixar o site aberto pra analise dos itens no inspecionar
    ### driver.close()

resposta = input('deseja iniciar o processo? (s/n)\n')
if resposta == 's':
    relatorioAuto()
elif resposta == 'n':
    print('processo cancelado')
else:
    print('opção inválida, tente novamente')