# Passo a passo do seu programa
# pip install pyautogui
# Passo 1 : Entrar no sistema da Empresa
# Passo 2 : Faze login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos;

   
import pyautogui
import time 


# Teclas e atalhos dessa função
# pyautogui.click   

# pyautogui.write
# pyautogui.press >> aperta uma tecla
# pyautogui.horkey >> aperta um atalho (hotkey)

pyautogui.PAUSE= 1
# Passo 1 : Entrar no sistema da Empresa
#abriria o navegador
pyautogui.press("win")
pyautogui.write("Microsoft Edge")
pyautogui.press("enter")

# acessar o site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa menor
time.sleep(3)

# Passo 2 : Faze login
# clicar no campo de email
# pegou a localização do mouse e teclado com pyautogui
pyautogui.click(x=397, y=988)
pyautogui.write("pythonimpressionador@gmail.com")
# para passar para o próximo campo de inuput vou clicar a tecla
pyautogui.press("tab")
pyautogui.write("developer2025#")
pyautogui.press("tab") # passar para proximo botão
pyautogui.press("enter") # passar para proximo botão
#fazer uma pausa até carregar
time.sleep(3)

# Passo 3: Abrir a base de dados (importar o arquivo)
# ferramenta para trabalhar com base de dados: Pandas
#pip install pandas openpyxl
import pandas

table = pandas.read_csv("produtos.csv")
print(table)

#para cada linha de cada tabela todas essas linhas abaixo

for linha in table.index:
    # Passo 4: Cadastrar um produto

    #codigo
    pyautogui.click(x=331, y=707) # clicar no campo do código
    codigo= str(table.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") # passar para o proximo campo
    #marca
    marca= str(table.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo= str(table.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria= str(table.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preço
    preco= str(table.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    #custo
    custo= str(table.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #obs
    obs= str(table.loc[linha, "obs"])
    #se a observação não for o texto Nan então escreve observação
    if obs != "nan":  
        pyautogui.write(obs)
    pyautogui.press("tab")# passa pro botao enviar

    pyautogui.press("enter")
    #voltar para o inicio da tela
    
    pyautogui.scroll(5000)

#Passo 5: Repetir o passo 4 até acabar a lista de produtos;







  