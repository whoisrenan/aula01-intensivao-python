#  Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa.

import pyautogui
import time

pyautogui.PAUSE = 0.5 #Pause de 0.5 segundos em todo o código.
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 tecla do teclado.
# pyautogui.hotkey ("ctrl", "c") -> combinação de teclas

# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


# Acessar o sistema da empresa
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")


# Dar uma pausa um pouco maior (3 segundos) num bloco específico.
time.sleep(3) #3 segundos de pausa neste bloco específico entre acessar o sistema e fazer o login (digitar email e senha)

# Passo 2: Fazer o Login.




# Passo 3: Importar a base de dados
# Passo 4: Cadastrar um produto.
# Passo 5: Repetir o processo de cadastro até acabar a base de dados.
