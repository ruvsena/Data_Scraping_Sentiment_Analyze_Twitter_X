###çeviri kısmı
text1 = open("tweetler.txt","r", encoding="utf-8")
txt =text1.readlines()
#print(txt)

user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
driver_path = r"C:\\Users\\pc\\Desktop\\chromedriver.exe"
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
browser =webdriver.Chrome(service=chrome_service, options=chrome_options)
browser.get("https://translate.google.com/?sl=tr&tl=en&op=translate")
sleep(2)

paste = browser.find_element(By.XPATH,"//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")
paste.send_keys(txt)
paste.send_keys(Keys.ENTER)
sonuc=[]
copy = browser.find_elements(By.XPATH,"//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]")
sleep(3)
print("------------\n" + str(len(copy)) + "adet tweet başarıyla çekildi\n-----------")
for i in copy:
   sonuc.append(i.text)


with open("tweetler_en.txt", "w", encoding="UTF-8") as file:
    for a in sonuc:
        file.write(f"{a}\n")
sleep(5)


###sentiment analiz
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentiment =SentimentIntensityAnalyzer()
d = open("tweetler_en.txt","r", encoding="utf-8")
sent=sentiment.polarity_scores(d)
print(sent)
