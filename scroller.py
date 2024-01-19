from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


# инициализируем драйвер
service = Service(executable_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://shikimori.one/'
driver.get(url)

# ожидаем загрузки драйвера
time.sleep(5)

# зацикливаем скроллинг
stop_scrolling = False
while not stop_scrolling:
# вставляем JavaScript-код в страницу
    driver.execute_script("window.scrollTo(0, 1500);")
    time.sleep(10)
    driver.refresh()

# ждем 10 секунд
time.sleep(60)

# закрываем драйвер
driver.quit()