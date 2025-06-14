from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

service = Service("driver/chromedriver.exe")

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
bot = webdriver.Chrome(service=service, options=options)

bot.get("https://www.viajesfalabella.com.co/")
time.sleep(15)
bot.maximize_window()
time.sleep(2)

saliendo = bot.find_element(By.XPATH, "/html/body/app-root/div/header-wrapper/header-view-1/div/div/sbox/div/div/searchbox-v2/div/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/div/div/input")
time.sleep(2)
saliendo.clear()
time.sleep(2)
saliendo.send_keys("Aeropuerto Internacional Jose Maria Cordova, Medellín, Colombia")

time.sleep(2)
destino = bot.find_element(By.XPATH, "/html/body/app-root/div/header-wrapper/header-view-1/div/div/sbox/div/div/searchbox-v2/div/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/input")
time.sleep(2)
destino.clear()
time.sleep(2)
destino.send_keys("Aeropuerto Reina Beatrix, Aruba, Aruba")
time.sleep(2)

# fechas de viaje
fecha_ida = bot.find_element(By.XPATH, "/html/body/app-root/div/header-wrapper/header-view-1/div/div/sbox/div/div/searchbox-v2/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/input")
time.sleep(2)
fecha_ida.send_keys("2025-06-29")
time.sleep(2)

fecha_vuelta = bot.find_element(By.XPATH, "/html/body/app-root/div/header-wrapper/header-view-1/div/div/sbox/div/div/searchbox-v2/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/div/input")
time.sleep(2)
fecha_vuelta.send_keys("2025-07-21")
time.sleep(2)

# Numero de habitaciones
habitaciones = bot.find_element(By.XPATH, "/html/body/app-root/div/header-wrapper/header-view-1/div/div/sbox/div/div/searchbox-v2/div/div/div/div/div/div/div/div[2]/div[1]/div[3]/div/div/div/div[1]/input")
time.sleep(2)
habitaciones.click
time.sleep(2)


# Numero de mayores 4
mayores = bot.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div/button[2]")
time.sleep(2)
acciones = ActionChains(bot)
acciones.double_click(mayores).perform()
time.sleep(2)

# agrega habitacion con 2 mayores
habitacion = bot.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[2]/button[1]")
time.sleep(2)
habitacion.click
time.sleep(2)

# Numero de mayores 2
mayoresdos= bot.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div/button[2]")
time.sleep(2)

# aplicar busqueda 

aplicar = bot.find_element(By.XPATH, "/html/body/div[4]/div[2]/div/div/div[3]/button[2]")
time.sleep(2)
aplicar.click()
time.sleep(5)