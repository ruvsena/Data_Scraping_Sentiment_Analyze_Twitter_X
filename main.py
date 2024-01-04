import selenium.webdriver as webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

#veri =input ("#Search: ")
veri="türkiye yüzyılı"
user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
driver_path = r"C:\\Users\\pc\\Desktop\\chromedriver.exe"
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
browser =webdriver.Chrome(service=chrome_service, options=chrome_options)
browser.get("https://twitter.com/search?q="+veri+"&src=typed_query")
sleep(10)


sleep(20)
###login sayfasını otomatik geçme"""""
username = browser.find_element(
    By.XPATH,
    "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
username.send_keys("kullanıcı adı")
next_button=browser.find_element(By.XPATH,"//span[contains(text(),'İleri')]")
next_button.click()
sleep(3)
password=browser.find_element(By.XPATH,"//input[@name='password']")
password.send_keys('şifre')
login=browser.find_element(By.XPATH,"//span[contains(text(),'Giriş yap')]")
login.click()

#search
sleep(3)
search=browser.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
search.send_keys(veri)
search.send_keys(Keys.ENTER)

sleep(3)
latest= browser.find_element(By.XPATH,"//span[contains(text(),'Latest')]")
latest.click()

sleep(3)

##tweetleri dosyaya kaydetme
sonuc =[]
twit = browser.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
sleep(3)
for i in twit:
    sonuc.append(i.text)
sayac= 0
son = browser.execute_script("return document.documentElement.scrollHeight")
while True:
    if sayac>3:
        break
    browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
    sleep(3)
    yeni =browser.execute_script("return document.documentElement.scrollHeight")
    if son== yeni :
        break
    son = yeni
    sayac +=1
    twit = browser.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
    sleep(3)
    print(str(len(twit)) + "adet tweet çekildi\n")
    for i in twit:
        sonuc.append(i.text)

adet =1
with open("tweetler.txt", "w", encoding="UTF-8") as file:
    for a in sonuc:
        file.write(f"{adet} - {a} \n\n")
        adet+=1
print("tweetler.txt dosyasına tweetler kaydedildi")


