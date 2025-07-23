import os
from dotenv import load_dotenv 
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

# cargar variables de entorno .env
load_dotenv()
email = os.getenv("GEO_EMAIL")
password = os.getenv("GEO_PASS")

options = Options()
# options.add_argument("--headless") # descomentar para no ver ventana
options.binary_location = "/usr/bin/google-chrome"
service = Service("/usr/local/bin/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service,options=options)

try:
	driver.get("https://clients.geovictoria.com/account/login")
	time.sleep(5)

	driver.find_element(By.ID, "user").send_keys(email)
	driver.find_element(By.ID, "password").send_keys(password) 
	driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

	print("Login enviado, esperando carga ...")
	time.sleep(5)
	"""
	try: 

		time.sleep(3)
		mark_button = WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable((By.ID, "btnExitWebPunch")) #btnEntryWebPunch
		)
		mark_button.click()
		print("✅ Salida marcada correctamente")
		time.sleep(3)
	except Exception as e:
		print("❌ No se pudo hacer clic en el botón:", e)
	"""
finally:
	driver.quit()