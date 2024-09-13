import pyautogui
from time import sleep


# 1- clicar e digitar o meu usuario
pyautogui.click(963,542,duration=2)
pyautogui.write('eduardo')

# 2- clicar e digitar minha senha
pyautogui.click(968,575,duration=2)
pyautogui.write('123456')

# 3- clicar em entrar
pyautogui.click(845,618,duration=2)

# 4- extrair cada produto
with open('produtos.txt', 'r') as file:
    for linha in file:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        
        # 1- clicar e digitar produto
        pyautogui.click(629,525,duration=2)
        pyautogui.write(produto)
        
        # 2- clicar e digitar quantidada
        pyautogui.click(630,557,duration=2)
        pyautogui.write(quantidade)
        
        # 3- clicar e digitar o preco   
        pyautogui.click(627,591,duration=2)
        pyautogui.write(preco)
        
        # 4- clicar em registrar
        pyautogui.click(500,782,duration=1)
        sleep (1)