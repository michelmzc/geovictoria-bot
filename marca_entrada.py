import os
from dotenv import load_dotenv 
import random
import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# cargar variables de entorno .env
load_dotenv()
email = os.getenv("GEO_EMAIL")
password = os.getenv("GEO_PASS")

options = Options()
options.binary_location = "/usr/bin/chromium-browser"
options.add_argument("--headless=new") # descomentar para no ver ventana
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)

try:
	driver.get("https://clients.geovictoria.com/account/login")
	time.sleep(5)

	driver.find_element(By.ID, "user").send_keys(email)
	driver.find_element(By.ID, "password").send_keys(password) 
	driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

	print("Login enviado, esperando carga ...")
	time.sleep(5)
	print("Login éxitoso")

	delay = random.randint(10, 30)

	try: 
		print(f"Esperando boton de salida {delay} segundos")
		mark_button = WebDriverWait(driver, delay).until(
			EC.element_to_be_clickable((By.ID, "btnEntryWebPunch"))
		)
		
		if mark_button.is_displayed():
			mark_button.click()
			print("✅ Salida marcada correctamente")		
		else:
			print("❌ El botón está presente pero no es visible.")
	except TimeoutException:
		print("❌ No se encontró el botón de salida en el tiempo esperado.")
except Exception as e:
	print("❌ No se pudo hacer clic en el botón:", e)
	traceback.print_exc()
finally:
	driver.quit()