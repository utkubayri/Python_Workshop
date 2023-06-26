import time
from web3 import Web3 # pip install web3
from web3.auto import w3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



# Tarayıcıyı başlat
driver = webdriver.Chrome()

# Web sitesini aç
driver.get("https://www.zkelon.com/airdrop")

# Belirli bir sayfaya yönlendirildikten sonra bir düğmeye tıkla 4 kere
for _ in range(4):
    button = driver.find_element("id", "progress-btn")
    button.click()
    time.sleep(1)  # 1 saniye bekleyin

# Oluşturulan web3 adresini text kutusuna yaz
address_textbox = driver.find_element("id", "progress-input")
address = "web3_adresi"
address_textbox.send_keys(address)

# Web3 cüzdanı oluştur
account = w3.eth.account.create()
private_key = account.privateKey.hex()

# Private key'i txt dosyasına kaydet
with open("private_key.txt", "w") as file:
    file.write(private_key)

# Cüzdan adresini text kutusuna yazdıktan sonra "wallet_add" butonuna tıkla
wallet_address = "cuzdan_adresi"
wallet_textbox = driver.find_element("id", "wallet-textbox")
wallet_textbox.send_keys(wallet_address)

wallet_add_button = driver.find_element("name", "wallet_add-button")
wallet_add_button.click()

# Ana sayfaya geri dön
driver.switch_to.window(driver.window_handles[0])

# İşlemleri tekrarla
# ...

# Tarayıcıyı kapat
driver.quit()
