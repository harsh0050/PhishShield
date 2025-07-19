import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
ocr_api_key = os.getenv("OCR_API_KEY")
ocr_endpoint = 'https://api.ocr.space/parse/image'


def get_screenshot(url: str) -> str:
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_service = webdriver.ChromeService("usr/bin/chromedriver")

        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.get(url)
        time.sleep(2)


        # driver.set_window_size(width=1920, height=1080)
        height = driver.execute_script('return document.documentElement.scrollHeight;')
        width = driver.execute_script('return document.documentElement.scrollWidth;')
        width = max(1280, width)
        height *= 2
        height = max(1080, height)
        driver.set_window_size(width=width, height=height)

        body = driver.find_element(By.TAG_NAME, "body")
        image_data = 'data:image/png;base64,' + driver.get_screenshot_as_base64()
        # image_data.__sizeof__() /
        # Image.open(BytesIO(body.screenshot_as_png))
        # Image.open(BytesIO(driver.get_screenshot_as_png())).show()
        driver.quit()
        return image_data
    except Exception as e:
        print(e)
        return 'data:image/png;base64,'


def get_text_from_image(image_data: str, lang: str) -> dict[str, str]:
    json_payload = {
        'apikey': ocr_api_key,
        'base64image': image_data,
        'language': lang
    }
    # print("sending request...")
    try:
        res = requests.post(url=ocr_endpoint, data=json_payload, timeout=10)
        # print("got the response")
        res_data = res.json()
        if res.json().get('OCRExitCode') != 1:
            return {'error': " ".join(res_data.get('ErrorMessage'))}
        text = res.json().get("ParsedResults")[0].get("ParsedText")
        text = text.replace('\r', '')
        text = text.replace('\n', ' ')
        return {'text': text}
    except requests.Timeout as e:
        return {'error': "OCR api took too long to respond or is down."}


def get_text_from_url(url: str) -> dict[str, str]:
    # print("getting image...")
    image = get_screenshot(url)
    # print("got the image")
    # print("now getting the text...")
    resp = get_text_from_image(image_data=image, lang='eng')
    # print("got the text")
    return resp

# print(get_text_from_url("https://facebook.com"))
