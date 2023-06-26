
from web3 import Web3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def claim_zkelon_airdrop():
    # Connect to an Ethereum node
    web3 = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/DRp5oFKJMH0s5PXVag4Nmccnc1ep70-u'))

    while True:
        # Generate a new Ethereum account
        account = web3.eth.account.create()
        private_key = account._private_key.hex()

        # Save the private key to the file
        with open("private_key.txt", "a") as file:
            file.write(private_key + "\n")

        # Open the web page
        driver = webdriver.Chrome()
        driver.get("https://www.zkelon.com/airdrop")

        # Click on the button four times
        for i in range(4):
            button = driver.find_element(By.ID, "progress-btn")
            button.click()
            time.sleep(40)

        # Enter the address into the input field
        address_field = driver.find_element(By.ID, 'progress-input')
        address_field.send_keys(account.address)

        # Click the "Wallet Add" button
        button = driver.find_element(By.CSS_SELECTOR, 'button[name="walled_add"]')
        button.click()

        # Wait for a while to let the process complete
        time.sleep(10)

        # Go back to the first page
        driver.switch_to.window(driver.window_handles[0])
        driver.get("https://www.zkelon.com/airdrop")

        # Close the browser
        driver.quit()

        # Wait for some time before generating the next account
        time.sleep(10)


if __name__ == "__main__":
    claim_zkelon_airdrop()
