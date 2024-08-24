from selenium import webdriver
from flask import Flask

app = Flask(__name__)

def gethtml():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(90)

    driver.get('https://www.facebook.com/CLBLapTrinhTrenThietBiDiDong')

    html = driver.page_source
    driver.quit()
    return html


@app.route('/')
def home():
    cc = gethtml()
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')