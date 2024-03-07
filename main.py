#  Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa.

import pyautogui
import time

pyautogui.PAUSE = 1.5 #Pause de 0.5 segundos em todo o código.
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 tecla do teclado.
# pyautogui.hotkey ("ctrl", "c") -> combinação de teclas

# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=675, y=590)

# Acessar o sistema da empresa
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)
print(pyautogui.position())


# Dar uma pausa um pouco maior (3 segundos) num bloco específico.
#time.sleep(3) #3 segundos de pausa neste bloco específico entre acessar o sistema e fazer o login (digitar email e senha)
#print(pyautogui.position())

#Passo 2: Fazer o Login.
# pyautogui.click(x=-1368, y=378)
# email = "teste@teste.com"
# pyautogui.write(email)
# pyautogui.click(x=-1377, y=478)
# senha = "senha123"
# pyautogui.write(senha)
# pyautogui.click(x=-1142, y=530)





# Passo 3: Importar a base de dados
# Passo 4: Cadastrar um produto.
# Passo 5: Repetir o processo de cadastro até acabar a base de dados.
