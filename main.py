from funcoes import pessoa
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
url = 'enter URL here'


nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
nav.get(url)
sleep(1)

for i in range(1): # Insira dentro do range a quantidade de vezes que o formulario será preenchido
    a = pessoa()
    nav.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(a[0])
    nav.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(a[1])
    nav.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(a[2])
    nav.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(a[3])
    nav.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    nav.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]').click()
