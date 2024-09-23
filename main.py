from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

Promised_down = 150
Promised_up = 10
Twitter_email = "the.bored.radio.demon@gmail.com"
Twitter_password = ""
chrome_path = r"D:\Games\chromedriver-win64\chromedriver.exe"


class InternetSpeedTwitterBot:
    def __init__(self):
        service = Service(executable_path=chrome_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.speedtest.net")
        self.down = None
        self.up = None

    def get_internet_speed(self):
        start = self.driver.find_element(By.CLASS_NAME,"start-text")
        start.click()
        # self.driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME,"download-speed").text
        print(f"down: {self.down}")
        self.up = self.driver.find_element(By.CLASS_NAME,"upload-speed").text
        print(f"up: {self.up}")


    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(4)
        self.driver.find_element(By.NAME,"text").send_keys("bored_radio")
        self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div').click()
        time.sleep(2)
        try:
            self.driver.find_element(By.NAME,"text").send_keys(Twitter_email+Keys.ENTER)
            time.sleep(1)
        except:
            print("not found")
        self.driver.find_element(By.NAME,"password").send_keys(Twitter_password)
        self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div').click()
        time.sleep(7)
        self.driver.find_element(By.CLASS_NAME,"public-DraftStyleDefault-ltr").send_keys(f"Hey internet provider! why is my internet speed {self.down}down/{self.up}up when I pay for {Promised_down}down/{Promised_up}up?")
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button').click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

