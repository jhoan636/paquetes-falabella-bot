from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)

bot.get("https://www.viajesfalabella.com.co/")
time.sleep(2)
bot.maximize_window()
time.sleep(2)

saliendo = bot.find_element(By.XPATH, "/html/body/app-root/div/header-wrapper/header-view-1/div/div/sbox/div/div/searchbox-v2/div/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div/div/input")
time.sleep(2)
saliendo.send_keys("Aeropuerto Internacional Jose Maria Cordova, Medellín, Colombia")

time.sleep(2)
destino = bot.find_element(By.XPATH, "/html/body/app-root/div/header-wrapper/header-view-1/div/div/sbox/div/div/searchbox-v2/div/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/input")
time.sleep(2)
destino.send_keys("Aeropuerto Reina Beatrix, Aruba, Aruba")
time.sleep(2)

destino.send_keys(Keys.ENTER)

fecha_ida = bot.find_element(By.XPATH, "/html/body/app-root/div/header-wrapper/header-view-1/div/div/sbox/div/div/searchbox-v2/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/input")
time.sleep(2)
fecha_ida.send_keys("2025-06-29")
time.sleep(2)

fecha_vuelta = bot.find_element(By.XPATH, "/html/body/app-root/div/header-wrapper/header-view-1/div/div/sbox/div/div/searchbox-v2/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/input")
time.sleep(2)
fecha_vuelta.send_keys("2025-07-21")
time.sleep(2)
